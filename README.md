# Simulasi Ujian Perangkat Desa Kabupaten Tuban — Computer Assisted Test (CBT)

> **Versi:** `v5.0.0` • **Lisensi & Hak Cipta:** `Copyright by fusionproject.id` • **Status:** `Production Ready`

Aplikasi simulasi Computer Assisted Test (CAT/CBT) modern, interaktif, dan modular yang dirancang khusus untuk persiapan seleksi calon Perangkat Desa (Sekretaris Desa, Kaur, Kasi, dan Kepala Dusun) di **Kabupaten Tuban, Jawa Timur** serta mengacu pada regulasi pemerintahan desa di Indonesia.

Aplikasi ini menggunakan format resmi ujian perangkat desa Kabupaten Tuban: **5 Bidang Ujian Tertulis berurutan (125 Soal, 150 Menit) dilanjutkan 10 Butir Ujian Praktik Komputer Berbasis Tugas Nyata (Tersedia Mode Microsoft Office Asli dan Simulasi Browser Interaktif)**. Nilai akhir dihitung secara otomatis menggunakan formula resmi: **Ujian Tertulis (87,50 Poin) + Praktik Komputer (12,50 Poin) = 100,00 Poin Maksimal**.

Aplikasi beroperasi **100% Offline, Privat Penuh, dan Bebas Dependensi Eksternal/CDN**.

---

## 🌟 Karakteristik Format Resmi Ujian Kabupaten Tuban

### 1. Ujian Tertulis 5 Bidang Materi Berurutan (Sequential Sections)
Sesuai standar seleksi Kabupaten Tuban, materi tertulis tidak digabung sekaligus melainkan dibagi ke dalam 5 seksi bidang materi yang harus dikerjakan secara berurutan:

| Bidang | Nama Bidang Materi | Jumlah Soal | Durasi Waktu | Bobot Nilai Maksimal | Fokus Materi & Dasar Regulasi |
|:---:|:---|:---:|:---:|:---:|:---|
| **Bidang 1** | **Pendidikan Agama & Moderasi Beragama** | 25 Soal | 30 Menit | 17,50 Poin | Fiqih jenazah desa, zakat fitrah & mal, wakaf UU 41/2004, batas usia nikah UU 16/2019, moderasi beragama PBM 9 & 8/2006, etika aparatur bebas risywah, sejarah Sunan Bonang Tuban. |
| **Bidang 2** | **Pengetahuan Pemerintahan Desa** | 25 Soal | 30 Menit | 17,50 Poin | UU No. 6/2014 jo. UU No. 3/2024, PP 11/2019 (Siltap), Permendagri 84/2015 (SOTK), Permendagri 20/2018 (APBDes & Keuangan Desa), Permendesa 21/2020, Perda Kab. Tuban No. 2/2016 jo. No. 16/2021, Perbup Tuban No. 11/2022. |
| **Bidang 3** | **Bahasa Indonesia** | 25 Soal | 30 Menit | 17,50 Poin | Tata bahasa baku EYD Edisi V, penulisan naskah dinas resmi, struktur surat undangan/edaran/berita acara desa, kapitalisasi jabatan, kalimat efektif tanpa pleonasme. |
| **Bidang 4** | **Pengetahuan Umum** | 25 Soal | 30 Menit | 17,50 Poin | Pancasila & butir pengamalan, Pembukaan UUD 1945, wawasan kebangsaan, matematika/numerik terapan desa (APBDes/lahan bengkok), logika penalaran, sejarah & profil daerah Tuban (Hari Jadi 12 Nov 1293). |
| **Bidang 5** | **Pengetahuan Komputer** | 25 Soal | 30 Menit | 17,50 Poin | Perangkat keras/lunak kantor desa, pengolah kata (Word), lembar kerja (Excel), pengarsipan digital, surat elektronik dinas, keamanan data & kerahasiaan kependudukan sesuai UU PDP No. 27/2022. |
| **TOTAL** | **5 Bidang Ujian Tertulis** | **125 Soal** | **150 Menit** | **87,50 Poin** | **125 Soal × 0,7 Poin / Benar** |

#### Mekanisme Alur Ujian Tertulis:
* **Penguncian Sekuensial (*Sequential Lock*):** Peserta harus memulai dari Bidang 1. Bidang 2 baru terbuka setelah Bidang 1 diselesaikan dan dikunci permanen oleh peserta (atau waktu habis). Peserta tidak dapat kembali ke bidang yang telah dikunci.
* **Timer Mandiri 30 Menit per Bidang:** Setiap bidang memiliki penghitung waktu mundur 30 menit independen dengan peringatan visual berkedip saat sisa waktu kurang dari 5 menit.
* **Ketahanan Sesi (*Crash/Refresh Resilience*):** Jika browser ditutup atau dimuat ulang secara tidak sengaja, sisa waktu, status jawaban, dan posisi bidang dipulihkan secara otomatis tanpa kehilangan data.

---

### 2. Ujian Praktik Komputer Realistis (Dua Mode Praktik & 10 Butir Tugas)

Setelah peserta menyelesaikan seluruh 5 bidang ujian tertulis, sistem secara otomatis membuka tahapan **Ujian Praktik Komputer**. Modul ini tidak menggunakan soal pilihan ganda, melainkan berbasis tugas nyata (*task-based production*) yang menguji kemampuan menghasilkan pekerjaan komputer perkantoran desa.

#### A. Dua Mode Praktik yang Tersedia

1. **Mode 1 — Praktik dengan Microsoft Office Asli (Mode Utama):**
   - Dirancang bagi peserta yang memiliki Microsoft Word, Excel, dan PowerPoint terpasang di komputer lokal.
   - **Alur Kerja Nyata:**
     1. Peserta membaca instruksi tugas dan skenario administrasi desa.
     2. Mengunduh berkas bahan latihan (`.txt`, `.docx`, `.xlsx`, `.pptx`) atau menyalin teks naskah ke papan klip (*clipboard*).
     3. Membuka dan mengerjakan tugas di Microsoft Office asli di komputer peserta.
     4. Menyimpan hasil pekerjaan sesuai format nama berkas yang telah ditentukan panitia (misal: `Tugas01_Ketik_Naskah.docx`, `Tugas06_Rumus_Anggaran.xlsx`, `Berkas_Praktik_Perangkat_Desa_[Nama].zip`).
     5. Mengunggah kembali berkas hasil ke aplikasi.
     6. Sistem menjalankan **pemeriksaan struktur OpenXML secara nyata** menggunakan dekompresi *deflate-raw* tanpa dependensi luar, mendeteksi keberadaan tag XML, teks, formula `<f>SUM</f>`, `<f>AVERAGE</f>`, tabel `<w:tbl>`, slide presentasi, dan nama file.
     7. Menyediakan **Lembar Verifikasi Rubrik Penilaian** transparan dengan status: `Lulus (Kriteria Terpenuhi)`, `Menunggu Penilaian Penguji`, atau `Perlu Perbaikan`.
   - **Kejujuran Teknis:** Aplikasi secara jujur menyatakan bahwa peramban browser tidak mengendalikan aplikasi Microsoft Office desktop secara gaib. Pemeriksaan dilakukan murni terhadap integritas struktur berkas yang diunggah. Nilai tidak diberikan penuh hanya karena peserta mengunggah berkas atau sekadar mencocokkan ekstensi file.

2. **Mode 2 — Simulasi Interaktif di dalam Browser (Mode Alternatif):**
   - Disediakan khusus sebagai alternatif bagi peserta yang tidak memiliki Microsoft Office terpasang pada komputernya.
   - Diberi label secara tegas dan transparan: `Simulasi Browser Interaktif (Bukan Microsoft Office Asli)`.
   - Menyediakan lingkungan kerja berbasis web yang menyerupai pengolah dokumen (pengetikan akurat & *formatting toolbar*), lembar kerja spreadsheet (*grid sel & live formula engine SUM/AVERAGE*), penyusunan slide presentasi 16:9, dan pengemasan berkas arsip.
   - Peserta melakukan tindakan nyata (mengetik, mengatur margin, memasukkan formula, mengurutkan/menyaring data, menyusun bullet presentasi), bukan sekadar memilih opsi A/B/C/D.

#### B. Daftar 10 Butir Tugas Praktik Komputer

Tepat 10 tugas praktik disusun secara terstruktur dengan alokasi skor **1,25 poin per butir** (Total 12,50 Poin):

| No | Aplikasi / Kategori | Judul Butir Tugas Praktik | Skenario Administrasi Desa & Hasil yang Diharapkan | Rubrik & Skor Maks. | Berkas yang Diharapkan |
|:---:|:---|:---|:---|:---:|:---|
| **1** | Word (Pengolah Kata) | **Mengetik Dokumen Sesuai Teks Sumber** | Mengetik naskah pengumuman resmi Pelayanan Kependudukan Desa Sukamaju secara teliti, lengkap, dan presisi tanpa saltik (*typo*). | Kelengkapan teks (0,50), Ketelitian nama/nomor/tanggal (0,50), Kerapian alinea (0,25) $\rightarrow$ **1,25 Poin** | `Tugas01_Ketik_Naskah.docx` |
| **2** | Word (Pengolah Kata) | **Memformat Judul, Paragraf, Margin, & Perataan** | Menata draf Berita Acara Musrenbangdes: Judul Center-Bold-14pt, Paragraf Justify spasi 1,5, Margin kearsipan (Kiri 3,5 cm, Lainnya 2,5 cm pada kertas F4). | Judul Center Bold 14pt (0,50), Justify 1,5 spasi (0,50), Margin F4 kearsipan (0,25) $\rightarrow$ **1,25 Poin** | `Tugas02_Format_Naskah.docx` |
| **3** | Word (Pengolah Kata) | **Membuat Tabel Sederhana** | Membuat tabel inventaris aset operasional kantor desa struktur 4 Kolom x 5 Baris dengan baris judul tebal (*header bold*) dan garis kisi tabel (*border*). | Struktur 4x5 kolom baku (0,50), Baris judul tebal (0,50), Garis tabel rapi (0,25) $\rightarrow$ **1,25 Poin** | `Tugas03_Tabel_Aset.docx` |
| **4** | Word (Pengolah Kata) | **Membuat Surat Resmi Sederhana** | Menyusun surat undangan dinas rapat koordinasi dusun lengkap memuat Kop Surat Pemkab Tuban bergaris ganda (*double line*), nomor, perihal, tanggal, alamat, isi, dan titimangsa Kades. | Kop surat hierarki Tuban + double line (0,50), Komponen nomor/tanggal/tujuan (0,50), Struktur isi & ttd Kades (0,25) $\rightarrow$ **1,25 Poin** | `Tugas04_Surat_Resmi.docx` |
| **5** | Excel (Spreadsheet) | **Memasukkan Data ke Tabel** | Menginput data rekapitulasi penerimaan honor 5 kader posyandu (No, Nama, Dusun, Kehadiran, Honor) secara akurat tanpa salah ketik angka/nama. | Kelengkapan 5 baris data (0,50), Ketepatan kehadiran & honor (0,50), Kerapian tata letak (0,25) $\rightarrow$ **1,25 Poin** | `Tugas05_Input_Tabel.xlsx` |
| **6** | Excel (Spreadsheet) | **Menggunakan Rumus SUM dan AVERAGE** | Menghitung belanja fisik desa pada sel D7 dengan rumus `=SUM(D2:D6)` (Rp 110.000.000) dan sel D8 dengan `=AVERAGE(D2:D6)` (Rp 22.000.000). | Formula =SUM(D2:D6) valid (0,50), Formula =AVERAGE(D2:D6) valid (0,50), Sintaks rumus baku (0,25) $\rightarrow$ **1,25 Poin** | `Tugas06_Rumus_Anggaran.xlsx` |
| **7** | Excel (Spreadsheet) | **Memformat Angka dan Tabel** | Memformat tabel siltap perangkat desa menjadi format mata uang Rupiah (`Rp ...`), memberikan garis kisi *All Borders*, dan pewarnaan latar (*fill color*) header. | Gaya mata uang Rupiah (0,50), Garis All Borders (0,50), Pewarnaan header kontras (0,25) $\rightarrow$ **1,25 Poin** | `Tugas07_Format_Angka.xlsx` |
| **8** | Excel (Spreadsheet) | **Mengurutkan atau Menyaring Data** | Mengurutkan daftar penerima bantuan berdasarkan kolom RT secara menaik (*Ascending*), lalu memfilter kolom status verifikasi hanya menampilkan yang 'Layak'. | Sort RT Ascending (0,50), Filter status Layak (0,50), Integritas data antar kolom (0,25) $\rightarrow$ **1,25 Poin** | `Tugas08_Sort_Filter.xlsx` |
| **9** | PowerPoint (Presentasi) | **Membuat & Memformat Slide Sederhana** | Membuat presentasi 2 slide paparan Musdes: Slide 1 Judul & Identitas Desa Sukamaju; Slide 2 Judul & 4 poin program prioritas infrastruktur (*bullet list*). | Slide 1 Judul & Subjudul Desa (0,50), Slide 2 Judul & 4 bullet points (0,50), Tata letak & kontras (0,25) $\rightarrow$ **1,25 Poin** | `Tugas09_Presentasi_Desa.pptx` |
| **10** | Tugas Terpadu | **Menyimpan, Memberi Nama, & Menyerahkan Berkas** | Mengemas seluruh berkas dokumen (Word, Excel, PPT) ke dalam file arsip penyerahan resmi bernama: `Berkas_Praktik_Perangkat_Desa_[NamaPeserta].zip`. | Nama file arsip ZIP baku (0,50), Kelengkapan 4 berkas utama (0,50), Integritas arsip penyerahan (0,25) $\rightarrow$ **1,25 Poin** | `Berkas_Praktik_Perangkat_Desa_[Nama].zip` |
| **TOTAL** | **10 Butir Praktik** | **10 Tugas Nyata Komputer Administrasi Desa** | **Penilaian Berbasis Rubrik Transparan & Terverifikasi** | **Maksimal: 12,50 Poin** | **Seluruh Format Standar Office** |

---

### 3. Konfigurasi Timer & Tata Tertib Praktik Komputer

- **Fleksibilitas Durasi Waktu:** Sesuai ketentuan, alokasi waktu ujian praktik komputer ditentukan oleh **Tim Penyusun Naskah Ujian / Panitia Pengawas Desa**. Aplikasi menyediakan dialog **⚙️ Atur Durasi Waktu Praktik**:
  - `30 Menit`: Simulasi waktu cepat (rata-rata 3 menit per butir tugas).
  - `45 Menit (Rekomendasi Standar)`: Alokasi rata-rata 4,5 menit per butir tugas.
  - `60 Menit (1 Jam Penuh)`: Alokasi longgar untuk pembuatan dokumen dan formula lengkap.
  - `90 Menit (1,5 Jam)`: Alokasi simulasi bertahap dan mendalam.
  - `Tanpa Batas Waktu`: Mode latihan bebas tanpa batas hitung mundur.
- **Peringatan Waktu & Penguncian Sesi:**
  - Timer menampilkan peringatan visual warna emas saat tersisa $\le$ 5 menit dan warna merah saat tersisa $\le$ 1 menit.
  - Saat waktu habis, sistem secara otomatis mengunci sesi (*lock session*), menonaktifkan perubahan berkas/input, dan mewajibkan peserta menyelesaikan ujian demi menjaga kepatuhan tata tertib.
- **Integritas Penyerahan:** Tugas yang belum diunggah atau belum dikerjakan ditandai secara tegas sebagai **Belum Diserahkan** dan mendapat nilai `0,00`, bukan otomatis dianggap benar.

---

### 4. Sistem Penilaian Resmi Gabungan & Status Nilai Akhir

Penilaian akhir menggabungkan hasil Ujian Tertulis dan Ujian Praktik Komputer secara proporsional sesuai ketentuan Kabupaten Tuban:

$$\text{Nilai Ujian Tertulis} = \text{Jumlah Jawaban Benar (dari 125 Soal)} \times 0,7 \quad (\text{Maks. } 87,50)$$
$$\text{Nilai Praktik Komputer} = \sum_{i=1}^{10} \text{Skor Tugas Praktik Ke-}i \quad (\text{Maks. } 12,50)$$
$$\mathbf{\text{Nilai Akhir Total}} = \mathbf{\text{Nilai Ujian Tertulis}} + \mathbf{\text{Nilai Praktik Komputer}} \quad (\mathbf{\text{Maksimal } 100,00})$$

#### Kategori Status Penilaian Praktik pada Lembar Hasil:
- **`✓ Lulus (Memenuhi Kriteria)`** (Pill Hijau): Seluruh kriteria teknis dan rubrik tugas telah terpenuhi secara penuh (skor 1,25).
- **`⏳ Menunggu Penilaian Penguji`** (Pill Kuning-Kuning Tua): Berkas telah diunggah dan lolos verifikasi struktur dasar, namun kriteria subjektif (estetika tata naskah, kerapian kop surat, perataan visual) menunggu verifikasi manual oleh panitia pemeriksa.
- **`⚠️ Perlu Perbaikan`** (Pill Merah Muda): Berkas tidak sesuai nama, format berkas keliru, atau formula salah sintaks.
- **`✕ Belum Diserahkan (0.00)`** (Pill Abu-Abu/Merah): Tugas tidak dikerjakan atau belum diunggah saat sesi diakhiri.

> [!IMPORTANT]
> **Prinsip Nilai Sementara:** Jika terdapat tugas praktik yang berstatus *Menunggu Penilaian Penguji* atau *Belum Diserahkan*, sistem tidak akan menyatakan nilai akhir sudah final. Nilai akan diberi tanda bintang (`*`) dan diberi label tegas: **(Nilai Sementara — Terdapat tugas menunggu verifikasi penguji)**.

---

### 5. Transparansi & Pembahasan Pasca-Ujian

* **Kerahasiaan Selama Ujian:** Selama ujian berlangsung, indikator kunci jawaban dan pembahasan disembunyikan secara total untuk mencegah kebocoran.
* **Pembahasan Lengkap Terbuka Setelah Ujian:** Setelah ujian berakhir, tombol **"Buka Pembahasan Lengkap Seluruh Soal"** akan membuka seluruh 125 butir soal tertulis beserta kunci jawaban benar, opsi yang dipilih peserta, status benar/salah, ulasan pembahasan komprehensif, dan rujukan pasal/regulasi yang valid.
* **Rincian Nilai 10 Butir Praktik:** Tabel hasil akhir menyajikan rekapitulasi 10 butir tugas mencakup: nomor butir, judul tugas, kategori & mode (Mode 1 Office Asli / Mode 2 Browser), skor diperoleh, skor maksimal, dan badge status penilaian.

---

## 🏛️ Arsitektur Modular & Struktur Direktori

Basis kode telah dipisahkan secara rapi dan modular ke dalam komponen HTML, CSS, JavaScript Data, dan JavaScript Engine:

```text
├── index.html                    # Entry point aplikasi modular (HTML5 semantik & bersih)
├── index_standalone_bundle.html  # Berkas tunggal mandiri (bundle all-in-one untuk distribusi tanpa folder)
├── favicon.svg                   # Favicon resmi terkompresi
├── logo.svg                      # Logo emblem vektor terkompresi
│
├── css/
│   ├── style.css                 # Desain sistem visual (Civic Navy & Gold, Responsive, Stepper, Widgets, Print)
│   └── style.min.css             # Versi minifikasi teroptimasi (penghematan 32.1%)
│
├── js/
│   ├── app.js                    # CBT Application Engine (State machine, timer, evaluator praktik, UI controller)
│   ├── app.min.js                # Versi minifikasi teroptimasi
│   └── data/
│       ├── questions.js          # Master database 1.000 butir soal lengkap (opsi, kunci, pembahasan, sumber regulasi)
│       ├── glossary.js           # Database 36 istilah resmi pemerintahan desa
│       └── practical.js          # Master 10 butir tugas praktik komputer realistis (dua mode & rubrik)
│
├── assets/                       # Aset vektor branding (logo-full.svg, logo.svg) terkompresi
│
├── generator/                    # Modul generator & builder Python (terisolasi rapi di dalam folder)
│   ├── build_index.py            # Script kompilasi/build otomatis Python untuk memvalidasi & menyinkronkan aset
│   ├── optimize_assets.py        # Script pembersih file tidak berguna & pemroses optimasi CSS/JS/SVG/HTML
│   ├── merge_and_validate.py     # Assembler & validasi master pool 1.000 butir soal
│   ├── bank_bidang1_agama.py     # Bank master Bidang 1: Agama & Moderasi Beragama (200 soal)
│   ├── bank_bidang2_pemdes.py    # Bank master Bidang 2: Pemerintahan Desa (200 soal)
│   ├── bank_bidang3_bahasa.py    # Bank master Bidang 3: Bahasa Indonesia (200 soal)
│   ├── bank_bidang4_umum.py      # Bank master Bidang 4: Pengetahuan Umum (200 soal)
│   └── bank_bidang5_komputer.py  # Bank master Bidang 5: Pengetahuan Komputer (200 soal)
│
├── .github/workflows/            # Otomasi CI/CD GitHub Actions
│   ├── cleanup-repo.yml          # Workflow pembersihan seluruh file tidak berguna di luar maupun di dalam folder
│   ├── optimize-assets.yml       # Workflow optimasi CSS, JS, SVG, HTML & verifikasi pengujian otomatis
│   └── deploy.yml                # Workflow deploy otomatis teroptimasi ke GitHub Pages
│
├── test_suite.js                 # Suite pengujian komprehensif Node.js untuk integritas modular & kuota bank soal
├── test_full_audit.js            # Audit privasi 100% offline, zero network leaks, dan struktur regulasi
├── test_cbt_engine_sim.js        # Simulasi state machine end-to-end (5 bidang tertulis + 10 butir praktik 2 mode)
├── test_zero_repetition.js       # Pengujian siklus state machine tanpa pengulangan (Zero Repetition Engine)
├── sync_github.bat               # Skrip one-click Windows Batch untuk optimasi, cleanup, dan push ke GitHub
├── sync_github.ps1               # Skrip one-click PowerShell untuk sinkronisasi GitHub
├── .gitignore                    # Konfigurasi pengabaian file cache & scratch lokal
└── README.md                     # Dokumentasi komprehensif proyek
```

---

## 📚 Master Bank Soal 1.000 Butir (5 Bidang Terisolasi Masing-Masing 200 Soal)

Master database bank soal kini berkapasitas **1.000 butir soal seimbang**, terisolasi secara ketat (*strict domain isolation*) ke dalam 5 modul mandiri ber-`bidangId` (1 s.d. 5) dan rentang ID berurutan rapi sehingga **soal bidang satu tidak akan pernah keluar di bidang lain dan tidak tercampur**:

| No | Bidang Materi Ujian | Rentang ID Bank | Kuota Ujian Tertulis | Jumlah di Master Bank | Tingkat Kesulitan | Fokus Materi Utama & Dasar Regulasi |
|:---:|:---|:---:|:---:|:---:|:---:|:---|
| **1** | **Pendidikan Agama & Moderasi Beragama** | ID 1 – 200 | 25 Soal (Sesi 1) | **200 Soal** | Mudah: 50, Sedang: 125, Sulit: 25 | Fiqih jenazah desa, zakat fitrah & mal, wakaf UU 41/2004, UU Nikah 16/2019, moderasi beragama PBM 9 & 8/2006, etika aparatur anti-risywah, sejarah Sunan Bonang Tuban. |
| **2** | **Pengetahuan Pemerintahan Desa** | ID 201 – 400 | 25 Soal (Sesi 2) | **200 Soal** | Mudah: 52, Sedang: 130, Sulit: 18 | UU 6/2014 jo. UU 3/2024, Permendagri 84/2015 (SOTK), PP 11/2019 (Siltap), Permendagri 20/2018 (APBDes & Keuangan Desa), Permendagri 1/2016 (Aset Desa), Permendesa 21/2020, Perda Tuban No. 2/2016 jo. No. 16/2021, Perbup Tuban 11/2022. |
| **3** | **Bahasa Indonesia** | ID 401 – 600 | 25 Soal (Sesi 3) | **200 Soal** | Mudah: 48, Sedang: 132, Sulit: 20 | Tata bahasa baku EYD Edisi V, penulisan naskah dinas resmi (Permendagri 54/2010), surat undangan/edaran/berita acara desa, kapitalisasi jabatan, kalimat efektif tanpa pleonasme, diksi laporan APBDes. |
| **4** | **Pengetahuan Umum** | ID 601 – 800 | 25 Soal (Sesi 4) | **200 Soal** | Mudah: 50, Sedang: 128, Sulit: 22 | Pancasila & butir pengamalan, UUD 1945, wawasan kebangsaan, matematika/numerik terapan desa (persentase realisasi APBDes/lahan bengkok), silogisme logika penalaran, sejarah & profil daerah Tuban (Hari Jadi 12 Nov 1293). |
| **5** | **Pengetahuan Komputer** | ID 801 – 1000 | 25 Soal (Sesi 5) | **200 Soal** | Mudah: 46, Sedang: 126, Sulit: 28 | MS Word (margin F4, kop surat, mail merge, tabel), MS Excel (SUM, AVERAGE, IF, VLOOKUP, sort & filter), Siskeudes, Sipades, manajemen berkas PDF/ZIP, jaringan LAN/Wi-Fi, keamanan sandi, dan UU Pelindungan Data Pribadi No. 27/2022. |
| **TOTAL** | **5 Bidang Ujian Tertulis** | **ID 1 – 1000** | **125 Soal** | **1.000 Soal** | **246 Mudah, 641 Sedang, 113 Sulit** | **100% Rujukan Regulasi Terverifikasi & Terisolasi 100% Bebas Campuran** |

---

## 🛠️ Fitur Pendukung & Aksesibilitas

1. **Pengacakan Fisher-Yates Otomatis:** Susunan soal dan urutan opsi pilihan jawaban (A, B, C, D) diacak secara otomatis dan aman untuk mencegah penghafalan posisi pola kunci.
2. **Glosarium 36 Istilah Pemerintahan Desa:** Buku saku interaktif berisi 36 singkatan dan istilah penting (Siltap, PKPKD, PPKD, APBDes, RPJMDes, RKPDes, BPD, Siskeudes, Sipades, Tanah Bengkok, ADD, dll.) dilengkapi fitur *live search* pencarian cepat.
3. **Grafik Tren Skor SVG Native:** Visualisasi riwayat performa ujian berbasis grafik SVG native tanpa library eksternal.
4. **Navigasi Keyboard Penuh:**
   - `A`, `B`, `C`, `D`: Memilih pilihan jawaban.
   - `Panah Kiri (←)`: Kembali ke nomor soal sebelumnya.
   - `Panah Kanan (→)`: Lanjut ke nomor soal berikutnya.
   - `R` atau `F`: Menandai soal ragu-ragu (*toggle flag*).
   - `Esc`: Menutup jendela modal yang sedang aktif.
5. **Pengatur Ukuran Font (*Font Scaler*):** Pilihan ukuran huruf di bilah atas: `A-` (90%), `A` (100%), dan `A+` (115%).
6. **Cadangan & Pemulihan Data JSON:** Ekspor hasil ujian dan riwayat performa ke berkas JSON serta impor kembali secara aman dengan validasi skema dan ukuran maksimal 2 MB.
7. **Mode Cetak Ramah Kertas (*Print-Optimized*):** Lembar hasil ujian dan rekapitulasi nilai siap dicetak atau disimpan sebagai PDF dengan tata letak resmi.

---

## 🚀 Panduan Penggunaan & Pengujian

### 1. Menjalankan Aplikasi
Cukup buka berkas `index.html` langsung menggunakan peramban modern apa pun:
* Google Chrome
* Microsoft Edge
* Mozilla Firefox
* Safari / Opera

> **Catatan:** Tidak memerlukan instalasi Node.js, Python, ataupun web server (Apache/Nginx) untuk menggunakan simulasi ini. Cukup klik ganda berkas `index.html`.

### 2. Menjalankan Suite Pengujian Otomatis
Pastikan Node.js telah terpasang pada komputer Anda, kemudian jalankan seluruh pengujian:
```bash
node test_suite.js; node test_full_audit.js; node test_cbt_engine_sim.js; node test_zero_repetition.js
```

Hasil pengujian:
- `test_suite.js`: 9/9 tes integritas file modular, ekstraksi 1.000 soal, 10 tugas praktik, rumus penilaian resmi 87,5 + 12,5 = 100,0, dan rendering teks berformat lulus 100%.
- `test_full_audit.js`: Audit keamanan offline 100% tanpa CDN eksternal, validasi bank soal 1.000 butir (5 bidang @ 200 butir), distribusi materi, dan simulasi penilaian resmi lulus 100%.
- `test_cbt_engine_sim.js`: Simulasi state machine end-to-end mengerjakan 5 bidang materi tertulis berurutan (125 soal) dan seluruh 10 butir tugas praktik komputer (kedua mode), penguncian sesi, dan perhitungan nilai akhir lulus 100%.
- `test_zero_repetition.js`: Verifikasi integritas bank soal 1.000 butir (0 duplikasi bank soal), isolasi 100% antarbidang (zero mixing), dan keunikan 125 butir soal per sesi ujian (1 soal keluar di 1 sesi ujian).

### 3. Mengompilasi Ulang Aset (Build System)
Jika Anda memperbarui bank soal di file sumber Python, jalankan script pembangun:
```bash
python generator/build_index.py
```

### 4. Pembersihan File Tidak Berguna & Optimasi Aset Mandiri
Proyek ini menyediakan tool optimasi mandiri di [`generator/optimize_assets.py`](file:///d:/FusionProject/Ujian/generator/optimize_assets.py) yang dapat dijalankan secara lokal kapan saja:
```bash
python generator/optimize_assets.py
```
**Operasi yang Dilakukan Secara Otomatis:**
1. **Pembersihan File Luar & Dalam Folder:**
   - Menghapus seluruh file skrip `.py` yang berada di luar folder (root).
   - Menghapus folder usang `dev_scratch/` dan seluruh file analisis sementara.
   - Menghapus modul generator lama yang sudah tidak terpakai (`expand_bank*.py`, `validate_data.py`).
   - Menghapus direktori cache `__pycache__` dan file compiled `.pyc`.
   - Menghapus file sampah OS (`Thumbs.db`, `.DS_Store`, `desktop.ini`).
   - Menghapus file duplikat di root jika file identik sudah tersedia di subfolder (`assets/logo.svg`).
2. **Optimasi CSS:**
   - Membaca `css/style.css` (53.4 KB) dan menghasilkan `css/style.min.css` (36.3 KB) dengan **penghematan 32.1%**.
   - Menghapus komentar, baris kosong, dan spasi redundan secara aman tanpa merusak CSS custom properties (`--primary-900`) maupun media query responsif.
3. **Optimasi JavaScript:**
   - Mengompresi `js/app.js` (150.4 KB) menjadi `js/app.min.js` (143.2 KB) secara aman dengan mempertahankan string template dan regex parser OpenXML.
4. **Optimasi Berkas Vektor SVG:**
   - Mengompresi `favicon.svg` (2.97 KB $\rightarrow$ 2.10 KB, **-29.5%**), `assets/logo.svg` (3.51 KB $\rightarrow$ 2.57 KB, **-26.9%**), dan `assets/logo-full.svg` (3.09 KB $\rightarrow$ 2.56 KB, **-17.0%**).
5. **Optimasi Berkas HTML:**
   - Mengompresi `index.html` (92.4 KB $\rightarrow$ 86.2 KB, **-6.7%**) dan `index_standalone_bundle.html`.

---

### 5. Alur Otomasi CI/CD GitHub Actions

Repositori ini dilengkapi 3 alur kerja (*workflows*) GitHub Actions otomatis yang terintegrasi di folder `.github/workflows/`:

#### A. Workflow Pembersihan Repositori (`.github/workflows/cleanup-repo.yml`)
- **Pemicu:** Dijalankan secara terjadwal setiap minggu (*weekly cron*), via manual trigger (*workflow_dispatch*), atau saat push file root.
- **Tugas Utama:**
  - Membersihkan file `.py` di root direktori.
  - Membersihkan folder usang `dev_scratch/`, modul generator legacy, file cache `__pycache__`, dan file sampah OS.
  - Melakukan `git commit` dan `git push` otomatis jika ditemukan file yang perlu dibersihkan.

#### B. Workflow Optimasi Aset (`.github/workflows/optimize-assets.yml`)
- **Pemicu:** Otomatis berjalan saat terjadi push atau pull-request yang mengubah berkas di folder `css/`, `js/`, `assets/`, `generator/`, atau `index.html`.
- **Tugas Utama:**
  1. Menjalankan skrip `generator/optimize_assets.py` untuk menghasilkan `style.min.css`, `app.min.js`, kompresi SVG, dan HTML.
  2. Menjalankan seluruh 4 test suite Node.js (`test_suite.js`, `test_full_audit.js`, `test_cbt_engine_sim.js`, `test_zero_repetition.js`) untuk memvalidasi bahwa hasil optimasi 100% aman dan berfungsi sempurna.
  3. Meng-commit dan mengunggah kembali aset teroptimasi ke branch repositori.

#### C. Workflow Deployment Bersih ke GitHub Pages (`.github/workflows/deploy.yml`)
- **Pemicu:** Otomatis berjalan pada setiap push ke branch `main` atau `master`.
- **Tugas Utama:**
  1. Memverifikasi kelulusan 100% dari 4 test suite.
  2. Menjalankan optimasi aset terbaru (`generator/optimize_assets.py`).
  3. Mengisolasi lingkungan web hanya menyertakan berkas web murni (`index.html`, `index_standalone_bundle.html`, `css/`, `js/`, `assets/`, `favicon.svg`, `logo.svg`). Berkas pengujian, generator, script sinkronisasi, dan source python tidak akan terunggah ke web.
  4. Mempublikasikan aplikasi web langsung aktif ke GitHub Pages:
     `https://<username>.github.io/<nama-repo>/`

---

### 6. Sinkronisasi Cepat One-Click (`sync_github.bat` / `sync_github.ps1`)
Untuk pengguna Windows, tersedia skrip one-click yang menggabungkan seluruh alur di atas:
- Cukup dobel-klik **`sync_github.bat`** (atau jalankan `.\sync_github.ps1` di PowerShell).
- Skrip akan otomatis:
  1. Menjalankan pembersihan file liar dan kompresi aset melalui `optimize_assets.py`.
  2. Melepaskan tracking git pada folder/berkas legacy (`git rm --cached`).
  3. Merekam seluruh perubahan (`git add -A`).
  4. Membuat commit terstruktur dan melakukan `git push` ke repositori GitHub.

---

## 📜 Daftar Rujukan Regulasi Resmi

1. **Undang-Undang No. 6 Tahun 2014** tentang Desa jo. **Undang-Undang No. 3 Tahun 2024** tentang Perubahan Kedua atas UU Desa.
2. **Peraturan Pemerintah No. 11 Tahun 2019** tentang Penghasilan Tetap Kepala Desa dan Perangkat Desa.
3. **Peraturan Pemerintah No. 11 Tahun 2021** tentang Badan Usaha Milik Desa (BUMDes).
4. **Permendagri No. 84 Tahun 2015** tentang Susunan Organisasi dan Tata Kerja (SOTK) Pemerintah Desa.
5. **Permendagri No. 67 Tahun 2017** tentang Pengangkatan dan Pemberhentian Perangkat Desa.
6. **Permendagri No. 20 Tahun 2018** tentang Pengelolaan Keuangan Desa.
7. **Permendagri No. 1 Tahun 2016** tentang Pengelolaan Aset Desa.
8. **Permendagri No. 47 Tahun 2016** tentang Administrasi Pemerintahan Desa.
9. **Permendagri No. 110 Tahun 2016** tentang Badan Permusyawaratan Desa (BPD).
10. **Permendagri No. 111 Tahun 2014** tentang Pedoman Teknis Peraturan di Desa.
11. **Permendesa PDTT No. 21 Tahun 2020** tentang Pedoman Umum Pembangunan Desa dan Pemberdayaan Masyarakat Desa.
12. **Peraturan Daerah Kabupaten Tuban No. 2 Tahun 2016** jo. **Perda No. 16 Tahun 2021** tentang Perangkat Desa.
13. **Peraturan Bupati Tuban No. 11 Tahun 2022** tentang Petunjuk Pelaksanaan Peraturan Daerah mengenai Pengangkatan Perangkat Desa.
14. **Peraturan Bupati Tuban No. 30 Tahun 2023** tentang Pengelolaan Keuangan Desa di Kabupaten Tuban.
15. **Undang-Undang No. 27 Tahun 2022** tentang Perlindungan Data Pribadi (UU PDP).
16. **Undang-Undang No. 41 Tahun 2004** tentang Wakaf jo. **PP No. 42 Tahun 2006**.
17. **Undang-Undang No. 16 Tahun 2019** tentang Perubahan atas **UU No. 1 Tahun 1974** tentang Perkawinan.
18. **Undang-Undang No. 23 Tahun 2011** tentang Pengelolaan Zakat.
19. **Peraturan Bersama Menteri Agama dan Menteri Dalam Negeri (PBM) No. 9 & 8 Tahun 2006** tentang Pemeliharaan Kerukunan Umat Beragama.
20. **Ejaan Bahasa Indonesia yang Disempurnakan (EYD Edisi V)** dari Kemendikbudristek.

---

## ⚖️ Lisensi, Hak Cipta, & Changelog Aplikasi

### 1. Hak Cipta (Copyright)
> **© 2026 Copyright by fusionproject.id**  
> Seluruh hak cipta dilindungi undang-undang. Aplikasi dikembangkan untuk tujuan simulasi latihan dan persiapan mandiri bagi calon aparatur pemerintah desa di Kabupaten Tuban dan sekitarnya. Seluruh data hasil pengerjaan ujian disimpan secara privat di penyimpanan lokal browser pengguna (*localStorage*) tanpa pernah dikirimkan ke server eksternal.

### 2. Aturan Penomoran Versi (Internal SemVer 3 Digit: `X.Y.Z`)
*Aturan ini digunakan oleh pengembang dan sistem otomasi git; versi bertambah secara otomatis pada setiap rilis fitur baru:*
* **Digit 1 (Besar / Major):** Perombakan arsitektur besar / format sistem (misal: `5.0.0`).
* **Digit 2 (Menengah / Minor):** Penambahan fitur baru, modul, atau aset branding (misal: `4.5.0`).
* **Digit 3 (Minor / Patch):** Perbaikan bug, penyesuaian teks, atau patch styling (misal: `4.5.1`).

### 3. Catatan Rilis & Riwayat Fitur (Changelog)

#### **v5.0.0 (Rilis Terkini — Perombakan Arsitektur Besar)**
- **Penyeimbangan Bank Soal 1.000 Butir (200 Soal per Bidang):** Restrukturisasi master bank soal menjadi tepat 200 butir soal per bidang untuk seluruh 5 bidang ujian (200 Agama, 200 Pemdes, 200 Bahasa Indonesia, 200 Pengetahuan Umum, 200 Pengetahuan Komputer).
- **Isolasi Ketat Antarbidang (Zero Mixing):** Pemisahan fisik file modul bank soal (`bank_bidang1_agama.py` s.d. `bank_bidang5_komputer.py`) dengan nomor ID unik berurutan (1–200, 201–400, 401–600, 601–800, 801–1000) dan filter `q.bidangId === cfg.id` saat pengundian sesi ujian sehingga soal bidang satu tidak akan pernah keluar atau tercampur di bidang lain.
- **Workflow Pembersihan Repositori Otomatis (cleanup-repo.yml):** Workflow GitHub Actions komprehensif yang otomatis membersihkan file `.py` di luar folder, folder usang `dev_scratch/`, modul generator legacy, cache python, file sampah OS, dan file duplikat baik di luar maupun di dalam subfolder.
- **Workflow & Skrip Optimasi Aset Mandiri (optimize-assets.yml & optimize_assets.py):** Workflow optimasi otomatis yang meminifikasi CSS (`style.min.css`, hemat 32.1%), kompresi JavaScript (`app.min.js`), optimasi gambar vektor SVG (hemat hingga 29.5%), dan kompresi HTML dengan validasi kelulusan 100% test suite.
- **Fitur Mode Latihan Mandiri Khusus per Bidang:** Menu latihan mandiri kini menyediakan dropdown filter materi khusus per bidang (Bidang 1 s.d. Bidang 5) selain per subkategori dan database lengkap.
- **Pembaruan Halaman Bantuan (Help) & Distribusi:** Tabel distribusi materi di Halaman Bantuan diperbarui dengan proporsi seimbang 1.000 butir soal berstandar Perda Kab. Tuban.

#### **v4.5.1**
- **Ekspansi Bank Soal Bahasa Indonesia (75 Butir):** Penambahan 40 butir soal baru (EYD V, tata naskah dinas desa, konjungsi antarkalimat, peluluhan fonem KTSP, nominal kas desa, dan kalimat efektif).
- **Eliminasi Kemiripan Soal:** Refaktorisasi butir soal bernuansa serupa sehingga seluruh 25 soal Bahasa Indonesia per sesi ujian memiliki konsep dan opsi 100% unik tanpa pengulangan.
- **Workflow Pembersih Repositori (cleanup-repo.yml):** Otomasi GitHub Actions untuk menghapus file Python dan cache di luar folder secara otomatis.

#### **v4.5.0**
- **Landing Page Sederhana & Bersih (Gambar 2):** Halaman depan kini tampil minimalis dan terfokus dengan kartu identitas peserta (Nama, Desa & Kecamatan, Fokus Regulasi) serta 2 tombol aksi utama: **"Mulai Ujian"** dan **"Mulai Mode Latihan"**.
- **Halaman Khusus Pusat Bantuan (Help):** Seluruh keterangan format ujian, tabel distribusi bank soal 585 butir, alur sekuensial 5 bidang, panduan praktik komputer, formula penilaian 87,5 + 12,5 = 100,0, dan rujukan hukum telah dipindahkan ke halaman tersendiri (`Bantuan`).
- **Menu Navigasi Modern & Minimalis (Gambar 3):** Desain navbar yang jauh lebih simpel, modern, dan elegan dengan tombol pill ber-backdrop blur, lencana versi aktif `v4.5.0`, drawer responsif mobile, dan pemilih skala font.
- **Footer direktori responsif:** Menyediakan navigasi latihan, materi, bantuan, informasi fitur aplikasi, dan tautan privasi.
- **Favicon & Logo Resmi:** Favicon SVG dan Logo Emblem CBT Kabupaten Tuban (`favicon.svg`, `logo.svg`, `assets/logo-full.svg`).
- **Atribusi Hak Cipta Konsisten:** Seluruh bagian aplikasi menggunakan atribusi resmi `Copyright by fusionproject.id`.
- **Workflow Deploy Bersih (deploy.yml):** Otomasi penghapusan file `.py` di root direktori, file non-web luar folder, dan pembersihan duplikat sebelum publikasi ke GitHub Pages.
- **Integritas Bank Soal:** 585 butir soal bebas duplikasi di bank data master dan pengundian 125 soal unik per sesi ujian tertulis.

#### **v4.4.0**
- **Sistem Ujian Praktik Komputer (10 Butir):** Modul tugas nyata Microsoft Office (Word, Excel, PowerPoint, ZIP) dengan skor maksimal 12,50 poin.
- **Dual-Mode Praktik:** Mode 1 (Office Asli dengan parser struktur OpenXML) dan Mode 2 (Simulasi Browser Interaktif dengan live spreadsheet grid).
- **Pengaturan Durasi Praktik:** Konfigurasi timer fleksibel (30m, 45m, 60m, 90m, dan Tanpa Batas).

#### **v4.3.0**
- **Struktur Ujian Resmi 5 Bidang Berurutan:** Agama (25 soal), Pemdes (25 soal), Bahasa Indonesia (25 soal), Pengetahuan Umum (25 soal), dan Komputer (25 soal).
- **Sequential Section Lock:** Penguncian sekuensial per seksi materi dengan timer independen 30 menit per bidang.
- **Formula Penilaian Resmi:** Perhitungan otomatis gabungan Tertulis (87,50) + Praktik (12,50) = 100,00 Poin Maksimal.

#### **v4.2.0**
- **Ekspansi Master Bank Soal (585 Butir):** Penambahan 100 butir soal baru (Pemerintahan Desa, Komputer Kantor Desa, dan Agama/Moderasi Beragama).
- **Audit Regulasi Terkini:** Penyelarasan materi dengan UU No. 3/2024 (Perubahan UU Desa), PP 11/2019, dan UU PDP No. 27/2022.

#### **v4.1.0**
- **Fitur Glosarium Pemerintahan Desa:** 36 istilah teknis administrasi desa lengkap dengan definisi dan rujukan hukum.
- **Rendering Teks Berformat:** Dukungan cetak miring (*italics*), tebal (*bold*), dan sintaks kode rumus pada soal dan pembahasan.

#### **v4.0.0**
- **Pemisahan Arsitektur Modular:** Refaktorisasi berkas menjadi `index.html`, `css/style.css`, dan `js/app.js` serta modul data terpisah.
- **Comprehensive Automated Test Suite:** Implementasi 4 modul pengujian berbasis Node.js untuk validasi otomatis offline dan CI/CD.

#### **v3.0.0**
- **Fitur Ekspor & Cadangan:** Ekspor hasil ujian ke format PDF/cetak sertifikat resmi, backup/restore riwayat berbasis JSON.
- **Mode Latihan Mandiri (Practice Mode):** Pemilihan materi per kategori dengan kunci pembahasan instan dan tombol ragu-ragu (*flagged*).

#### **v2.0.0**
- **Antarmuka Responsif & Tema Gelap (Dark Mode):** Desain mobile-first responsif, tombol pintas keyboard, dan navigasi nomor soal interaktif.

#### **v1.0.0**
- **Peluncuran Awal CBT Engine:** Simulasi ujian perangkat desa berbasis web peramban lokal dengan penyimpanan data privat (*localStorage*).

