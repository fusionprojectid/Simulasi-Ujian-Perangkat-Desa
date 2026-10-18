# Simulasi Ujian Perangkat Desa — Computer Assisted Test (CBT) Mandiri

Aplikasi simulasi seleksi Computer Assisted Test (CAT/CBT) untuk calon Perangkat Desa (Sekretaris Desa, Kepala Urusan/Kaur, Kepala Seksi/Kasi, dan Kepala Dusun/Kasun). Aplikasi ini dirancang khusus untuk persiapan seleksi perangkat desa di **Kabupaten Tuban, Jawa Timur** serta mengacu pada **Standar Nasional Indonesia**.

Aplikasi berupa **satu file tunggal mandiri (`index.html`)** yang beroperasi **100% offline**, tanpa backend server, tanpa dependensi framework/CDN eksternal, dan tanpa mengirimkan data ke jaringan (privat penuh).

---

## 🌟 Fitur Utama & Keunggulan

### 1. Bank Soal Master 200 Butir & Generator 100 Soal Acak
* **Database Master 200 Soal:** Seluruh butir soal telah diverifikasi, bebas duplikasi, dan dilengkapi pembahasan mendalam serta dasar hukum resmi.
* **Pengundian Proporsional:** Sistem mengundi tepat **100 butir soal secara acak** pada setiap sesi simulasi dengan memenuhi kuota resmi 12 kategori materi.
* **Pengacakan Pilihan Jawaban Aman:** Susunan opsi jawaban (A, B, C, D) diacak menggunakan algoritma *Fisher-Yates Shuffle*, sementara kunci jawaban (`answer`) disinkronkan secara otomatis berdasarkan teks aslinya sehingga penilaian dan pembahasan tetap 100% akurat.
* **Opsi Fleksibel:** Pengguna dapat mengaktifkan atau menonaktifkan pengacakan soal maupun pengacakan opsi jawaban melalui kontrol di beranda.

### 2. Sistem Timer CAT Realistis
* **Timer Total Ujian:** 100 Menit (6.000 detik) hitung mundur dengan peringatan visual berkedip (*urgent alert*) ketika waktu tersisa kurang dari 5 menit.
* **Timer Per Kunjungan Soal:** Batas maksimal 60 detik per soal. Jika waktu 60 detik habis, sistem otomatis melompat ke soal berikutnya dan mencatat soal yang dilewati.
* **Sinkronisasi Presisi:** Berbasis cap waktu riil (`Date.now()`) sehingga timer tidak mengalami desinkronisasi saat tab peramban diminimalkan.

### 3. Siklus Antrean Soal Belum Terjawab (*Automatic Priority Queue*)
* **Putaran Pertama (Sekuensial):** Menjawab soal secara otomatis melompat ke nomor berikutnya yang belum terjawab.
* **Putaran Kedua (Prioritas Soal Kosong):** Ketika mencapai akhir soal, sistem secara otomatis mengarahkan peserta ke nomor soal kosong terkecil secara berurutan hingga seluruh 100 butir terjawab atau waktu habis.

### 4. Mode CAT Realistis & Ringkasan Pra-Pengakhiran
* **Penanda Ragu-Ragu (`btnFlagQuestion` / Shortcut `R`):** Peserta dapat menandai soal yang belum pasti dengan tombol status kuning emas (`.btn-flagged`).
* **Palet Nomor Soal Interaktif:** Menampilkan status nomor (Hijau: Dijawab, Kuning: Ragu-ragu, Merah/Abu: Belum, Biru: Sedang Aktif) dilengkapi filter tab cepat.
* **Ringkasan Status Pra-Pengakhiran (*Pre-Finish Modal*):** Rekapitulasi jumlah soal yang dijawab, ragu-ragu, dan kosong sebelum ujian diakhiri, dilengkapi peringatan bahwa soal kosong bernilai 0 serta *interactive jump chips* untuk melompat langsung ke soal yang belum beres.

### 5. Analisis Kelemahan & Rekomendasi Pembelajaran
* Mengalkulasi persentase akurasi untuk setiap kategori materi secara otomatis.
* Mengurutkan kategori materi dari yang **paling lemah (akurasi terendah)**.
* Memberikan lencana status penguasaan:
  * `< 50%` : `[PERLU PENDALAMAN SERIUS]` (Merah)
  * `50% – 69%` : `[CUKUP - PERLU PENGUATAN]` (Kuning Emas)
  * `≥ 70%` : `[MENGUASAI DENGAN BAIK]` (Hijau Emerald)
* Memberikan rekomendasi rujukan pasal dan tombol **"Latihan Kategori Ini"** untuk langsung membuka sesi latihan terfokus.

### 6. Latihan Adaptif Sederhana (*Adaptive Drill*)
* **Ulangi Soal Salah:** Sesi khusus mengulang butir-butir soal yang dijawab salah pada sesi sebelumnya.
* **Ulangi Soal Kosong:** Mengerjakan kembali butir soal yang terlewat karena batas waktu kunjungan.
* **Ulangi Soal Ragu-ragu:** Memantapkan materi pada butir soal yang sempat ditandai bendera ragu-ragu.

### 7. Glosarium 36 Istilah Pemerintahan Desa
* Buku saku digital interaktif berisi **36 istilah penting dan singkatan regulasi desa** (Siltap, PKPKD, PPKD, APB Desa, RPJM Desa, RKP Desa, Musdes, Musrenbangdes, BPD, LKD, LAD, BUMDes, LKPPD, LPPD, IPPD, Siskeudes, Sipades, Tanah Kas Desa/Bengkok, Silpa, Dana Desa, ADD, BHPR, PADes, Perdes, Perkades, SK Kades, Sekdes, Kaur, Kasi, Kasun, batas usia pendaftaran 20–42 tahun, batas usia pensiun 60 tahun, masa jabatan kades 8 tahun per UU 3/2024, dll.).
* Dilengkapi **pencarian langsung (*live search filter*)** dan filter kategori.

### 8. Grafik Perkembangan Nilai SVG & Komparasi Sesi yang Adil
* Riwayat skor tersimpan otomatis di penyimpanan lokal browser.
* **Grafik Tren SVG Native:** Visualisasi garis tren kenaikan nilai yang responsif tanpa dependensi library eksternal.
* **Komparasi Antar-Sesi yang Adil:**
  * Sesi Simulasi Resmi 100 Soal hanya dibandingkan apel-ke-apel dengan Simulasi Resmi 100 Soal sebelumnya (`+poin` dan `+akurasi%`).
  * Jika membandingkan dua sesi yang berbeda jenis atau jumlah soalnya (misal latihan 25 soal vs simulasi 100 soal), sistem menampilkan peringatan eksplisit (*Disparity Warning*) bahwa hasil tidak dapat disetarakan secara langsung.

### 9. Cadangan Data Lokal (Ekspor & Impor JSON)
* **Ekspor Cadangan:** Mengunduh berkas `CBT_Perangkat_Desa_Cadangan_[TIMESTAMP].json` yang berisi seluruh riwayat sesi, profil peserta, dan pengaturan.
* **Impor Cadangan Aman:**
  * Membatasi ukuran berkas maksimal **2 MB**.
  * Validasi struktur dan skema (`app: "CBT_PERANGKAT_DESA"`).
  * Sanitasi data teks tanpa eksekusi kode dinamis (`no eval()`).
  * Pilihan: "Gabungkan Riwayat" (tanpa duplikasi) atau "Ganti Penuh".

### 10. Aksesibilitas (A11y) & Desain Responsif
* **Navigasi Keyboard Lengkap:**
  * `A`, `B`, `C`, `D`: Memilih pilihan jawaban.
  * `Panah Kiri (←)`: Soal sebelumnya.
  * `Panah Kanan (→)`: Soal berikutnya / lewati.
  * `R` atau `F`: Menandai ragu-ragu (*toggle flag*).
  * `Esc`: Menutup jendela modal yang aktif.
* **Font Scaler:** Tombol pengatur ukuran huruf di bilah atas: `A-` (90%), `A` (100%), dan `A+` (115%).
* **Fokus Visual:** Cincin fokus kontras tinggi (`outline: 3px solid var(--accent-gold-500)`).
* Standar rasio kontras warna memenuhi standar WCAG AA/AAA.

### 11. Privasi 100% & Ketahanan Aplikasi
* **Nol Pelacak & 100% Offline:** Tidak ada skrip analitik, piksel pelacak, iklan, atau transmisi jaringan.
* **Penanganan Penyimpanan Tangguh:** Fungsi wrapper penyimpanan aman (`safeGetStorage` dan `safeSetStorage`) memastikan aplikasi tetap berjalan normal jika kuota `localStorage` penuh atau dalam mode *incognito* ketat.
* **Pemulihan Sesi Otomatis:** Jika halaman di-refresh saat ujian berlangsung, sesi dipulihkan dengan urutan soal dan urutan opsi jawaban yang sama persis.

---

## 📊 Sebaran 12 Kategori Materi & Kuota Ujian

| No | Kategori Materi | Kuota Ujian | Jumlah di Database | Fokus Regulasi & Materi Utama |
|:---:|:---|:---:|:---:|:---|
| 1 | Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa | 20 Soal | **40 Soal** | UU No. 6/2014 jo. UU No. 3/2024, Permendagri 84/2015, Permendagri 67/2017, PP 11/2019, Siltap, usia & pensiun |
| 2 | Peraturan perundang-undangan dan tata kelola pemerintahan | 12 Soal | **24 Soal** | UU 12/2011, Permendagri 111/2014, asas desa, Perda Kab. Tuban 2/2016 jo. 16/2021, Perbup Tuban 11/2022 |
| 3 | Pancasila, UUD 1945, dan wawasan kebangsaan | 10 Soal | **20 Soal** | Butir pengamalan Sila 1-5, Pembukaan UUD 1945 alinea IV, Pasal 1(2), 27(3), 30(1), Bhinneka Tunggal Ika |
| 4 | Administrasi pemerintahan, surat-menyurat, dan pengarsipan | 10 Soal | **20 Soal** | Permendagri 47/2016 (5 buku adm desa), tata naskah dinas, buku ekspedisi, kop surat, SK Kades, retensi arsip |
| 5 | Keuangan desa, APB Desa, dan aset desa | 10 Soal | **20 Soal** | Permendagri 20/2018 (PKPKD, PPKD, Siskeudes, 5 bidang belanja), Permendagri 1/2016 (sewa aset desa maks 3 th) |
| 6 | Pembangunan desa, perencanaan, dan pemberdayaan masyarakat | 8 Soal | **16 Soal** | Permendesa 21/2020 (RPJM Desa 8 th, RKP Desa akhir Sept, Musrenbangdes), SDGs Desa, BUMDes PP 11/2021 |
| 7 | BPD, kelembagaan desa, dan musyawarah | 5 Soal | **10 Soal** | UU 6/2014 Pasal 55, Permendagri 110/2016 (3 fungsi BPD, larangan rangkap jabatan), Musdes, LKPPD 3 bulan |
| 8 | Bahasa Indonesia | 7 Soal | **14 Soal** | EYD V (antre, izin, kuitansi, jadwal, risiko), kapitalisasi naskah dinas, kalimat efektif bebas pleonasme |
| 9 | Matematika dan numerik | 6 Soal | **12 Soal** | Persentase silpa APB Desa, konversi hektar lahan bengkok, PPh 22, rata-rata pupuk, deret bilangan |
| 10 | Logika dan penalaran | 5 Soal | **10 Soal** | Silogisme kategorial seragam dinas, jadwal piket staf, modus tollens, himpunan bansos, mediasi batas |
| 11 | Pengetahuan umum | 4 Soal | **8 Soal** | Hari Jadi Tuban 12 Nov 1293 (Ronggolawe), Makam Sunan Bonang, hierarki pemda, lambang Garuda |
| 12 | Komputer dasar dan pelayanan publik | 3 Soal | **6 Soal** | Microsoft Excel (`=SUM`, `=AVERAGE`), Word Mail Merge surat desa, UU Perlindungan Data Pribadi (UU PDP 27/2022) |
| **TOTAL** | **12 Kategori Lengkap** | **100 Soal** | **200 Soal** | **100% Terverifikasi Regulasi Resmi** |

---

## 📂 Struktur Berkas Repository

```text
├── index.html              # Berkas tunggal mandiri aplikasi CBT (siap pakai di browser)
├── build_index.py          # Script generator Python untuk mengompilasi index.html
├── glossary_data.py        # Dataset 36 istilah glosarium resmi pemerintahan desa
├── merge_and_validate.py   # Script validasi & penggabungan master pool (200 butir)
├── expand_bank.py          # Dataset butir soal nomor 101 s.d. 200
├── validate_data.py        # Dataset butir soal nomor 1 s.d. 100
├── test_suite.js           # Pengujian komprehensif Node.js untuk 12 fitur sistem
└── README.md               # Dokumentasi lengkap proyek
```

---

## 🚀 Panduan Penggunaan

### 1. Menjalankan Aplikasi
Cukup klik ganda atau buka berkas `index.html` menggunakan peramban modern apa pun:
* Google Chrome
* Mozilla Firefox
* Microsoft Edge
* Safari / Opera

> **Catatan:** Tidak diperlukan koneksi internet, instalasi web server (Apache/Nginx/Node.js), ataupun ekstensi tambahan.

### 2. Mengompilasi Ulang `index.html` (Jika Mengubah Bank Soal / Glosarium)
Jika Anda menambahkan butir soal pada `expand_bank.py` atau memperbarui istilah di `glossary_data.py`, jalankan:
```bash
python build_index.py
```
Perintah ini akan memvalidasi data dan menghasilkan kembali berkas `index.html` mandiri secara otomatis.

### 3. Menjalankan Pengujian Otomatis
Pastikan Node.js terpasang, lalu jalankan:
```bash
node test_suite.js
```
Pengujian mencakup:
1. Ekstraksi master database 200 butir soal.
2. Integritas struktur soal, 4 opsi, 1 kunci benar, pembahasan, dan sumber regulasi.
3. Sebaran 12 kategori materi pada master database.
4. Pengacakan aman (Fisher-Yates) dan verifikasi sinkronisasi kunci jawaban acak.
5. Antrean prioritas soal kosong (sekuensial ke putaran soal kosong nomor terkecil).
6. Analisis kelemahan kategori dan pengurutan prioritas belajar.
7. Glosarium 36 istilah desa dan fungsi pencarian instan.
8. Komparasi antar-sesi adil (sesi setara vs deteksi perbedaan sesi).
9. Validasi berkas cadangan JSON (batas ukuran 2 MB dan verifikasi skema).
10. Verifikasi elemen antarmuka, aksesibilitas, dan modal CBT.

---

## 📜 Rujukan Regulasi Resmi yang Diverifikasi

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
15. **Ejaan Bahasa Indonesia yang Disempurnakan (EYD Edisi V)** dari Badan Pengembangan dan Pembinaan Bahasa Kemendikbudristek.
16. **Undang-Undang No. 27 Tahun 2022** tentang Perlindungan Data Pribadi (UU PDP).

---

## ⚖️ Lisensi & Ketentuan Penggunaan
Aplikasi ini dikembangkan untuk tujuan simulasi latihan dan persiapan mandiri bagi calon aparatur pemerintah desa. Materi dan bank soal disusun berdasarkan regulasi yang berlaku secara resmi. Seluruh data hasil ujian disimpan secara privat di perangkat pengguna.
