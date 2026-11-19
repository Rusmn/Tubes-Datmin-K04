import csv
import gzip
import os
import sys
from pathlib import Path

from lxml import etree

ROOT = Path(__file__).resolve().parent.parent
Y0, Y1 = 2015, 2025


def extract(xml_path, out_csv):
    parser_kwargs = dict(events=("end",), tag="inproceedings", load_dtd=True,
                         resolve_entities=True, huge_tree=True)
    n_all = n_kept = 0
    xml_path = Path(xml_path).resolve()
    out_csv = Path(out_csv).resolve()
    os.chdir(xml_path.parent)  # supaya dblp.dtd (relatif) ditemukan
    with gzip.open(xml_path, "rb") as src, open(out_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["key", "authors", "title", "year", "booktitle", "pages"])
        for _, el in etree.iterparse(src, **parser_kwargs):
            n_all += 1
            year = (el.findtext("year") or "").strip()
            if year.isdigit() and Y0 <= int(year) <= Y1:
                authors = "|".join((a.text or "").strip() for a in el.findall("author"))
                w.writerow([el.get("key"), authors,
                            "".join(el.find("title").itertext()) if el.find("title") is not None else "",
                            year, (el.findtext("booktitle") or "").strip(),
                            (el.findtext("pages") or "").strip()])
                n_kept += 1
            el.clear()
            while el.getprevious() is not None:
                del el.getparent()[0]
    print(f"inproceedings total={n_all:,}  disimpan ({Y0}-{Y1})={n_kept:,} -> {out_csv}")
    return n_all, n_kept


if __name__ == "__main__":
    xml = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "data/raw/dblp.xml.gz"
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "data/raw/inproceedings_2015_2025.csv"
    extract(xml, out)
