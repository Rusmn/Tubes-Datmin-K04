# **PROJECT DATA MINING** 

## **Conference Popularity and Association Pattern Mining Using DBLP Dataset** 

## **A. Deskripsi Project** 

DBLP (Digital Bibliography & Library Project) merupakan basis data bibliografi yang berisi publikasi ilmiah di bidang Computer Science. DBLP menyimpan berbagai informasi publikasi, seperti judul paper, nama penulis, tahun publikasi, dan venue publikasi. 

Dalam project ini, Anda diminta untuk melakukan analisis terhadap dataset DBLP untuk menemukan informasi mengenai popularitas konferensi dan pola hubungan antar-konferensi berdasarkan riwayat publikasi para peneliti. 

Anda akan menerapkan teknik **Frequent Pattern Mining** dan **Association Rule Mining** menggunakan algoritma Apriori dan FP-Growth. 

Perlu diperhatikan bahwa popularitas konferensi dalam project ini diukur berdasarkan aktivitas publikasi. 

## **B. Tujuan Project** 

Setelah menyelesaikan project ini, mahasiswa diharapkan mampu: 

1. Memahami dan melakukan preprocessing terhadap dataset bibliografi. 

2. Mengubah data bibliografi menjadi transactional database. 

3. Mengimplementasikan algoritma Apriori dan FP-Growth. 

4. Menemukan frequent itemsets dari transactional database. 

5. Menghasilkan dan menganalisis association rules. 

6. Mengevaluasi performa algoritma Frequent Pattern Mining. 

7. Menginterpretasikan hasil mining menjadi informasi yang bermakna. 

## **C. Dataset** 

Gunakan dataset DBLP yang dapat diperoleh melalui: https://dblp.org/ 

Ketentuan dataset: 

1. Gunakan publikasi dari seluruh bidang Computer Science. 2. Gunakan periode publikasi tahun 2015–2025. 

3. Fokus pada publikasi konferensi dan workshop ( `inproceedings` ). 

4. Gunakan atribut yang relevan, seperti author, title, year, dan venue. 

5. Jelaskan sumber dataset, tanggal pengambilan, serta jumlah data yang digunakan. 

## **D. Soal dan Tugas** 

### **Task 1 — Data Understanding and Preprocessing** 

1. Lakukan eksplorasi terhadap dataset DBLP yang digunakan. Jelaskan struktur dataset, atribut, jumlah record, dan jenis publikasi yang tersedia. 

2. Lakukan proses preprocessing terhadap dataset dengan ketentuan: 

   - Memilih publikasi konferensi dan workshop. 

   - Menangani missing values. 

   - Menghilangkan data duplikat. 

   - Melakukan normalisasi nama author. 

   - Melakukan normalisasi nama conference/venue. 

   - Memastikan konsistensi atribut tahun publikasi. 

3. Jelaskan setiap tahapan preprocessing yang dilakukan beserta alasan pemilihan metode tersebut. 

4. Tampilkan statistik dataset setelah preprocessing, meliputi: `o` Total publikasi. 

   - Total author unik. 

   - Total conference/venue unik. 

   - Distribusi publikasi berdasarkan tahun. 

   - Distribusi publikasi berdasarkan conference. 

### **Task 2 — Conference Popularity Analysis** 

Lakukan analisis untuk mengidentifikasi konferensi yang memiliki aktivitas publikasi tertinggi. 

1. Identifikasi 10 konferensi dengan jumlah publikasi terbanyak. 

2. Identifikasi 10 konferensi dengan jumlah author unik terbanyak. 

3. Analisis tren jumlah publikasi konferensi berdasarkan tahun selama periode 2015–2025. 

4. Bandingkan hasil ranking berdasarkan jumlah publikasi dan jumlah author unik. 

5. Berdasarkan hasil analisis, jelaskan: 

   - Konferensi mana yang paling populer berdasarkan jumlah publikasi? 

   - Apakah konferensi dengan jumlah publikasi terbanyak juga memiliki jumlah author unik terbanyak? 

   - Bagaimana perubahan aktivitas publikasi konferensi selama periode pengamatan? 

Sertakan visualisasi yang relevan untuk mendukung analisis. 

### **Task 3 — Transactional Database Construction** 

Ubahlah dataset DBLP yang telah melalui preprocessing menjadi transactional database. 

Buat dua jenis representasi transaksi berikut. 

### **A. Author-Based Transaction** 

- Setiap transaksi merepresentasikan satu author. 

- Item dalam transaksi merupakan daftar conference tempat author tersebut pernah memublikasikan paper selama periode pengamatan. 

### **B. Author-Year-Based Transaction** 

- Setiap transaksi merepresentasikan kombinasi satu author dan satu tahun. 

- Item dalam transaksi merupakan daftar conference tempat author tersebut memublikasikan paper pada tahun tersebut. 

### Kerjakan hal-hal berikut: 

1. Bentuk kedua transactional database tersebut. 

2. Tampilkan minimal 10 contoh transaksi dari masing-masing representasi. 

3. Hitung jumlah transaksi pada masing-masing transactional database. 

4. Hitung jumlah item unik dan distribusi jumlah item per transaksi. 

5. Analisis perbedaan kedua representasi transaksi tersebut. 

6. Jelaskan kelebihan dan keterbatasan masing-masing representasi untuk Frequent Pattern Mining. 

### **Task 4 — Frequent Pattern Mining** 

Implementasikan algoritma berikut pada Author-Based Transactional Database: 

1. Apriori. 

2. FP-Growth. 

Lakukan eksperimen menggunakan beberapa nilai minimum support yang berbeda, yaitu: 

- 0,1% 

- 0,5% 

- 1% 

- 2% 

Untuk setiap eksperimen: 

1. Temukan frequent itemsets yang memenuhi minimum support. 

2. Identifikasi frequent 1-itemsets, 2-itemsets, dan 3-itemsets. 

3. Tampilkan 10 frequent itemsets dengan support tertinggi. 

4. Analisis pengaruh perubahan minimum support terhadap jumlah frequent itemsets yang dihasilkan. 

5. Identifikasi kombinasi conference yang paling sering muncul bersama. 

6. Interpretasikan hasil frequent patterns yang diperoleh. 

### **Task 5 — Association Rule Mining** 

Gunakan frequent itemsets yang diperoleh untuk menghasilkan association rules. 

Ketentuan eksperimen: 

- Gunakan minimum confidence sebesar 50%. 

- Hitung support, confidence, dan lift untuk setiap association rule. 

- Identifikasi 10 association rules dengan lift tertinggi. 

Kerjakan hal-hal berikut: 

1. Bangkitkan association rules dari frequent itemsets. 

2. Tampilkan hasil association rules beserta nilai support, confidence, dan lift. 

3. Identifikasi hubungan asosiasi antar-konferensi yang paling menarik. 

4. Analisis apakah conference yang memiliki support tinggi selalu menghasilkan lift yang tinggi. 

5. Jelaskan perbedaan interpretasi support, confidence, dan lift. 

6. Berdasarkan association rules yang ditemukan, jelaskan pola publikasi antar-konferensi yang dapat diidentifikasi. 

### **Task 6 — Algorithm Performance Comparison** 

Bandingkan performa algoritma Apriori dan FP-Growth menggunakan transactional database dan parameter minimum support yang sama. 

Lakukan pengukuran berdasarkan: 

1. Number of frequent itemsets. 

2. Number of association rules yang dihasilkan dari frequent itemsets. 

Lakukan pengujian untuk setiap nilai minimum support yang telah ditentukan pada Task 4. 

Kemudian jawab pertanyaan berikut: 

1. Bagaimana perubahan minimum support memengaruhi performa kedua algoritma? 

2. Apakah kedua algoritma menghasilkan frequent itemsets yang sama? 

3. Berdasarkan hasil eksperimen, algoritma mana yang lebih sesuai untuk dataset DBLP yang digunakan? Jelaskan alasan Anda. 

## **E. Temporal Association Analysis** 

Lakukan analisis pola asosiasi konferensi berdasarkan periode waktu. 

Gunakan pembagian periode berikut: 

- 2015–2017 

- 2018–2020 

- 2021–2023 

- 2024–2025 

Gunakan Author-Year-Based Transactional Database. 

Kerjakan hal-hal berikut: 

1. Jalankan Frequent Pattern Mining pada setiap periode. 

2. Identifikasi frequent itemsets pada setiap periode. 

3. Bangkitkan association rules untuk setiap periode. 

4. Bandingkan association rules yang ditemukan antarperiode. 

5. Identifikasi pola asosiasi yang bertahan dan pola yang mengalami perubahan. 

6. Jelaskan kemungkinan perubahan tren publikasi berdasarkan hasil eksperimen. 

## **F. Ketentuan Pengerjaan** 

1. Project dikerjakan secara berkelompok. 

2. Algoritma Apriori dan FP-Growth harus diimplementasikan dan diuji. 

3. Seluruh eksperimen harus menggunakan dataset yang telah melalui preprocessing. 

4. Setiap hasil eksperimen harus dapat direproduksi. 

5. Sertakan visualisasi yang relevan untuk mendukung hasil analisis. 

6. Setiap hasil mining harus disertai interpretasi, bukan hanya menampilkan output algoritma. 

7. Cantumkan sumber dataset dan referensi yang digunakan. 

8. Dokumentasikan keterbatasan dataset dan asumsi yang digunakan dalam analisis. 

## **G. Deliverables** 

Setiap kelompok wajib mengumpulkan: 

1. **Source Code / Jupyter Notebook** 

   - Data extraction. 

   - Data preprocessing. 

   - Transactional database construction. 

   - Apriori implementation. 

   - FP-Growth implementation. 

   - Association Rule Mining. 

   - Performance evaluation. 

   - Data visualization. 

### 2. **Laporan Project** 

- Pendahuluan. 

- Deskripsi dataset. 

- Metodologi. 

- Hasil preprocessing. 

- Hasil conference popularity analysis. 

   - Hasil frequent pattern mining. 

   - Hasil association rule mining. 

   - Perbandingan performa algoritma. 

   - Analisis dan interpretasi. 

   - Kesimpulan. 

3. **Presentasi** 

   - Penjelasan metodologi. 

   - Demonstrasi hasil eksperimen. 

   - Temuan utama (key findings). 

   - Kesimpulan project. 

## **H. Pertanyaan Kesimpulan** 

Berdasarkan seluruh eksperimen yang telah dilakukan, jawablah pertanyaan berikut: 

1. Konferensi apa yang memiliki popularitas publikasi tertinggi berdasarkan dataset DBLP? 2. Apakah konferensi yang paling populer juga memiliki asosiasi paling kuat dengan konferensi lain? 

3. Kombinasi konferensi apa yang paling sering muncul bersama dalam riwayat publikasi author? 

4. Association rules apa yang menghasilkan lift tertinggi? Apa makna dari rule tersebut? 5. Apakah terdapat perbedaan pola yang ditemukan pada Author-Based dan Author-YearBased Transactional Database? 

6. Algoritma mana yang memberikan performa terbaik pada dataset yang digunakan? 7. Apa pengetahuan atau insight utama yang berhasil diperoleh dari penerapan Frequent Pattern Mining dan Association Rule Mining terhadap dataset DBLP? 

**Catatan:** Kesimpulan harus didasarkan pada hasil eksperimen. 

