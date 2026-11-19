# DBLP-08 — Analisis asosiasi temporal

- **Prioritas:** P1
- **Jenis:** Analisis
- **Status:** Backlog
- **Dependensi:** DBLP-04, DBLP-06

## User story

Sebagai analis, saya ingin membandingkan pola asosiasi antarperiode untuk mengetahui hubungan venue yang bertahan atau berubah sepanjang waktu.

## Ruang lingkup

- Gunakan transaksi author-year-based.
- Analisis periode 2015–2017, 2018–2020, 2021–2023, dan 2024–2025.
- Jalankan Frequent Pattern Mining dan bangkitkan association rules per periode.
- Bandingkan aturan antarperiode dan identifikasi aturan yang bertahan maupun berubah.
- Jelaskan kemungkinan perubahan tren publikasi berdasarkan hasil.

## Kriteria penerimaan

- Itemset dan aturan tersedia untuk setiap periode.
- Parameter support dan confidence dicatat dan diterapkan secara konsisten.
- Perbandingan periode membedakan aturan yang persisten dan yang hanya muncul pada periode tertentu.
- Kesimpulan temporal didukung output dan mencatat keterbatasan periode yang lebih pendek.
