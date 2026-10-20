# -*- coding: utf-8 -*-
"""
Database Tambahan Soal 301 s.d. 400 untuk Simulasi CBT Perangkat Desa
Memperluas master bank soal dari 300 menjadi 400 butir soal.
Proporsional sesuai kuota 12 kategori ujian resmi:
- Kat 1 (Pemerintahan desa): 20 soal (ID 301 - 320)
- Kat 2 (Perundang-undangan): 12 soal (ID 321 - 332)
- Kat 3 (Pancasila & Wawasan Kebangsaan): 10 soal (ID 333 - 342)
- Kat 4 (Administrasi & Surat): 10 soal (ID 343 - 352)
- Kat 5 (Keuangan & Aset Desa): 10 soal (ID 353 - 362)
- Kat 6 (Pembangunan & Pemberdayaan): 8 soal (ID 363 - 370)
- Kat 7 (BPD & Musyawarah): 5 soal (ID 371 - 375)
- Kat 8 (Bahasa Indonesia): 7 soal (ID 376 - 382)
- Kat 9 (Matematika & Numerik): 6 soal (ID 383 - 388)
- Kat 10 (Logika & Penalaran): 5 soal (ID 389 - 393)
- Kat 11 (Pengetahuan Umum): 4 soal (ID 394 - 397)
- Kat 12 (Komputer & Pelayanan): 3 soal (ID 398 - 400)
TOTAL: 100 butir soal terverifikasi (ID 301 - 400).
"""

QUESTIONS_301_400 = [
  # =========================================================================
  # KATEGORI 1: Pemerintahan desa, struktur organisasi, tugas dan fungsi (20 Soal: ID 301-320)
  # =========================================================================
  {
    "id": 301,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Berdasarkan Undang-Undang Nomor 3 Tahun 2024 Pasal 26 ayat (3) dan Pasal 50A, Kepala Desa dan Perangkat Desa berhak menerima jaminan sosial dan tunjangan purnatugas, yang meliputi...",
    "options": [
      "Jaminan kesehatan, ketenagakerjaan, dan tunjangan purnatugas 1 kali di akhir masa jabatan sesuai kemampuan keuangan desa",
      "Gaji pensiun bulanan seumur hidup dari APBN setara PNS pusat",
      "Kepemilikan permanen tanah kas desa/bengkok tanpa batas waktu",
      "Bebas dari segala kewajiban hukum pajak dan retribusi daerah"
    ],
    "answer": 0,
    "explanation": "UU No. 3 Tahun 2024 secara tegas memperkuat hak Kepala Desa dan Perangkat Desa untuk memperoleh jaminan kesehatan, jaminan ketenagakerjaan, tunjangan purnatugas 1 (satu) kali di akhir masa pengabdian, serta perlindungan hukum kedinasan.",
    "source": "UU No. 3 Tahun 2024 Pasal 26 ayat (3) dan Pasal 50A"
  },
  {
    "id": 302,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Menurut UU No. 3 Tahun 2024 Pasal 50A, hak baru apakah yang dijamin undang-undang bagi Perangkat Desa setelah purnatugas?",
    "options": [
      "Mendapatkan pensiun bulanan seumur hidup setara PNS golongan IV",
      "Mendapatkan tunjangan purnatugas 1 (satu) kali di akhir masa jabatan sesuai kemampuan keuangan desa",
      "Mendapatkan hak kepemilikan penuh tanah kas desa/bengkok tanpa batas waktu",
      "Mendapatkan prioritas diangkat menjadi anggota legislatif daerah tanpa pemilu"
    ],
    "answer": 1,
    "explanation": "UU No. 3 Tahun 2024 menyisipkan Pasal 50A yang mengatur bahwa Perangkat Desa berhak mendapatkan tunjangan purnatugas 1 (satu) kali di akhir masa jabatan yang disesuaikan dengan kemampuan keuangan desa.",
    "source": "UU No. 3 Tahun 2024 Pasal 50A"
  },
  {
    "id": 303,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "mudah",
    "question": "Berdasarkan Permendagri No. 83 Tahun 2015 jo. Permendagri No. 67 Tahun 2017, syarat pendidikan formal minimal untuk diangkat menjadi Perangkat Desa adalah...",
    "options": [
      "Sekolah Dasar (SD) atau sederajat",
      "Sekolah Menengah Pertama (SMP) atau sederajat",
      "Sekolah Menengah Atas (SMA/SLTA) atau sederajat",
      "Diploma Tiga (D3) atau Sarjana (S1)"
    ],
    "answer": 2,
    "explanation": "Syarat umum pengangkatan perangkat desa menurut Permendagri No. 83 Tahun 2015 Pasal 2 ayat (2) huruf b adalah berpendidikan paling rendah Sekolah Menengah Umum atau yang sederajat.",
    "source": "Permendagri No. 83 Tahun 2015 Pasal 2 ayat (2) huruf b"
  },
  {
    "id": 304,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Dalam struktur Sekretariat Desa, pejabat yang bertugas membantu Sekretaris Desa dalam urusan penyusunan RAPBDesa dan evaluasi program pembangunan adalah...",
    "options": [
      "Kepala Urusan Tata Usaha dan Umum",
      "Kepala Urusan Perencanaan",
      "Kepala Seksi Pembangunan",
      "Kepala Dusun"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 84 Tahun 2015 Pasal 9 mengatur bahwa Kepala Urusan Perencanaan bertugas membantu Sekretaris Desa dalam urusan pelayanan administrasi pendukung tata pemerintahan, mengoordinasikan penyusunan perencanaan desa (RPJM Desa, RKP Desa, RAPBDesa), inventarisasi data pembangunan, dan monitoring evaluasi.",
    "source": "Permendagri No. 84 Tahun 2015 Pasal 9"
  },
  {
    "id": 305,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Pembangunan sarana prasarana fisik desa, pembinaan kesehatan masyarakat, dan pendidikan formal/non-formal di desa merupakan tugas dari...",
    "options": [
      "Kepala Seksi Kesejahteraan",
      "Kepala Urusan Keuangan",
      "Kepala Seksi Pelayanan",
      "Kepala Urusan Umum"
    ],
    "answer": 0,
    "explanation": "Permendagri No. 84 Tahun 2015 Pasal 10 ayat (2) menyebutkan Kepala Seksi Kesejahteraan bertugas melaksanakan pembangunan sarana prasarana perdesaan, pembangunan bidang pendidikan, kesehatan, dan sosialisasi serta motivasi masyarakat di bidang kebudayaan dan ekonomi.",
    "source": "Permendagri No. 84 Tahun 2015 Pasal 10"
  },
  {
    "id": 306,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Pelaksanaan pembinaan ketenteraman dusun, pengawasan ketertiban umum, dan mobilisasi warga dalam kegiatan gotong royong di tingkat kewilayahan dipimpin oleh...",
    "options": [
      "Sekretaris Desa",
      "Kepala Dusun (Kasun)",
      "Kepala Seksi Kesejahteraan",
      "Ketua Lembaga Pemberdayaan Masyarakat Desa (LPMD)"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 84 Tahun 2015 Pasal 12 menjelaskan Kepala Dusun berkedudukan sebagai unsur satuan tugas kewilayahan yang bertugas membantu Kepala Desa dalam pelaksanaan tugas di wilayah kerjanya.",
    "source": "Permendagri No. 84 Tahun 2015 Pasal 12"
  },
  {
    "id": 307,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "mudah",
    "question": "Berdasarkan PP No. 11 Tahun 2019, besaran penghasilan tetap (Siltap) Kepala Desa per bulan paling sedikit setara dengan...",
    "options": [
      "100% dari gaji pokok PNS Golongan II/a",
      "110% dari gaji pokok PNS Golongan II/a",
      "120% dari gaji pokok PNS Golongan II/a",
      "150% dari gaji pokok PNS Golongan II/a"
    ],
    "answer": 2,
    "explanation": "PP No. 11 Tahun 2019 Pasal 81 ayat (2) huruf a menetapkan besaran penghasilan tetap Kepala Desa paling sedikit Rp2.426.640,00 setara 120% dari gaji pokok Pegawai Negeri Sipil golongan ruang II/a.",
    "source": "PP No. 11 Tahun 2019 Pasal 81 ayat (2) huruf a"
  },
  {
    "id": 308,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "mudah",
    "question": "Berdasarkan Peraturan Pemerintah (PP) Nomor 11 Tahun 2019, sumber utama pendanaan yang digunakan untuk membayar Penghasilan Tetap (Siltap) dan tunjangan Kepala Desa serta Perangkat Desa dianggarkan dalam APB Desa yang bersumber dari...",
    "options": [
      "Alokasi Dana Desa (ADD) yang bersumber dari APBD Kabupaten",
      "Dana Desa (DD) yang bersumber dari APBN",
      "Iuran swadaya wajib masyarakat dusun",
      "Pendapatan dari denda penertiban ternak warga"
    ],
    "answer": 0,
    "explanation": "PP No. 11 Tahun 2019 Pasal 81 ayat (1) menegaskan bahwa penghasilan tetap Kepala Desa, Sekretaris Desa, dan Perangkat Desa lainnya dianggarkan dalam APB Desa yang bersumber dari Alokasi Dana Desa (ADD).",
    "source": "PP No. 11 Tahun 2019 Pasal 81 ayat (1)"
  },
  {
    "id": 309,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "mudah",
    "question": "Berdasarkan PP No. 11 Tahun 2019, besaran penghasilan tetap (Siltap) Perangkat Desa lainnya (Kaur, Kasi, dan Kasun) per bulan paling sedikit adalah...",
    "options": [
      "80% dari gaji pokok PNS Golongan II/a",
      "90% dari gaji pokok PNS Golongan II/a",
      "100% dari gaji pokok PNS Golongan II/a",
      "110% dari gaji pokok PNS Golongan II/a"
    ],
    "answer": 2,
    "explanation": "PP No. 11 Tahun 2019 Pasal 81 ayat (2) huruf c menetapkan besaran penghasilan tetap Perangkat Desa lainnya paling sedikit Rp2.022.200,00 setara 100% dari gaji pokok PNS golongan ruang II/a.",
    "source": "PP No. 11 Tahun 2019 Pasal 81 ayat (2) huruf c"
  },
  {
    "id": 310,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Dalam tata kelola penatausahaan keuangan desa, Kaur Keuangan (Bendahara Desa) dilarang mencairkan atau membayarkan uang belanja APB Desa apabila...",
    "options": [
      "Dokumen transaksi belum diverifikasi oleh Sekretaris Desa dan belum disetujui melalui SPP sah oleh Kepala Desa",
      "Penerima pembayaran belum menjadi nasabah bank swasta nasional",
      "Warga dusun belum menghadiri musyawarah khusus",
      "Kepala BPD sedang tidak berada di kantor balai desa"
    ],
    "answer": 0,
    "explanation": "Permendagri No. 20 Tahun 2018 Pasal 51 dan 54 menegaskan bahwa Bendahara Desa hanya dapat membayarkan belanja atas dasar Surat Permintaan Pembayaran (SPP) sah yang telah diverifikasi kelengkapannya oleh Sekretaris Desa dan disetujui Kepala Desa.",
    "source": "Permendagri No. 20 Tahun 2018 Pasal 51 dan 54"
  },
  {
    "id": 311,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Berdasarkan Permendagri No. 67 Tahun 2017, usia maksimal seorang Perangkat Desa untuk purnatugas (pemberhentian dengan hormat karena usia) adalah...",
    "options": [
      "Genap berusia 56 tahun",
      "Genap berusia 58 tahun",
      "Genap berusia 60 tahun",
      "Genap berusia 65 tahun"
    ],
    "answer": 2,
    "explanation": "Permendagri No. 67 Tahun 2017 Pasal 5 ayat (2) huruf b menyatakan bahwa Perangkat Desa diberhentikan karena telah berusia genap 60 (enam puluh) tahun.",
    "source": "Permendagri No. 67 Tahun 2017 Pasal 5 ayat (2) huruf b"
  },
  {
    "id": 312,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Berdasarkan Permendagri No. 67 Tahun 2017, dalam hal seorang Perangkat Desa ditetapkan sebagai tersangka tindak pidana korupsi, tindakan yang wajib diambil oleh Kepala Desa adalah...",
    "options": [
      "Memberhentikan secara tetap tanpa menunggu proses hukum",
      "Memberhentikan sementara sampai ada putusan pengadilan berkekuatan hukum tetap",
      "Memindahkannya ke dusun lain yang terpencil",
      "Membiarkan tetap aktif bertugas hingga dinyatakan vonis bersalah"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 67 Tahun 2017 Pasal 6 mengatur bahwa Perangkat Desa diberhentikan sementara oleh Kepala Desa setelah ditetapkan sebagai tersangka dalam tindak pidana korupsi, terorisme, makar, atau tindak pidana terhadap keamanan negara.",
    "source": "Permendagri No. 67 Tahun 2017 Pasal 6"
  },
  {
    "id": 313,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sulit",
    "question": "Berapakah jangka waktu maksimal bagi Camat untuk memberikan rekomendasi tertulis terhadap calon Perangkat Desa yang lolos penyaringan seleksi?",
    "options": [
      "3 hari kerja",
      "7 hari kerja",
      "14 hari kerja",
      "30 hari kerja"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 83 Tahun 2015 jo. Permendagri No. 67 Tahun 2017 Pasal 4 mengatur bahwa Camat memberikan rekomendasi tertulis paling lambat 7 (tujuh) hari kerja sejak diterimanya permohonan konsultasi dari Kepala Desa.",
    "source": "Permendagri No. 83 Tahun 2015 Pasal 4 ayat (4)"
  },
  {
    "id": 314,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Berdasarkan Permendagri No. 84 Tahun 2015, susunan organisasi pemerintah desa untuk Desa Swasembada wajib memiliki paling banyak...",
    "options": [
      "2 Kaur dan 2 Kasi",
      "3 Kaur dan 2 Kasi",
      "3 Kaur dan 3 Kasi",
      "4 Kaur dan 4 Kasi"
    ],
    "answer": 2,
    "explanation": "Permendagri No. 84 Tahun 2015 Pasal 3 mengatur bahwa desa swasembada wajib memiliki 3 urusan dan 3 seksi (3 Kaur dan 3 Kasi), sedangkan desa swakarya dapat 3 atau 2, dan desa swadaya maksimal 2 urusan dan 2 seksi.",
    "source": "Permendagri No. 84 Tahun 2015 Pasal 3"
  },
  {
    "id": 315,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "UU No. 6 Tahun 2014 Pasal 51 huruf a menegaskan larangan bagi Perangkat Desa untuk merugikan kepentingan umum. Selain itu, perangkat desa dilarang merangkap jabatan sebagai...",
    "options": [
      "Pengurus takmir masjid desa",
      "Anggota BPD, DPR/DPD/DPRD, dan jabatan lain yang dilarang undang-undang",
      "Anggota kelompok tani desa",
      "Pengurus paguyuban rukun tetangga"
    ],
    "answer": 1,
    "explanation": "UU No. 6 Tahun 2014 Pasal 51 huruf f melarang perangkat desa merangkap jabatan sebagai ketua atau anggota BPD, anggota DPR RI, DPD RI, DPRD Provinsi, DPRD Kabupaten/Kota, dan jabatan lain yang diatur peraturan perundang-undangan.",
    "source": "UU No. 6 Tahun 2014 Pasal 51 huruf f"
  },
  {
    "id": 316,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Kepala Urusan Tata Usaha dan Umum dalam menjalankan tugasnya bertanggung jawab langsung kepada...",
    "options": [
      "Kepala Seksi Pemerintahan",
      "Sekretaris Desa",
      "Ketua BPD",
      "Camat"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 84 Tahun 2015 mengatur bahwa Kepala Urusan (Kaur) berada di bawah dan bertanggung jawab kepada Sekretaris Desa sebagai pimpinan sekretariat desa.",
    "source": "Permendagri No. 84 Tahun 2015 Pasal 8 ayat (1)"
  },
  {
    "id": 317,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Berdasarkan Perda Kabupaten Tuban No. 2 Tahun 2016 jo. No. 16 Tahun 2021, pengangkatan Perangkat Desa dilakukan secara resmi dengan penerbitan...",
    "options": [
      "Surat Keputusan Camat",
      "Keputusan Kepala Desa",
      "Peraturan Desa",
      "Surat Perintah Kerja dari BPD"
    ],
    "answer": 1,
    "explanation": "Perda Kab. Tuban No. 2/2016 jo. 16/2021 mengatur bahwa Perangkat Desa diangkat oleh Kepala Desa dengan Keputusan Kepala Desa setelah mendapatkan rekomendasi tertulis dari Camat.",
    "source": "Perda Kab. Tuban No. 2/2016 jo. No. 16/2021 Pasal 12"
  },
  {
    "id": 318,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Kepada siapakah Kepala Desa wajib menyampaikan Laporan Penyelenggaraan Pemerintahan Desa (LPPD) tertulis pada setiap akhir tahun anggaran?",
    "options": [
      "Kepada BPD secara langsung",
      "Kepada Bupati melalui Camat",
      "Kepada seluruh pengurus RT/RW",
      "Kepada Menteri Desa PDTT"
    ],
    "answer": 1,
    "explanation": "Berdasarkan UU No. 6 Tahun 2014 Pasal 27 huruf a, Kepala Desa wajib menyampaikan Laporan Penyelenggaraan Pemerintahan Desa (LPPD) kepada Bupati/Walikota melalui Camat paling lambat 3 bulan setelah akhir tahun anggaran.",
    "source": "UU No. 6 Tahun 2014 Pasal 27 huruf a"
  },
  {
    "id": 319,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Laporan pertanggungjawaban penyelenggaraan pemerintahan desa yang disampaikan oleh Kepala Desa kepada Badan Permusyawaratan Desa (BPD) disebut...",
    "options": [
      "Laporan Keterangan Penyelenggaraan Pemerintahan Desa (LKPPD)",
      "Laporan Penyelenggaraan Pemerintahan Desa (LPPD)",
      "Informasi Penyelenggaraan Pemerintahan Desa (IPPD)",
      "Laporan Kinerja Instansi Pemerintah (LKjIP)"
    ],
    "answer": 0,
    "explanation": "Berdasarkan UU No. 6 Tahun 2014 Pasal 27 huruf b dan Permendagri No. 46 Tahun 2016, laporan yang wajib disampaikan Kades kepada BPD secara tertulis adalah LKPPD (Laporan Keterangan Penyelenggaraan Pemerintahan Desa).",
    "source": "UU No. 6 Tahun 2014 Pasal 27 huruf b & Permendagri No. 46 Tahun 2016"
  },
  {
    "id": 320,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "mudah",
    "question": "Informasi Penyelenggaraan Pemerintahan Desa (IPPD) wajib dipublikasikan oleh Kepala Desa kepada masyarakat melalui...",
    "options": [
      "Pemberitahuan surat rahasia tertutup kepada tokoh masyarakat tertentu",
      "Papan pengumuman desa, radio komunitas, atau media informasi resmi desa lainnya yang mudah diakses warga",
      "Pemberitahuan lisan saat rapat tertutup perangkat desa",
      "Grup perpesanan pribadi perangkat desa"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 46 Tahun 2016 Pasal 10 mengatur bahwa Informasi Penyelenggaraan Pemerintahan Desa (IPPD) disampaikan kepada masyarakat desa melalui media informasi yang mudah diakses masyarakat, seperti papan pengumuman, media cetak, atau media elektronik.",
    "source": "Permendagri No. 46 Tahun 2016 Pasal 10"
  },

  # =========================================================================
  # KATEGORI 2: Peraturan perundang-undangan dan tata kelola (12 Soal: ID 321-332)
  # =========================================================================
  {
    "id": 321,
    "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
    "difficulty": "mudah",
    "question": "Berdasarkan Undang-Undang No. 12 Tahun 2011 Pasal 7 ayat (1), peraturan hukum yang menempati hierarki tertinggi di Negara Kesatuan Republik Indonesia adalah...",
    "options": [
      "Undang-Undang / Peraturan Pemerintah Pengganti Undang-Undang",
      "Ketetapan Majelis Permusyawaratan Rakyat (TAP MPR)",
      "Undang-Undang Dasar Negara Republik Indonesia Tahun 1945",
      "Peraturan Presiden"
    ],
    "answer": 2,
    "explanation": "UU No. 12 Tahun 2011 Pasal 7 ayat (1) menyatakan jenis dan hierarki peraturan perundang-undangan di Indonesia berturut-turut adalah: 1. UUD 1945, 2. Tap MPR, 3. UU/Perppu, 4. Peraturan Pemerintah, 5. Peraturan Presiden, 6. Perda Provinsi, 7. Perda Kabupaten/Kota.",
    "source": "UU No. 12 Tahun 2011 Pasal 7 ayat (1)"
  },
  {
    "id": 322,
    "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
    "difficulty": "sedang",
    "question": "Berdasarkan Undang-Undang Nomor 12 Tahun 2011 Pasal 15, materi muatan tentang ketentuan sanksi pidana (kurungan atau denda) hanya dapat dimuat dalam peraturan perundang-undangan tingkat...",
    "options": [
      "Undang-Undang, Peraturan Daerah Provinsi, dan Peraturan Daerah Kabupaten/Kota",
      "Peraturan Desa dan Peraturan Kepala Desa",
      "Peraturan Menteri dan Keputusan Camat",
      "Semua tingkatan produk hukum tanpa terkecuali"
    ],
    "answer": 0,
    "explanation": "Pasal 15 UU No. 12 Tahun 2011 menegaskan materi muatan mengenai sanksi pidana hanya boleh dimuat dalam Undang-Undang dan Peraturan Daerah (Provinsi/Kabupaten/Kota). Perdes dilarang memuat sanksi pidana kurungan.",
    "source": "UU No. 12 Tahun 2011 Pasal 15"
  },
  {
    "id": 323,
    "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
    "difficulty": "sedang",
    "question": "Berdasarkan Permendagri No. 111 Tahun 2014, Badan Permusyawaratan Desa (BPD) berhak mengajukan usulan Rancangan Peraturan Desa inisiatif, KECUALI terhadap rancangan perdes tentang...",
    "options": [
      "Rancangan Perdes tentang RPJM Desa, RKP Desa, APB Desa, dan Laporan Pertanggungjawaban Realisasi APB Desa",
      "Rancangan Perdes tentang Pelestarian Sumber Air Desa",
      "Rancangan Perdes tentang Pengelolaan Sampah Dusun",
      "Rancangan Perdes tentang Penertiban Hewan Liar"
    ],
    "answer": 0,
    "explanation": "Permendagri No. 111 Tahun 2014 Pasal 8 mengatur BPD berhak mengusulkan rancangan Perdes, kecuali untuk rancangan RPJM Desa, RKP Desa, APB Desa, dan LPJ Realisasi APB Desa yang merupakan wewenang mutlak Pemerintah Desa.",
    "source": "Permendagri No. 111 Tahun 2014 Pasal 8"
  },
  {
    "id": 324,
    "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
    "difficulty": "mudah",
    "question": "Media publikasi resmi pemerintah desa yang digunakan untuk mengundangkan Peraturan Desa (Perdes) agar memiliki kekuatan hukum berlaku adalah...",
    "options": [
      "Berita Desa",
      "Lembaran Desa",
      "Lembaran Daerah",
      "Papan Pengumuman Dusun"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 111 Tahun 2014 Pasal 22 mengatur bahwa Peraturan Desa diundangkan dalam Lembaran Desa oleh Sekretaris Desa.",
    "source": "Permendagri No. 111 Tahun 2014 Pasal 22"
  },
  {
    "id": 325,
    "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
    "difficulty": "mudah",
    "question": "Peraturan Kepala Desa (Perkades) yang bersifat pengaturan teknis operasional mulai berlaku sah dan memiliki kekuatan hukum mengikat sejak...",
    "options": [
      "Tanggal diundangkannya dalam Berita Desa oleh Sekretaris Desa",
      "Tanggal diucapkannya pidato oleh Kepala Desa di balai desa",
      "Tanggal disetujuinya oleh rapat keluarga Kepala Desa",
      "Tiga tahun setelah tanggal penetapan"
    ],
    "answer": 0,
    "explanation": "Permendagri No. 111 Tahun 2014 Pasal 24 ayat (2) menyatakan bahwa Peraturan Kepala Desa mulai berlaku dan mempunyai kekuatan hukum mengikat sejak tanggal diundangkan dalam Berita Desa oleh Sekretaris Desa.",
    "source": "Permendagri No. 111 Tahun 2014 Pasal 24"
  },
  {
    "id": 326,
    "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
    "difficulty": "sedang",
    "question": "Asas pembentukan peraturan perundang-undangan yang mewajibkan setiap regulasi memiliki tujuan yang jelas dan pasti untuk apa dibentuk disebut...",
    "options": [
      "Asas kejelasan tujuan",
      "Asas organ pembentuk yang tepat",
      "Asas kejelasan rumusan",
      "Asas keterbukaan"
    ],
    "answer": 0,
    "explanation": "UU No. 12 Tahun 2011 Pasal 5 huruf a menjelaskan asas 'kejelasan tujuan' bermakna bahwa setiap pembentukan peraturan perundang-undangan harus mempunyai tujuan yang jelas yang hendak dicapai.",
    "source": "UU No. 12 Tahun 2011 Pasal 5 huruf a"
  },
  {
    "id": 327,
    "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
    "difficulty": "sedang",
    "question": "Menurut UU No. 6 Tahun 2014 Pasal 69 ayat (2), materi muatan Peraturan Desa dilarang bertentangan dengan...",
    "options": [
      "Hasil rapat internal partai politik pemenang pemilu",
      "Kepentingan umum dan peraturan perundang-undangan yang lebih tinggi",
      "Kebijakan kepala desa periode sebelumnya",
      "Opini yang berkembang di media sosial desa"
    ],
    "answer": 1,
    "explanation": "UU No. 6 Tahun 2014 Pasal 69 ayat (2) menegaskan bahwa Peraturan Desa dilarang bertentangan dengan kepentingan umum dan/atau ketentuan peraturan perundang-undangan yang lebih tinggi.",
    "source": "UU No. 6 Tahun 2014 Pasal 69 ayat (2)"
  },
  {
    "id": 328,
    "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
    "difficulty": "sulit",
    "question": "Berdasarkan Permendagri No. 111 Tahun 2014 dan Permendagri No. 20 Tahun 2018, hasil evaluasi Camat atas Rancangan Peraturan Desa tentang APB Desa wajib disampaikan kepada Kepala Desa paling lambat...",
    "options": [
      "20 (dua puluh) hari kerja sejak diterimanya rancangan peraturan desa oleh Camat",
      "3 hari kerja sejak pengajuan",
      "60 hari kalender tanpa batasan",
      "6 bulan setelah tahun anggaran dimulai"
    ],
    "answer": 0,
    "explanation": "Permendagri No. 20 Tahun 2018 Pasal 38 ayat (2) menetapkan bahwa evaluasi rancangan Perdes APB Desa oleh bupati/camat dilakukan paling lama 20 (dua puluh) hari kerja sejak diterima.",
    "source": "Permendagri No. 111 Tahun 2014 Pasal 13 jo. Permendagri No. 20 Tahun 2018 Pasal 38"
  },
  {
    "id": 329,
    "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
    "difficulty": "sedang",
    "question": "Berdasarkan UU No. 12 Tahun 2011, asas yang menghendaki agar setiap pembentukan regulasi melibatkan masyarakat secara bermakna (meaningful participation) disebut...",
    "options": [
      "Asas legalitas",
      "Asas keterbukaan",
      "Asas praduga tak bersalah",
      "Asas sentralisasi wewenang"
    ],
    "answer": 1,
    "explanation": "Asas keterbukaan (Pasal 5 huruf g UU 12/2011) menuntut agar pembentukan regulasi mulai dari perencanaan hingga pengundangan bersifat transparan dan memberi ruang partisipasi bagi publik.",
    "source": "UU No. 12 Tahun 2011 Pasal 5 huruf g"
  },
  {
    "id": 330,
    "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
    "difficulty": "sedang",
    "question": "Di Kabupaten Tuban, peraturan bupati yang mengatur petunjuk teknis seleksi pengangkatan dan pemberhentian perangkat desa adalah...",
    "options": [
      "Peraturan Bupati Tuban No. 11 Tahun 2022",
      "Peraturan Bupati Tuban No. 50 Tahun 2010",
      "Peraturan Daerah Tuban No. 1 Tahun 2005",
      "Instruksi Camat Tuban No. 3 Tahun 2020"
    ],
    "answer": 0,
    "explanation": "Perbup Tuban No. 11 Tahun 2022 merupakan pedoman teknis yang mengatur pelaksanaan pengangkatan dan pemberhentian perangkat desa di seluruh wilayah Kabupaten Tuban.",
    "source": "Peraturan Bupati Tuban No. 11 Tahun 2022"
  },
  {
    "id": 331,
    "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
    "difficulty": "sedang",
    "question": "Berdasarkan UU No. 30 Tahun 2014 tentang Administrasi Pemerintahan, asas yang melarang pejabat pemerintah memihak dan mewajibkan pelayanan yang netral adalah...",
    "options": [
      "Asas Ketidakberpihakan (Impartiality)",
      "Asas Kemanfaatan",
      "Asas Otonomi Daerah",
      "Asas Efisiensi Anggaran"
    ],
    "answer": 0,
    "explanation": "UU No. 30 Tahun 2014 Pasal 10 ayat (1) huruf c mengatur Asas Ketidakberpihakan, yaitu asas yang mewajibkan Badan dan/atau Pejabat Pemerintahan dalam menetapkan dan/atau melakukan keputusan dan/atau tindakan dengan mempertimbangkan kepentingan para pihak secara keseluruhan dan tidak diskriminatif.",
    "source": "UU No. 30 Tahun 2014 Pasal 10 ayat (1) huruf c"
  },
  {
    "id": 332,
    "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
    "difficulty": "sedang",
    "question": "Sanksi apakah yang dapat dijatuhkan apabila suatu Peraturan Desa terbukti bertentangan dengan peraturan perundang-undangan yang lebih tinggi?",
    "options": [
      "Pembatalan Peraturan Desa melalui Keputusan Bupati",
      "Pemberian denda uang tunai kepada seluruh warga desa",
      "Penghapusan status otonomi desa menjadi kelurahan seketika",
      "Pembubaran BPD dan pelantikan perangkat desa baru"
    ],
    "answer": 0,
    "explanation": "Permendagri No. 111 Tahun 2014 dan UU No. 6 Tahun 2014 mengatur bahwa Peraturan Desa yang bertentangan dengan kepentingan umum dan peraturan yang lebih tinggi dibatalkan oleh Bupati/Walikota melalui Keputusan Bupati/Walikota.",
    "source": "Permendagri No. 111 Tahun 2014 Pasal 26"
  },

  # =========================================================================
  # KATEGORI 3: Pancasila, UUD 1945, dan wawasan kebangsaan (10 Soal: ID 333-342)
  # =========================================================================
  {
    "id": 333,
    "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
    "difficulty": "mudah",
    "question": "Perangkat desa yang memfasilitasi izin perayaan hari besar seluruh agama warga tanpa membeda-bedakan keyakinan merupakan wujud pengamalan Pancasila sila ke-...",
    "options": [
      "Pertama: Ketuhanan Yang Maha Esa",
      "Kedua: Kemanusiaan yang Adil dan Beradab",
      "Ketiga: Persatuan Indonesia",
      "Kelima: Keadilan Sosial bagi Seluruh Rakyat Indonesia"
    ],
    "answer": 0,
    "explanation": "Mengembangkan sikap toleransi dan membina kerukunan antarumat beragama merupakan butir pokok pengamalan Sila ke-1 Pancasila: Ketuhanan Yang Maha Esa.",
    "source": "Ketetapan MPR No. I/MPR/2003 Butir Pengamalan Sila 1"
  },
  {
    "id": 334,
    "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
    "difficulty": "mudah",
    "question": "Aksi tanggap darurat aparatur desa bersama warga menggalang bantuan pangan bagi keluarga prasejahtera yang terdampak banjir luapan sungai mencerminkan pengamalan Pancasila sila ke-...",
    "options": [
      "Pertama",
      "Kedua",
      "Keempat",
      "Kelima"
    ],
    "answer": 1,
    "explanation": "Gemar melakukan kegiatan kemanusiaan dan menjunjung tinggi nilai-nilai kemanusiaan sesama manusia merupakan pengamalan Sila ke-2: Kemanusiaan yang Adil dan Beradab.",
    "source": "Ketetapan MPR No. I/MPR/2003 Butir Pengamalan Sila 2"
  },
  {
    "id": 335,
    "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
    "difficulty": "sedang",
    "question": "Sikap mendahulukan kepentingan bersama desa di atas kepentingan pribadi, keluarga, atau dusun sendiri merupakan pengamalan sila ke-...",
    "options": [
      "Pertama",
      "Kedua",
      "Ketiga",
      "Keempat"
    ],
    "answer": 2,
    "explanation": "Menempatkan persatuan, kesatuan, serta kepentingan dan keselamatan bangsa/masyarakat di atas kepentingan pribadi atau golongan merupakan butir Sila ke-3: Persatuan Indonesia.",
    "source": "Ketetapan MPR No. I/MPR/2003 Butir Pengamalan Sila 3"
  },
  {
    "id": 336,
    "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
    "difficulty": "mudah",
    "question": "Pengambilan keputusan pembangunan jembatan desa melalui musyawarah mufakat di Balai Desa tanpa memaksakan kehendak kelompok mayoritas merupakan pengamalan sila ke-...",
    "options": [
      "Kedua",
      "Ketiga",
      "Keempat",
      "Kelima"
    ],
    "answer": 2,
    "explanation": "Musyawarah untuk mufakat yang diliputi oleh semangat kekeluargaan dan tidak memaksakan kehendak kepada orang lain merupakan wujud nyata pengamalan Sila ke-4 Pancasila.",
    "source": "Ketetapan MPR No. I/MPR/2003 Butir Pengamalan Sila 4"
  },
  {
    "id": 337,
    "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
    "difficulty": "sedang",
    "question": "Penyaluran Bantuan Langsung Tunai (BLT) Desa secara transparan, tepat sasaran kepada warga miskin tanpa nepotisme mencerminkan pengamalan sila ke-...",
    "options": [
      "Kedua",
      "Ketiga",
      "Keempat",
      "Kelima"
    ],
    "answer": 3,
    "explanation": "Mengembangkan perbuatan luhur yang mencerminkan sikap kekeluargaan dan gotong royong serta menjaga keseimbangan antara hak dan kewajiban secara adil merupakan butir Sila ke-5: Keadilan Sosial bagi Seluruh Rakyat Indonesia.",
    "source": "Ketetapan MPR No. I/MPR/2003 Butir Pengamalan Sila 5"
  },
  {
    "id": 338,
    "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
    "difficulty": "sedang",
    "question": "Tujuan negara Republik Indonesia untuk 'mencerdaskan kehidupan bangsa' dan 'memajukan kesejahteraan umum' tercantum secara tegas di dalam...",
    "options": [
      "Pembukaan UUD NRI 1945 Alinea I",
      "Pembukaan UUD NRI 1945 Alinea II",
      "Pembukaan UUD NRI 1945 Alinea III",
      "Pembukaan UUD NRI 1945 Alinea IV"
    ],
    "answer": 3,
    "explanation": "Alinea IV Pembukaan UUD 1945 memuat 4 tujuan negara Indonesia: melindungi segenap bangsa dan seluruh tumpah darah, memajukan kesejahteraan umum, mencerdaskan kehidupan bangsa, dan ikut melaksanakan ketertiban dunia.",
    "source": "Pembukaan UUD 1945 Alinea IV"
  },
  {
    "id": 339,
    "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
    "difficulty": "sedang",
    "question": "Pasal di dalam UUD 1945 yang secara khusus mengakui dan menghormati kesatuan-kesatuan masyarakat hukum adat beserta hak-hak tradisionalnya sepanjang masih hidup adalah...",
    "options": [
      "Pasal 18B ayat (2)",
      "Pasal 27 ayat (3)",
      "Pasal 30 ayat (1)",
      "Pasal 33 ayat (1)"
    ],
    "answer": 0,
    "explanation": "UUD 1945 Pasal 18B ayat (2) menyatakan: 'Negara mengakui dan menghormati kesatuan-kesatuan masyarakat hukum adat serta hak-hak tradisionalnya sepanjang masih hidup dan sesuai dengan perkembangan masyarakat dan prinsip NKRI'.",
    "source": "UUD 1945 Pasal 18B ayat (2)"
  },
  {
    "id": 340,
    "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
    "difficulty": "mudah",
    "question": "UUD 1945 Pasal 27 ayat (1) mengatur tentang prinsip persamaan warga negara, yaitu bahwa segala warga negara bersamaan kedudukannya di dalam...",
    "options": [
      "Ekonomi dan perdagangan",
      "Hukum dan pemerintahan",
      "Organisasi kemasyarakatan",
      "Pendidikan tinggi dan profesi"
    ],
    "answer": 1,
    "explanation": "Pasal 27 ayat (1) UUD 1945 berbunyi: 'Segala warga negara bersamaan kedudukannya di dalam hukum dan pemerintahan dan wajib menjunjung hukum dan pemerintahan itu dengan tidak ada kecualinya'.",
    "source": "UUD 1945 Pasal 27 ayat (1)"
  },
  {
    "id": 341,
    "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
    "difficulty": "mudah",
    "question": "Landasan konstitusional yang menjadi dasar penyelenggaraan jaring pengaman sosial di desa (Pasal 34 ayat 1 UUD 1945) menyatakan bahwa...",
    "options": [
      "Bumi dan air dikuasai oleh pengusaha swasta",
      "Fakir miskin dan anak-anak terlantar dipelihara oleh negara",
      "Pendidikan dasar dipungut biaya sesuai kesepakatan",
      "Tiap warga negara wajib menjadi anggota kepolisian"
    ],
    "answer": 1,
    "explanation": "Pasal 34 ayat (1) UUD 1945 menyatakan: 'Fakir miskin dan anak-anak yang terlantar dipelihara oleh negara'. Ini menjadi fondasi dasar bantuan sosial kemasyarakatan di desa.",
    "source": "UUD 1945 Pasal 34 ayat (1)"
  },
  {
    "id": 342,
    "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
    "difficulty": "sedang",
    "question": "Konsep geopolitik Indonesia yang memandang tanah air Indonesia sebagai satu kesatuan utuh politik, ekonomi, sosial budaya, dan pertahanan keamanan disebut...",
    "options": [
      "Ketahanan Nasional",
      "Wawasan Nusantara",
      "Bhinneka Tunggal Ika",
      "Sumpah Palapa"
    ],
    "answer": 1,
    "explanation": "Wawasan Nusantara adalah cara pandang bangsa Indonesia tentang diri dan lingkungannya berdasarkan Pancasila dan UUD 1945 sebagai satu kesatuan utuh kepulauan nusantara.",
    "source": "Doktrin Dasar Wawasan Nusantara Lemhannas"
  },

  # =========================================================================
  # KATEGORI 4: Administrasi pemerintahan, surat-menyurat, dan pengarsipan (10 Soal: ID 343-352)
  # =========================================================================
  {
    "id": 343,
    "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
    "difficulty": "mudah",
    "question": "Berdasarkan Permendagri No. 47 Tahun 2016, buku administrasi desa yang digunakan untuk mencatat surat masuk dan surat keluar secara berurutan tanggal penerimaan dan pengiriman adalah...",
    "options": [
      "Buku Agenda",
      "Buku Kas Umum",
      "Buku Mutasi Penduduk",
      "Buku Inventaris Desa"
    ],
    "answer": 0,
    "explanation": "Permendagri No. 47 Tahun 2016 mengatur Buku Agenda sebagai buku administrasi umum untuk mencatat keluar masuknya surat dinas secara tertib.",
    "source": "Permendagri No. 47 Tahun 2016 Lampiran Buku Administrasi Umum"
  },
  {
    "id": 344,
    "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
    "difficulty": "mudah",
    "question": "Dalam tata persuratan desa, buku administrasi umum yang digunakan untuk mencatat seluruh surat dinas yang diterima oleh pemerintah desa secara kronologis disebut...",
    "options": [
      "Buku Agenda Surat Masuk",
      "Buku Notula Musyawarah",
      "Buku Kas Pembantu Bank",
      "Buku Tamu Umum"
    ],
    "answer": 0,
    "explanation": "Buku Agenda Surat Masuk mencatat nomor urut, tanggal penerimaan, tanggal dan nomor surat masuk, instansi pengirim, perihal/isi ringkas surat, dan disposisi tindak lanjut.",
    "source": "Permendagri No. 47 Tahun 2016 tentang Administrasi Pemerintahan Desa"
  },
  {
    "id": 345,
    "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
    "difficulty": "sedang",
    "question": "Buku administrasi umum yang digunakan untuk mencatat identitas lengkap, nomor SK pengangkatan, dan riwayat pendidikan seluruh perangkat desa adalah...",
    "options": [
      "Buku Induk Penduduk",
      "Buku Aparat Pemerintah Desa",
      "Buku Kader Pemberdayaan",
      "Buku Data Inventaris Aset"
    ],
    "answer": 1,
    "explanation": "Buku Aparat Pemerintah Desa memuat data nama, jenis kelamin, jabatan, nomor dan tanggal pengangkatan/pelantikan, serta keterangan pendidikan seluruh aparatur desa.",
    "source": "Permendagri No. 47 Tahun 2016"
  },
  {
    "id": 346,
    "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
    "difficulty": "sedang",
    "question": "Dalam administrasi kependudukan desa, peristiwa mutasi penduduk yang wajib dicatat di Buku Mutasi Penduduk meliputi...",
    "options": [
      "Kelahiran, kematian, kepindahan, dan kedatangan penduduk",
      "Pernikahan, perceraian, dan pembelian kendaraan",
      "Pelunasan pajak PBB dan arisan warga",
      "Perubahan warna cat rumah warga"
    ],
    "answer": 0,
    "explanation": "Buku Data Mutasi Penduduk Desa mencatat empat peristiwa vital perubahan demografi: kelahiran, kematian, pindah datang, dan pindah pergi.",
    "source": "Permendagri No. 47 Tahun 2016 Lampiran Administrasi Penduduk"
  },
  {
    "id": 347,
    "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
    "difficulty": "mudah",
    "question": "Pada kepala surat (kop surat) resmi Pemerintah Desa di Kabupaten Tuban, letak lambang daerah Kabupaten Tuban diposisikan di...",
    "options": [
      "Sebelah kiri atas kepala surat",
      "Sebelah kanan bawah surat",
      "Tengah-tengah halaman belakang surat",
      "Kiri bawah tepat di atas tanda tangan kades"
    ],
    "answer": 0,
    "explanation": "Sesuai tata naskah dinas pemerintah daerah dan desa, lambang daerah kabupaten diletakkan di sisi kiri atas kop surat dinas resmi.",
    "source": "Pedoman Tata Naskah Dinas Permendagri No. 1 Tahun 2023"
  },
  {
    "id": 348,
    "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
    "difficulty": "sedang",
    "question": "Penulisan bagian 'Tembusan' yang benar dan baku pada naskah dinas resmi pemerintah desa adalah...",
    "options": [
      "Tembusan Yth. Bapak Camat Tuban di tempat.",
      "Tembusan disampaikan kepada c.c. Yth. Camat.",
      "Tembusan: 1. Camat Tuban; 2. Ketua BPD",
      "C.C.: Kepada Yang Terhormat Bapak Camat"
    ],
    "answer": 2,
    "explanation": "Aturan tata naskah dinas baku: kata 'Tembusan' diikuti tanda titik dua (:) tanpa menambahkan kata 'Yth.' atau 'kepada' atau singkatan 'c.c.', melainkan langsung nomor urut dan nama jabatan pejabat yang ditembuskan.",
    "source": "Tata Naskah Dinas Kemendagri"
  },
  {
    "id": 349,
    "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
    "difficulty": "sedang",
    "question": "Dalam penomoran surat resmi desa (contoh: 140/012/414.300.01/2026), angka '140' pada urutan pertama umumnya menunjukkan...",
    "options": [
      "Nomor urut buku agenda surat",
      "Kode klasifikasi masalah surat (Pemerintahan)",
      "Jumlah halaman lampiran surat",
      "Tahun pembuatan naskah dinas"
    ],
    "answer": 1,
    "explanation": "Angka urutan awal pada nomor surat dinas menunjukkan kode klasifikasi arsip/masalah (kode 140 merupakan kode klasifikasi urusan pemerintahan desa).",
    "source": "Permendagri No. 83 Tahun 2022 tentang Kode Klasifikasi Arsip"
  },
  {
    "id": 350,
    "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
    "difficulty": "sedang",
    "question": "Arsip kantor desa yang frekuensi penggunaannya telah menurun tetapi masih disimpan karena masih memiliki nilai guna administrasi atau hukum disebut...",
    "options": [
      "Arsip dinamis aktif",
      "Arsip dinamis inaktif",
      "Arsip statis permanen",
      "Arsip musnah"
    ],
    "answer": 1,
    "explanation": "UU No. 43 Tahun 2009 tentang Kearsipan membedakan arsip dinamis aktif (masih sering dipakai) dan arsip dinamis inaktif (frekuensi penggunaan menurun tetapi masih disimpan sesuai retensi).",
    "source": "UU No. 43 Tahun 2009 tentang Kearsipan Pasal 1"
  },
  {
    "id": 351,
    "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
    "difficulty": "sedang",
    "question": "Bagian dari Surat Keputusan (SK) Kepala Desa yang memuat pertimbangan latar belakang atau alasan perlunya keputusan diterbitkan diawali dengan kata...",
    "options": [
      "Mengingat :",
      "Menimbang :",
      "Memutuskan :",
      "Menetapkan :"
    ],
    "answer": 1,
    "explanation": "Bagian konsiderans diawali kata 'Menimbang:' yang memuat pokok-pokok pikiran, latar belakang, dan alasan perlunya diterbitkannya keputusan tersebut.",
    "source": "Tata Naskah Dinas Surat Keputusan Kemendagri"
  },
  {
    "id": 352,
    "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
    "difficulty": "sedang",
    "question": "Jadwal Retensi Arsip (JRA) di kantor desa berfungsi sebagai pedoman untuk...",
    "options": [
      "Menentukan jangka waktu penyimpanan dan nasib akhir suatu arsip (dimusnahkan atau dipermanenkan)",
      "Menghitung jumlah gaji perangkat desa setiap bulan",
      "Mencatat kehadiran apel pagi pegawai desa",
      "Menentukan giliran piket ronda malam dusun"
    ],
    "answer": 0,
    "explanation": "Jadwal Retensi Arsip (JRA) adalah daftar yang memuat sekurang-kurangnya jangka waktu penyimpanan atau retensi, jenis arsip, dan rekomendasi nasib akhir arsip.",
    "source": "UU No. 43 Tahun 2009 Pasal 1 angka 23"
  },

  # =========================================================================
  # KATEGORI 5: Keuangan desa, APB Desa, dan aset desa (10 Soal: ID 353-362)
  # =========================================================================
  {
    "id": 353,
    "category": "Keuangan desa, APB Desa, dan aset desa",
    "difficulty": "mudah",
    "question": "Pemerintah Desa memasang banner/baliho rincian ringkasan APB Desa di depan kantor desa dan memuatnya di situs web desa. Hal ini merupakan wujud penerapan asas...",
    "options": [
      "Transparan (Keterbukaan)",
      "Kerahasiaan fiskal",
      "Otoritas mutlak kades",
      "Sentralisasi anggaran"
    ],
    "answer": 0,
    "explanation": "Asas transparan (Permendagri No. 20 Tahun 2018 Pasal 2) menuntut pengelolaan keuangan desa terbuka bagi masyarakat untuk mengetahui dan mendapatkan akses informasi seluas-luasnya.",
    "source": "Permendagri No. 20 Tahun 2018 Pasal 2"
  },
  {
    "id": 354,
    "category": "Keuangan desa, APB Desa, dan aset desa",
    "difficulty": "sedang",
    "question": "Berdasarkan Permendagri No. 20 Tahun 2018, siapakah yang bertindak selaku Koordinator Pengelola Keuangan Desa (PPKD)?",
    "options": [
      "Kepala Desa",
      "Sekretaris Desa",
      "Kaur Keuangan",
      "Ketua BPD"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 20 Tahun 2018 Pasal 5 menegaskan bahwa Sekretaris Desa bertindak selaku Koordinator PPKD yang memverifikasi seluruh DPA, RAK, dan SPP.",
    "source": "Permendagri No. 20 Tahun 2018 Pasal 5"
  },
  {
    "id": 355,
    "category": "Keuangan desa, APB Desa, dan aset desa",
    "difficulty": "sedang",
    "question": "Siapakah yang bertindak sebagai Pelaksana Kegiatan Anggaran (PKA) dalam pelaksanaan kegiatan APB Desa sesuai dengan bidang tugasnya?",
    "options": [
      "Kepala Urusan dan Kepala Seksi",
      "Bupati dan Camat",
      "Ketua BPD dan Anggota BPD",
      "Pengurus BUMDes"
    ],
    "answer": 0,
    "explanation": "Permendagri No. 20 Tahun 2018 Pasal 6 menetapkan bahwa Kepala Urusan (Kaur) dan Kepala Seksi (Kasi) bertindak sebagai Pelaksana Kegiatan Anggaran (PKA).",
    "source": "Permendagri No. 20 Tahun 2018 Pasal 6"
  },
  {
    "id": 356,
    "category": "Keuangan desa, APB Desa, dan aset desa",
    "difficulty": "sedang",
    "question": "Sebelum Kaur Keuangan membayarkan uang belanja kegiatan APB Desa, Pelaksana Kegiatan Anggaran (PKA) wajib mengajukan dokumen...",
    "options": [
      "Surat Keputusan Camat",
      "Surat Permintaan Pembayaran (SPP) yang diverifikasi Sekretaris Desa",
      "Nota kesepakatan partai politik",
      "Laporan audit dari BPK"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 20 Tahun 2018 Pasal 51 mengatur bahwa pengeluaran atas beban APB Desa dilakukan setelah PKA mengajukan SPP yang diverifikasi oleh Sekretaris Desa dan disetujui Kepala Desa.",
    "source": "Permendagri No. 20 Tahun 2018 Pasal 51"
  },
  {
    "id": 357,
    "category": "Keuangan desa, APB Desa, dan aset desa",
    "difficulty": "sedang",
    "question": "Berdasarkan PP No. 11 Tahun 2019 Pasal 100, batas paling banyak anggaran belanja desa yang boleh dialokasikan untuk Siltap, tunjangan, operasional pemdes, BPD, dan insentif RT/RW adalah...",
    "options": [
      "Paling banyak 20% dari total belanja APB Desa",
      "Paling banyak 30% dari total belanja APB Desa",
      "Paling banyak 50% dari total belanja APB Desa",
      "Paling banyak 70% dari total belanja APB Desa"
    ],
    "answer": 1,
    "explanation": "PP No. 11 Tahun 2019 Pasal 100 mengatur komposisi belanja APB Desa: paling banyak 30% untuk siltap & operasional, dan paling sedikit 70% untuk mendanai pembangunan, pemberdayaan, dan kemasyarakatan.",
    "source": "PP No. 11 Tahun 2019 Pasal 100 ayat (1) huruf a"
  },
  {
    "id": 358,
    "category": "Keuangan desa, APB Desa, dan aset desa",
    "difficulty": "sedang",
    "question": "Dalam struktur APB Desa, apabila total estimasi belanja desa lebih besar daripada total estimasi pendapatan desa, maka kondisi anggaran tersebut mengalami...",
    "options": [
      "Defisit anggaran, yang ditutup melalui pos Penerimaan Pembiayaan",
      "Surplus anggaran, yang dibagikan tunai kepada warga desa",
      "Keseimbangan mutlak tanpa sisa",
      "Kebangkrutan administrasi desa"
    ],
    "answer": 0,
    "explanation": "Permendagri No. 20 Tahun 2018 Pasal 13 mengatur bahwa selisih antara Pendapatan Desa dan Belanja Desa menghasilkan surplus atau defisit. Bila belanja lebih besar daripada pendapatan maka terjadi defisit, yang ditutup melalui pos Penerimaan Pembiayaan (misal SiLPA tahun sebelumnya).",
    "source": "Permendagri No. 20 Tahun 2018 Pasal 13 dan 26"
  },
  {
    "id": 359,
    "category": "Keuangan desa, APB Desa, dan aset desa",
    "difficulty": "sedang",
    "question": "Berdasarkan Permendagri No. 1 Tahun 2016 tentang Pengelolaan Aset Desa, jangka waktu maksimal penyewaan tanah kas desa/tanah bengkok kepada pihak lain adalah...",
    "options": [
      "Paling lama 1 tahun",
      "Paling lama 3 tahun dan dapat diperpanjang",
      "Paling lama 10 tahun tanpa perpanjangan",
      "Paling lama 25 tahun"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 1 Tahun 2016 Pasal 11 ayat (3) mengatur bahwa jangka waktu sewa aset desa paling lama 3 (tiga) tahun dan dapat diperpanjang.",
    "source": "Permendagri No. 1 Tahun 2016 Pasal 11 ayat (3)"
  },
  {
    "id": 360,
    "category": "Keuangan desa, APB Desa, dan aset desa",
    "difficulty": "mudah",
    "question": "Manakah di antara pernyataan berikut mengenai aset desa yang dilarang keras oleh peraturan perundang-undangan?",
    "options": [
      "Aset desa dicatat dalam buku inventaris kekayaan desa",
      "Tanah kas desa disewakan kepada kelompok tani desa selama 2 tahun",
      "Aset desa digadaikan atau dijadikan jaminan untuk pinjaman pribadi kepala desa/perangkat",
      "Kendaraan dinas desa dirawat secara berkala menggunakan anggaran operasional"
    ],
    "answer": 2,
    "explanation": "Permendagri No. 1 Tahun 2016 Pasal 15 tegas melarang aset desa digadaikan, dipindahtangankan, atau dijadikan jaminan untuk mendapatkan pinjaman.",
    "source": "Permendagri No. 1 Tahun 2016 Pasal 15"
  },
  {
    "id": 361,
    "category": "Keuangan desa, APB Desa, dan aset desa",
    "difficulty": "sedang",
    "question": "Berdasarkan Permendagri No. 20 Tahun 2018, Surat Permintaan Pembayaran (SPP) yang diajukan oleh Pelaksana Kegiatan Anggaran untuk memperoleh uang muka kerja guna mendanai kegiatan operasional lapangan dinamakan...",
    "options": [
      "SPP Panjar (Uang Muka)",
      "SPP Definitif",
      "Surat Kuasa Khusus",
      "Kuitansi Pelunasan Total"
    ],
    "answer": 0,
    "explanation": "Permendagri No. 20 Tahun 2018 Pasal 51 ayat (2) menyebutkan jenis pengajuan SPP terdiri atas SPP Panjar (uang muka kerja yang dipertanggungjawabkan kemudian) dan SPP Definitif (setelah pekerjaan/barang diterima).",
    "source": "Permendagri No. 20 Tahun 2018 Pasal 51"
  },
  {
    "id": 362,
    "category": "Keuangan desa, APB Desa, dan aset desa",
    "difficulty": "sedang",
    "question": "Bendahara Desa melakukan pemotongan Pajak Penghasilan (PPh) Pasal 23 atas transaksi belanja APB Desa untuk pos...",
    "options": [
      "Pembelian alat tulis kantor senilai Rp500.000",
      "Jasa sewa kendaraan/alat berat dan jasa tenaga teknis dari rekanan",
      "Pemberian bantuan beras bagi warga miskin",
      "Pembayaran insentif kader posyandu"
    ],
    "answer": 1,
    "explanation": "PPh Pasal 23 dikenakan atas penghasilan berupa bunga, royalti, dividen, hadiah, serta sewa dan imbalan jasa selain yang dipotong PPh 21 (misal sewa alat berat/kendaraan sebesar 2% ber-NPWP).",
    "source": "UU Pajak Penghasilan (PPh) Pasal 23"
  },

  # =========================================================================
  # KATEGORI 6: Pembangunan desa, perencanaan, dan pemberdayaan (8 Soal: ID 363-370)
  # =========================================================================
  {
    "id": 363,
    "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
    "difficulty": "sedang",
    "question": "Berdasarkan UU No. 3 Tahun 2024 jo. Permendesa PDTT No. 21 Tahun 2020, dokumen Rencana Pembangunan Jangka Menengah Desa (RPJM Desa) disusun untuk jangka waktu...",
    "options": [
      "5 tahun",
      "6 tahun",
      "8 tahun",
      "10 tahun"
    ],
    "answer": 2,
    "explanation": "Menyesuaikan masa jabatan Kepala Desa yang kini 8 tahun berdasarkan UU No. 3 Tahun 2024, dokumen RPJM Desa memuat rencana pembangunan desa untuk periode 8 (delapan) tahun.",
    "source": "UU No. 3 Tahun 2024 jo. Permendesa PDTT No. 21 Tahun 2020"
  },
  {
    "id": 364,
    "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
    "difficulty": "mudah",
    "question": "Berdasarkan Permendesa PDTT No. 21 Tahun 2020, Rencana Kerja Pemerintah Desa (RKP Desa) wajib ditetapkan paling lambat pada...",
    "options": [
      "Bulan Juni tahun berjalan",
      "Tanggal 30 September tahun berjalan",
      "Tanggal 31 Desember tahun berjalan",
      "Tanggal 31 Maret tahun berikutnya"
    ],
    "answer": 1,
    "explanation": "Permendesa PDTT No. 21 Tahun 2020 Pasal 43 ayat (1) menyatakan bahwa RKP Desa ditetapkan dengan Peraturan Desa paling lambat akhir bulan September tahun berjalan.",
    "source": "Permendesa PDTT No. 21 Tahun 2020 Pasal 43"
  },
  {
    "id": 365,
    "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
    "difficulty": "sedang",
    "question": "Berdasarkan Permendesa PDTT No. 21 Tahun 2020, Tim Penyusun Rencana Kerja Pemerintah Desa (RKP Desa) dibentuk dengan jumlah anggota berjumlah...",
    "options": [
      "Paling sedikit 7 orang dan paling banyak 11 orang, dengan mengikutsertakan perempuan paling sedikit 30%",
      "Hanya 3 orang staf kantor desa",
      "Tepat 25 orang perwakilan setiap RT",
      "Seluruh warga desa yang hadir musdes"
    ],
    "answer": 0,
    "explanation": "Permendesa PDTT No. 21 Tahun 2020 Pasal 35 ayat (3) menetapkan Tim Penyusun RKP Desa berjumlah ganjil paling sedikit 7 orang dan paling banyak 11 orang dengan keterwakilan perempuan minimal 30%.",
    "source": "Permendesa PDTT No. 21 Tahun 2020 Pasal 35"
  },
  {
    "id": 366,
    "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
    "difficulty": "sedang",
    "question": "Peraturan Desa tentang Rencana Kerja Pemerintah Desa (Perdes RKP Desa) untuk tahun anggaran berikutnya wajib disepakati dan ditetapkan bersama oleh Kepala Desa dan BPD paling lambat pada...",
    "options": [
      "Tanggal 30 September tahun anggaran berjalan",
      "Tanggal 31 Desember tahun anggaran berjalan",
      "Bulan Januari tahun berkenaan",
      "Bulan Juni tahun berjalan"
    ],
    "answer": 0,
    "explanation": "Permendesa PDTT No. 21 Tahun 2020 Pasal 43 ayat (1) menegaskan bahwa RKP Desa ditetapkan dengan Peraturan Desa paling lambat akhir bulan September tahun berjalan.",
    "source": "Permendesa PDTT No. 21 Tahun 2020 Pasal 43"
  },
  {
    "id": 367,
    "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
    "difficulty": "sedang",
    "question": "Dalam konsep SDGs Desa (Sustainable Development Goals Desa), tujuan ke-1 yang menjadi fokus penanggulangan kerentanan sosial masyarakat desa adalah...",
    "options": [
      "Desa Berenergi Bersih dan Terbarukan",
      "Desa Tanpa Kemiskinan",
      "Desa Berjejaring Digital",
      "Desa Wisata Unggulan"
    ],
    "answer": 1,
    "explanation": "SDGs Desa memuat 18 tujuan pembangunan perdesaan, dengan tujuan ke-1 adalah 'Desa Tanpa Kemiskinan' (Zero Poverty).",
    "source": "Permendesa PDTT No. 21 Tahun 2020 tentang SDGs Desa"
  },
  {
    "id": 368,
    "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
    "difficulty": "sedang",
    "question": "Berdasarkan Peraturan Pemerintah No. 11 Tahun 2021 tentang Badan Usaha Milik Desa, organ tertinggi dalam struktur BUMDes adalah...",
    "options": [
      "Musyawarah Desa (Musdes)",
      "Direktur Operasional",
      "Dewan Pengawas BUMDes",
      "Camat setempat"
    ],
    "answer": 0,
    "explanation": "PP No. 11 Tahun 2021 Pasal 16 menetapkan bahwa perangkat organisasi BUMDes terdiri atas Musyawarah Desa/Musyawarah Antar Desa, Penasihat, Pelaksana Operasional, dan Pengawas. Musdes memegang kekuasaan tertinggi.",
    "source": "PP No. 11 Tahun 2021 Pasal 16"
  },
  {
    "id": 369,
    "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
    "difficulty": "mudah",
    "question": "Berdasarkan PP No. 11 Tahun 2021, jabatan Penasihat BUMDes secara ex-officio (karena kedudukan jabatannya) dipegang oleh...",
    "options": [
      "Ketua BPD",
      "Kepala Desa",
      "Sekretaris Desa",
      "Kepala Dusun tertua"
    ],
    "answer": 1,
    "explanation": "PP No. 11 Tahun 2021 Pasal 20 ayat (1) menyatakan bahwa Penasihat dijabat secara ex-officio oleh Kepala Desa yang sedang menjabat.",
    "source": "PP No. 11 Tahun 2021 Pasal 20 ayat (1)"
  },
  {
    "id": 370,
    "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
    "difficulty": "sedang",
    "question": "Berdasarkan Permendagri No. 18 Tahun 2018, Lembaga Kemasyarakatan Desa (LKD) seperti Karang Taruna dan PKK berkedudukan sebagai...",
    "options": [
      "Lembaga tandingan pemerintah desa",
      "Mitra pemerintah desa dalam memberdayakan masyarakat desa",
      "Pengawas yudisial aparatur desa",
      "Organisasi sayap partai politik"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 18 Tahun 2018 Pasal 3 menyatakan LKD bertugas membantu Kepala Desa dan menjadi mitra Pemerintah Desa dalam memberdayakan masyarakat.",
    "source": "Permendagri No. 18 Tahun 2018 Pasal 3"
  },

  # =========================================================================
  # KATEGORI 7: BPD, kelembagaan desa, dan musyawarah (5 Soal: ID 371-375)
  # =========================================================================
  {
    "id": 371,
    "category": "BPD, kelembagaan desa, dan musyawarah",
    "difficulty": "sedang",
    "question": "Berdasarkan Permendagri No. 110 Tahun 2016, hubungan kerja antara Badan Permusyawaratan Desa (BPD) dengan Pemerintah Desa bersifat...",
    "options": [
      "Atasan dan bawahan langsung",
      "Kemitraan, konsultatif, dan koordinatif",
      "Kompetitif saling menjatuhkan",
      "Instruktif dan hierarkis mutlak"
    ],
    "answer": 1,
    "explanation": "Hubungan kerja antara BPD dan Pemerintah Desa merupakan hubungan kemitraan yang harmonis, konsultatif, dan koordinatif dalam memajukan desa.",
    "source": "Permendagri No. 110 Tahun 2016 tentang BPD"
  },
  {
    "id": 372,
    "category": "BPD, kelembagaan desa, dan musyawarah",
    "difficulty": "sedang",
    "question": "Berdasarkan Undang-Undang Nomor 3 Tahun 2024 tentang Desa, anggota Badan Permusyawaratan Desa (BPD) dapat memegang masa keanggotaan paling banyak...",
    "options": [
      "2 (dua) kali masa keanggotaan secara berturut-turut atau tidak secara berturut-turut (total maksimal 16 tahun)",
      "3 kali masa jabatan berturut-turut",
      "1 kali periode saja tanpa hak dipilih kembali",
      "Seumur hidup tanpa batas periode"
    ],
    "answer": 0,
    "explanation": "UU No. 3 Tahun 2024 Pasal 56 ayat (2) menyatakan anggota BPD memegang jabatan selama 8 tahun dan dapat dipilih paling banyak 2 (dua) kali masa jabatan secara berturut-turut atau tidak secara berturut-turut.",
    "source": "UU No. 3 Tahun 2024 Pasal 56 ayat (2)"
  },
  {
    "id": 373,
    "category": "BPD, kelembagaan desa, dan musyawarah",
    "difficulty": "mudah",
    "question": "Salah satu dari 3 (tiga) fungsi utama BPD menurut UU No. 6 Tahun 2014 Pasal 55 adalah...",
    "options": [
      "Mengelola rekening kas desa dan mencairkan uang belanja APB Desa",
      "Membahas dan menyepakati Rancangan Peraturan Desa bersama Kepala Desa",
      "Menerbitkan surat izin mendirikan bangunan di wilayah kecamatan",
      "Mengangkat dan memberhentikan perangkat desa secara sepihak"
    ],
    "answer": 1,
    "explanation": "Tiga fungsi utama BPD (Pasal 55 UU 6/2014): 1. Membahas dan menyepakati rancangan Perdes bersama Kades, 2. Menampung dan menyalurkan aspirasi masyarakat, 3. Melakukan pengawasan kinerja Kades.",
    "source": "UU No. 6 Tahun 2014 Pasal 55"
  },
  {
    "id": 374,
    "category": "BPD, kelembagaan desa, dan musyawarah",
    "difficulty": "sedang",
    "question": "Apabila ada anggota BPD yang mengundurkan diri atau meninggal dunia sebelum masa jabatannya berakhir, mekanisme pengisiannya dilakukan melalui...",
    "options": [
      "Penunjukan langsung oleh Kepala Desa",
      "Penggantian Antar Waktu (PAW)",
      "Pelelangan terbuka jabatan ke publik",
      "Penyerahan jabatan kepada ahli waris"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 110 Tahun 2016 Pasal 23 mengatur pengisian anggota BPD yang berhenti antarwaktu dilakukan melalui Penggantian Antar Waktu (PAW) dari perolehan suara terbanyak berikutnya pada proses pemilihan.",
    "source": "Permendagri No. 110 Tahun 2016 Pasal 23"
  },
  {
    "id": 375,
    "category": "BPD, kelembagaan desa, dan musyawarah",
    "difficulty": "sedang",
    "question": "Siapakah yang memimpin pelaksanaan Musyawarah Desa (Musdes) menurut Permendagri No. 110 Tahun 2016?",
    "options": [
      "Kepala Desa",
      "Ketua BPD atau anggota BPD yang ditunjuk",
      "Sekretaris Desa",
      "Camat setempat"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 110 Tahun 2016 Pasal 36 menegaskan bahwa Musyawarah Desa dipimpin oleh Ketua BPD atau salah satu anggota BPD yang ditunjuk oleh pimpinan BPD.",
    "source": "Permendagri No. 110 Tahun 2016 Pasal 36"
  },

  # =========================================================================
  # KATEGORI 8: Bahasa Indonesia (7 Soal: ID 376-382)
  # =========================================================================
  {
    "id": 376,
    "category": "Bahasa Indonesia",
    "difficulty": "mudah",
    "question": "Manakah kelompok kata berikut yang semuanya merupakan kata baku sesuai Ejaan Bahasa Indonesia yang Disempurnakan (EYD V)?",
    "options": [
      "Resiko, ijin, kwitansi",
      "Risiko, izin, kuitansi",
      "Resiko, izin, kwitansi",
      "Risiko, ijin, kuitansi"
    ],
    "answer": 1,
    "explanation": "Sesuai KBBI dan EYD V, bentuk baku yang benar adalah: 'risiko' (bukan resiko), 'izin' (bukan ijin), dan 'kuitansi' (bukan kwitansi).",
    "source": "EYD Edisi V & KBBI Daring"
  },
  {
    "id": 377,
    "category": "Bahasa Indonesia",
    "difficulty": "sedang",
    "question": "Penulisan bentuk terikat 'antar-' yang tepat sesuai kaidah EYD V adalah...",
    "options": [
      "Kerjasama antar warga desa",
      "Kerjasama antar-warga desa",
      "Kerja sama antarwarga desa",
      "Kerja sama antar warga desa"
    ],
    "answer": 2,
    "explanation": "Kata 'kerja sama' ditulis terpisah dua kata. Bentuk terikat 'antar-' wajib ditulis serangkai dengan kata dasar yang mengikutinya ('antarwarga').",
    "source": "EYD Edisi V Kaidah Penulisan Bentuk Terikat"
  },
  {
    "id": 378,
    "category": "Bahasa Indonesia",
    "difficulty": "sedang",
    "question": "Cermati kalimat berikut: 'Demi untuk kelancaran acara rapat, para hadirin sekalian dimohon hadir tepat waktu.' Perbaikan kalimat agar efektif dan tidak pleonastis adalah...",
    "options": [
      "Demi untuk kelancaran acara rapat, hadirin dimohon hadir tepat waktu.",
      "Untuk kelancaran rapat, hadirin dimohon hadir tepat waktu.",
      "Demi kelancaran acara rapat, para hadirin sekalian mohon hadir tepat waktu.",
      "Untuk kelancaran rapat, para hadirin dimohon supaya hadir tepat waktu."
    ],
    "answer": 1,
    "explanation": "'Demi untuk' dan 'para hadirin sekalian' adalah bentuk pleonastis (pemborosan kata). Bentuk hemat dan efektif adalah 'Untuk kelancaran rapat, hadirin dimohon hadir tepat waktu.'",
    "source": "Tata Bahasa Baku Bahasa Indonesia"
  },
  {
    "id": 379,
    "category": "Bahasa Indonesia",
    "difficulty": "sedang",
    "question": "Penggunaan tanda titik dua (:) yang tepat sesuai kaidah bahasa Indonesia terdapat pada kalimat...",
    "options": [
      "Pemerintah Desa memerlukan: meja, kursi, dan komputer baru.",
      "Rapat dihadiri oleh: Kepala Desa, Sekretaris Desa, dan Kaur Keuangan.",
      "Pemerintah desa membutuhkan perabot kantor berikut: meja, kursi, dan lemari arsip.",
      "Kita memerlukan barang: seperti beras, gula, dan minyak."
    ],
    "answer": 2,
    "explanation": "Tanda titik dua dipakai pada akhir suatu pernyataan lengkap yang diikuti pemerincian. Jika kalimat belum lengkap (ada kata kerja 'memerlukan/dihadiri'), tanda titik dua tidak boleh dipakai.",
    "source": "EYD Edisi V Penggunaan Tanda Baca Titik Dua"
  },
  {
    "id": 380,
    "category": "Bahasa Indonesia",
    "difficulty": "sedang",
    "question": "Penulisan huruf kapital yang benar untuk gelar dan jabatan dinas adalah...",
    "options": [
      "Surat itu ditandatangani oleh bupati Tuban.",
      "Surat itu ditandatangani oleh Bupati Tuban.",
      "Surat itu ditandatangani oleh Bupati tuban.",
      "Semua Kepala Desa harus hadir di pendopo."
    ],
    "answer": 1,
    "explanation": "Huruf kapital dipakai sebagai huruf pertama unsur nama gelar kehormatan, keturunan, keagamaan, atau profesi serta nama jabatan dan kepangkatan yang diikuti nama orang atau nama daerah/instansi ('Bupati Tuban'). Jika tidak diikuti nama diri/tempat, ditulis huruf kecil ('semua kepala desa').",
    "source": "EYD Edisi V Penulisan Huruf Kapital"
  },
  {
    "id": 381,
    "category": "Bahasa Indonesia",
    "difficulty": "mudah",
    "question": "Manakah penulisan kata baku berikut yang tepat?",
    "options": [
      "Jadual kegiatan dan fihak terkait",
      "Jadwal kegiatan dan pihak terkait",
      "Jadwal kegiatan dan fihak terkait",
      "Jadual kegiatan dan pihak terkait"
    ],
    "answer": 1,
    "explanation": "Bentuk baku yang tepat adalah 'jadwal' (bukan jadual) dan 'pihak' (bukan fihak).",
    "source": "KBBI Daring & EYD V"
  },
  {
    "id": 382,
    "category": "Bahasa Indonesia",
    "difficulty": "mudah",
    "question": "Penulisan salam pembuka yang benar pada surat dinas pemerintahan adalah...",
    "options": [
      "Dengan Hormat,",
      "Dengan hormat,",
      "Dengan hormat.",
      "Dengan Hormat;"
    ],
    "answer": 1,
    "explanation": "Salam pembuka 'Dengan hormat,' ditulis dengan huruf kapital pada kata pertama ('Dengan') dan huruf kecil pada kata kedua ('hormat'), serta diakhiri tanda koma.",
    "source": "Tata Naskah Dinas & EYD V"
  },

  # =========================================================================
  # KATEGORI 9: Matematika dan numerik (6 Soal: ID 383-388)
  # =========================================================================
  {
    "id": 383,
    "category": "Matematika dan numerik",
    "difficulty": "mudah",
    "question": "Pendapatan Desa yang terealisasi dalam APB Desa tercatat sebesar Rp1.250.000.000,00, sedangkan total Belanja Desa terealisasi sebesar Rp1.100.000.000,00. Berapakah sisa anggaran (surplus belanja) sebelum pos pembiayaan?",
    "options": [
      "Rp100.000.000,00",
      "Rp150.000.000,00",
      "Rp200.000.000,00",
      "Rp250.000.000,00"
    ],
    "answer": 1,
    "explanation": "Surplus = Pendapatan - Belanja = Rp1.250.000.000,00 - Rp1.100.000.000,00 = Rp150.000.000,00.",
    "source": "Perhitungan Matematika Keuangan APB Desa"
  },
  {
    "id": 384,
    "category": "Matematika dan numerik",
    "difficulty": "sedang",
    "question": "Pemerintah Desa membeli 1 unit laptop seharga Rp11.100.000,00 (harga sudah termasuk PPN 11%). Berapakah Dasar Pengenaan Pajak (DPP) dan nilai PPN laptop tersebut?",
    "options": [
      "DPP Rp10.000.000,00 dan PPN Rp1.100.000,00",
      "DPP Rp9.990.000,00 dan PPN Rp1.110.000,00",
      "DPP Rp10.500.000,00 dan PPN Rp600.000,00",
      "DPP Rp11.000.000,00 dan PPN Rp100.000,00"
    ],
    "answer": 0,
    "explanation": "DPP = 100 / 111 x Rp11.100.000,00 = Rp10.000.000,00. Nilai PPN (11%) = 11% x Rp10.000.000,00 = Rp1.100.000,00.",
    "source": "Perhitungan Pajak Pertambahan Nilai (PPN 11%)"
  },
  {
    "id": 385,
    "category": "Matematika dan numerik",
    "difficulty": "mudah",
    "question": "Sebidang tanah kas desa memiliki luas 2,5 hektar. Berapakah luas tanah tersebut jika dikonversikan ke dalam satuan meter persegi (m²)?",
    "options": [
      "2.500 m²",
      "25.000 m²",
      "250.000 m²",
      "250 m²"
    ],
    "answer": 1,
    "explanation": "1 hektar (ha) = 10.000 m². Maka 2,5 ha = 2,5 x 10.000 m² = 25.000 m².",
    "source": "Konversi Satuan Luas Tanah"
  },
  {
    "id": 386,
    "category": "Matematika dan numerik",
    "difficulty": "sedang",
    "question": "Pemerintah Desa mengalokasikan anggaran pembangunan pos kesehatan desa sebesar Rp40.000.000,00. Dari total anggaran tersebut, 60% dialokasikan untuk belanja material bangunan, 30% untuk upah tenaga kerja lokal, dan sisanya untuk biaya operasional Tim Pelaksana Kegiatan (TPK). Berapakah nominal anggaran untuk operasional TPK?",
    "options": [
      "Rp4.000.000,00",
      "Rp6.000.000,00",
      "Rp8.000.000,00",
      "Rp10.000.000,00"
    ],
    "answer": 0,
    "explanation": "Persentase operasional TPK = 100% - (60% + 30%) = 10%. Nominal operasional TPK = 10% x Rp40.000.000,00 = Rp4.000.000,00.",
    "source": "Matematika Keuangan APB Desa / Perhitungan Anggaran Biaya"
  },
  {
    "id": 387,
    "category": "Matematika dan numerik",
    "difficulty": "mudah",
    "question": "Hasil panen padi pada 5 petak sawah kas desa berturut-turut adalah 5,2 ton; 5,8 ton; 6,1 ton; 5,5 ton; dan 6,4 ton. Berapakah rata-rata (mean) hasil panen per petak?",
    "options": [
      "5,6 ton",
      "5,7 ton",
      "5,8 ton",
      "5,9 ton"
    ],
    "answer": 2,
    "explanation": "Rata-rata = (5,2 + 5,8 + 6,1 + 5,5 + 6,4) / 5 = 29,0 / 5 = 5,8 ton.",
    "source": "Statistika Dasar Nilai Rata-rata"
  },
  {
    "id": 388,
    "category": "Matematika dan numerik",
    "difficulty": "sedang",
    "question": "Kas Simpan Pinjam BUMDes mencatat pertumbuhan penerimaan angsuran bulanan yang membentuk barisan aritmetika: Rp2.000.000, Rp2.500.000, Rp3.000.000, Rp3.500.000... Berapakah penerimaan kas pada bulan ke-8?",
    "options": [
      "Rp4.500.000,00",
      "Rp5.000.000,00",
      "Rp5.500.000,00",
      "Rp6.000.000,00"
    ],
    "answer": 2,
    "explanation": "Suku pertama (a) = 2.000.000, beda (b) = 500.000. Suku ke-8 (U8) = a + (8 - 1)b = 2.000.000 + 7 x 500.000 = 2.000.000 + 3.500.000 = Rp5.500.000,00.",
    "source": "Barisan dan Deret Aritmetika"
  },

  # =========================================================================
  # KATEGORI 10: Logika dan penalaran (5 Soal: ID 389-393)
  # =========================================================================
  {
    "id": 389,
    "category": "Logika dan penalaran",
    "difficulty": "sedang",
    "question": "Premis 1: Semua perangkat desa wajib mengikuti apel kerja setiap hari Senin pagi.\nPremis 2: Pak Budi adalah Kaur Perencanaan Desa.\nKesimpulan yang sah dan logis adalah...",
    "options": [
      "Pak Budi boleh tidak mengikuti apel jika sibuk menyusun RKP Desa",
      "Pak Budi wajib mengikuti apel kerja setiap hari Senin pagi",
      "Pak Budi hanya mengikuti apel jika diperintah Sekretaris Desa",
      "Sebagian perangkat desa tidak wajib apel pagi"
    ],
    "answer": 1,
    "explanation": "Silogisme kategorial: Semua A adalah B. C adalah A. Maka C adalah B (Pak Budi wajib mengikuti apel kerja hari Senin pagi).",
    "source": "Silogisme Kategorial Logika Deduktif"
  },
  {
    "id": 390,
    "category": "Logika dan penalaran",
    "difficulty": "sedang",
    "question": "Premis 1: Jika Dana Desa tahap I telah ditransfer ke kas desa, maka pemerintah desa menyalurkan BLT Desa.\nPremis 2: Pemerintah desa belum menyalurkan BLT Desa.\nKesimpulan yang benar menurut kaidah logika adalah...",
    "options": [
      "Dana Desa tahap I telah ditransfer ke kas desa",
      "Dana Desa tahap I belum ditransfer ke kas desa",
      "Pemerintah desa membatalkan penyaluran BLT Desa",
      "Kepala Desa sedang dinas luar"
    ],
    "answer": 1,
    "explanation": "Kaidah Modus Tollens: Jika P maka Q. Negasi Q (~Q). Maka kesimpulannya Negasi P (~P), yaitu Dana Desa tahap I belum ditransfer ke kas desa.",
    "source": "Logika Matematika Modus Tollens"
  },
  {
    "id": 391,
    "category": "Logika dan penalaran",
    "difficulty": "sulit",
    "question": "Lima orang perangkat desa (Ali, Budi, Citra, Dedi, dan Eka) bertugas piket pelayanan desa dari Senin hingga Jumat. Aturan penugasan:\n1. Budi bertugas tepat satu hari sebelum Citra.\n2. Ali bertugas pada hari Rabu.\n3. Dedi bertugas pada hari pertama (Senin).\nSiapakah yang bertugas piket pada hari Jumat?",
    "options": [
      "Budi",
      "Citra",
      "Eka",
      "Dedi"
    ],
    "answer": 1,
    "explanation": "Senin: Dedi. Rabu: Ali. Tersisa Selasa, Kamis, Jumat. Budi tepat sebelum Citra, sehingga pasangan berurutan (Budi, Citra) hanya bisa di Kamis dan Jumat. Hari Selasa diisi Eka. Maka yang piket hari Jumat adalah Citra.",
    "source": "Penalaran Analitis Urutan Logis"
  },
  {
    "id": 392,
    "category": "Logika dan penalaran",
    "difficulty": "sedang",
    "question": "Dari 100 kepala keluarga di Dusun Krajan, tercatat 60 KK menerima bantuan beras, 45 KK menerima bantuan bibit pertanian, dan 20 KK menerima kedua jenis bantuan tersebut. Berapakah jumlah KK yang sama sekali tidak menerima kedua bantuan tersebut?",
    "options": [
      "10 KK",
      "15 KK",
      "20 KK",
      "25 KK"
    ],
    "answer": 1,
    "explanation": "Jumlah KK penerima bantuan = 60 + 45 - 20 = 85 KK. KK yang tidak menerima kedua bantuan = 100 - 85 = 15 KK.",
    "source": "Diagram Venn Teori Himpunan"
  },
  {
    "id": 393,
    "category": "Logika dan penalaran",
    "difficulty": "sedang",
    "question": "Premis 1: Warga yang mengurus surat keterangan usaha wajib membawa surat pengantar RT atau surat bukti kepemilikan tempat usaha.\nPremis 2: Pak Joko tidak membawa surat pengantar RT.\nKesimpulan yang sah adalah...",
    "options": [
      "Pak Joko tidak boleh mengurus surat keterangan usaha",
      "Pak Joko wajib membawa surat bukti kepemilikan tempat usaha",
      "Pak Joko harus membayar denda administrasi",
      "Pak Joko dapat langsung meminta tanda tangan Kades"
    ],
    "answer": 1,
    "explanation": "Silogisme Disjungtif (P atau Q. Tidak P. Maka Q). Karena Pak Joko tidak membawa surat RT, ia wajib membawa bukti tempat usaha.",
    "source": "Silogisme Disjungtif"
  },

  # =========================================================================
  # KATEGORI 11: Pengetahuan umum (4 Soal: ID 394-397)
  # =========================================================================
  {
    "id": 394,
    "category": "Pengetahuan umum",
    "difficulty": "sedang",
    "question": "Pada masa keemasan Kerajaan Singasari dan Majapahit abad ke-13 hingga ke-15, wilayah Kabupaten Tuban memegang peranan sangat penting dalam percaturan ekonomi Nusantara sebagai...",
    "options": [
      "Bandar pelabuhan niaga maritim internasional utama tempat bersandarnya kapal dagang mancanegara (Tiongkok, Arab, dan Gujarat)",
      "Pusat penempaan senjata keris utama kerajaan di pedalaman",
      "Lumbung padi utama pegunungan kapur",
      "Pusat pemerintahan istana Majapahit"
    ],
    "answer": 0,
    "explanation": "Tuban merupakan pelabuhan utama Kerajaan Majapahit (kambang putih) di pesisir utara Jawa Timur, menjadi pintu gerbang perdagangan maritim internasional rempah-rempah dan keramik sutra.",
    "source": "Sejarah Maritim Nusantara; Ensiklopedia Sejarah Tuban"
  },
  {
    "id": 395,
    "category": "Pengetahuan umum",
    "difficulty": "mudah",
    "question": "Kawasan perbukitan kapur (karst) di wilayah barat Kabupaten Tuban menjadi lokasi beroperasinya salah satu industri manufaktur strategis nasional terbesar di Indonesia, yaitu...",
    "options": [
      "Industri Pabrik Semen (PT Semen Indonesia / SIG Pabrik Tuban)",
      "Pabrik Peleburan Timah",
      "Pabrik Kertas Tisu",
      "Kawasan Industri Perakitan Pesawat Terbang"
    ],
    "answer": 0,
    "explanation": "Kabupaten Tuban memiliki deposit batu gamping/kapur melimpah yang menopang kompleks industri pabrik semen PT Semen Indonesia (Persero) Tbk di wilayah Kerek dan Merakurak.",
    "source": "Dinas Perindustrian dan Perdagangan Kabupaten Tuban"
  },
  {
    "id": 396,
    "category": "Pengetahuan umum",
    "difficulty": "mudah",
    "question": "Di sebelah barat, wilayah Kabupaten Tuban berbatasan langsung dengan kabupaten yang termasuk wilayah Provinsi Jawa Tengah, yaitu...",
    "options": [
      "Kabupaten Rembang",
      "Kabupaten Bojonegoro",
      "Kabupaten Blora",
      "Kabupaten Lamongan"
    ],
    "answer": 0,
    "explanation": "Batas wilayah Kabupaten Tuban di sebelah barat berbatasan langsung dengan Kabupaten Rembang (Provinsi Jawa Tengah).",
    "source": "Profil Geografis Kabupaten Tuban"
  },
  {
    "id": 397,
    "category": "Pengetahuan umum",
    "difficulty": "sedang",
    "question": "Salah satu hidangan kuliner tradisional khas pesisir dan pedesaan Kabupaten Tuban yang terkenal bercita rasa sangat pedas dan menggunakan kuah santan bumbu rempah kuning adalah...",
    "options": [
      "Rajungan Pedas dan Becek Mentok khas Tuban",
      "Rawon Daging Surabaya",
      "Gudeg Nangka Manis",
      "Rujak Cingur Petis"
    ],
    "answer": 0,
    "explanation": "Rajungan Pedas dan Becek Mentok adalah kuliner khas legendaris Kabupaten Tuban yang bercita rasa pedas gurih kaya rempah khas pesisir laut Jawa.",
    "source": "Pariwisata dan Kuliner Khas Kabupaten Tuban"
  },

  # =========================================================================
  # KATEGORI 12: Komputer dasar dan pelayanan publik (3 Soal: ID 398-400)
  # =========================================================================
  {
    "id": 398,
    "category": "Komputer dasar dan pelayanan publik",
    "difficulty": "mudah",
    "question": "Ketika staf pelayanan desa sedang mengetik dokumen dan tiba-tiba aplikasi pengolah kata macet/membeku (keterangan 'Not Responding'), kombinasi tombol cepat untuk membuka Task Manager guna menutup paksa aplikasi yang macet adalah...",
    "options": [
      "Ctrl + Shift + Esc (atau Ctrl + Alt + Del)",
      "Ctrl + Alt + Tab",
      "Alt + Shift + Enter",
      "Windows + Spasi"
    ],
    "answer": 0,
    "explanation": "Kombinasi tombol `Ctrl + Shift + Esc` (atau `Ctrl + Alt + Del`) langsung membuka Windows Task Manager. Di Task Manager, pengguna dapat memilih aplikasi yang bermasalah lalu mengklik 'End Task' untuk menutup paksa aplikasi yang membeku tanpa harus merestart paksa komputer.",
    "source": "Troubleshooting Sistem Operasi Windows & Perawatan Komputer Kantor"
  },
  {
    "id": 399,
    "category": "Komputer dasar dan pelayanan publik",
    "difficulty": "mudah",
    "question": "Komponen perangkat keras komputer yang berfungsi sebagai memori penyimpanan data kerja sementara saat komputer menyala dan seluruh datanya akan hilang saat komputer dimatikan (bersifat volatile) adalah...",
    "options": [
      "RAM (Random Access Memory)",
      "ROM (Read-Only Memory)",
      "Harddisk Eksternal",
      "Flashdisk"
    ],
    "answer": 0,
    "explanation": "RAM (Random Access Memory) adalah memori kerja sementara komputer berkecepatan tinggi yang menyimpan data dan instruksi yang sedang diproses oleh prosesor. Jika komputer mati, data dalam RAM otomatis hilang (volatile).",
    "source": "Dasar Arsitektur Komputer & Perangkat Keras TIK"
  },
  {
    "id": 400,
    "category": "Komputer dasar dan pelayanan publik",
    "difficulty": "sedang",
    "question": "Demi menjaga keamanan dan kerahasiaan data kependudukan warga di komputer pelayanan desa saat staf harus meninggalkan meja kerja sementara waktu, kombinasi tombol cepat pada keyboard untuk mengunci layar monitor seketika adalah...",
    "options": [
      "Windows + L",
      "Windows + D",
      "Alt + F4",
      "Ctrl + Alt + P"
    ],
    "answer": 0,
    "explanation": "Kombinasi tombol `Windows + L` (Lock) berfungsi langsung mengunci komputer seketika sehingga siapa pun yang ingin menggunakan komputer harus memasukkan kata sandi (password) terlebih dahulu. Ini praktik keamanan standar saat meninggalkan meja kerja.",
    "source": "Standar Keamanan Informasi & Pintasan Keyboard Windows"
  }
]
