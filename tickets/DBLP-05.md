# DBLP-05 — Implementasi dan eksperimen Apriori serta FP-Growth

- **Prioritas:** P1
- **Jenis:** Algoritma
- **Status:** Backlog
- **Dependensi:** DBLP-04

## User story

Sebagai tim proyek, kami ingin menemukan frequent itemsets dengan dua algoritma pada transaksi author-based dan membandingkan hasilnya.

## Ruang lingkup

- Implementasikan dan uji Apriori serta FP-Growth.
- Jalankan keduanya pada minimum support 0,1%, 0,5%, 1%, dan 2%.
- Untuk tiap nilai, laporkan jumlah itemset ukuran 1, 2, dan 3 serta 10 itemset dengan support tertinggi.
- Identifikasi pasangan venue yang sering muncul bersama.
- Analisis dampak perubahan minimum support dan interpretasikan pola.

## Kriteria penerimaan

- Kedua algoritma menggunakan transaksi dan nilai minimum support yang sama.
- Output memuat support dan jumlah kemunculan itemset.
- Hasil itemset kedua algoritma dibandingkan untuk setiap eksperimen.
- Interpretasi menyebutkan batasan dan tidak menyimpulkan sebab-akibat dari pola asosiasi.
