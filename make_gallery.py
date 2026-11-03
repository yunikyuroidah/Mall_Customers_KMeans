import base64
import os

artifact_dir = r"C:\Users\HP\.gemini\antigravity\brain\72c02476-0ca1-46c8-bc8c-ea70a7af107d"
os.makedirs(artifact_dir, exist_ok=True)

def get_b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

b64_elbow = get_b64("output_results/03_elbow_and_silhouette.png")
b64_scatter = get_b64("output_results/04_final_clusters_scatter.png")
b64_iter = get_b64("output_results/02_manual_iteration_steps.png")
b64_bar = get_b64("output_results/05_cluster_profiling_barchart.png")

html_content = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    .tab-btn.active {{ border-bottom: 3px solid #2563eb; color: #2563eb; font-weight: 700; }}
  </style>
</head>
<body class="bg-[var(--background)] text-[var(--foreground)] antialiased p-4 font-sans">
  <div class="max-w-5xl mx-auto space-y-6">
    <!-- Header -->
    <div class="bg-[var(--card)] border border-[var(--border)] rounded-2xl p-5 shadow-sm">
      <div class="flex flex-wrap items-center justify-between gap-3">
        <div>
          <span class="px-2.5 py-1 text-xs font-bold rounded-full bg-blue-500/10 text-blue-600 uppercase tracking-wide">Visualisasi K-Means</span>
          <h1 class="text-xl font-bold text-[var(--foreground)] mt-1.5">Galeri Diagram & Hasil Segmentasi Pelanggan Mall</h1>
          <p class="text-sm text-[var(--muted-foreground)] mt-0.5">Menampilkan Kurva Elbow, Silhouette Score, Persebaran Kluster Final, dan Tahapan Konvergensi Excel.</p>
        </div>
        <div class="text-xs text-[var(--muted-foreground)] bg-slate-100 dark:bg-slate-800 px-3 py-1.5 rounded-lg border border-[var(--border)]">
          Status: <strong class="text-emerald-600">Konvergen (Iterasi 4)</strong> | K = 5
        </div>
      </div>

      <!-- Navigation Tabs -->
      <div class="flex space-x-6 border-b border-[var(--border)] mt-5 text-sm overflow-x-auto">
        <button onclick="showTab('elbow')" id="btn-elbow" class="tab-btn active pb-2 transition-colors whitespace-nowrap">1. Diagram Elbow & Silhouette</button>
        <button onclick="showTab('scatter')" id="btn-scatter" class="tab-btn pb-2 text-[var(--muted-foreground)] transition-colors whitespace-nowrap">2. Diagram Persebaran Kluster Final</button>
        <button onclick="showTab('iter')" id="btn-iter" class="tab-btn pb-2 text-[var(--muted-foreground)] transition-colors whitespace-nowrap">3. Tahapan Iterasi Excel (1-4)</button>
        <button onclick="showTab('bar')" id="btn-bar" class="tab-btn pb-2 text-[var(--muted-foreground)] transition-colors whitespace-nowrap">4. Profiling Rata-Rata Antar Kluster</button>
      </div>
    </div>

    <!-- Tab 1: Elbow & Silhouette -->
    <div id="tab-elbow" class="tab-pane bg-[var(--card)] border border-[var(--border)] rounded-2xl p-5 shadow-sm space-y-4">
      <div class="flex items-start justify-between flex-wrap gap-2">
        <div>
          <h2 class="text-lg font-bold text-[var(--foreground)]">Metode Elbow & Analisis Silhouette Score</h2>
          <p class="text-sm text-[var(--muted-foreground)]">Bukti statistik matematis pemilihan jumlah kluster optimal (K = 5).</p>
        </div>
        <span class="text-xs bg-emerald-500/10 text-emerald-600 font-semibold px-2.5 py-1 rounded-full">Puncak Tertinggi: K=5 (Silhouette: 0.5539)</span>
      </div>
      <div class="rounded-xl overflow-hidden border border-[var(--border)] bg-white p-2">
        <img src="data:image/png;base64,{b64_elbow}" alt="Diagram Elbow & Silhouette" class="w-full h-auto rounded-lg object-contain" />
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs bg-slate-50 dark:bg-slate-900/50 p-3.5 rounded-xl border border-[var(--border)]">
        <div>
          <strong class="text-[var(--foreground)] block mb-1 text-sm font-semibold">1. Metode Elbow (Grafik Kiri):</strong>
          <p class="text-[var(--muted-foreground)] leading-relaxed">Grafik penurunan WCSS (Inertia) menunjukkan lekukan siku yang sangat tegas pada <strong>K = 5</strong> (Inertia = 44,448). Menambah K &gt; 5 hanya menghasilkan penurunan inersia yang sangat landai.</p>
        </div>
        <div>
          <strong class="text-[var(--foreground)] block mb-1 text-sm font-semibold">2. Koefisien Silhouette (Grafik Kanan):</strong>
          <p class="text-[var(--muted-foreground)] leading-relaxed">Nilai Silhouette mencapai puncak global tertinggi di <strong>K = 5</strong> sebesar <strong>0.5539</strong>. Ini membuktikan bahwa pembagian 5 kelompok adalah partisi paling optimal secara matematis.</p>
        </div>
      </div>
    </div>

    <!-- Tab 2: Final Cluster Scatter -->
    <div id="tab-scatter" class="tab-pane hidden bg-[var(--card)] border border-[var(--border)] rounded-2xl p-5 shadow-sm space-y-4">
      <div class="flex items-start justify-between flex-wrap gap-2">
        <div>
          <h2 class="text-lg font-bold text-[var(--foreground)]">Peta Persebaran 200 Pelanggan Mall (Final Cluster Map)</h2>
          <p class="text-sm text-[var(--muted-foreground)]">Visualisasi sebaran 200 pelanggan dalam 5 segmen persona beserta titik pusat koordinat (Centroid).</p>
        </div>
        <span class="text-xs bg-blue-500/10 text-blue-600 font-semibold px-2.5 py-1 rounded-full">Total: 200 Pelanggan</span>
      </div>
      <div class="rounded-xl overflow-hidden border border-[var(--border)] bg-white p-2">
        <img src="data:image/png;base64,{b64_scatter}" alt="Peta Persebaran Kluster" class="w-full h-auto rounded-lg object-contain" />
      </div>
      <div class="grid grid-cols-2 sm:grid-cols-5 gap-2 text-xs pt-1">
        <div class="p-2.5 rounded-xl border border-[var(--border)] bg-orange-500/5">
          <span class="font-bold text-orange-600 block text-sm">C1: Hemat</span>
          <span class="text-[var(--muted-foreground)] text-xs">23 orang (11.5%)</span>
          <p class="text-[var(--muted-foreground)] text-[11px] mt-1">Pendapatan Rendah, Belanja Rendah</p>
        </div>
        <div class="p-2.5 rounded-xl border border-[var(--border)] bg-purple-500/5">
          <span class="font-bold text-purple-600 block text-sm">C2: Impulsif</span>
          <span class="text-[var(--muted-foreground)] text-xs">22 orang (11.0%)</span>
          <p class="text-[var(--muted-foreground)] text-[11px] mt-1">Pendapatan Rendah, Belanja Tinggi</p>
        </div>
        <div class="p-2.5 rounded-xl border border-[var(--border)] bg-pink-500/5">
          <span class="font-bold text-pink-600 block text-sm">C3: Konservatif</span>
          <span class="text-[var(--muted-foreground)] text-xs">36 orang (18.0%)</span>
          <p class="text-[var(--muted-foreground)] text-[11px] mt-1">Pendapatan Tinggi, Belanja Rendah</p>
        </div>
        <div class="p-2.5 rounded-xl border border-[var(--border)] bg-emerald-500/5">
          <span class="font-bold text-emerald-600 block text-sm">C4: VIP (Sultan)</span>
          <span class="text-[var(--muted-foreground)] text-xs">39 orang (19.5%)</span>
          <p class="text-[var(--muted-foreground)] text-[11px] mt-1">Pendapatan Tinggi, Belanja Tinggi</p>
        </div>
        <div class="p-2.5 rounded-xl border border-[var(--border)] bg-lime-500/5">
          <span class="font-bold text-lime-600 block text-sm">C5: Moderat</span>
          <span class="text-[var(--muted-foreground)] text-xs">80 orang (40.0%)</span>
          <p class="text-[var(--muted-foreground)] text-[11px] mt-1">Pendapatan Sedang, Belanja Sedang</p>
        </div>
      </div>
    </div>

    <!-- Tab 3: Iteration Steps -->
    <div id="tab-iter" class="tab-pane hidden bg-[var(--card)] border border-[var(--border)] rounded-2xl p-5 shadow-sm space-y-4">
      <div class="flex items-start justify-between flex-wrap gap-2">
        <div>
          <h2 class="text-lg font-bold text-[var(--foreground)]">Validasi 4 Tahap Iterasi Manual Sesuai Excel</h2>
          <p class="text-sm text-[var(--muted-foreground)]">Pergerakan posisi centroid dan alokasi anggota dari Iterasi 1 hingga konvergen di Iterasi 4.</p>
        </div>
        <span class="text-xs bg-slate-500/10 text-[var(--foreground)] font-semibold px-2.5 py-1 rounded-full">Iterasi 1 s.d. 4</span>
      </div>
      <div class="rounded-xl overflow-hidden border border-[var(--border)] bg-white p-2">
        <img src="data:image/png;base64,{b64_iter}" alt="Tahapan Iterasi Manual" class="w-full h-auto rounded-lg object-contain" />
      </div>
      <p class="text-xs text-[var(--muted-foreground)] bg-slate-50 dark:bg-slate-900/50 p-3 rounded-xl border border-[var(--border)]">
        Perhitungan manual Excel dimulai dengan inisialisasi titik C1=P13, C2=P16, C3=P167, C4=P172, dan C5=P81. Pada Iterasi 1 ke 2 berpindah 3 data, Iterasi 2 ke 3 berpindah 2 data, dan pada Iterasi 3 ke 4 berpindah 0 data (status konvergen tercapai sempurna).
      </p>
    </div>

    <!-- Tab 4: Bar Chart Profiling -->
    <div id="tab-bar" class="tab-pane hidden bg-[var(--card)] border border-[var(--border)] rounded-2xl p-5 shadow-sm space-y-4">
      <div class="flex items-start justify-between flex-wrap gap-2">
        <div>
          <h2 class="text-lg font-bold text-[var(--foreground)]">Perbandingan Profil Rata-Rata Antar Kluster</h2>
          <p class="text-sm text-[var(--muted-foreground)]">Diagram komparasi nilai rata-rata pendapatan tahunan ($k) dan skor belanja (1-100) per kluster.</p>
        </div>
      </div>
      <div class="rounded-xl overflow-hidden border border-[var(--border)] bg-white p-2">
        <img src="data:image/png;base64,{b64_bar}" alt="Diagram Profil Kluster" class="w-full h-auto rounded-lg object-contain" />
      </div>
    </div>
  </div>

  <script>
    function showTab(tabId) {{
      document.querySelectorAll('.tab-pane').forEach(el => el.classList.add('hidden'));
      document.querySelectorAll('.tab-btn').forEach(el => {{
        el.classList.remove('active', 'text-blue-600', 'font-bold');
        el.classList.add('text-[var(--muted-foreground)]');
      }});
      
      const activePane = document.getElementById('tab-' + tabId);
      if (activePane) activePane.classList.remove('hidden');
      
      const activeBtn = document.getElementById('btn-' + tabId);
      if (activeBtn) {{
        activeBtn.classList.add('active');
        activeBtn.classList.remove('text-[var(--muted-foreground)]');
      }}
    }}
  </script>
</body>
</html>
"""

out_path = os.path.join(artifact_dir, "galeri_visualisasi_kmeans.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Artifact created successfully at:", out_path)

