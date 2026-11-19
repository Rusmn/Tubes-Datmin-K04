import sys
import time
from collections import Counter
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fpm import apriori, fpgrowth, association_rules  # noqa: E402
from preprocess import author_based, author_year_based  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "output"
FIG = OUT / "figures"
SUPPORTS = [0.001, 0.005, 0.01, 0.02]
MIN_CONF = 0.5
PERIODS = [(2015, 2017), (2018, 2020), (2021, 2023), (2024, 2025)]
S = []  # ringkasan teks


def say(*a):
    line = " ".join(str(x) for x in a)
    print(line)
    S.append(line)


def savefig(name):
    plt.tight_layout()
    plt.savefig(FIG / name, dpi=130)
    plt.close()


def task1_stats(df):
    say("== TASK 1: statistik setelah preprocessing ==")
    say("Total publikasi:", f"{len(df):,}")
    say("Total author unik:", f"{len({a for l in df.author_list for a in l}):,}")
    say("Total venue unik:", df.venue.nunique())
    by_year = df.groupby("year").size()
    by_conf = df.groupby("venue").size().sort_values(ascending=False)
    by_year.to_csv(OUT / "t1_pubs_per_year.csv")
    by_conf.to_csv(OUT / "t1_pubs_per_venue.csv")
    by_year.plot.bar(color="#3b6ea5", title="Publikasi per tahun (conf+workshop, DBLP)")
    plt.ylabel("jumlah publikasi")
    savefig("t1_pubs_per_year.png")
    by_conf.head(30).iloc[::-1].plot.barh(color="#3b6ea5", title="30 venue terbanyak (jumlah publikasi)")
    savefig("t1_pubs_per_venue_top30.png")


def task2(df):
    say("\n== TASK 2: popularitas konferensi ==")
    pubs = df.groupby("venue").size().rename("n_pubs")
    ex = df[["venue", "year", "author_list"]].explode("author_list")
    auth = ex.groupby("venue")["author_list"].nunique().rename("n_authors")
    t = pd.concat([pubs, auth], axis=1)
    t["rank_pubs"] = t.n_pubs.rank(ascending=False, method="min").astype(int)
    t["rank_authors"] = t.n_authors.rank(ascending=False, method="min").astype(int)
    t = t.sort_values("n_pubs", ascending=False)
    t.to_csv(OUT / "t2_venue_ranking.csv")
    say("Top 10 by publikasi:\n" + t.head(10).to_string())
    say("Top 10 by author unik:\n" + t.sort_values("n_authors", ascending=False).head(10).to_string())
    top_p = set(t.head(10).index)
    top_a = set(t.sort_values("n_authors", ascending=False).head(10).index)
    say("Irisan top10 pub & top10 author:", len(top_p & top_a), sorted(top_p & top_a))

    top = t.head(10).index
    pv = df[df.venue.isin(top)].pivot_table(index="year", columns="venue", values="key",
                                            aggfunc="count", fill_value=0)
    pv.to_csv(OUT / "t2_trend_top10.csv")
    pv.plot(marker="o", figsize=(9, 5), title="Tren publikasi 10 konferensi teratas")
    plt.ylabel("jumlah publikasi")
    savefig("t2_trend_top10.png")
    fig, ax = plt.subplots(1, 2, figsize=(12, 4.5))
    t.head(10).iloc[::-1].n_pubs.plot.barh(ax=ax[0], color="#3b6ea5", title="Top 10: publikasi")
    t.sort_values("n_authors", ascending=False).head(10).iloc[::-1].n_authors.plot.barh(
        ax=ax[1], color="#d98a2b", title="Top 10: author unik")
    savefig("t2_top10_pubs_vs_authors.png")


def build_author_tx(df):
    ab = author_based(df)
    return list(ab.values()), ab


def task3(df):
    say("\n== TASK 3: transactional database ==")
    ab = author_based(df)
    ay = author_year_based(df)
    for name, d in [("Author-Based", ab), ("Author-Year-Based", ay)]:
        sizes = pd.Series([len(v) for v in d.values()])
        items = {i for v in d.values() for i in v}
        say(f"{name}: transaksi={len(d):,}  item unik={len(items)}  "
            f"rata2 item/tx={sizes.mean():.2f}  median={sizes.median()}  max={sizes.max()}")
        dist = sizes.value_counts().sort_index()
        dist.to_csv(OUT / f"t3_items_per_tx_{name}.csv")
        say("  distribusi item/tx (1..10):", dict(dist.head(10)))
    for name, d, fn in [("author", ab, "t3_sample_author_based.csv"),
                        ("author-year", ay, "t3_sample_author_year_based.csv")]:
        sample = [(k, sorted(v)) for k, v in d.items() if len(v) >= 3][:10]
        pd.DataFrame({"transaction_id": [str(k) for k, _ in sample],
                      "items": [", ".join(v) for _, v in sample]}).to_csv(OUT / fn, index=False)
    return ab, ay


def top_itemsets(freq, n, k=None, top=10):
    rows = [(tuple(sorted(s)), c, c / n) for s, c in freq.items() if (k is None or len(s) == k)]
    rows.sort(key=lambda r: -r[1])
    return rows[:top]


def task4_5_6(ab):
    say("\n== TASK 4/5/6: FPM, ARM, performa ==")
    tx = list(ab.values())
    perf, best_rules = [], None
    for sup in SUPPORTS:
        t0 = time.perf_counter(); fa, n = apriori(tx, sup); ta = time.perf_counter() - t0
        t0 = time.perf_counter(); ff, _ = fpgrowth(tx, sup); tf = time.perf_counter() - t0
        same = fa == ff
        rules = association_rules(ff, n, MIN_CONF)
        by_k = Counter(len(s) for s in ff)
        perf.append({"min_support": sup, "n_tx": n, "freq_itemsets": len(ff),
                     "k1": by_k[1], "k2": by_k[2], "k3": by_k[3],
                     "rules": len(rules), "apriori_s": round(ta, 3), "fpgrowth_s": round(tf, 3),
                     "same_result": same})
        say(f"[sup={sup:.3%}] itemsets={len(ff)} (1:{by_k[1]} 2:{by_k[2]} 3:{by_k[3]}) "
            f"rules={len(rules)} apriori={ta:.2f}s fpgrowth={tf:.2f}s sama={same}")
        say("  Top10 itemset (support):")
        for it, c, s in top_itemsets(ff, n):
            say(f"    {it} count={c} support={s:.4%}")
        pairs = top_itemsets(ff, n, k=2, top=10)
        pd.DataFrame([{"itemset": " + ".join(i), "count": c, "support": s} for i, c, s in pairs]
                     ).to_csv(OUT / f"t4_top_pairs_sup{sup}.csv", index=False)
        pd.DataFrame([{"itemset": " + ".join(i), "k": len(i), "count": c, "support": s}
                      for i, c, s in top_itemsets(ff, n)]).to_csv(OUT / f"t4_top10_sup{sup}.csv", index=False)
        r = pd.DataFrame(rules)
        if len(r):
            r = r.sort_values("lift", ascending=False)
            r.to_csv(OUT / f"t5_rules_sup{sup}.csv", index=False)
            say("  Top10 rules by lift:")
            for _, x in r.head(10).iterrows():
                say(f"    {x.antecedent} -> {x.consequent} sup={x.support:.4%} conf={x.confidence:.2%} lift={x.lift:.1f}")
        if sup == 0.001:
            best_rules = r
    p = pd.DataFrame(perf)
    p.to_csv(OUT / "t6_performance.csv", index=False)
    fig, ax = plt.subplots(1, 2, figsize=(11, 4))
    ax[0].plot(p.min_support * 100, p.apriori_s, "o-", label="Apriori")
    ax[0].plot(p.min_support * 100, p.fpgrowth_s, "s-", label="FP-Growth")
    ax[0].set(xscale="log", xlabel="min support (%)", ylabel="detik", title="Waktu eksekusi")
    ax[0].legend()
    ax[1].plot(p.min_support * 100, p.freq_itemsets, "o-", label="frequent itemsets")
    ax[1].plot(p.min_support * 100, p.rules, "s-", label="rules")
    ax[1].set(xscale="log", yscale="log", xlabel="min support (%)", title="Jumlah hasil")
    ax[1].legend()
    savefig("t6_performance.png")
    return best_rules


def temporal(ay_df):
    say("\n== TEMPORAL: Author-Year DB per periode ==")
    ay = author_year_based(ay_df)
    sup = 0.005
    res = {}
    for a, b in PERIODS:
        tx = [v for (au, y), v in ay.items() if a <= y <= b]
        f, n = fpgrowth(tx, sup)
        rules = association_rules(f, n, MIN_CONF)
        res[(a, b)] = rules
        say(f"{a}-{b}: tx={n:,} itemsets={len(f)} rules={len(rules)} (min_sup={sup:.1%})")
        pd.DataFrame(rules).sort_values("lift", ascending=False).to_csv(
            OUT / f"temporal_rules_{a}_{b}.csv", index=False) if rules else None
    keyset = {p: {(r["antecedent"], r["consequent"]) for r in rs} for p, rs in res.items()}
    stable = set.intersection(*keyset.values()) if keyset else set()
    say(f"Rule yang muncul di SEMUA periode: {len(stable)}")
    for r in list(stable)[:15]:
        say("   ", r[0], "->", r[1])
    allr = set.union(*keyset.values())
    say(f"Total rule unik lintas periode: {len(allr)}")


def main():
    OUT.mkdir(exist_ok=True)
    FIG.mkdir(parents=True, exist_ok=True)
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "data/dblp_clean.pkl"
    df = pd.read_pickle(src)
    task1_stats(df)
    task2(df)
    ab, _ = task3(df)
    task4_5_6(ab)
    temporal(df)
    (OUT / "summary.txt").write_text("\n".join(S), encoding="utf-8")


if __name__ == "__main__":
    main()
