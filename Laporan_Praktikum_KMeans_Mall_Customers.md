# LAPORAN PRAKTIKUM MACHINE LEARNING
## ACARA X: CLUSTERING DENGAN ALGORITMA K-MEANS
### Studi Kasus: Segmentasi 200 Pelanggan Mall Berdasarkan Pendapatan Tahunan dan Skor Belanja untuk Optimalisasi Strategi Pemasaran Manajerial

---

**Mata Kuliah:** Machine Learning / Data Mining  
**Pokok Bahasan:** Clustering (Unsupervised Learning)  
**Dataset:** `Clustering_KMeans_Mall_Customers.xlsx` (200 Data Pelanggan)  
**Dokumentasi Program:** `kmeans_mall_customers.py`, `kmeans_mall_customers.ipynb`, `Presentasi_Segmentasi_Mall_Customers.pptx`, `Hasil_Segmentasi_Pelanggan_Mall.xlsx`  

---

## 1. PENDAHULUAN & INDIKATOR CAPAIAN

### 1.1 Indikator Pembelajaran
1. Mahasiswa mampu menjelaskan konsep dasar klastering (*clustering*) dan perbedaannya dengan metode klasifikasi (*supervised learning*).
2. Mahasiswa mampu memahami alur kerja dan formulasi matematis algoritma K-Means (perhitungan jarak Euclidean, rekalkulasi centroid, serta kriteria konvergensi).
3. Mahasiswa mampu menyelesaikan studi kasus nyata segmentasi pelanggan menggunakan perhitungan bertahap (*spreadsheet/Excel*) dan program komputasi (*Python*).
4. Mahasiswa mampu menganalisis hasil pengelompokan (*profiling*) dan merumuskan rekomendasi strategi bisnis yang aplikatif berdasarkan temuan data.

### 1.2 Latar Belakang Masalah (Skenario Manajer Mall)
> *"Bayangkan kalian adalah seorang manajer mall. Kalian memiliki 200 data pelanggan. Setiap pelanggan memiliki informasi usia, pendapatan tahunan, dan skor belanja. Sebagai manajer, kalian ingin mengetahui karakteristik pelanggan agar dapat membuat strategi pemasaran yang tepat."*

Dalam persaingan pusat perbelanjaan (*shopping mall*) modern, pendekatan pemasaran massal (*mass marketing / one-size-fits-all*) telah terbukti tidak efisien dan menghamburkan anggaran promosi. Pelanggan memiliki variasi daya beli (*Annual Income*) dan kecenderungan berbelanja (*Spending Score*) yang sangat beragam:
- Terdapat kelompok pelanggan berdaya beli tinggi yang gemar membelanjakan uangnya (kandidat program VIP).
- Terdapat kelompok berpendapatan tinggi yang sangat hemat dan selektif (membutuhkan promosi eksklusif bernilai guna).
- Terdapat kelompok berpendapatan terbatas namun memiliki kecenderungan belanja impulsif tinggi (memerlukan program promo cicilan atau flash sale).
- Serta kelompok mayoritas berpendapatan sedang yang menopang stabilitas omset mall sehari-hari.

Oleh karena itu, algoritma **K-Means Clustering** digunakan sebagai solusi objektif berbasis data untuk mengelompokkan 200 pelanggan mall tersebut secara otomatis ke dalam kluster-kluster homogen.

---

## 2. DASAR TEORI

### 2.1 Definisi Clustering (Unsupervised Learning)
*Clustering* adalah cabang pembelajaran mesin tanpa pengawasan (*unsupervised learning*) yang bertujuan untuk mengorganisasi sekumpulan objek atau data ke dalam beberapa kelompok (*cluster*) sedemikian rupa sehingga objek-objek dalam satu kelompok memiliki tingkat kemiripan (*homogeneity/similarity*) yang tinggi, sedangkan antar kelompok memiliki perbedaan (*heterogeneity/dissimilarity*) yang signifikan.

Berbeda dengan *supervised learning* (seperti regresi atau klasifikasi), data pada clustering tidak memiliki target atau label kelas awal (*unlabeled data*). Algoritma bertugas menemukan struktur dan pola tersembunyi (*latent patterns*) dari fitur-fitur data.

### 2.2 Mekanisme Algoritma K-Means
Algoritma K-Means pertama kali diperkenalkan oleh MacQueen (1967) dan distandarisasi oleh Lloyd (1982). Algoritma ini mempartisi $N$ data ke dalam $K$ kluster secara iteratif dengan meminimalkan jumlah kuadrat jarak antara data dengan pusat kluster masing-masing (*Centroid*).

Langkah-langkah sistematis K-Means adalah:
1. **Menentukan Jumlah Kluster ($K$):** Menetapkan banyak kelompok yang akan dibentuk.
2. **Inisialisasi Centroid Awal:** Memilih $K$ titik awal sebagai pusat kluster ($C_1, C_2, \dots, C_k$). Titik ini dapat ditentukan secara acak, dipilih dari data tertentu, atau menggunakan algoritma *K-Means++*.
3. **Menghitung Jarak Data ke Centroid (Jarak Euclidean):** Jarak antara setiap data $x_i = (x_{i1}, x_{i2}, \dots, x_{im})$ dengan centroid $c_k = (c_{k1}, c_{k2}, \dots, c_{km})$ dihitung dengan rumus Euclidean:
   $$d(x_i, c_k) = \sqrt{\sum_{j=1}^{m} (x_{ij} - c_{kj})^2}$$
4. **Penentuan Keanggotaan Kluster:** Setiap data $x_i$ dialokasikan ke kluster yang memiliki centroid terdekat (jarak minimum):
   $$\text{Kluster}(x_i) = \arg\min_{k \in \{1, \dots, K\}} d(x_i, c_k)$$
5. **Menghitung Ulang Posisi Centroid Baru:** Centroid baru dihitung sebagai rata-rata aritmatika (*mean*) dari seluruh titik data anggota kluster tersebut:
   $$c_k^{\text{baru}} = \frac{1}{|S_k|} \sum_{x \in S_k} x$$
   di mana $S_k$ adalah himpunan data anggota kluster $k$, dan $|S_k|$ adalah jumlah anggotanya.
6. **Pemeriksaan Kondisi Berhenti (Konvergensi):** Mengulangi langkah 3 sampai 5 hingga kriteria konvergensi terpenuhi:
   - Keanggotaan kluster tidak mengalami perubahan lagi (jumlah anggota yang berpindah kluster = 0).
   - Perubahan posisi centroid bernilai sangat kecil ($\Delta c \approx 0$).
   - Batas maksimum iterasi (*maximum iteration*) tercapai.

### 2.3 Evaluasi Kualitas Kluster
1. **Within-Cluster Sum of Squares (WCSS / Inertia):**
   $$WCSS = \sum_{k=1}^{K} \sum_{x \in S_k} ||x - c_k||^2$$
   Nilai WCSS digunakan dalam **Metode Elbow**, di mana titik belokan tajam (*elbow point*) menunjukkan nilai $K$ yang paling efisien sebelum penambahan kluster baru hanya memberikan penurunan variansi marjinal.
2. **Analisis Silhouette Coefficient:**
   Mengukur seberapa dekat suatu titik dengan kluster tetangganya dibandingkan dengan kluster tempat ia bernaung:
   $$s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}$$
   Rentang nilai $s(i) \in [-1, 1]$. Nilai mendekati +1 mengindikasikan bahwa data terpisah sangat baik dari kluster lain dan sangat kompak di klusternya sendiri.

---

## 3. DESKRIPSI DATASET & EKSPLORASI DATA (EDA)

Dataset yang digunakan bersumber dari file `Clustering_KMeans_Mall_Customers.xlsx` pada sheet `DataAwal`, yang memuat 200 observasi pelanggan mall:
- **Pelanggan:** Kode identifikasi pelanggan ($P_1$ sampai $P_{200}$).
- **Pendapatan Tahunan (Annual Income):** Pendapatan tahunan pelanggan dalam ribuan dolar ($k\$$).
- **Skor Belanja (Spending Score):** Skor perilaku belanja yang diberikan oleh pihak manajemen mall dalam skala 1 hingga 100 berdasarkan riwayat transaksi.

### 3.1 Ringkasan Statistik Deskriptif

| Parameter Statistik | Pendapatan Tahunan (k$) | Skor Belanja (1-100) |
| :--- | :---: | :---: |
| **Jumlah Data (Count)** | 200 | 200 |
| **Nilai Rata-rata (Mean)** | 60.56 | 50.20 |
| **Standar Deviasi (Std)** | 26.26 | 25.82 |
| **Nilai Minimum (Min)** | 15.00 | 1.00 |
| **Kuartil 1 ($Q_1$ / 25%)** | 41.50 | 34.75 |
| **Median (50%)** | 61.50 | 50.00 |
| **Kuartil 3 ($Q_3$ / 75%)** | 78.00 | 73.00 |
| **Nilai Maksimum (Max)** | 137.00 | 99.00 |

> **Catatan Analisis Skala Fitur:**  
> Rentang nilai kedua fitur berada pada skala yang setara (pendapatan berkisar 15–137 dan skor belanja berkisar 1–99). Oleh sebab itu, perhitungan jarak Euclidean secara langsung pada data asli mempertahankan kejelasan satuan bisnis ($k\$$ dan skor belanja) tanpa distorsi bobot jarak antar fitur, persis seperti yang dirancang pada spreadsheet Excel.

---

## 4. VALIDASI PERHITUNGAN MANUAL EXCEL VS PROGRAM PYTHON

Pada sheet `Parameter` di file Excel, ditentukan konfigurasi awal $K = 5$ dengan centroid awal:
- **$C_1$ (dari Pelanggan $P_{13}$):** $(20, 15)$
- **$C_2$ (dari Pelanggan $P_{16}$):** $(20, 79)$
- **$C_3$ (dari Pelanggan $P_{167}$):** $(86, 20)$
- **$C_4$ (dari Pelanggan $P_{172}$):** $(87, 75)$
- **$C_5$ (dari Pelanggan $P_{81}$):** $(54, 51)$

### 4.1 Perbandingan Hasil Tiap Tahap Iterasi

Tabel berikut membuktikan keabsahan perhitungan manual Excel yang telah dihitung dan divalidasi silang menggunakan simulasi algoritma Python:

| Iterasi | Kluster | Jumlah Anggota (Excel) | Jumlah Anggota (Python) | Koordinat Centroid Baru $(X_{\text{income}}, Y_{\text{score}})$ | Anggota Berpindah | Status Konvergensi |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Iterasi 1** | $C_1$  <br>$C_2$  <br>$C_3$  <br>$C_4$  <br>$C_5$ | 21  <br>21  <br>38  <br>39  <br>81 | 21  <br>21  <br>38  <br>39  <br>81 | $(25.14, 19.52)$  <br>$(25.10, 80.05)$  <br>$(87.00, 18.63)$  <br>$(86.54, 82.13)$  <br>$(54.02, 49.85)$ | - | Belum Konvergen |
| **Iterasi 2** | $C_1$  <br>$C_2$  <br>$C_3$  <br>$C_4$  <br>$C_5$ | 22  <br>22  <br>37  <br>39  <br>80 | 22  <br>22  <br>37  <br>39  <br>80 | $(25.73, 20.23)$  <br>$(25.73, 79.36)$  <br>$(87.43, 18.19)$  <br>$(86.54, 82.13)$  <br>$(54.63, 49.66)$ | 3 data | Belum Konvergen |
| **Iterasi 3** | $C_1$  <br>$C_2$  <br>$C_3$  <br>$C_4$  <br>$C_5$ | 23  <br>22  <br>36  <br>39  <br>80 | 23  <br>22  <br>36  <br>39  <br>80 | $(26.30, 20.91)$  <br>$(25.73, 79.36)$  <br>$(87.75, 17.58)$  <br>$(86.54, 82.13)$  <br>$(55.09, 49.71)$ | 2 data | Belum Konvergen |
| **Iterasi 4** | $C_1$  <br>$C_2$  <br>$C_3$  <br>$C_4$  <br>$C_5$ | **23**  <br>**22**  <br>**36**  <br>**39**  <br>**80** | **23**  <br>**22**  <br>**36**  <br>**39**  <br>**80** | **$(26.30, 20.91)$**  <br>**$(25.73, 79.36)$**  <br>**$(87.75, 17.58)$**  <br>**$(86.54, 82.13)$**  <br>**$(55.09, 49.71)$** | **0 data** | **KONVERGEN!** |

> **Kesimpulan Validasi:**  
> Hasil perhitungan pada spreadsheet `Clustering_KMeans_Mall_Customers.xlsx` (Sheet Iterasi 1 s.d. 4 dan Sheet Evaluasi) terbukti **100% akurat dan identik** dengan hasil komputasi script Python. Tidak ada satupun selisih nilai, membuktikan bahwa perhitungan manual yang telah dibuat sudah benar dan teliti.

---

## 5. BUKTI MATEMATIS PENENTUAN JUMLAH KLUSTER OPTIMAL ($K$)

Untuk menguji apakah pemilihan $K = 5$ merupakan keputusan yang tepat secara ilmiah, dilakukan pengujian parameter kluster untuk $K = 1$ hingga $K = 10$:

| Nilai $K$ | WCSS / Inertia | Silhouette Score | Davies-Bouldin Index | Calinski-Harabasz Index | Keterangan Evaluasi |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **$K=2$** | 181,363.60 | 0.2969 | 1.2568 | 96.75 | Pemisahan terlalu kasar |
| **$K=3$** | 106,348.37 | 0.4676 | 0.7153 | 151.56 | Kluster masih heterogen |
| **$K=4$** | 73,679.79 | 0.4932 | 0.7104 | 174.06 | Belum optimal |
| **$K=5$** | **44,448.46** | **0.5539** | **0.5726** | **247.36** | **OPTIMAL GLOBAL (Elbow & Silhouette Peak)** |
| **$K=6$** | 37,233.81 | 0.5398 | 0.6522 | 242.54 | Silhouette menurun |
| **$K=7$** | 30,241.34 | 0.5288 | 0.7108 | 255.00 | Mengalami over-segmentasi |
| **$K=8$** | 25,036.42 | 0.4548 | 0.7594 | 268.35 | Kualitas partisi menurun |

**Interpretasi Hasil:**
1. **Metode Elbow:** Penurunan nilai *inertia* melambat secara tajam tepat di $K = 5$ (membentuk sudut siku-siku / *elbow*). Penambahan kluster setelah $K = 5$ tidak memberikan keuntungan variansi yang signifikan.
2. **Silhouette Score:** Puncak tertinggi koefisien siluet dicapai pada $K = 5$ dengan nilai **0.5539**. Nilai di atas 0.5 menunjukkan struktur kluster yang kuat (*strong clustering structure*).
3. **Davies-Bouldin Index:** Nilai terendah (terbaik) dicapai pada $K = 5$ sebesar **0.5726**, menandakan rasio jarak dalam kluster terhadap jarak antar kluster adalah yang paling optimal.

---

## 6. PROFILING 5 SEGMEN PELANGGAN & STRATEGI PEMASARAN MANAJERIAL

Berdasarkan posisi koordinat kuadran $(X_{\text{income}}, Y_{\text{score}})$, 200 pelanggan mall terbagi ke dalam 5 profil persona yang memiliki perilaku berbeda:

```
              Skor Belanja (1-100)
                   ^
    (Low Inc,      |      (High Inc,
     High Spend)   |       High Spend)
       KLUSTER 2   |       KLUSTER 4
      [Impulsif]   |        [VIP]
                   |
       -------------------------> Pendapatan Tahunan (k$)
                   |      
       KLUSTER 1   |       KLUSTER 3
        [Hemat]    |     [Konservatif]
    (Low Inc,      |      (High Inc,
     Low Spend)    |       Low Spend)
                   |
             KLUSTER 5 (Pusat)
             [Moderat / Rata-rata]
```

### Rincian Profil & Rekomendasi Aksi Nyata Manajerial:

#### 1. Kluster 1: Sensible / Budget Customers (Pendapatan Rendah, Skor Belanja Rendah)
- **Centroid:** Pendapatan \$26.30k, Skor Belanja 20.91
- **Jumlah Anggota:** 23 pelanggan (11.5% dari populasi)
- **Karakteristik Perilaku:** Pelanggan yang berhemat dan berhati-hati dalam membelanjakan uang. Mereka sangat sensitif terhadap harga dan memprioritaskan kebutuhan esensial.
- **Strategi Pemasaran Manajer Mall:**
  - Luncurkan program kupon diskon langsung (*direct price cut*) dan voucher belanja kebutuhan pokok harian (*supermarket groceries*).
  - Promo *bundling* produk hemat (*buy 1 get 1 free* atau paket hemat akhir bulan).
  - Event pameran diskon berkala seperti "Pasar Murah Mall" untuk menarik kunjungan fisik mereka ke mall.

#### 2. Kluster 2: Impulsive / Trend Spenders (Pendapatan Rendah, Skor Belanja Tinggi)
- **Centroid:** Pendapatan \$25.73k, Skor Belanja 79.36
- **Jumlah Anggota:** 22 pelanggan (11.0% dari populasi)
- **Karakteristik Perilaku:** Mayoritas kelompok usia muda (*Gen-Z / Millennials*), menyukai gaya hidup, tren fashion kekinian, nongkrong di café/F&B, dan belanja spontan tanpa terlalu mengkhawatirkan anggaran tabungan.
- **Strategi Pemasaran Manajer Mall:**
  - Promosi *Flash Sale* akhir pekan (*midnight sale*) pada merchant pakaian, kosmetik, dan aksesoris.
  - Kerja sama dengan platform fintech untuk menyediakan opsi cicilan 0% dan *Buy Now Pay Later* (BNPL).
  - Penyelenggaraan event tematik yang *Instagramable*, pameran sneakers, live music, dan diskon F&B (*food & beverage*).

#### 3. Kluster 3: Conservative / Careful Customers (Pendapatan Tinggi, Skor Belanja Rendah)
- **Centroid:** Pendapatan \$87.75k, Skor Belanja 17.58
- **Jumlah Anggota:** 36 pelanggan (18.0% dari populasi)
- **Karakteristik Perilaku:** Konsumen matang dan mapan secara finansial namun bersikap rasional dan skeptis terhadap promosi murahan. Mereka hanya membelanjakan uang jika produk memiliki kualitas unggul, nilai investasi, atau fungsi jangka panjang yang jelas.
- **Strategi Pemasaran Manajer Mall:**
  - Jangan gunakan promosi diskon heboh (*hard-selling*); gunakan pendekatan *value-focused marketing*.
  - Tawarkan produk bernilai investasi tinggi (elektronik premium, furnitur berkelas, asuransi, perhiasan, otomotif).
  - Undangan seminar finansial, workshop gaya hidup sehat (*wellness*), serta garansi kepuasan atau layanan purna jual premium.

#### 4. Kluster 4: VIP / High Spenders "Sultan" (Pendapatan Tinggi, Skor Belanja Tinggi)
- **Centroid:** Pendapatan \$86.54k, Skor Belanja 82.13
- **Jumlah Anggota:** 39 pelanggan (19.5% dari populasi)
- **Karakteristik Perilaku:** **Segmen paling bernilai (*Highest Value Segment*)** bagi mall. Memiliki daya beli berlimpah sekaligus antusiasme tinggi terhadap belanja merek mewah (*luxury brands*), eksklusivitas, dan pelayanan istimewa.
- **Strategi Pemasaran Manajer Mall:**
  - Luncurkan program loyalitas tier tertinggi (*Black Card VIP Membership*).
  - Fasilitas eksklusif: Ruang tunggu *VIP Lounge*, layanan asisten belanja pribadi (*Personal Shopper*), dan parkir valet gratis (*Free Valet Service*).
  - Undangan khusus ke *Private Trunk Show*, pre-order koleksi desainer internasional sebelum dirilis ke publik, serta *champagne networking gathering*.

#### 5. Kluster 5: Middle Class / Moderate Average (Pendapatan Sedang, Skor Belanja Sedang)
- **Centroid:** Pendapatan \$55.09k, Skor Belanja 49.71
- **Jumlah Anggota:** 80 pelanggan (40.0% dari populasi - **Mayoritas Terbesar**)
- **Karakteristik Perilaku:** Tulang punggung arus kunjungan (*traffic*) harian mall. Mewakili keluarga kelas menengah yang datang ke mall untuk berbelanja bulanan rutin, menonton bioskop, makan bersama keluarga, dan berekreasi.
- **Strategi Pemasaran Manajer Mall:**
  - Program loyalitas akumulasi poin belanja berhadiah langsung (*reward points program*).
  - Paket promosi kombo keluarga (misalnya tiket bioskop + voucher restoran keluarga).
  - Pesta diskon musiman pada momen liburan sekolah, hari raya besar keagamaan, dan perayaan tahun baru (*seasonal family fair*).

---

## 7. STRUKTUR PROGRAM PYTHON & FILE OUTPUT

Seluruh kode pemrograman dasar dari panduan praktikum PDF telah dikembangkan secara signifikan menjadi sistem komputasi modular yang rapi:

### Daftar File dalam Proyek:
1. `kmeans_mall_customers.py`: Script otomatisasi lengkap (EDA, validasi iterasi manual, Elbow & Silhouette, visualisasi, dan ekspor data).
2. `kmeans_mall_customers.ipynb`: Notebook interaktif terstruktur dengan visualisasi inline dan penjelasan naratif Markdown.
3. `create_presentation.py` & `Presentasi_Segmentasi_Mall_Customers.pptx`: Slide presentasi PowerPoint 16:9 berstandar profesional (10 slide) dengan gambar visualisasi tertanam.
4. `Hasil_Segmentasi_Pelanggan_Mall.xlsx`: File spreadsheet hasil segmentasi lengkap berisi 4 sheet:
   - `Data_Segmentasi_Lengkap`: 200 pelanggan dengan label kluster dan nama segmen.
   - `Ringkasan_Profil_Kluster`: Tabel rekapitulasi anggota dan centroid.
   - `Riwayat_Iterasi_Manual`: Catatan matematis pergerakan centroid iterasi 1 s.d. 4.
   - `Strategi_Pemasaran_Mall`: Panduan implementasi manajerial mall.
5. Folder `output_results/`:
   - `01_eda_distributions.png`: Grafik distribusi pendapatan dan skor belanja.
   - `02_manual_iteration_steps.png`: Grafik evolusi 4 tahap iterasi manual.
   - `03_elbow_and_silhouette.png`: Kurva penentuan K optimal.
   - `04_final_clusters_scatter.png`: Peta sebaran 5 kluster dan posisi centroid.
   - `05_cluster_profiling_barchart.png`: Diagram batang komparasi rata-rata antar kluster.

---

## 8. KESIMPULAN

1. **Pemahaman Algoritma:** Algoritma K-Means terbukti sangat andal dan efisien untuk menyelesaikan permasalahan segmentasi data numerik multidimensi tanpa label (*unsupervised*). Mekanisme pembaharuan centroid rata-rata secara iteratif berhasil meminimalkan variansi dalam kelompok (*within-cluster variance*).
2. **Ketelitian Perhitungan Manual:** Proses perhitungan berulang yang disusun pada file `Clustering_KMeans_Mall_Customers.xlsx` terkonfirmasi **100% konsisten dan identik secara matematis** dengan eksekusi algoritma pada Python, di mana kondisi konvergen tercapai pada Iterasi ke-4 dengan 0 data berpindah kluster.
3. **Konfirmasi Ilmiah Nilai K:** Berdasarkan evaluasi Metode Elbow (*WCSS*) dan Silhouette Analysis, konfigurasi **$K = 5$** adalah nilai paling ideal dengan Silhouette Score tertinggi sebesar **0.5539** dan Davies-Bouldin Index terendah sebesar **0.5726**.
4. **Implikasi Bisnis Praktis:** Hasil segmentasi memberikan pemetaan yang sangat jelas bagi manajer mall dalam membagi 200 pelanggan ke dalam 5 kelompok strategis (Hemat, Impulsif, Konservatif, VIP, dan Moderat). Dengan strategi pemasaran terarah (*targeted marketing*), mall dapat meningkatkan efisiensi anggaran belanja promosi, memaksimalkan loyalitas pelanggan VIP, dan mendongkrak total pendapatan bisnis secara berkelanjutan.

---

## 9. DAFTAR PUSTAKA / REFERENSI

1. MacQueen, J. (1967). *Some methods for classification and analysis of multivariate observations*. In Proceedings of the fifth Berkeley symposium on mathematical statistics and probability (Vol. 1, No. 14, pp. 281-297).
2. Lloyd, S. (1982). *Least squares quantization in PCM*. IEEE Transactions on Information Theory, 28(2), 129-137.
3. Rousseeuw, P. J. (1987). *Silhouettes: a graphical aid to the interpretation and validation of cluster analysis*. Journal of Computational and Applied Mathematics, 20, 53-65.
4. Pedregosa, F., et al. (2011). *Scikit-learn: Machine Learning in Python*. Journal of Machine Learning Research, 12, 2825-2830.
5. Arthur, D., & Vassilvitskii, S. (2007). *k-means++: The advantages of careful seeding*. In Proceedings of the eighteenth annual ACM-SIAM symposium on Discrete algorithms (pp. 1027-1035).
6. Han, J., Kamber, M., & Pei, J. (2012). *Data Mining: Concepts and Techniques (3rd ed.)*. Morgan Kaufmann Publishers.

