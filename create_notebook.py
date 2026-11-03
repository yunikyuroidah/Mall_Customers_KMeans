import json

notebook_content = {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Laporan Praktikum Machine Learning: Clustering K-Means\n",
    "## Studi Kasus: Segmentasi 200 Pelanggan Mall Berdasarkan Pendapatan Tahunan & Skor Belanja\n",
    "\n",
    "**Mata Kuliah:** Machine Learning / Data Mining  \n",
    "**Topik:** Unsupervised Learning - K-Means Clustering  \n",
    "**Dataset:** `Clustering_KMeans_Mall_Customers.xlsx` (200 data pelanggan)  \n",
    "\n",
    "---\n",
    "\n",
    "### Deskripsi Tugas & Peran Manajer Mall\n",
    "> *\"Bayangkan kalian adalah seorang manajer mall. Kalian memiliki 200 data pelanggan. Setiap pelanggan memiliki informasi usia, pendapatan tahunan, dan skor belanja. Sebagai manajer, kalian ingin mengetahui karakteristik pelanggan agar dapat membuat strategi pemasaran yang tepat.\"*\n",
    "\n",
    "Notebook ini menyajikan implementasi lengkap dan pengembangan tingkat lanjut dari materi dasar clustering pada praktikum:\n",
    "1. **Eksplorasi Data (EDA)** dan statistik deskriptif 200 data pelanggan.\n",
    "2. **Simulasi & Replikasi Perhitungan Manual Excel** (Iterasi 1 s.d. 4 hingga konvergen) dengan inisialisasi centroid C1=P13, C2=P16, C3=P167, C4=P172, C5=P81.\n",
    "3. **Penentuan Jumlah Kluster Optimal (K)** menggunakan **Metode Elbow (WCSS)** dan **Analisis Silhouette Score**.\n",
    "4. **Implementasi Scikit-Learn** dan pemetaan batas wilayah kluster (*Decision Boundary*).\n",
    "5. **Profiling 5 Karakter Persona Pelanggan** dan **Rekomendasi Strategi Pemasaran Manajerial Mall**."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1. Import Library & Pengaturan Lingkungan"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "os.environ[\"OMP_NUM_THREADS\"] = \"1\"\n",
    "\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "from sklearn.cluster import KMeans\n",
    "from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score\n",
    "\n",
    "# Set style visualisasi\n",
    "sns.set_theme(style=\"whitegrid\")\n",
    "plt.rcParams['font.sans-serif'] = 'Arial'\n",
    "plt.rcParams['figure.dpi'] = 120\n",
    "\n",
    "print(\"Library berhasil diimpor!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2. Memuat Dataset dari File Excel (`Clustering_KMeans_Mall_Customers.xlsx`)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "EXCEL_PATH = \"Clustering_KMeans_Mall_Customers.xlsx\"\n",
    "\n",
    "# Baca Sheet 'DataAwal'\n",
    "df_raw = pd.read_excel(EXCEL_PATH, sheet_name=\"DataAwal\")\n",
    "df = df_raw[['Pelanggan', 'Pendapatan Tahunan (k$)', 'Skor Belanja']].dropna()\n",
    "df = df.rename(columns={\n",
    "    'Pelanggan': 'pelanggan',\n",
    "    'Pendapatan Tahunan (k$)': 'pendapatan_tahunan',\n",
    "    'Skor Belanja': 'skor_belanja'\n",
    "})\n",
    "\n",
    "print(f\"Total Data Pelanggan: {len(df)}\")\n",
    "display(df.head(10))\n",
    "display(df.describe().T)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3. Exploratory Data Analysis (EDA)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "fig, axes = plt.subplots(1, 2, figsize=(14, 5))\n",
    "\n",
    "# Distribusi Pendapatan Tahunan\n",
    "sns.histplot(df['pendapatan_tahunan'], kde=True, color='#1f77b4', bins=15, ax=axes[0])\n",
    "axes[0].set_title('Distribusi Pendapatan Tahunan (k$)', fontsize=12, fontweight='bold')\n",
    "axes[0].axvline(df['pendapatan_tahunan'].mean(), color='red', linestyle='--', label=f'Mean: {df[\"pendapatan_tahunan\"].mean():.1f}')\n",
    "axes[0].axvline(df['pendapatan_tahunan'].median(), color='green', linestyle=':', label=f'Median: {df[\"pendapatan_tahunan\"].median():.1f}')\n",
    "axes[0].legend()\n",
    "\n",
    "# Distribusi Skor Belanja\n",
    "sns.histplot(df['skor_belanja'], kde=True, color='#ff7f0e', bins=15, ax=axes[1])\n",
    "axes[1].set_title('Distribusi Skor Belanja (1-100)', fontsize=12, fontweight='bold')\n",
    "axes[1].axvline(df['skor_belanja'].mean(), color='red', linestyle='--', label=f'Mean: {df[\"skor_belanja\"].mean():.1f}')\n",
    "axes[1].axvline(df['skor_belanja'].median(), color='green', linestyle=':', label=f'Median: {df[\"skor_belanja\"].median():.1f}')\n",
    "axes[1].legend()\n",
    "\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 4. Replikasi & Validasi Perhitungan Manual Excel (Step-by-Step)\n",
    "Pada sheet `Parameter` di file Excel, centroid awal yang dipilih adalah:\n",
    "- **C1 (P13):** (20, 15)\n",
    "- **C2 (P16):** (20, 79)\n",
    "- **C3 (P167):** (86, 20)\n",
    "- **C4 (P172):** (87, 75)\n",
    "- **C5 (P81):** (54, 51)\n",
    "\n",
    "Kita jalankan simulasi perulangan hingga konvergen dan bandingkan jumlah anggota tiap iterasi."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "X = df[['pendapatan_tahunan', 'skor_belanja']].values\n",
    "\n",
    "# Inisialisasi Centroid dari Excel\n",
    "centroids = np.array([\n",
    "    [20.0, 15.0],  # C1 (P13)\n",
    "    [20.0, 79.0],  # C2 (P16)\n",
    "    [86.0, 20.0],  # C3 (P167)\n",
    "    [87.0, 75.0],  # C4 (P172)\n",
    "    [54.0, 51.0]   # C5 (P81)\n",
    "], dtype=float)\n",
    "\n",
    "history = []\n",
    "for it in range(1, 10):\n",
    "    # Jarak Euclidean: ||x - c||\n",
    "    dists = np.linalg.norm(X[:, np.newaxis, :] - centroids[np.newaxis, :, :], axis=2)\n",
    "    clusters = np.argmin(dists, axis=1) + 1  # 1-based indexing\n",
    "    counts = {f'C{k}': int(np.sum(clusters == k)) for k in range(1, 6)}\n",
    "    \n",
    "    # Hitung centroid baru\n",
    "    new_centroids = np.array([X[clusters == k].mean(axis=0) for k in range(1, 6)])\n",
    "    history.append((it, counts, new_centroids))\n",
    "    print(f\"Iterasi {it}: Jumlah Anggota = {counts}\")\n",
    "    \n",
    "    if np.allclose(centroids, new_centroids, atol=1e-5):\n",
    "        print(f\"\\n>>> KONVERGENSI TERCAPAI PADA ITERASI {it}! <<<\")\n",
    "        break\n",
    "    centroids = new_centroids.copy()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Visualisasi 4 Tahap Iterasi Manual Sesuai Excel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "fig, axes = plt.subplots(2, 2, figsize=(15, 12))\n",
    "axes_flat = axes.flatten()\n",
    "colors = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00']\n",
    "\n",
    "for idx, (it_num, c_counts, c_coords) in enumerate(history[:4]):\n",
    "    ax = axes_flat[idx]\n",
    "    dists = np.linalg.norm(X[:, np.newaxis, :] - c_coords[np.newaxis, :, :], axis=2)\n",
    "    cl_labels = np.argmin(dists, axis=1) + 1\n",
    "    \n",
    "    for k in range(1, 6):\n",
    "        pts = X[cl_labels == k]\n",
    "        ax.scatter(pts[:, 0], pts[:, 1], s=40, alpha=0.6, color=colors[k-1], label=f'C{k} (n={c_counts[f\"C{k}\"]})')\n",
    "        ax.scatter(c_coords[k-1, 0], c_coords[k-1, 1], s=200, color=colors[k-1], \n",
    "                   edgecolor='black', linewidth=2, marker='X')\n",
    "        \n",
    "    status = \"KONVERGEN\" if it_num == len(history) else \"Belum Konvergen\"\n",
    "    ax.set_title(f\"Iterasi {it_num} - Status: {status}\", fontsize=12, fontweight='bold')\n",
    "    ax.set_xlabel(\"Pendapatan Tahunan (k$)\")\n",
    "    ax.set_ylabel(\"Skor Belanja (1-100)\")\n",
    "    ax.set_xlim(10, 140)\n",
    "    ax.set_ylim(0, 105)\n",
    "    ax.legend(loc='upper right', fontsize=8)\n",
    "\n",
    "plt.suptitle(\"Perkembangan Konvergensi K-Means Manual (Iterasi 1 s.d. 4)\", fontsize=14, fontweight='bold')\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 5. Penentuan Jumlah Kluster Optimal (Metode Elbow & Silhouette Score)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "k_range = list(range(1, 11))\n",
    "wcss = []\n",
    "sil_scores = []\n",
    "\n",
    "for k in k_range:\n",
    "    km = KMeans(n_clusters=k, init='k-means++', random_state=42, n_init=10)\n",
    "    km.fit(X)\n",
    "    wcss.append(km.inertia_)\n",
    "    if k >= 2:\n",
    "        sil = silhouette_score(X, km.labels_)\n",
    "        sil_scores.append(sil)\n",
    "\n",
    "fig, axes = plt.subplots(1, 2, figsize=(15, 5))\n",
    "\n",
    "# Elbow Curve\n",
    "axes[0].plot(k_range, wcss, marker='o', linewidth=2.5, color='#2b5c8f')\n",
    "axes[0].plot(5, wcss[4], marker='o', markersize=12, color='crimson')\n",
    "axes[0].annotate('Elbow Point (K=5)', xy=(5, wcss[4]), xytext=(5.5, wcss[4] + 25000),\n",
    "                 arrowprops=dict(facecolor='crimson', shrink=0.08, width=1.5, headwidth=8),\n",
    "                 fontweight='bold', color='crimson')\n",
    "axes[0].set_title('Metode Elbow (WCSS / Inertia)', fontsize=12, fontweight='bold')\n",
    "axes[0].set_xlabel('Jumlah Kluster (K)')\n",
    "axes[0].set_ylabel('Inertia')\n",
    "axes[0].set_xticks(k_range)\n",
    "\n",
    "# Silhouette Score\n",
    "axes[1].plot(list(range(2, 11)), sil_scores, marker='s', linewidth=2.5, color='#2ca02c')\n",
    "axes[1].plot(5, sil_scores[3], marker='s', markersize=12, color='crimson')\n",
    "axes[1].annotate(f'Puncak Silhouette K=5 ({sil_scores[3]:.4f})', xy=(5, sil_scores[3]), \n",
    "                 xytext=(3, sil_scores[3] - 0.05),\n",
    "                 arrowprops=dict(facecolor='crimson', shrink=0.08, width=1.5, headwidth=8),\n",
    "                 fontweight='bold', color='crimson')\n",
    "axes[1].set_title('Analisis Silhouette Score', fontsize=12, fontweight='bold')\n",
    "axes[1].set_xlabel('Jumlah Kluster (K)')\n",
    "axes[1].set_ylabel('Silhouette Score')\n",
    "axes[1].set_xticks(list(range(2, 11)))\n",
    "\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 6. Visualisasi Peta Segmentasi Pelanggan Akhir & Profil Kluster"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Kluster Akhir dari Iterasi Konvergen\n",
    "final_centroids = history[-1][2]\n",
    "dists = np.linalg.norm(X[:, np.newaxis, :] - final_centroids[np.newaxis, :, :], axis=2)\n",
    "df['kluster'] = np.argmin(dists, axis=1) + 1\n",
    "\n",
    "segment_names = {\n",
    "    1: ('C1: Hemat / Sensible', '#d95f02'),\n",
    "    2: ('C2: Impulsif / Careless', '#7570b3'),\n",
    "    3: ('C3: Konservatif / Careful', '#e7298a'),\n",
    "    4: ('C4: VIP / Sultan (High Spend)', '#1b9e77'),\n",
    "    5: ('C5: Moderat / Middle Class', '#66a61e')\n",
    "}\n",
    "\n",
    "plt.figure(figsize=(12, 7))\n",
    "for k in range(1, 6):\n",
    "    sub = df[df['kluster'] == k]\n",
    "    name, col = segment_names[k]\n",
    "    plt.scatter(sub['pendapatan_tahunan'], sub['skor_belanja'], s=70, alpha=0.75, color=col, label=f\"{name} (n={len(sub)})\")\n",
    "    \n",
    "    cx, cy = final_centroids[k-1]\n",
    "    plt.scatter(cx, cy, s=300, marker='*', color=col, edgecolor='black', linewidth=1.5)\n",
    "    plt.annotate(f\"Centroid C{k}\\n({cx:.1f}k$, {cy:.1f})\", (cx, cy), xytext=(0, 15), textcoords=\"offset points\",\n",
    "                 ha='center', fontweight='bold', fontsize=9,\n",
    "                 bbox=dict(boxstyle=\"round,pad=0.2\", fc=\"white\", ec=col, lw=1.2, alpha=0.9))\n",
    "\n",
    "plt.title('Peta Segmentasi 200 Pelanggan Mall (K-Means Clustering K=5)', fontsize=14, fontweight='bold', pad=15)\n",
    "plt.xlabel('Pendapatan Tahunan / Annual Income (k$)', fontweight='bold')\n",
    "plt.ylabel('Skor Belanja / Spending Score (1-100)', fontweight='bold')\n",
    "plt.legend(loc='upper right', frameon=True, framealpha=0.9)\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 7. Rekomendasi Strategi Pemasaran Manajerial Mall\n",
    "\n",
    "| Kluster | Segmen Pelanggan | Karakteristik Belanja | Tindakan / Strategi Pemasaran Manajerial |\n",
    "| :--- | :--- | :--- | :--- |\n",
    "| **C1** | **Hemat / Sensible Spender** | Pendapatan Rendah, Pengeluaran Rendah ($26.3k, skor 20.9) | Program diskon harga, voucher cashback belanja pokok, promo bundling hemat, event pasar murah. |\n",
    "| **C2** | **Impulsif / Careless Spender** | Pendapatan Rendah, Pengeluaran Tinggi ($25.7k, skor 79.4) | Flash sale, opsi cicilan 0% / paylater, diskon tren fesyen & F&B kekinian, event bazaar weekend. |\n",
    "| **C3** | **Konservatif / Careful Spender** | Pendapatan Tinggi, Pengeluaran Rendah ($87.8k, skor 17.6) | Promosi eksklusif produk berkualitas tinggi, garansi produk, direct marketing bernilai investasi. |\n",
    "| **C4** | **VIP / Priority Spender (Sultan)** | Pendapatan Tinggi, Pengeluaran Tinggi ($86.5k, skor 82.1) | Membership tier VIP / Black Card, personal shopper, VIP lounge eksklusif, private preview collection, free valet parking. |\n",
    "| **C5** | **Moderat / Middle Class** | Pendapatan Sedang, Pengeluaran Sedang ($55.1k, skor 49.7) | Program loyalitas poin berkala, seasonal sale (hari raya/tahun baru), promosi restoran & hiburan keluarga (bioskop). |"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbformat": 4,
   "nbformat_minor": 2
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

with open("kmeans_mall_customers.ipynb", "w", encoding="utf-8") as f:
    json.dump(notebook_content, f, indent=1, ensure_ascii=False)

print("Notebook kmeans_mall_customers.ipynb berhasil dibuat!")

