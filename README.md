# Segmentasi Pelanggan Mall Menggunakan Algoritma K-Means (Mall Customers Clustering)

> **Catatan:** Proyek ini dibuat sebagai pemenuhan **Tugas / Laporan Praktikum Mata Kuliah Machine Learning / Data Mining** (Topik: *Clustering dengan Algoritma K-Means*).

---

## 📌 Deskripsi Proyek
Proyek ini melakukan analisis klastering (*Unsupervised Learning*) untuk segmentasi 200 pelanggan pusat perbelanjaan (*shopping mall*) berdasarkan dua atribut utama:
1. **Annual Income (k$)**: Pendapatan tahunan pelanggan dalam ribuan dollar.
2. **Spending Score (1-100)**: Skor kebiasaan belanja pelanggan yang diberikan oleh pihak mall berdasarkan perilaku transaksi.

Tujuan utama dari proyek ini adalah mengidentifikasi kelompok-kelompok (*cluster*) pelanggan secara objektif berbasis data guna membantu pihak manajemen mall dalam merumuskan strategi pemasaran yang tepat sasaran, efektif, dan efisien.

---

## 🎯 Indikator Capaian & Tujuan Pembelajaran
1. Memahami konsep dasar *Unsupervised Learning* khususnya klastering serta perbedaannya dengan *Supervised Learning*.
2. Memahami alur matematis algoritma K-Means (perhitungan jarak Euclidean, alokasi kluster terdekat, rekalkulasi centroid baru, dan kriteria konvergensi).
3. Melakukan validasi hasil perhitungan bertahap secara manual (*spreadsheet / Excel*) dengan implementasi program komputasi (*Python*).
4. Melakukan evaluasi kluster menggunakan **Metode Elbow (WCSS / Inertia)** dan **Silhouette Score**.
5. Menganalisis karakteristik tiap segmen (*profiling*) dan menyusun rekomendasi strategi manajerial mall yang aplikatif.

---

## 📂 Struktur Repositori

```text
├── output_results/                          # Direktori output grafik visualisasi (.png)
│   ├── 01_eda_distributions.png             # Distribusi fitur pendapatan & skor belanja
│   ├── 02_manual_iteration_steps.png        # Visualisasi pergerakan centroid iterasi 1 - konvergen
│   ├── 03_elbow_and_silhouette.png          # Grafik Elbow Method & Silhouette Coefficient
│   ├── 04_final_clusters_scatter.png        # Scatter plot hasil klastering akhir
│   └── 05_cluster_profiling_barchart.png    # Bar chart profil rata-rata tiap kluster
├── Clustering_KMeans_Mall_Customers.xlsx    # Dataset & simulasi iterasi Excel manual
├── Hasil_Segmentasi_Pelanggan_Mall.xlsx      # Output hasil segmentasi dan label kluster
├── 20261030_132346_63e7868d_Clustering_K-Means.pdf # Dokumen panduan / modul praktikum
├── Laporan_Praktikum_KMeans_Mall_Customers.md      # Laporan lengkap praktikum
├── Presentasi_Segmentasi_Mall_Customers.pptx       # Slide presentasi manajerial
├── kmeans_mall_customers.py                 # Script utama pemodelan K-Means Python
├── kmeans_mall_customers.ipynb              # Jupyter Notebook interaktif
├── create_notebook.py                       # Script pembantu pembuatan notebook
├── create_presentation.py                   # Script pembantu pembuatan slide presentasi
├── make_gallery.py                          # Script utilitas galeri gambar
├── perkembangan konvergensi.png             # Grafik riwayat konvergensi centroid
└── README.md                                # Dokumentasi proyek
```

---

## 🔬 Metodologi & Alur Eksperimen

1. **Eksplorasi Data (EDA):**
   - Menganalisis sebaran data `Annual Income` (15 - 137 k$) dan `Spending Score` (1 - 99).
   - Menghitung statistik deskriptif (*mean, median, standard deviation, interquartile range*).

2. **Simulasi Perhitungan Manual (Excel):**
   - Menetapkan $K = 5$ dengan inisialisasi centroid awal dari pelanggan data riil ($P_{13}, P_{16}, P_{35}, P_{47}, P_{60}$).
   - Menghitung jarak Euclidean untuk 200 data, menentukan kluster minimum, menghitung centroid baru, dan mengamati proses konvergensi hingga tidak ada pergeseran anggota kluster.

3. **Evaluasi Penentuan Nilai K Optimal:**
   - **Elbow Method:** Mengamati titik belokan tajam (*elbow*) pada kurva WCSS (*Within-Cluster Sum of Squares*).
   - **Silhouette Analysis:** Menguji kualitas pemisahan kluster untuk rentang nilai $K = 2$ hingga $K = 8$. Nilai optimal terkonfirmasi pada $K = 5$.

4. **Implementasi & Verifikasi Program Python:**
   - Memvalidasi konsistensi hasil algoritma manual dengan pustaka `scikit-learn`.

---

## 📊 Hasil Segmentasi & Profiling Kluster ($K = 5$)

Berdasarkan hasil analisis, 200 pelanggan terbagi menjadi 5 segmen karakteristik:

| Kluster | Nama Segmen | Pendapatan Tahunan | Skor Belanja | Karakteristik & Rekomendasi Bisnis |
| :---: | :--- | :---: | :---: | :--- |
| **0** | **Target Utama (VIP)** | Tinggi | Tinggi | Pelanggan loyal dengan daya beli tinggi. Strategi: *Loyalty program VIP, exclusive lounge, private preview sale*, layanan *personal shopper*. |
| **1** | **Rasional / Menengah** | Sedang | Sedang | Segmen mayoritas yang menjaga stabilitas omset mall. Strategi: Promo *cashback*, diskon akhir pekan, program poin belanja keluarga. |
| **2** | **Hemat / Selektif** | Tinggi | Rendah | Berpenghasilan tinggi tetapi sangat cermat. Strategi: Penawaran produk fungsional/investasi, diskon musiman *branded*, promosi bernilai guna tinggi. |
| **3** | **Impulsif / Pemboros** | Rendah | Tinggi | Berpenghasilan rendah namun antusiasme belanja tinggi (biasanya usia muda). Strategi: Promo *flash sale*, cicilan 0%, bundling hemat, kafe/hiburan terjangkau. |
| **4** | **Hemat Ekstrem / Hati-hati** | Rendah | Rendah | Berpenghasilan terbatas dan belanja seperlunya. Strategi: Promo kebutuhan pokok harian (*supermarket promo*), diskon kupon, bazar murah. |

---

## 💻 Cara Menjalankan Proyek

### 1. Clone Repositori
```bash
git clone https://github.com/yunikyuroidah/Mall_Customers_KMeans.git
cd Mall_Customers_KMeans
```

### 2. Persiapan Environment & Dependensi
Pastikan telah menginstal Python (>= 3.8). Pasang pustaka yang diperlukan:
```bash
pip install numpy pandas matplotlib seaborn scikit-learn openpyxl
```

### 3. Menjalankan Script Pemodelan
```bash
python kmeans_mall_customers.py
```
Hasil visualisasi akan otomatis disimpan ke dalam folder `output_results/` dan segmentasi lengkap diekspor ke file Excel.

### 4. Menjalankan Jupyter Notebook
Jika ingin menjalankan secara interaktif:
```bash
jupyter notebook kmeans_mall_customers.ipynb
```

---

## 👤 Pembuat Proyek
- **Nama / Akun GitHub:** [@yunikyuroidah](https://github.com/yunikyuroidah)
- **Repositori:** [Mall_Customers_KMeans](https://github.com/yunikyuroidah/Mall_Customers_KMeans)
- **Topik:** Tugas Praktikum Machine Learning - Segmentasi Pelanggan Menggunakan K-Means
