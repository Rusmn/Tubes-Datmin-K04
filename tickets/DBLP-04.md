# DBLP-04 — Pembuatan transactional database

- **Prioritas:** P1
- **Jenis:** Data/Analisis
- **Status:** Backlog
- **Dependensi:** DBLP-02

## User story

Sebagai analis frequent pattern, saya ingin dua representasi transaksi agar pola lintas karier author dan pola per tahun dapat dibandingkan.

## Ruang lingkup

- Bentuk transaksi author-based: satu transaksi per author, item berupa venue.
- Bentuk transaksi author-year-based: satu transaksi per pasangan author-tahun, item berupa venue.
- Hitung jumlah transaksi, jumlah item unik, dan distribusi jumlah item per transaksi.
- Tampilkan minimal 10 contoh dari tiap representasi.
- Bahas kelebihan dan keterbatasan keduanya.

## Kriteria penerimaan

- Transaksi dibentuk hanya dari dataset hasil preprocessing.
- Sampel minimal 10 transaksi per representasi tersedia.
- Statistik dan distribusi item per transaksi tersedia.
- Perbedaan interpretasi serta dampaknya bagi Frequent Pattern Mining dijelaskan.
