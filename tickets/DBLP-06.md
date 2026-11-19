# DBLP-06 — Association rule mining

- **Prioritas:** P1
- **Jenis:** Analisis
- **Status:** Backlog
- **Dependensi:** DBLP-05

## User story

Sebagai pembaca, saya ingin melihat aturan asosiasi venue yang memenuhi minimum confidence agar hubungan publikasi lintas konferensi dapat ditafsirkan.

## Ruang lingkup

- Bangkitkan aturan dari frequent itemsets dengan minimum confidence 50%.
- Hitung support, confidence, dan lift untuk setiap aturan.
- Sajikan 10 aturan dengan lift tertinggi.
- Bahas aturan yang menarik, hubungan support dengan lift, makna setiap metrik, dan pola lintas venue.

## Kriteria penerimaan

- Setiap aturan menampilkan antecedent, consequent, support, confidence, dan lift.
- Aturan memenuhi ambang confidence yang ditetapkan.
- Analisis membedakan interpretasi support, confidence, dan lift.
- Hasil diberi konteks ukuran data dan keterbatasan transaksi.
