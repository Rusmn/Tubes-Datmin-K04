# DBLP-01 — Akuisisi dataset DBLP dan dokumentasi sumber

- **Prioritas:** P0
- **Jenis:** Data
- **Status:** Backlog
- **Dependensi:** —

## User story

Sebagai anggota tim, saya ingin menggunakan snapshot DBLP yang dapat dilacak agar seluruh analisis memakai sumber data yang jelas dan dapat direproduksi.

## Ruang lingkup

- Unduh/sediakan dataset DBLP dari sumber resmi.
- Ekstrak publikasi `inproceedings` pada 2015–2025 dengan atribut key, author, title, year, dan venue.
- Catat URL sumber, tanggal pengambilan, format/snapshot dataset, jumlah record sumber, dan jumlah record hasil ekstraksi.
- Dokumentasikan kebutuhan file sumber dan cara menjalankan ekstraksi.

## Kriteria penerimaan

- Dataset hanya berisi publikasi `inproceedings` dengan tahun 2015–2025.
- Atribut yang dibutuhkan tersedia pada hasil ekstraksi.
- Metadata sumber dan tanggal pengambilan tersimpan dalam dokumentasi proyek.
- Proses ekstraksi dapat dijalankan ulang dari instruksi yang terdokumentasi.
