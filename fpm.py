from collections import Counter, defaultdict
from itertools import combinations
import math


def _weighted(transactions):
    """Gabungkan transaksi identik -> {frozenset: bobot}. Mempercepat counting."""
    c = Counter(frozenset(t) for t in transactions)
    return c


def min_count_from_support(min_support, n):
    return max(1, math.ceil(min_support * n - 1e-9))


# ----------------------------------------------------------------- Apriori
def apriori(transactions, min_support):
    """Return (itemsets: {frozenset: count}, n_transactions)."""
    wt = _weighted(transactions)
    n = sum(wt.values())
    min_count = min_count_from_support(min_support, n)

    item_cnt = Counter()
    for t, w in wt.items():
        for i in t:
            item_cnt[i] += w
    freq = {frozenset([i]): c for i, c in item_cnt.items() if c >= min_count}
    result = dict(freq)
    frequent_items = {next(iter(s)) for s in freq}
    # buang item tidak frequent dari transaksi (aman: anti-monotone)
    wt = _reduce(wt, frequent_items)

    prev = sorted(tuple(sorted(s)) for s in freq)
    k = 2
    while prev:
        cands = _gen_candidates(prev, k)
        if not cands:
            break
        cand_set = set(cands)
        counts = Counter()
        for t, w in wt.items():
            if len(t) < k:
                continue
            ts = sorted(t)
            if len(ts) < 40 or math.comb(len(ts), k) <= len(cand_set):
                for comb in combinations(ts, k):
                    if comb in cand_set:
                        counts[comb] += w
            else:  # transaksi besar: cek kandidat langsung
                tset = set(ts)
                for c in cand_set:
                    if tset.issuperset(c):
                        counts[c] += w
        cur = {c: v for c, v in counts.items() if v >= min_count}
        for c, v in cur.items():
            result[frozenset(c)] = v
        prev = sorted(cur)
        k += 1
    return result, n


def _reduce(wt, keep):
    out = Counter()
    for t, w in wt.items():
        r = t & keep
        if r:
            out[frozenset(r)] += w
    return out


def _gen_candidates(prev, k):
    """Join langkah Apriori (prefix k-2 sama) + prune subset."""
    prev_set = set(prev)
    cands = []
    for i in range(len(prev)):
        a = prev[i]
        for j in range(i + 1, len(prev)):
            b = prev[j]
            if a[:-1] != b[:-1]:
                break
            c = a + (b[-1],)
            if all(sub in prev_set for sub in combinations(c, k - 1)):
                cands.append(c)
    return cands


# --------------------------------------------------------------- FP-Growth
class _Node:
    __slots__ = ("item", "count", "parent", "children", "link")

    def __init__(self, item, parent):
        self.item, self.count, self.parent = item, 0, parent
        self.children, self.link = {}, None


def _build_tree(weighted_txns, order):
    root = _Node(None, None)
    header = {}
    tails = {}
    for items, w in weighted_txns:
        node = root
        for it in sorted((i for i in items if i in order), key=order.get):
            ch = node.children.get(it)
            if ch is None:
                ch = _Node(it, node)
                node.children[it] = ch
                if it in header:
                    tails[it].link = ch
                else:
                    header[it] = ch
                tails[it] = ch
            ch.count += w
            node = ch
    return header


def _mine(header, counts, min_count, suffix, out):
    # proses item dari frekuensi terendah
    for item in sorted(counts, key=lambda i: (counts[i], str(i))):
        new = suffix | {item}
        out[frozenset(new)] = counts[item]
        # conditional pattern base
        base = []
        node = header[item]
        while node is not None:
            path = []
            p = node.parent
            while p is not None and p.item is not None:
                path.append(p.item)
                p = p.parent
            if path:
                base.append((path, node.count))
            node = node.link
        cc = Counter()
        for path, w in base:
            for i in path:
                cc[i] += w
        cc = {i: c for i, c in cc.items() if c >= min_count}
        if not cc:
            continue
        order = {i: r for r, i in enumerate(sorted(cc, key=lambda x: (-cc[x], str(x))))}
        sub = _build_tree(((p, w) for p, w in base), order)
        _mine(sub, cc, min_count, new, out)


def fpgrowth(transactions, min_support):
    wt = _weighted(transactions)
    n = sum(wt.values())
    min_count = min_count_from_support(min_support, n)
    item_cnt = Counter()
    for t, w in wt.items():
        for i in t:
            item_cnt[i] += w
    item_cnt = {i: c for i, c in item_cnt.items() if c >= min_count}
    order = {i: r for r, i in enumerate(sorted(item_cnt, key=lambda x: (-item_cnt[x], str(x))))}
    header = _build_tree(wt.items(), order)
    out = {}
    _mine(header, item_cnt, min_count, frozenset(), out)
    return out, n


# ------------------------------------------------------- Association Rules
def association_rules(itemsets, n, min_confidence=0.5):
    """itemsets: {frozenset: count} (harus closed under subset = hasil Apriori/FPG)."""
    rows = []
    for itemset, cnt in itemsets.items():
        if len(itemset) < 2:
            continue
        items = list(itemset)
        for r in range(1, len(items)):
            for ante in combinations(items, r):
                ante = frozenset(ante)
                cons = itemset - ante
                ca, cc = itemsets.get(ante), itemsets.get(cons)
                if not ca or not cc:
                    continue
                conf = cnt / ca
                if conf + 1e-12 >= min_confidence:
                    rows.append({
                        "antecedent": tuple(sorted(ante)),
                        "consequent": tuple(sorted(cons)),
                        "support": cnt / n,
                        "confidence": conf,
                        "lift": conf / (cc / n),
                        "count": cnt,
                    })
    return rows
