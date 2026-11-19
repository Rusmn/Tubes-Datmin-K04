# DBLP-02 — Preprocessing dan statistik dataset

- **Prioritas:** P0
- **Jenis:** Data
- **Status:** Backlog
- **Dependensi:** DBLP-01

## User story

Sebagai analis, saya ingin dataset DBLP dibersihkan dan dinormalisasi agar hasil popularitas dan mining tidak bias oleh data kosong, duplikat, atau variasi penamaan.

## Ruang lingkup

- Eksplorasi struktur, atribut, jumlah record, serta jenis publikasi.
- Seleksi publikasi konferensi dan workshop.
- Tangani missing values, duplikasi, dan konsistensi tahun.
- Normalisasi nama author dan conference/venue dengan aturan yang didokumentasikan.
- Hasilkan statistik dataset bersih: publikasi, author unik, venue unik, publikasi per tahun, dan publikasi per venue.
- Jelaskan alasan setiap keputusan preprocessing dan batasannya.

## Kriteria penerimaan

- Dataset bersih hanya memuat record yang memenuhi aturan periode dan jenis publikasi.
- Aturan normalisasi, missing value, deduplikasi, dan tahun dijelaskan serta dapat diulang.
- Semua statistik yang diminta tersedia sebagai output yang bisa dirujuk.
- Jumlah record sebelum dan sesudah setiap tahap dapat ditelusuri.
