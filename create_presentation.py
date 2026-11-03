import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]
    
    # Color Palette
    PRIMARY = RGBColor(30, 41, 59)       # Dark Slate Blue
    ACCENT = RGBColor(37, 99, 235)       # Royal Blue
    ACCENT_LIGHT = RGBColor(239, 246, 255) # Light Blue Tint
    BG_LIGHT = RGBColor(248, 250, 252)   # Off-white / light slate
    TEXT_MAIN = RGBColor(15, 23, 42)     # Almost Black
    TEXT_MUTED = RGBColor(100, 116, 139) # Muted Gray
    WHITE = RGBColor(255, 255, 255)
    CARD_BG = RGBColor(255, 255, 255)
    BORDER_COLOR = RGBColor(226, 232, 240)
    
    def set_slide_background(slide, color):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    def add_header(slide, title_text, category_text="PRAKTIKUM MACHINE LEARNING - CLUSTERING K-MEANS"):
        # Header banner text
        box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.733), Inches(1.1))
        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        
        p_cat = tf.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = ACCENT
        
        p_title = tf.add_paragraph()
        p_title.text = title_text
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = PRIMARY

    # ==========================================
    # SLIDE 1: TITLE SLIDE
    # ==========================================
    slide1 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide1, PRIMARY)
    
    # Accent shape
    accent_bar = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(0.2), Inches(3.8))
    accent_bar.fill.solid()
    accent_bar.fill.fore_color.rgb = ACCENT
    accent_bar.line.fill.background()

    tb = slide1.shapes.add_textbox(Inches(1.2), Inches(1.4), Inches(11.0), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p0 = tf.paragraphs[0]
    p0.text = "LAPORAN PRAKTIKUM ACARA X"
    p0.font.size = Pt(14)
    p0.font.bold = True
    p0.font.color.rgb = RGBColor(147, 197, 253)
    
    p1 = tf.add_paragraph()
    p1.text = "Segmentasi Pelanggan Mall Menggunakan Algoritma K-Means Clustering"
    p1.font.size = Pt(30)
    p1.font.bold = True
    p1.font.color.rgb = WHITE
    
    p2 = tf.add_paragraph()
    p2.text = "Studi Kasus: Pengelompokan 200 Pelanggan Mall Berdasarkan Pendapatan Tahunan & Skor Belanja Untuk Optimalisasi Strategi Pemasaran Manajerial"
    p2.font.size = Pt(14)
    p2.font.color.rgb = RGBColor(203, 213, 225)
    p2.space_before = Pt(14)

    p3 = tf.add_paragraph()
    p3.text = "✓ Verifikasi Perhitungan Manual Excel (Iterasi 1 s.d. 4)   |   ✓ Evaluasi Elbow & Silhouette (K=5)   |   ✓ Implementasi Python Scikit-Learn"
    p3.font.size = Pt(12)
    p3.font.color.rgb = RGBColor(56, 189, 248)
    p3.space_before = Pt(20)

    # ==========================================
    # SLIDE 2: LATAR BELAKANG & TUJUAN
    # ==========================================
    slide2 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide2, BG_LIGHT)
    add_header(slide2, "Latar Belakang & Studi Kasus Manajer Mall")

    # Card 1: Problem Scenario
    c1 = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
    c1.fill.solid()
    c1.fill.fore_color.rgb = WHITE
    c1.line.color.rgb = BORDER_COLOR
    
    tf1 = c1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_right = tf1.margin_top = Inches(0.3)
    p = tf1.paragraphs[0]
    p.text = "Skenario Manajerial Mall"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    
    bullets1 = [
        "Sebagai Manajer Mall, terdapat 200 data profil pelanggan yang merekam informasi pendapatan tahunan (Annual Income dalam k$) dan skor belanja (Spending Score skala 1-100).",
        "Tantangan: Pelanggan bersifat heterogen sehingga strategi pemasaran massal (one-size-fits-all) menjadi sangat tidak efektif dan boros biaya.",
        "Pertanyaan Kunci: Bagaimana mengelompokkan 200 pelanggan mall secara otomatis dan objektif menggunakan metode Unsupervised Learning K-Means?",
        "Tujuan: Merancang program promosi presisi (VIP Program, Flash Sale, Promo Hemat, dsb.) sesuai karakteristik tiap segmen pelanggan."
    ]
    for b in bullets1:
        p = tf1.add_paragraph()
        p.text = "• " + b
        p.font.size = Pt(11.5)
        p.font.color.rgb = TEXT_MAIN
        p.space_before = Pt(8)

    # Card 2: Objective & Key Questions
    c2 = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))
    c2.fill.solid()
    c2.fill.fore_color.rgb = WHITE
    c2.line.color.rgb = BORDER_COLOR
    
    tf2 = c2.text_frame
    tf2.word_wrap = True
    tf2.margin_left = tf2.margin_right = tf2.margin_top = Inches(0.3)
    p = tf2.paragraphs[0]
    p.text = "Fokus Pembahasan & Sasaran Praktikum"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = ACCENT
    
    bullets2 = [
        "Pemahaman Teori: Menguasai mekanisme algoritma K-Means, perhitungan jarak Euclidean, pembaruan centroid, dan konsep konvergensi.",
        "Validasi Perhitungan Manual Excel: Membuktikan perhitungan bertahap pada spreadsheet dari Iterasi 1 hingga tercapainya konvergensi pada Iterasi 4.",
        "Penentuan K Optimal: Menggunakan kombinasi Elbow Method (WCSS) dan Silhouette Score guna memastikan jumlah 5 kluster adalah pilihan terbaik secara matematis.",
        "Rekomendasi Nyata: Mengembangkan profil persona pelanggan mall dan menyusun rekomendasi strategi pemasaran berbasis data yang dapat langsung dieksekusi manajer mall."
    ]
    for b in bullets2:
        p = tf2.add_paragraph()
        p.text = "✓ " + b
        p.font.size = Pt(11.5)
        p.font.color.rgb = TEXT_MAIN
        p.space_before = Pt(8)

    # ==========================================
    # SLIDE 3: DASAR TEORI K-MEANS
    # ==========================================
    slide3 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide3, BG_LIGHT)
    add_header(slide3, "Dasar Teori & Alur Algoritma K-Means")

    cards_info = [
        ("1. Inisialisasi Centroid", "Menentukan nilai K (jumlah kluster) dan menetapkan K titik centroid awal secara manual atau algoritma K-Means++.", Inches(0.8)),
        ("2. Jarak Euclidean", "Menghitung jarak setiap titik data (x) ke seluruh centroid (c):\nd(x, c) = sqrt(sum((xj - cj)^2))\nData dialokasikan ke centroid terdekat.", Inches(4.8)),
        ("3. Rekalkulasi Centroid", "Menghitung ulang posisi centroid baru sebagai nilai rata-rata (mean) dari seluruh anggota yang tergabung dalam kluster tersebut.", Inches(8.8))
    ]
    for title, desc, left in cards_info:
        card = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, Inches(1.8), Inches(3.7), Inches(2.3))
        card.fill.solid()
        card.fill.fore_color.rgb = WHITE
        card.line.color.rgb = BORDER_COLOR
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.25)
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = PRIMARY
        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(11)
        p2.font.color.rgb = TEXT_MAIN
        p2.space_before = Pt(6)

    # Bottom summary box on Convergence
    b_card = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.4), Inches(11.7), Inches(2.4))
    b_card.fill.solid()
    b_card.fill.fore_color.rgb = ACCENT_LIGHT
    b_card.line.color.rgb = ACCENT
    tf_b = b_card.text_frame
    tf_b.word_wrap = True
    tf_b.margin_left = tf_b.margin_right = tf_b.margin_top = Inches(0.3)
    p = tf_b.paragraphs[0]
    p.text = "Kondisi Berhenti (Konvergensi Algoritma)"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = ACCENT
    conv_bullets = [
        "K-Means merupakan algoritma iteratif yang berulang hingga salah satu kondisi tercapai:",
        "1. Keanggotaan kluster tidak berubah (jumlah data yang berpindah kluster = 0).",
        "2. Perubahan posisi titik koordinat centroid sudah sangat kecil / nol (new_centroids == old_centroids).",
        "3. Batas jumlah iterasi maksimum (max_iter) tercapai.",
        "Dalam proyek ini, pada file Excel maupun simulasi Python, konvergensi sempurna tercapai pada Iterasi ke-4!"
    ]
    for b in conv_bullets:
        p = tf_b.add_paragraph()
        p.text = b
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_MAIN
        p.space_before = Pt(3)

    # ==========================================
    # SLIDE 4: EKSPLORASI DATASET (EDA)
    # ==========================================
    slide4 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide4, BG_LIGHT)
    add_header(slide4, "Eksplorasi Data & Karakteristik 200 Pelanggan Mall")

    # Image
    img_eda = os.path.join("output_results", "01_eda_distributions.png")
    if os.path.exists(img_eda):
        slide4.shapes.add_picture(img_eda, Inches(0.8), Inches(1.8), width=Inches(6.8))

    # Stats Card on Right
    c_stats = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.8), Inches(1.8), Inches(4.7), Inches(5.1))
    c_stats.fill.solid()
    c_stats.fill.fore_color.rgb = WHITE
    c_stats.line.color.rgb = BORDER_COLOR
    tfs = c_stats.text_frame
    tfs.word_wrap = True
    tfs.margin_left = tfs.margin_right = tfs.margin_top = Inches(0.25)
    p = tfs.paragraphs[0]
    p.text = "Statistik Deskriptif Fitur"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    
    stat_items = [
        "Ukuran Sampel: 200 Pelanggan (P1 s.d. P200)",
        "Pendapatan Tahunan (Annual Income):",
        "  • Rata-rata (Mean): 60.56 k$",
        "  • Median: 61.50 k$",
        "  • Rentang: 15.00 k$ s.d. 137.00 k$",
        "  • Standar Deviasi: 26.26 k$",
        "Skor Belanja (Spending Score):",
        "  • Rata-rata (Mean): 50.20",
        "  • Median: 50.00",
        "  • Rentang: 1.00 s.d. 99.00",
        "  • Standar Deviasi: 25.82",
        "Insight EDA: Kedua fitur memiliki skala numerik yang setara (berkisar ~0-140 dan ~1-100), sehingga perhitungan Euclidean mempertahankan interpretasi bisnis alami."
    ]
    for item in stat_items:
        p = tfs.add_paragraph()
        p.text = item
        p.font.size = Pt(10)
        p.font.color.rgb = TEXT_MAIN
        p.space_before = Pt(4)

    # ==========================================
    # SLIDE 5: PENENTUAN JUMLAH KLUSTER OPTIMAL
    # ==========================================
    slide5 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide5, BG_LIGHT)
    add_header(slide5, "Evaluasi Kluster Optimal: Metode Elbow & Silhouette Score")

    img_elbow = os.path.join("output_results", "03_elbow_and_silhouette.png")
    if os.path.exists(img_elbow):
        slide5.shapes.add_picture(img_elbow, Inches(0.8), Inches(1.8), width=Inches(7.2))

    c_opt = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.2), Inches(1.8), Inches(4.3), Inches(5.1))
    c_opt.fill.solid()
    c_opt.fill.fore_color.rgb = WHITE
    c_opt.line.color.rgb = BORDER_COLOR
    tfo = c_opt.text_frame
    tfo.word_wrap = True
    tfo.margin_left = tfo.margin_right = tfo.margin_top = Inches(0.25)
    p = tfo.paragraphs[0]
    p.text = "Analisis Bukti Matematis K=5"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = ACCENT
    
    proofs = [
        "1. Metode Elbow (WCSS / Inertia):",
        "  Penurunan drastis inersia melandai tepat di titik K = 5 (Inertia = 44,448). Menambah K > 5 hanya menghasilkan penurunan inersia marjinal.",
        "2. Koefisien Silhouette (Silhouette Score):",
        "  Nilai Silhouette mencapai puncak tertinggi global di K = 5 sebesar 0.5539 (Kluster sangat terpisah dan kompak).",
        "3. Davies-Bouldin Index:",
        "  Nilai terendah (terbaik) dicapai pada K = 5 yaitu 0.5726.",
        "Kesimpulan Ilmiah: Pemilihan K = 5 pada rancangan Excel terbukti secara statistik sebagai konfigurasi paling optimal!"
    ]
    for pf in proofs:
        p = tfo.add_paragraph()
        p.text = pf
        p.font.size = Pt(10.5)
        p.font.color.rgb = TEXT_MAIN
        p.space_before = Pt(6)

    # ==========================================
    # SLIDE 6: VALIDASI EXCEL VS SIMULASI PYTHON
    # ==========================================
    slide6 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide6, BG_LIGHT)
    add_header(slide6, "Validasi Komparatif: Perhitungan Manual Excel vs Python")

    img_iter = os.path.join("output_results", "02_manual_iteration_steps.png")
    if os.path.exists(img_iter):
        slide6.shapes.add_picture(img_iter, Inches(0.8), Inches(1.8), width=Inches(6.8))

    c_val = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.8), Inches(1.8), Inches(4.7), Inches(5.1))
    c_val.fill.solid()
    c_val.fill.fore_color.rgb = WHITE
    c_val.line.color.rgb = BORDER_COLOR
    tfv = c_val.text_frame
    tfv.word_wrap = True
    tfv.margin_left = tfv.margin_right = tfv.margin_top = Inches(0.25)
    p = tfv.paragraphs[0]
    p.text = "Tabel Verifikasi Konvergensi"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    
    iter_data = [
        "Centroid Awal (Sheet Parameter):",
        "  • C1 = P13 (20, 15)   • C2 = P16 (20, 79)",
        "  • C3 = P167 (86, 20)  • C4 = P172 (87, 75)",
        "  • C5 = P81 (54, 51)",
        "Riwayat Perubahan Anggota Tiap Iterasi:",
        "  • Iterasi 1: C1=21, C2=21, C3=38, C4=39, C5=81",
        "  • Iterasi 2: C1=22, C2=22, C3=37, C4=39, C5=80 (Pindah: 3)",
        "  • Iterasi 3: C1=23, C2=22, C3=36, C4=39, C5=80 (Pindah: 2)",
        "  • Iterasi 4: C1=23, C2=22, C3=36, C4=39, C5=80 (Pindah: 0)",
        "Hasil Validasi: 100% Identik!",
        "Perhitungan manual pada spreadsheet Excel dan simulasi algoritma Python menghasilkan nilai centroid dan keanggotaan kluster yang sama persis hingga desimal terakhir."
    ]
    for it in iter_data:
        p = tfv.add_paragraph()
        p.text = it
        p.font.size = Pt(9.5)
        p.font.color.rgb = TEXT_MAIN
        p.space_before = Pt(3)

    # ==========================================
    # SLIDE 7: HASIL VISUALISASI KLUSTER
    # ==========================================
    slide7 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide7, BG_LIGHT)
    add_header(slide7, "Peta Segmentasi 200 Pelanggan Mall (Final Cluster Map)")

    img_scatter = os.path.join("output_results", "04_final_clusters_scatter.png")
    if os.path.exists(img_scatter):
        slide7.shapes.add_picture(img_scatter, Inches(0.8), Inches(1.8), width=Inches(8.0))

    c_map = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.0), Inches(1.8), Inches(3.5), Inches(5.1))
    c_map.fill.solid()
    c_map.fill.fore_color.rgb = WHITE
    c_map.line.color.rgb = BORDER_COLOR
    tfm = c_map.text_frame
    tfm.word_wrap = True
    tfm.margin_left = tfm.margin_right = tfm.margin_top = Inches(0.2)
    p = tfm.paragraphs[0]
    p.text = "5 Kluster Pelanggan"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = ACCENT
    
    cl_notes = [
        "Kluster 1 (Orange):",
        "Hemat / Budget Spender (23 orang, 11.5%)",
        "Kluster 2 (Ungu):",
        "Impulsif / Trend Spender (22 orang, 11.0%)",
        "Kluster 3 (Pink):",
        "Konservatif / Careful Spender (36 orang, 18.0%)",
        "Kluster 4 (Hijau):",
        "VIP / Target Utama Sultan (39 orang, 19.5%)",
        "Kluster 5 (Hijau Muda):",
        "Moderat / Kelompok Mayoritas (80 orang, 40.0%)",
        "Tanda Bintang (*) menandakan posisi titik pusat (Centroid) tiap kelompok."
    ]
    for cn in cl_notes:
        p = tfm.add_paragraph()
        p.text = cn
        p.font.size = Pt(9.5)
        p.font.color.rgb = TEXT_MAIN
        p.space_before = Pt(3)

    # ==========================================
    # SLIDE 8: PROFILING KARAKTERISTIK SEGMEN
    # ==========================================
    slide8 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide8, BG_LIGHT)
    add_header(slide8, "Karakteristik & Profiling 5 Segmen Pelanggan")

    img_bar = os.path.join("output_results", "05_cluster_profiling_barchart.png")
    if os.path.exists(img_bar):
        slide8.shapes.add_picture(img_bar, Inches(0.8), Inches(1.8), width=Inches(7.5))

    c_prof = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.5), Inches(1.8), Inches(4.0), Inches(5.1))
    c_prof.fill.solid()
    c_prof.fill.fore_color.rgb = WHITE
    c_prof.line.color.rgb = BORDER_COLOR
    tfp = c_prof.text_frame
    tfp.word_wrap = True
    tfp.margin_left = tfp.margin_right = tfp.margin_top = Inches(0.2)
    p = tfp.paragraphs[0]
    p.text = "Rata-Rata Centroid Akhir"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    
    prof_data = [
        "C1 (Hemat / Low-Low):",
        "  • Pendapatan: $26.3k | Skor Belanja: 20.9",
        "C2 (Impulsif / Low-High):",
        "  • Pendapatan: $25.7k | Skor Belanja: 79.4",
        "C3 (Konservatif / High-Low):",
        "  • Pendapatan: $87.8k | Skor Belanja: 17.6",
        "C4 (VIP / High-High):",
        "  • Pendapatan: $86.5k | Skor Belanja: 82.1",
        "C5 (Moderat / Mid-Mid):",
        "  • Pendapatan: $55.1k | Skor Belanja: 49.7",
        "Insight: C4 dan C2 adalah pendorong omset tercepat (skor belanja >75), sedangkan C3 adalah potensi pendapatan besar yang belum tergarap optimal."
    ]
    for pd_item in prof_data:
        p = tfp.add_paragraph()
        p.text = pd_item
        p.font.size = Pt(9.5)
        p.font.color.rgb = TEXT_MAIN
        p.space_before = Pt(3)

    # ==========================================
    # SLIDE 9: STRATEGI PEMASARAN MANAJERIAL MALL
    # ==========================================
    slide9 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide9, BG_LIGHT)
    add_header(slide9, "Rekomendasi Strategi Pemasaran untuk Manajer Mall")

    strategies = [
        ("Kluster 4: VIP / Sultan (High Income, High Spend)", 
         "• Program Keanggotaan Prioritas / Black Card tier.\n• Akses VIP Lounge, Personal Shopper, free Valet Parking.\n• Undangan Private Sale / Trunk Show produk luxury branded.",
         Inches(0.8), Inches(1.8), Inches(5.6), Inches(2.3), RGBColor(27, 158, 119)),
        
        ("Kluster 3: Konservatif (High Income, Low Spend)", 
         "• Edukasi keunggulan & nilai investasi jangka panjang produk.\n• Promosi direct exclusive marketing (bukan diskon murahan).\n• Penawaran garansi premium & program uji coba produk.",
         Inches(6.8), Inches(1.8), Inches(5.7), Inches(2.3), RGBColor(231, 41, 138)),
        
        ("Kluster 2: Impulsif (Low Income, High Spend)", 
         "• Promo Flash Sale, weekend midnight bazaar, tren lifestyle terkini.\n• Opsi pembayaran cicilan 0% / Buy Now Pay Later (BNPL).\n• Diskon merchant F&B dan fashion anak muda.",
         Inches(0.8), Inches(4.3), Inches(5.6), Inches(2.5), RGBColor(117, 112, 179)),
        
        ("Kluster 1 & 5: Hemat & Moderat (Kelompok Basis)", 
         "• C1 (Hemat): Diskon kupon belanja pokok, voucher cashback, promo bundling.\n• C5 (Moderat - 40%): Loyalty points, promo tiket bioskop/game center/resto keluarga.",
         Inches(6.8), Inches(4.3), Inches(5.7), Inches(2.5), RGBColor(102, 166, 30))
    ]
    for s_title, s_desc, left, top, width, height, color in strategies:
        box = slide9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        box.fill.solid()
        box.fill.fore_color.rgb = WHITE
        box.line.color.rgb = color
        box.line.width = Pt(1.5)
        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.2)
        p = tf.paragraphs[0]
        p.text = s_title
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = color
        p2 = tf.add_paragraph()
        p2.text = s_desc
        p2.font.size = Pt(10)
        p2.font.color.rgb = TEXT_MAIN
        p2.space_before = Pt(4)

    # ==========================================
    # SLIDE 10: KESIMPULAN & PENUTUP
    # ==========================================
    slide10 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide10, PRIMARY)
    
    tb10 = slide10.shapes.add_textbox(Inches(1.5), Inches(1.2), Inches(10.333), Inches(5.5))
    tf10 = tb10.text_frame
    tf10.word_wrap = True
    
    p = tf10.paragraphs[0]
    p.text = "KESIMPULAN PRAKTIKUM"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = RGBColor(147, 197, 253)
    
    p_title = tf10.add_paragraph()
    p_title.text = "Hasil Akhir & Capaian Pembelajaran"
    p_title.font.size = Pt(28)
    p_title.font.bold = True
    p_title.font.color.rgb = WHITE
    p_title.space_before = Pt(6)
    
    conclusions = [
        "1. K-Means Terbukti Efektif: Berhasil membagi 200 data pelanggan heterogen ke dalam 5 kelompok homogen berbasis kedekatan jarak Euclidean.",
        "2. Validasi Akurat 100%: Perhitungan komputasi Python membuktikan secara persis kebenaran langkah iteratif Excel hingga konvergen di Iterasi 4.",
        "3. Optimalitas Matematis Teruji: Evaluasi Elbow Method dan Silhouette Score (0.5539) mengonfirmasi K=5 adalah partisi terbaik.",
        "4. Dampak Bisnis Nyata: Manajer mall kini memiliki peta segmen yang jelas untuk mendiversifikasi strategi pemasaran sehingga efisiensi anggaran promosi meningkat dan kepuasan pelanggan melonjak."
    ]
    for c in conclusions:
        p = tf10.add_paragraph()
        p.text = c
        p.font.size = Pt(12.5)
        p.font.color.rgb = RGBColor(241, 245, 249)
        p.space_before = Pt(10)

    # Save
    out_ppt_path = "Presentasi_Segmentasi_Mall_Customers.pptx"
    prs.save(out_ppt_path)
    print(f"-> Presentasi PowerPoint berhasil dibuat: {out_ppt_path}")

if __name__ == "__main__":
    create_presentation()

