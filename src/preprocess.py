import re
import sys
import unicodedata
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
_SUFFIX = re.compile(r"\s+\d{4}$")  # DBLP disambiguator: "Wei Wang 0001"


def norm_author(name):
    name = unicodedata.normalize("NFKC", name)
    name = _SUFFIX.sub("", name)
    return re.sub(r"\s+", " ", name).strip()


def venue_from_key(key):
    """conf/aaai/Foo15 -> AAAI. Normalisasi venue = akronim DBLP dari key."""
    parts = str(key).split("/")
    return parts[1].upper() if len(parts) > 2 and parts[0] == "conf" else None


def preprocess(raw_csv):
    log = {}
    df = pd.read_csv(raw_csv, dtype=str, keep_default_na=False)
    log["raw_records"] = len(df)

    # pilih konferensi & workshop (key conf/*); journal-style 'journals/*' dibuang
    df["venue"] = df["key"].map(venue_from_key)
    df = df[df["venue"].notna()].copy()
    log["after_conf_filter"] = len(df)

    # missing values
    for col in ["authors", "title", "year", "venue"]:
        df = df[df[col].str.strip() != ""]
    log["after_missing"] = len(df)

    # tipe workshop (info tambahan)
    df["is_workshop"] = df["booktitle"].str.contains("workshop", case=False, na=False)

    # normalisasi author, hapus author duplikat dalam satu paper
    def clean_authors(s):
        seen, out = set(), []
        for a in s.split("|"):
            a = norm_author(a)
            if a and a not in seen:
                seen.add(a)
                out.append(a)
        return out

    df["author_list"] = df["authors"].map(clean_authors)
    df = df[df["author_list"].map(len) > 0]
    df["year"] = df["year"].astype(int)
    df["title_norm"] = df["title"].str.lower().str.replace(r"[^a-z0-9]+", " ", regex=True).str.strip()

    # duplikat: key sama, atau (judul, tahun, venue) sama
    df = df.drop_duplicates("key")
    df = df.drop_duplicates(["title_norm", "year", "venue"])
    log["after_dedup"] = len(df)
    return df.reset_index(drop=True), log


def author_based(df):
    """{author: set(venue)} -> list of transactions."""
    d = {}
    for authors, v in zip(df["author_list"], df["venue"]):
        for a in authors:
            d.setdefault(a, set()).add(v)
    return d


def author_year_based(df):
    """{(author, year): set(venue)}"""
    d = {}
    for authors, v, y in zip(df["author_list"], df["venue"], df["year"]):
        for a in authors:
            d.setdefault((a, y), set()).add(v)
    return d


if __name__ == "__main__":
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "data/raw/inproceedings_2015_2025.csv"
    df, log = preprocess(src)
    out = ROOT / "data/dblp_clean.pkl"
    df.to_pickle(out)
    print(log, "->", out)
