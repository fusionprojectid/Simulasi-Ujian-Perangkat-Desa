# -*- coding: utf-8 -*-
"""
Database Tambahan Soal 401 s.d. 500 untuk Simulasi CBT Perangkat Desa
Memperluas master bank soal dari 400 menjadi 500 butir soal lengkap.
Proporsional sesuai kuota 12 kategori ujian resmi:
- Kat 1 (Pemerintahan desa): 20 soal (ID 401 - 420)
- Kat 2 (Perundang-undangan): 12 soal (ID 421 - 432)
- Kat 3 (Pancasila & Wawasan Kebangsaan): 10 soal (ID 433 - 442)
- Kat 4 (Administrasi & Surat): 10 soal (ID 443 - 452)
- Kat 5 (Keuangan & Aset Desa): 10 soal (ID 453 - 462)
- Kat 6 (Pembangunan & Pemberdayaan): 8 soal (ID 463 - 470)
- Kat 7 (BPD & Musyawarah): 5 soal (ID 471 - 475)
- Kat 8 (Bahasa Indonesia): 7 soal (ID 476 - 482)
- Kat 9 (Matematika & Numerik): 6 soal (ID 483 - 488)
- Kat 10 (Logika & Penalaran): 5 soal (ID 489 - 493)
- Kat 11 (Pengetahuan Umum): 4 soal (ID 494 - 497)
- Kat 12 (Komputer & Pelayanan): 3 soal (ID 498 - 500)
TOTAL: 100 butir soal terverifikasi (ID 401 - 500).
"""

QUESTIONS_401_500 = [
  # =========================================================================
  # KATEGORI 1: Pemerintahan desa, struktur organisasi, tugas dan fungsi (20 Soal: ID 401-420)
  # =========================================================================
  {
    "id": 401,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Berdasarkan UU No. 3 Tahun 2024 tentang Perubahan Kedua atas UU No. 6 Tahun 2014, mekanisme transfer Dana Desa bersumber dari APBN disalurkan secara langsung ke...",
    "options": [
      "Rekening Kas Pribadi Kepala Desa",
      "Rekening Kas Desa (RKD) pada bank yang ditunjuk",
      "Rekening Kas Pengurus Lembaga Adat Desa",
      "Rekening Kas BUMDes"
    ],
    "answer": 1,
    "explanation": "UU No. 3 Tahun 2024 dan regulasi keuangan negara menegaskan bahwa Dana Desa dari APBN disalurkan langsung dari Rekening Kas Umum Negara (RKUN) ke Rekening Kas Desa (RKD) untuk efisiensi dan transparansi.",
    "source": "UU No. 3 Tahun 2024 Pasal 72 ayat (1) huruf b"
  },
  {
    "id": 402,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "mudah",
    "question": "Dalam struktur organisasi Pemerintah Desa, pimpinan Sekretariat Desa yang bertugas memimpin urusan ketatausahaan, keuangan, dan perencanaan adalah...",
    "options": [
      "Kepala Seksi Pemerintahan",
      "Sekretaris Desa",
      "Kepala Dusun",
      "Ketua BPD"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 84 Tahun 2015 Pasal 7 menegaskan bahwa Sekretaris Desa berkedudukan sebagai pimpinan sekretariat desa dan bertugas membantu Kepala Desa dalam bidang administrasi pemerintahan.",
    "source": "Permendagri No. 84 Tahun 2015 Pasal 7"
  },
  {
    "id": 403,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Berdasarkan Permendagri No. 84 Tahun 2015, apabila pemerintah desa membutuhkan staf pembantu perangkat desa, siapakah yang berwenang mengangkat staf tersebut?",
    "options": [
      "Camat atas persetujuan Bupati",
      "Kepala Desa dengan Keputusan Kepala Desa",
      "Ketua BPD atas usulan warga",
      "Sekretaris Daerah Kabupaten"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 84 Tahun 2015 Pasal 13 menyebutkan bahwa dalam hal diperlukan, Kepala Desa dapat mengangkat staf pembantu perangkat desa sesuai kemampuan keuangan desa dengan Keputusan Kepala Desa.",
    "source": "Permendagri No. 84 Tahun 2015 Pasal 13"
  },
  {
    "id": 404,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Berdasarkan Permendagri No. 67 Tahun 2017 Pasal 2, pengisian jabatan Perangkat Desa yang lowong dapat dilakukan melalui 2 (dua) cara, yaitu...",
    "options": [
      "Mutasi jabatan antarperangkat desa dan penjaringan/penyaringan calon perangkat desa",
      "Penunjukan langsung oleh Camat dan lelang jabatan",
      "Pemilihan suara langsung warga dan undian terbuka",
      "Pengangkatan otomatis keluarga kepala desa dan tes wawancara BPD"
    ],
    "answer": 0,
    "explanation": "Permendagri No. 67 Tahun 2017 Pasal 2 ayat (1) menyatakan pengisian jabatan perangkat desa yang kosong dapat dilakukan melalui mutasi jabatan antarperangkat desa di lingkungan pemdes atau penjaringan dan penyaringan calon perangkat desa.",
    "source": "Permendagri No. 67 Tahun 2017 Pasal 2"
  },
  {
    "id": 405,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sulit",
    "question": "Berdasarkan Permendagri No. 67 Tahun 2017 Pasal 7, perangkat desa yang berstatus diberhentikan sementara diberikan penghasilan tetap sebesar...",
    "options": [
      "100% dari penghasilan tetap setiap bulan",
      "75% dari penghasilan tetap setiap bulan",
      "50% dari penghasilan tetap setiap bulan",
      "Tidak diberikan penghasilan sama sekali (0%)"
    ],
    "answer": 2,
    "explanation": "Permendagri No. 67 Tahun 2017 Pasal 7 ayat (1) mengatur bahwa perangkat desa yang diberhentikan sementara diberikan penghasilan tetap sebesar 50% (lima puluh persen) dari penghasilan tetap yang diterimanya setiap bulan.",
    "source": "Permendagri No. 67 Tahun 2017 Pasal 7 ayat (1)"
  },
  {
    "id": 406,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Jika perangkat desa yang diberhentikan sementara diputus bebas atau tidak bersalah oleh pengadilan dengan putusan berkekuatan hukum tetap, kewajiban Kepala Desa adalah...",
    "options": [
      "Memberikan uang pesangon lalu memberhentikannya",
      "Merehabilitasi dan mengembalikan jabatannya sebagai perangkat desa",
      "Menurunkan jabatannya menjadi tenaga honorer lepas",
      "Menyerahkan keputusannya kepada BPD"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 67 Tahun 2017 Pasal 7 ayat (3) menegaskan bahwa perangkat desa yang diberhentikan sementara dan diputus bebas oleh pengadilan wajib direhabilitasi dan dikembalikan pada jabatannya semula.",
    "source": "Permendagri No. 67 Tahun 2017 Pasal 7 ayat (3)"
  },
  {
    "id": 407,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "mudah",
    "question": "Menurut UU No. 6 Tahun 2014 Pasal 48, unsur Perangkat Desa terdiri atas...",
    "options": [
      "Sekretariat Desa, Pelaksana Teknis, dan Pelaksana Kewilayahan",
      "Kepala Desa, BPD, dan RT/RW",
      "Sekretaris Desa, Bendahara Desa, dan Petugas Linmas",
      "Camat, Lurah, dan Kepala Lingkungan"
    ],
    "answer": 0,
    "explanation": "UU No. 6 Tahun 2014 Pasal 48 menegaskan perangkat desa terdiri atas: a. Sekretariat Desa (Kaur), b. Pelaksana Teknis (Kasi), dan c. Pelaksana Kewilayahan (Kepala Dusun).",
    "source": "UU No. 6 Tahun 2014 Pasal 48"
  },
  {
    "id": 408,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Pencatatan kas harian, pengelolaan buku bank desa, penatausahaan bukti belanja APB Desa, dan verifikasi kuitansi belanja desa merupakan fungsi pokok dari...",
    "options": [
      "Kepala Seksi Pelayanan",
      "Kepala Urusan Keuangan",
      "Kepala Urusan Perencanaan",
      "Kepala Dusun"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 84 Tahun 2015 Pasal 8 ayat (3) menjelaskan bahwa Kepala Urusan Keuangan bertugas melaksanakan penatausahaan keuangan, penerimaan kas, bukti pengeluaran kas, dan buku kas.",
    "source": "Permendagri No. 84 Tahun 2015 Pasal 8"
  },
  {
    "id": 409,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Pelaksanaan administrasi kependudukan (KK, KTP, mutasi warga), pembinaan ketenteraman ketertiban, dan fasilitasi pemilihan RT/RW merupakan tugas pokok...",
    "options": [
      "Kepala Seksi Pemerintahan",
      "Kepala Urusan Tata Usaha dan Umum",
      "Kepala Seksi Kesejahteraan",
      "Sekretaris Desa"
    ],
    "answer": 0,
    "explanation": "Permendagri No. 84 Tahun 2015 Pasal 9 ayat (2) menyatakan Kepala Seksi Pemerintahan bertugas menyusun rancangan regulasi, pembinaan ketenteraman ketertiban, administrasi kependudukan, dan pembinaan kelembagaan masyarakat.",
    "source": "Permendagri No. 84 Tahun 2015 Pasal 9"
  },
  {
    "id": 410,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Pengelolaan program Posyandu, percepatan penurunan stunting desa, dan pembangunan gedung PAUD desa secara teknis diampu oleh...",
    "options": [
      "Kepala Seksi Kesejahteraan",
      "Kepala Urusan Umum",
      "Kepala Seksi Keamanan",
      "Kepala Dusun"
    ],
    "answer": 0,
    "explanation": "Permendagri No. 84 Tahun 2015 Pasal 10 menyebutkan Kepala Seksi Kesejahteraan mengampu bidang pelaksanaan pembangunan sarana prasarana desa, kesehatan, dan pendidikan perdesaan.",
    "source": "Permendagri No. 84 Tahun 2015 Pasal 10"
  },
  {
    "id": 411,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Pelayanan pencatatan pengantar nikah, talak, cerai, dan rujuk (NTCR), pelestarian seni budaya tradisional desa, dan pembinaan karang taruna diampu oleh...",
    "options": [
      "Kepala Seksi Pelayanan",
      "Kepala Urusan Keuangan",
      "Kepala Urusan Perencanaan",
      "Sekretaris Desa"
    ],
    "answer": 0,
    "explanation": "Permendagri No. 84 Tahun 2015 Pasal 11 mengatur Kepala Seksi Pelayanan bertugas melaksanakan pelayanan sosial keagamaan, kebudayaan, pencatatan sipil sosial, dan kepemudaan.",
    "source": "Permendagri No. 84 Tahun 2015 Pasal 11"
  },
  {
    "id": 412,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Berdasarkan Permendagri No. 83 Tahun 2015, anggota Tim Penjaringan dan Penyaringan Calon Perangkat Desa yang dibentuk Kepala Desa berasal dari...",
    "options": [
      "Perangkat desa, pengurus lembaga kemasyarakatan desa (LKD), dan tokoh masyarakat desa",
      "Aparatur sipil negara dari kantor kecamatan saja",
      "Pengurus partai politik tingkat ranting",
      "Anggota BPD yang sedang aktif"
    ],
    "answer": 0,
    "explanation": "Permendagri No. 83 Tahun 2015 Pasal 4 menjelaskan Tim Seleksi terdiri atas unsur perangkat desa, pengurus kelembagaan kemasyarakatan, dan tokoh masyarakat desa.",
    "source": "Permendagri No. 83 Tahun 2015 Pasal 4"
  },
  {
    "id": 413,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sulit",
    "question": "Berdasarkan Permendagri No. 83 Tahun 2015 jo. Permendagri No. 67 Tahun 2017, berapa orang calon perangkat desa yang hasil penyaringannya dikonsultasikan oleh Kepala Desa kepada Camat?",
    "options": [
      "Hanya 1 orang dengan nilai tertinggi",
      "Paling sedikit 2 (dua) orang calon",
      "Seluruh peserta seleksi tanpa terkecuali",
      "Minimal 5 orang peserta terbaik"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 83 Tahun 2015 Pasal 4 ayat (3) menetapkan bahwa Kepala Desa mengonsultasikan paling sedikit 2 (dua) orang calon perangkat desa hasil seleksi kepada Camat.",
    "source": "Permendagri No. 83 Tahun 2015 Pasal 4 ayat (3)"
  },
  {
    "id": 414,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Berdasarkan Perda Kabupaten Tuban No. 2 Tahun 2016 jo. No. 16 Tahun 2021, batas waktu pelantikan perangkat desa terpilih setelah terbitnya Keputusan Kepala Desa adalah...",
    "options": [
      "Paling lambat 7 hari kerja",
      "Paling lambat 14 hari kalender",
      "Paling lambat 30 hari kalender",
      "Paling lambat 60 hari kalender"
    ],
    "answer": 2,
    "explanation": "Perda Kab. Tuban No. 2/2016 jo. 16/2021 Pasal 14 mengatur bahwa pelantikan perangkat desa dilaksanakan paling lambat 30 (tiga puluh) hari kalender sejak ditetapkannya Keputusan Kepala Desa.",
    "source": "Perda Kab. Tuban No. 2/2016 jo. No. 16/2021 Pasal 14"
  },
  {
    "id": 415,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "mudah",
    "question": "Berdasarkan UU No. 6 Tahun 2014 Pasal 26 ayat (2) huruf c, pemegang kekuasaan pengelolaan keuangan dan aset desa adalah...",
    "options": [
      "Ketua BPD",
      "Kepala Desa",
      "Sekretaris Desa",
      "Kaur Keuangan"
    ],
    "answer": 1,
    "explanation": "Kepala Desa adalah Pemegang Kekuasaan Pengelolaan Keuangan Desa (PKPKD) dan mewakili Pemerintah Desa dalam kepemilikan aset desa.",
    "source": "UU No. 6 Tahun 2014 Pasal 26 ayat (2) huruf c"
  },
  {
    "id": 416,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Sanksi administratif apakah yang dapat diberikan kepada Kepala Desa jika tidak menyampaikan LPPD atau LKPPD dalam batas waktu yang ditentukan undang-undang?",
    "options": [
      "Denda uang tunai Rp100.000.000",
      "Teguran lisan, teguran tertulis, hingga pemberhentian sementara oleh bupati",
      "Hukuman kurungan langsung dari BPD",
      "Penghapusan nomor register desa"
    ],
    "answer": 1,
    "explanation": "UU No. 6 Tahun 2014 Pasal 28 mengatur bahwa Kepala Desa yang tidak memenuhi kewajiban menyampaikan LPPD/LKPPD dikenai sanksi administratif berupa teguran lisan, tertulis, hingga pemberhentian sementara.",
    "source": "UU No. 6 Tahun 2014 Pasal 28"
  },
  {
    "id": 417,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Berdasarkan PP No. 43 Tahun 2014 jo. PP No. 11 Tahun 2019, Alokasi Dana Desa (ADD) yang dialokasikan Pemerintah Kabupaten paling sedikit adalah...",
    "options": [
      "5% dari dana perimbangan yang diterima kabupaten setelah dikurangi DAK",
      "10% dari dana perimbangan yang diterima kabupaten setelah dikurangi DAK",
      "15% dari total Pendapatan Asli Daerah (PAD)",
      "20% dari APBD kabupaten"
    ],
    "answer": 1,
    "explanation": "PP No. 43/2014 Pasal 96 ayat (1) menegaskan Pemerintah Daerah Kabupaten mengalokasikan Alokasi Dana Desa (ADD) dalam APBD paling sedikit 10% dari dana perimbangan setelah dikurangi DAK.",
    "source": "PP No. 43 Tahun 2014 Pasal 96 ayat (1)"
  },
  {
    "id": 418,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Menurut UU No. 3 Tahun 2024, dalam menjalankan tugas dan kewajiban kedinasannya, Kepala Desa dan Perangkat Desa berhak memperoleh...",
    "options": [
      "Perlindungan hukum atas pelaksanaan tugas kedinasan",
      "Kekebalan hukum mutlak dari segala tindak pidana",
      "Hak veto terhadap putusan pengadilan negeri",
      "Hak monopoli atas seluruh usaha perdagangan di desa"
    ],
    "answer": 0,
    "explanation": "UU No. 3 Tahun 2024 menyisipkan ketentuan hak memperoleh perlindungan hukum bagi aparatur desa sepanjang tindakan kedinasan yang diambil sesuai dengan ketentuan peraturan perundang-undangan.",
    "source": "UU No. 3 Tahun 2024 Pasal 26 & Pasal 50A"
  },
  {
    "id": 419,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sulit",
    "question": "Berdasarkan Permendagri No. 83 Tahun 2015, Kepala Desa membentuk Tim Seleksi Penjaringan dan Penyaringan Perangkat Desa paling lambat...",
    "options": [
      "1 minggu setelah kekosongan",
      "1 bulan setelah kekosongan",
      "2 bulan setelah kekosongan jabatan perangkat desa",
      "6 bulan setelah kekosongan"
    ],
    "answer": 2,
    "explanation": "Permendagri No. 83 Tahun 2015 Pasal 4 ayat (1) menetapkan bahwa Kepala Desa membentuk Tim Seleksi paling lambat 2 (dua) bulan setelah jabatan Perangkat Desa dinyatakan kosong.",
    "source": "Permendagri No. 83 Tahun 2015 Pasal 4 ayat (1)"
  },

  {
    "id": 420,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Pembagian wilayah desa ke dalam beberapa dusun didasarkan atas pertimbangan...",
    "options": [
      "Jumlah perolehan suara pemilukada",
      "Kondisi geografis, jumlah penduduk, dan rentang kendali pelayanan pemerintahan",
      "Permintaan kelompok arisan warga setempat",
      "Jumlah gedung pertokoan di wilayah desa"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 84 Tahun 2015 mengatur pembentukan dusun (wilayah kerja Kasun) didasarkan pada faktor geografis, luas wilayah, jumlah penduduk, dan efektivitas rentang kendali pelayanan.",
    "source": "Permendagri No. 84 Tahun 2015 Pasal 12"
  },

  # =========================================================================
  # KATEGORI 2: Peraturan perundang-undangan dan tata kelola (12 Soal: ID 421-432)
  # =========================================================================
  {
    "id": 421,
    "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
    "difficulty": "mudah",
    "question": "Di dalam hierarki peraturan perundang-undangan menurut UU No. 12 Tahun 2011 Pasal 7 ayat (1), Ketetapan MPR menempati urutan...",
    "options": [
      "Di atas UUD 1945",
      "Di bawah UUD 1945 dan di atas Undang-Undang/Perppu",
      "Setara dengan Peraturan Pemerintah",
      "Di bawah Peraturan Presiden"
    ],
    "answer": 1,
    "explanation": "Urutan hierarki perundang-undangan: 1. UUD 1945, 2. Tap MPR, 3. UU/Perppu, 4. PP, 5. Perpres, 6. Perda Provinsi, 7. Perda Kabupaten/Kota.",
    "source": "UU No. 12 Tahun 2011 Pasal 7 ayat (1)"
  },
  {
    "id": 422,
    "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
    "difficulty": "sedang",
    "question": "Menurut UU No. 12 Tahun 2011 Pasal 15, materi muatan tentang sanksi pidana hanya boleh dimuat di dalam...",
    "options": [
      "Undang-Undang, Peraturan Daerah Provinsi, dan Peraturan Daerah Kabupaten/Kota",
      "Peraturan Desa dan Peraturan Kepala Desa",
      "Peraturan Pemerintah dan Keputusan Camat",
      "Seluruh jenis peraturan perundang-undangan"
    ],
    "answer": 0,
    "explanation": "UU No. 12 Tahun 2011 Pasal 15 menegaskan materi muatan mengenai ketentuan pidana hanya dapat dimuat dalam Undang-Undang dan Peraturan Daerah (Perda). Peraturan Desa tidak berwenang memuat ancaman sanksi pidana kurungan.",
    "source": "UU No. 12 Tahun 2011 Pasal 15"
  },
  {
    "id": 423,
    "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
    "difficulty": "sedang",
    "question": "Peraturan yang ditetapkan oleh dua Kepala Desa atau lebih dalam rangka kerja sama antardesa (misal pengelolaan sumber mata air bersama) disebut...",
    "options": [
      "Peraturan Desa Bersama (Permakades)",
      "Peraturan Gabungan Camat",
      "Peraturan Wilayah Dusun",
      "Keputusan Bersama RT/RW"
    ],
    "answer": 0,
    "explanation": "Permendagri No. 111 Tahun 2014 Pasal 2 mengatur Peraturan Bersama Kepala Desa (Permakades) adalah peraturan yang ditetapkan oleh dua atau lebih Kepala Desa dalam rangka kerja sama antardesa.",
    "source": "Permendagri No. 111 Tahun 2014 Pasal 2"
  },
  {
    "id": 424,
    "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
    "difficulty": "mudah",
    "question": "Berdasarkan UU No. 6 Tahun 2014 Pasal 70, hak apakah yang dimiliki oleh masyarakat desa dalam pembentukan Peraturan Desa?",
    "options": [
      "Berhak memveto secara sepihak isi Perdes",
      "Berhak memberikan masukan secara lisan atau tertulis dalam penyiapan atau pembahasan rancangan Perdes",
      "Berhak membubarkan tim penyusun rancangan Perdes",
      "Berhak mengesahkan Perdes tanpa keterlibatan BPD"
    ],
    "answer": 1,
    "explanation": "UU No. 6 Tahun 2014 Pasal 70 menjamin hak masyarakat desa untuk memberikan masukan secara lisan atau tertulis dalam penyiapan atau pembahasan rancangan Perdes.",
    "source": "UU No. 6 Tahun 2014 Pasal 70"
  },
  {
    "id": 425,
    "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
    "difficulty": "sedang",
    "question": "Asas dalam pembentukan regulasi yang memperhitungkan bahwa peraturan yang dibuat dapat berlaku efektif secara filosofis, yuridis, dan sosiologis di masyarakat disebut...",
    "options": [
      "Asas dapat dilaksanakan",
      "Asas kelembagaan yang tepat",
      "Asas kejelasan rumusan",
      "Asas keterbukaan"
    ],
    "answer": 0,
    "explanation": "UU No. 12 Tahun 2011 Pasal 5 huruf d menjelaskan asas 'dapat dilaksanakan' berarti setiap pembentukan peraturan harus memperhitungkan efektivitas peraturan di dalam masyarakat.",
    "source": "UU No. 12 Tahun 2011 Pasal 5 huruf d"
  },
  {
    "id": 426,
    "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
    "difficulty": "sedang",
    "question": "Asas 'kedayagunaan dan kehasilgunaan' dalam pembentukan peraturan perundang-undangan (Pasal 5 huruf e UU 12/2011) mengandung makna bahwa...",
    "options": [
      "Peraturan dibuat sesering mungkin untuk menyerap anggaran",
      "Peraturan dibuat karena memang benar-benar dibutuhkan dan bermanfaat dalam mengatur kehidupan masyarakat",
      "Peraturan harus disalin persis dari peraturan daerah lain",
      "Peraturan harus menguntungkan pihak pemerintah semata"
    ],
    "answer": 1,
    "explanation": "Asas kedayagunaan dan kehasilgunaan menyatakan bahwa setiap peraturan perundang-undangan dibuat karena memang benar-benar dibutuhkan dan bermanfaat dalam mengatur kehidupan bermasyarakat, berbangsa, dan bernegara.",
    "source": "UU No. 12 Tahun 2011 Pasal 5 huruf e"
  },
  {
    "id": 427,
    "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
    "difficulty": "mudah",
    "question": "Setelah Peraturan Desa diundangkan dalam Lembaran Desa, Pemerintah Desa wajib melakukan sosialisasi kepada...",
    "options": [
      "Aparatur kecamatan saja",
      "Masyarakat desa agar mengetahui dan melaksanakannya",
      "Pengurus partai politik",
      "Media cetak nasional"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 111 Tahun 2014 mewajibkan sosialisasi Perdes kepada seluruh masyarakat desa agar tercipta ketaatan hukum.",
    "source": "Permendagri No. 111 Tahun 2014"
  },
  {
    "id": 428,
    "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
    "difficulty": "sedang",
    "question": "Asas hukum yang menyatakan bahwa peraturan hukum yang lebih tinggi mengesampingkan peraturan hukum yang lebih rendah disebut asas...",
    "options": [
      "Lex superior derogat legi inferiori",
      "Lex posterior derogat legi priori",
      "Lex specialis derogat legi generali",
      "Pacta sunt servanda"
    ],
    "answer": 0,
    "explanation": "Asas Lex Superior Derogat Legi Inferiori adalah prinsip hukum bahwa aturan yang lebih tinggi kedudukannya mengesampingkan aturan yang lebih rendah.",
    "source": "Prinsip Hukum Perundang-undangan Indonesia"
  },
  {
    "id": 429,
    "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
    "difficulty": "sedang",
    "question": "Asas hukum yang menyatakan bahwa peraturan yang baru mengesampingkan peraturan lama yang sederajat mengenai materi yang sama disebut asas...",
    "options": [
      "Lex superior derogat legi inferiori",
      "Lex posterior derogat legi priori",
      "Lex specialis derogat legi generali",
      "Presumption of innocence"
    ],
    "answer": 1,
    "explanation": "Asas Lex Posterior Derogat Legi Priori berarti peraturan perundang-undangan baru mengesampingkan peraturan perundang-undangan lama yang mengatur hal yang sama.",
    "source": "Prinsip Hukum Perundang-undangan Indonesia"
  },
  {
    "id": 430,
    "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
    "difficulty": "sedang",
    "question": "Asas hukum yang menyatakan bahwa norma hukum yang bersifat khusus mengesampingkan norma hukum yang bersifat umum disebut asas...",
    "options": [
      "Lex superior derogat legi inferiori",
      "Lex posterior derogat legi priori",
      "Lex specialis derogat legi generali",
      "Equality before the law"
    ],
    "answer": 2,
    "explanation": "Asas Lex Specialis Derogat Legi Generali menyatakan bahwa aturan hukum khusus mengesampingkan aturan hukum umum.",
    "source": "Prinsip Hukum Perundang-undangan Indonesia"
  },
  {
    "id": 431,
    "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
    "difficulty": "sedang",
    "question": "Berdasarkan UU No. 30 Tahun 2014 tentang Administrasi Pemerintahan, Asas Kecermatan menuntut pejabat pemerintahan desa untuk...",
    "options": [
      "Menandatangani surat tanpa membaca isinya demi kecepatan pelayanan",
      "Meneliti seluruh dokumen, fakta hukum, dan bukti secara teliti sebelum menetapkan keputusan",
      "Menolak seluruh permohonan warga yang tidak dikenal",
      "Meminta bayaran tambahan atas pemeriksaan dokumen"
    ],
    "answer": 1,
    "explanation": "Asas Kecermatan (UU 30/2014 Pasal 10 ayat 1 huruf d) mengharuskan pejabat pemerintah meneliti semua fakta yang relevan dan memasukkan semua aspek yang relevan dalam pertimbangan sebelum menerbitkan keputusan.",
    "source": "UU No. 30 Tahun 2014 Pasal 10 ayat (1) huruf d"
  },
  {
    "id": 432,
    "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
    "difficulty": "sedang",
    "question": "Berdasarkan UU No. 30 Tahun 2014, Keputusan Tata Usaha Negara Desa (Keputusan Kepala Desa) memiliki ciri-ciri pokok...",
    "options": [
      "Konkret, individual, dan final",
      "Abstrak, umum, dan sementara",
      "Rahasia, sepihak, dan tidak dapat digugat",
      "Lisan, fleksibel, dan tanpa nomor registrasi"
    ],
    "answer": 0,
    "explanation": "Keputusan administrasi pemerintahan bersifat konkret (objeknya nyata), individual (subjeknya tertentu), dan final (sudah definitif dan menimbulkan akibat hukum).",
    "source": "UU No. 30 Tahun 2014 tentang Administrasi Pemerintahan"
  },

  # =========================================================================
  # KATEGORI 3: Pancasila, UUD 1945, dan wawasan kebangsaan (10 Soal: ID 433-442)
  # =========================================================================
  {
    "id": 433,
    "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
    "difficulty": "mudah",
    "question": "Sikap warga desa yang tidak memaksakan agama atau kepercayaannya kepada tetangga yang berbeda keyakinan merupakan butir pengamalan sila ke-...",
    "options": [
      "Sila Pertama",
      "Sila Kedua",
      "Sila Ketiga",
      "Sila Keempat"
    ],
    "answer": 0,
    "explanation": "Tidak memaksakan suatu agama dan kepercayaan terhadap Tuhan Yang Maha Esa kepada orang lain adalah butir Sila ke-1 Pancasila.",
    "source": "Ketetapan MPR No. I/MPR/2003 Butir Sila 1"
  },
  {
    "id": 434,
    "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
    "difficulty": "mudah",
    "question": "Mengembangkan sikap tenggang rasa (tepa salira) dalam pergaulan hidup bermasyarakat di dusun merupakan wujud pengamalan sila ke-...",
    "options": [
      "Pertama",
      "Kedua",
      "Ketiga",
      "Kelima"
    ],
    "answer": 1,
    "explanation": "Mengembangkan sikap tenggang rasa dan tepa salira merupakan butir pengamalan Sila ke-2 Pancasila: Kemanusiaan yang Adil dan Beradab.",
    "source": "Ketetapan MPR No. I/MPR/2003 Butir Sila 2"
  },
  {
    "id": 435,
    "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
    "difficulty": "mudah",
    "question": "Pemerintah Desa menggalakkan pemakaian produk kerajinan batik gedog khas Tuban dan olahan pangan lokal warga. Hal ini mencerminkan pengamalan Pancasila sila ke-...",
    "options": [
      "Pertama",
      "Kedua",
      "Ketiga",
      "Keempat"
    ],
    "answer": 2,
    "explanation": "Bangga sebagai bangsa Indonesia dan cinta tanah air melalui pengutamaan produk lokal adalah perwujudan Sila ke-3: Persatuan Indonesia.",
    "source": "Ketetapan MPR No. I/MPR/2003 Butir Sila 3"
  },
  {
    "id": 436,
    "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
    "difficulty": "sedang",
    "question": "Menerima dan melaksanakan hasil keputusan musyawarah desa dengan itikad baik dan rasa tanggung jawab moral kepada Tuhan Yang Maha Esa merupakan pengamalan sila ke-...",
    "options": [
      "Kedua",
      "Ketiga",
      "Keempat",
      "Kelima"
    ],
    "answer": 2,
    "explanation": "Dengan itikad baik dan rasa tanggung jawab menerima dan melaksanakan hasil keputusan musyawarah merupakan butir pokok Sila ke-4 Pancasila.",
    "source": "Ketetapan MPR No. I/MPR/2003 Butir Sila 4"
  },
  {
    "id": 437,
    "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
    "difficulty": "sedang",
    "question": "Seorang perangkat desa yang mengutamakan kesederhanaan, tidak bergaya hidup mewah, dan tidak memamerkan kekayaan di media sosial mengamalkan nilai sila ke-...",
    "options": [
      "Kedua",
      "Ketiga",
      "Keempat",
      "Kelima"
    ],
    "answer": 3,
    "explanation": "Tidak bersikap boros dan tidak bergaya hidup mewah merupakan butir pengamalan Sila ke-5 Pancasila: Keadilan Sosial bagi Seluruh Rakyat Indonesia.",
    "source": "Ketetapan MPR No. I/MPR/2003 Butir Sila 5"
  },
  {
    "id": 438,
    "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
    "difficulty": "sedang",
    "question": "Pasal 28D ayat (1) UUD 1945 menegaskan bahwa setiap orang berhak atas...",
    "options": [
      "Bantuan modal usaha cuma-cuma",
      "Pengakuan, jaminan, perlindungan, dan kepastian hukum yang adil serta perlakuan yang sama di hadapan hukum",
      "Pembebasan dari seluruh kewajiban membayar pajak",
      "Jabatan di struktur pemerintahan tanpa melalui seleksi"
    ],
    "answer": 1,
    "explanation": "Pasal 28D ayat (1) UUD 1945 berbunyi: 'Setiap orang berhak atas pengakuan, jaminan, perlindungan, dan kepastian hukum yang adil serta perlakuan yang sama dihadapan hukum'.",
    "source": "UUD NRI 1945 Pasal 28D ayat (1)"
  },
  {
    "id": 439,
    "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
    "difficulty": "sedang",
    "question": "Berdasarkan Pasal 30 ayat (2) UUD 1945, usaha pertahanan dan keamanan negara dilaksanakan melalui sistem pertahanan dan keamanan rakyat semesta dengan kedudukan TNI dan Polri sebagai...",
    "options": [
      "Kekuatan utama",
      "Kekuatan pendukung",
      "Satu-satunya komponen",
      "Penonton pasif"
    ],
    "answer": 0,
    "explanation": "Pasal 30 ayat (2) UUD 1945 menyebutkan usaha pertahanan dan keamanan negara dilaksanakan melalui Sishankamrata dengan Tentara Nasional Indonesia dan Kepolisian Negara RI sebagai kekuatan utama, dan rakyat sebagai kekuatan pendukung.",
    "source": "UUD NRI 1945 Pasal 30 ayat (2)"
  },
  {
    "id": 440,
    "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
    "difficulty": "mudah",
    "question": "Penyediaan sarana belajar Pos PAUD dan beasiswa bagi anak tidak mampu di desa merupakan implementasi amanat konstitusi Pasal 31 ayat (1) UUD 1945 yang berbunyi...",
    "options": [
      "Setiap warga negara berhak mendapat pendidikan",
      "Negara memajukan kebudayaan nasional",
      "Pemerintah memajukan ilmu pengetahuan dan teknologi",
      "Fakir miskin dipelihara oleh negara"
    ],
    "answer": 0,
    "explanation": "Pasal 31 ayat (1) UUD 1945 berbunyi: 'Setiap warga negara berhak mendapat pendidikan'.",
    "source": "UUD NRI 1945 Pasal 31 ayat (1)"
  },
  {
    "id": 441,
    "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
    "difficulty": "mudah",
    "question": "Berdasarkan Pasal 33 ayat (1) UUD 1945, sistem perekonomian nasional Indonesia disusun sebagai usaha bersama berdasar atas asas...",
    "options": [
      "Persaingan bebas kapitalistik",
      "Kekeluargaan",
      "Monopoli pemerintah semata",
      "Konglomerasi swasta"
    ],
    "answer": 1,
    "explanation": "Pasal 33 ayat (1) UUD 1945 menyatakan: 'Perekonomian disusun sebagai usaha bersama berdasar atas asas kekeluargaan'. Asas ini menjiwai pembentukan Koperasi dan BUMDes.",
    "source": "UUD NRI 1945 Pasal 33 ayat (1)"
  },
  {
    "id": 442,
    "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
    "difficulty": "mudah",
    "question": "Jumlah bulu pada sayap burung Garuda Pancasila berjumlah 17 helai, pada ekor 8 helai, pada pangkal ekor 19 helai, dan pada leher 45 helai. Kombinasi angka tersebut melambangkan...",
    "options": [
      "Jumlah pasal dalam Undang-Undang Dasar 1945",
      "Tanggal Proklamasi Kemerdekaan Republik Indonesia (17 Agustus 1945)",
      "Jumlah pahlawan nasional yang menandatangani teks proklamasi",
      "Jumlah kementerian koordinator era kabinet pertama"
    ],
    "answer": 1,
    "explanation": "Konfigurasi jumlah bulu lambang Garuda Pancasila melambangkan momentum bersejarah Proklamasi Kemerdekaan RI yaitu tanggal 17 Agustus 1945 (17-8-1945).",
    "source": "UU No. 24 Tahun 2009 tentang Bendera, Bahasa, dan Lambang Negara"
  },

  # =========================================================================
  # KATEGORI 4: Administrasi pemerintahan, surat-menyurat, dan pengarsipan (10 Soal: ID 443-452)
  # =========================================================================
  {
    "id": 443,
    "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
    "difficulty": "sedang",
    "question": "Buku administrasi umum desa yang khusus mencatat luas, lokasi, status perolehan, dan nama pemegang hak sewa atas tanah milik pemerintah desa adalah...",
    "options": [
      "Buku Tanah Kas Desa",
      "Buku Kas Umum",
      "Buku Ekspedisi",
      "Buku Rencana Anggaran Biaya"
    ],
    "answer": 0,
    "explanation": "Permendagri No. 47 Tahun 2016 mengatur Buku Tanah Kas Desa sebagai register resmi untuk mencatat status, asal-usul, luas, dan pemanfaatan tanah bengkok/kas desa.",
    "source": "Permendagri No. 47 Tahun 2016"
  },
  {
    "id": 444,
    "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
    "difficulty": "sedang",
    "question": "Buku administrasi umum yang digunakan untuk mencatat nomor urut, nomor keputusan, tanggal penetapan, dan perihal Keputusan Kepala Desa adalah...",
    "options": [
      "Buku Data Peraturan Desa",
      "Buku Data Keputusan Kepala Desa",
      "Buku Register Surat Keterangan",
      "Buku Lembaran Daerah"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 47 Tahun 2016 mengatur Buku Data Keputusan Kepala Desa untuk membukukan seluruh Surat Keputusan (SK) yang diterbitkan Kepala Desa.",
    "source": "Permendagri No. 47 Tahun 2016"
  },
  {
    "id": 445,
    "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
    "difficulty": "sedang",
    "question": "Warga pendatang yang berdomisili sementara di suatu desa untuk keperluan kerja proyek tanpa pindah KTP dicatatkan oleh perangkat desa ke dalam...",
    "options": [
      "Buku Data Induk Penduduk",
      "Buku Data Penduduk Sementara",
      "Buku Inventaris Desa",
      "Buku Agenda Rahasia"
    ],
    "answer": 1,
    "explanation": "Buku Data Penduduk Sementara digunakan untuk mencatat setiap warga yang berdomisili di desa tetapi tidak memiliki KTP-el desa setempat.",
    "source": "Permendagri No. 47 Tahun 2016 Lampiran Administrasi Kependudukan"
  },
  {
    "id": 446,
    "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
    "difficulty": "sedang",
    "question": "Buku administrasi pembangunan desa yang mencatat nama, jenis kelamin, keahlian, dan bidang tugas tenaga penggerak swadaya masyarakat adalah...",
    "options": [
      "Buku Rencana Kerja Pembangunan",
      "Buku Kader Pemberdayaan Masyarakat Desa (KPMD)",
      "Buku Inventarisasi Hasil Pembangunan",
      "Buku Kas Pembantu Kegiatan"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 47 Tahun 2016 mengatur Buku Kader Pemberdayaan Masyarakat untuk mencatat identitas dan peran kader pendamping pembangunan desa.",
    "source": "Permendagri No. 47 Tahun 2016"
  },
  {
    "id": 447,
    "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
    "difficulty": "sedang",
    "question": "Pada naskah dinas resmi yang ditandatangani oleh Kepala Desa, penulisan nama pejabat penandatangan yang tepat adalah...",
    "options": [
      "Nama lengkap dengan gelar akademis dan tanpa mencantumkan NIP (kecuali Kades PNS)",
      "Nama lengkap disertai nomor rekening bank",
      "Hanya paraf kecil tanpa nama terang",
      "Nama samaran atau julukan warga"
    ],
    "answer": 0,
    "explanation": "Format baku tanda tangan Kepala Desa mencantumkan nama jabatan di atas tanda tangan, nama lengkap pejabat (ditambah gelar bila ada), dan tidak mencantumkan NIP karena Kades merupakan jabatan politis/bukan PNS (kecuali Kades penjabat/Pj. PNS).",
    "source": "Permendagri No. 1 Tahun 2023 tentang Tata Naskah Dinas"
  },
  {
    "id": 448,
    "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
    "difficulty": "mudah",
    "question": "Cap dinas (stempel) resmi Pemerintah Desa dibubuhkan pada bagian...",
    "options": [
      "Pojok kanan atas surat mengenai perangko",
      "Menyentuh bagian kiri tanda tangan pejabat penandatangan naskah dinas",
      "Tepat di tengah teks isi surat",
      "Halaman belakang amplop surat saja"
    ],
    "answer": 1,
    "explanation": "Sesuai kaidah tata naskah dinas, cap dinas dibubuhkan di sebelah kiri menyinggung sedikit bagian tanda tangan pejabat penandatangan.",
    "source": "Permendagri No. 1 Tahun 2023 tentang Tata Naskah Dinas"
  },
  {
    "id": 449,
    "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
    "difficulty": "sedang",
    "question": "Bagian penutup amar putusan pada Surat Keputusan (SK) Kepala Desa yang memuat tanggal berlakunya keputusan tersebut biasanya dirumuskan pada diktum...",
    "options": [
      "Menimbang",
      "Mengingat",
      "MEMUTUSKAN: KESATU / KEDUA / KETIGA",
      "Lampiran Tabel"
    ],
    "answer": 2,
    "explanation": "Amar keputusan dan klausul mulai berlakunya keputusan dirumuskan dalam Diktum 'MEMUTUSKAN: Menetapkan...' (misal Diktum KETIGA: Keputusan ini mulai berlaku pada tanggal ditetapkan).",
    "source": "Tata Naskah Dinas Keputusan Kepala Desa"
  },
  {
    "id": 450,
    "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
    "difficulty": "sedang",
    "question": "Dalam pelaksanaan pemusnahan arsip dinas kantor desa yang telah melewati batas retensi dan tidak memiliki nilai guna, dokumen legalitas yang wajib dibuat adalah...",
    "options": [
      "Berita Acara Pemusnahan Arsip dan Daftar Pertelaan Arsip yang Dimusnahkan",
      "Kuitansi pembayaran biaya pembakaran berkas",
      "Surat peringatan kepada mantan pegawai",
      "Peraturan Desa tentang Pembakaran Sampah Kantor"
    ],
    "answer": 0,
    "explanation": "UU No. 43 Tahun 2009 Pasal 66 mewajibkan setiap pemusnahan arsip disertai Berita Acara Pemusnahan Arsip dan daftar pertelaan arsip serta disaksikan minimal 2 orang saksi bidang hukum/pengawasan.",
    "source": "UU No. 43 Tahun 2009 tentang Kearsipan Pasal 66"
  },
  {
    "id": 451,
    "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
    "difficulty": "mudah",
    "question": "Surat dinas yang diterbitkan oleh Kepala Desa untuk menerangkan status domisili, usaha, atau keadaan belum menikah warga disebut...",
    "options": [
      "Surat Perintah Tugas",
      "Surat Keterangan Desa (SKD)",
      "Nota Dinas",
      "Lembar Disposisi"
    ],
    "answer": 1,
    "explanation": "Surat Keterangan Desa adalah naskah dinas yang memuat keterangan resmi mengenai suatu fakta atau keadaan seseorang/barang yang diketahui pemerintah desa.",
    "source": "Pedoman Tata Naskah Dinas Kemendagri"
  },
  {
    "id": 452,
    "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
    "difficulty": "sedang",
    "question": "Naskah dinas yang berisi pelimpahan wewenang dari Kepala Desa kepada Sekretaris Desa untuk menandatangani surat-surat tertentu selama Kepala Desa menjalankan dinas luar kota disebut...",
    "options": [
      "Surat Kuasa / Surat Pelimpahan Kewenangan",
      "Surat Edaran",
      "Surat Perjanjian Kerja Bersama",
      "Surat Pengantar"
    ],
    "answer": 0,
    "explanation": "Surat Kuasa Kedinasan / Surat Pelimpahan Wewenang adalah naskah dinas resmi untuk melimpahkan wewenang tertentu kepada pejabat bawahan.",
    "source": "Tata Naskah Dinas Kemendagri"
  },

  # =========================================================================
  # KATEGORI 5: Keuangan desa, APB Desa, dan aset desa (10 Soal: ID 453-462)
  # =========================================================================
  {
    "id": 453,
    "category": "Keuangan desa, APB Desa, dan aset desa",
    "difficulty": "sedang",
    "question": "Berdasarkan Permendagri No. 20 Tahun 2018, dokumen yang memuat perkiraan penerimaan kas dan kebutuhan penarikan dana belanja per bulan atau triwulan adalah...",
    "options": [
      "Rencana Kerja Pemerintah Desa (RKP Desa)",
      "Rencana Anggaran Kas Desa (RAK Desa)",
      "Buku Bank Kas Desa",
      "Laporan Keterangan Penyelenggaraan Pemdes"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 20 Tahun 2018 Pasal 38 mengatur bahwa Rencana Anggaran Kas (RAK) Desa disusun oleh Kaur Keuangan untuk mengendalikan arus kas masuk dan arus kas keluar setiap periode.",
    "source": "Permendagri No. 20 Tahun 2018 Pasal 38"
  },
  {
    "id": 454,
    "category": "Keuangan desa, APB Desa, dan aset desa",
    "difficulty": "sedang",
    "question": "Dokumen Pelaksanaan Anggaran (DPA) yang memuat rencana kegiatan dan rincian belanja disusun oleh...",
    "options": [
      "Kepala Seksi dan Kepala Urusan selaku Pelaksana Kegiatan Anggaran (PKA)",
      "Ketua BPD bersama Camat",
      "Tenaga Ahli Pemberdayaan Masyarakat Kabupaten",
      "Pengurus Karang Taruna"
    ],
    "answer": 0,
    "explanation": "Permendagri No. 20 Tahun 2018 Pasal 35 menyebutkan Kaur dan Kasi selaku PKA menyusun DPA paling lambat 6 hari kerja setelah Perdes APB Desa ditetapkan.",
    "source": "Permendagri No. 20 Tahun 2018 Pasal 35"
  },
  {
    "id": 455,
    "category": "Keuangan desa, APB Desa, dan aset desa",
    "difficulty": "sedang",
    "question": "Buku pembantu dalam penatausahaan keuangan desa yang khusus mencatat pemotongan dan penyetoran pajak (PPN dan PPh) ke Kas Negara adalah...",
    "options": [
      "Buku Pembantu Pajak",
      "Buku Kas Umum",
      "Buku Pembantu Bank",
      "Buku Kas Pembantu Panjar"
    ],
    "answer": 0,
    "explanation": "Buku Pembantu Pajak merupakan buku wajib yang dipegang Bendahara Desa untuk mencatat transaksi penerimaan dan penyetoran pajak negara ke kas negara melalui sistem e-billing.",
    "source": "Permendagri No. 20 Tahun 2018 Lampiran Penatausahaan Keuangan"
  },
  {
    "id": 456,
    "category": "Keuangan desa, APB Desa, dan aset desa",
    "difficulty": "sedang",
    "question": "Kepala Desa wajib menyampaikan Laporan Realisasi Pelaksanaan APB Desa Semester Pertama kepada Bupati melalui Camat paling lambat pada...",
    "options": [
      "Akhir bulan Maret tahun berjalan",
      "Akhir bulan Juli tahun berjalan",
      "Akhir bulan Oktober tahun berjalan",
      "Akhir bulan Desember tahun berjalan"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 20 Tahun 2018 Pasal 68 ayat (1) menyatakan bahwa laporan realisasi pelaksanaan APB Desa semester pertama disampaikan paling lambat pada akhir bulan Juli tahun berjalan.",
    "source": "Permendagri No. 20 Tahun 2018 Pasal 68 ayat (1)"
  },
  {
    "id": 457,
    "category": "Keuangan desa, APB Desa, dan aset desa",
    "difficulty": "sulit",
    "question": "Berdasarkan Permendagri No. 1 Tahun 2016, pemanfaatan aset desa berupa tanah melalui skema Bangun Guna Serah (BGS) dapat dilakukan paling lama untuk jangka waktu...",
    "options": [
      "5 tahun",
      "10 tahun",
      "20 tahun",
      "50 tahun"
    ],
    "answer": 2,
    "explanation": "Permendagri No. 1 Tahun 2016 Pasal 14 ayat (3) mengatur bahwa jangka waktu Bangun Guna Serah (BGS) dan Bangun Serah Guna (BSG) paling lama 20 (dua puluh) tahun dan dapat diperpanjang.",
    "source": "Permendagri No. 1 Tahun 2016 Pasal 14 ayat (3)"
  },
  {
    "id": 458,
    "category": "Keuangan desa, APB Desa, dan aset desa",
    "difficulty": "sedang",
    "question": "Berdasarkan Permendagri No. 1 Tahun 2016, pemanfaatan aset desa berupa Pinjam Pakai barang milik desa dapat dilakukan antar...",
    "options": [
      "Pemerintah Desa dengan perusahaan swasta multinasional untuk bisnis",
      "Pemerintah Desa dengan Pemerintah Desa lain atau Lembaga Kemasyarakatan Desa tanpa imbalan uang",
      "Kepala Desa dengan anggota keluarganya untuk kepentingan pribadi",
      "Pemerintah Desa dengan pengurus partai politik untuk kampanye"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 1 Tahun 2016 Pasal 12 menjelaskan Pinjam Pakai aset desa dilakukan antara Pemdes dengan Pemda/Pemdes lain atau Lembaga Kemasyarakatan Desa untuk kepentingan umum tanpa memungut imbalan.",
    "source": "Permendagri No. 1 Tahun 2016 Pasal 12"
  },
  {
    "id": 459,
    "category": "Keuangan desa, APB Desa, dan aset desa",
    "difficulty": "mudah",
    "question": "Semua penerimaan dan pengeluaran desa dalam rangka pelaksanaan APB Desa wajib dilakukan melalui...",
    "options": [
      "Rekening Kas Desa (RKD) pada bank pemerintah yang ditunjuk",
      "Dompet digital pribadi Kaur Keuangan",
      "Kotak brankas rahasia di rumah Kepala Desa",
      "Rekening giro pengurus BPD"
    ],
    "answer": 0,
    "explanation": "Permendagri No. 20 Tahun 2018 Pasal 14 menegaskan seluruh transaksi keuangan desa wajib disalurkan melalui Rekening Kas Desa (RKD).",
    "source": "Permendagri No. 20 Tahun 2018 Pasal 14"
  },
  {
    "id": 460,
    "category": "Keuangan desa, APB Desa, dan aset desa",
    "difficulty": "sedang",
    "question": "Pengadaan Barang dan Jasa di Desa mengutamakan swakelola dengan prinsip Padat Karya Tunai Desa (PKTD). Tujuan utama dari prinsip ini adalah...",
    "options": [
      "Memberikan keuntungan maksimal bagi kontraktor besar luar kota",
      "Menyerap tenaga kerja warga setempat, memanfaatkan bahan baku lokal, dan menggerakkan ekonomi desa",
      "Menghindari kewajiban membayar upah tenaga kerja",
      "Memperlambat penyelesaian proyek fisik desa"
    ],
    "answer": 1,
    "explanation": "Prinsip Padat Karya Tunai Desa (PKTD) bertujuan memberdayakan masyarakat desa, memperluas kesempatan kerja lokal, dan mengalirkan dana desa langsung ke masyarakat setempat.",
    "source": "Peraturan LKPP No. 12 Tahun 2019 & SKB 4 Menteri tentang PKTD"
  },
  {
    "id": 461,
    "category": "Keuangan desa, APB Desa, dan aset desa",
    "difficulty": "mudah",
    "question": "Kelompok pendapatan desa yang bersumber dari Bagi Hasil Pajak Daerah dan Retribusi Daerah (BHPR) Kabupaten termasuk dalam kelompok...",
    "options": [
      "Pendapatan Asli Desa (PADes)",
      "Pendapatan Transfer",
      "Pendapatan Lain-lain",
      "Penerimaan Pembiayaan"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 20 Tahun 2018 Pasal 11 menyatakan kelompok Pendapatan Transfer terdiri dari: Dana Desa, ADD, Bagi Hasil Pajak dan Retribusi Daerah (BHPR), serta Bantuan Keuangan.",
    "source": "Permendagri No. 20 Tahun 2018 Pasal 11"
  },
  {
    "id": 462,
    "category": "Keuangan desa, APB Desa, dan aset desa",
    "difficulty": "sedang",
    "question": "Bendahara Desa wajib memungut Pajak Penghasilan (PPh) Pasal 22 sebesar 1,5% atas transaksi belanja barang jika nilai transaksi...",
    "options": [
      "Di atas Rp1.000.000,00 tidak termasuk PPN",
      "Di atas Rp2.000.000,00 tidak termasuk PPN",
      "Di atas Rp5.000.000,00 termasuk PPN",
      "Di atas Rp10.000.000,00 termasuk PPN"
    ],
    "answer": 1,
    "explanation": "Sesuai ketentuan perpajakan bendahara instansi pemerintah, pemungutan PPh Pasal 22 dikenakan atas belanja pengadaan barang dengan nilai di atas Rp2.000.000,00 tidak termasuk PPN (PMK No. 231/PMK.03/2019).",
    "source": "PMK No. 231/PMK.03/2019 tentang Pemungutan Pajak oleh Bendahara"
  },

  # =========================================================================
  # KATEGORI 6: Pembangunan desa, perencanaan, dan pemberdayaan (8 Soal: ID 463-470)
  # =========================================================================
  {
    "id": 463,
    "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
    "difficulty": "mudah",
    "question": "Berdasarkan Permendesa PDTT No. 21 Tahun 2020, tahapan siklus tahunan penyusunan RKP Desa secara resmi dimulai pada...",
    "options": [
      "Bulan Januari tahun berjalan",
      "Bulan Juli tahun berjalan",
      "Bulan Oktober tahun berjalan",
      "Bulan Desember tahun berjalan"
    ],
    "answer": 1,
    "explanation": "Permendesa No. 21 Tahun 2020 Pasal 34 ayat (1) menyatakan penyusunan RKP Desa dimulai pada bulan Juli tahun berjalan dengan pembentukan tim penyusun RKP Desa oleh Kepala Desa.",
    "source": "Permendesa PDTT No. 21 Tahun 2020 Pasal 34"
  },
  {
    "id": 464,
    "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
    "difficulty": "sedang",
    "question": "Dalam Musrenbangdes pembahasan rancangan RKP Desa, keterlibatan kelompok perempuan, kelompok disabilitas, dan warga miskin dijamin regulasi untuk mewujudkan prinsip...",
    "options": [
      "Pembangunan eksklusif elit desa",
      "Pembangunan desa yang partisipatif dan inklusif",
      "Pengurangan peran pemerintah desa",
      "Peniadaan kewenangan BPD"
    ],
    "answer": 1,
    "explanation": "Pembangunan inklusif memastikan semua lapisan masyarakat, khususnya kelompok rentan dan marginal, memiliki hak bersuara dan terakomodasi kebutuhannya dalam perencanaan desa.",
    "source": "Permendesa PDTT No. 21 Tahun 2020"
  },
  {
    "id": 465,
    "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
    "difficulty": "sedang",
    "question": "SDGs Desa Tujuan ke-5 yaitu 'Keterlibatan Perempuan Desa' mengamanatkan bahwa dalam kelembagaan desa dan musyawarah desa...",
    "options": [
      "Perempuan dilarang mencalonkan diri menjadi kepala desa",
      "Keterwakilan perempuan sekurang-kurangnya 30% dalam pengambilan keputusan pembangunan desa",
      "Hanya kaum pria yang boleh mengelola BUMDes",
      "Perempuan hanya diperkenankan menjadi staf administrasi tanpa hak suara"
    ],
    "answer": 1,
    "explanation": "Tujuan ke-5 SDGs Desa mendorong kesetaraan gender dan keterlibatan aktif perempuan minimal 30% di berbagai forum musyawarah desa dan kepengurusan kelembagaan desa.",
    "source": "Permendesa PDTT No. 21 Tahun 2020 tentang SDGs Desa"
  },
  {
    "id": 466,
    "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
    "difficulty": "mudah",
    "question": "Upaya Pemerintah Desa menyediakan sarana air bersih melalui program HIPPAM (Himpunan Penduduk Pemakai Air Minum) dan jamban sehat warga sejalan dengan SDGs Desa tujuan ke-...",
    "options": [
      "Ke-2: Desa Tanpa Kelaparan",
      "Ke-6: Desa Layak Air Bersih dan Sanitasi",
      "Ke-7: Desa Berenergi Bersih",
      "Ke-13: Tanggap Perubahan Iklim"
    ],
    "answer": 1,
    "explanation": "SDGs Desa tujuan ke-6 adalah 'Desa Layak Air Bersih dan Sanitasi' yang menargetkan akses air minum aman dan sanitasi yang layak bagi seluruh warga desa.",
    "source": "Permendesa PDTT No. 21 Tahun 2020 tentang SDGs Desa"
  },
  {
    "id": 467,
    "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
    "difficulty": "sedang",
    "question": "Berdasarkan PP No. 11 Tahun 2021, modal awal pendirian BUMDes bersumber dari APB Desa melalui mekanisme...",
    "options": [
      "Pinjaman bank komersial berbunga tinggi",
      "Penyertaan modal desa yang ditetapkan dengan Peraturan Desa",
      "Iuran wajib seluruh kepala keluarga di desa",
      "Pungutan liar sewa lahan perumahan warga"
    ],
    "answer": 1,
    "explanation": "PP No. 11 Tahun 2021 Pasal 39 menyebutkan bahwa modal awal BUMDes bersumber dari APB Desa melalui pos penyertaan modal desa yang ditetapkan dengan Peraturan Desa.",
    "source": "PP No. 11 Tahun 2021 Pasal 39"
  },
  {
    "id": 468,
    "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
    "difficulty": "sedang",
    "question": "Apabila beberapa desa di suatu kawasan kecamatan ingin mendirikan usaha pariwisata terpadu bersama, kelembagaan ekonomi yang tepat dibentuk adalah...",
    "options": [
      "BUMDes Bersama (BUMDesma)",
      "Koperasi Simpan Pinjam Swasta",
      "Perseroan Terbatas Milik Camat",
      "Yayasan Amal Lingkungan"
    ],
    "answer": 0,
    "explanation": "PP No. 11 Tahun 2021 mengatur pendirian BUMDes Bersama (BUMDesma) yang didirikan oleh 2 (dua) desa atau lebih dalam rangka kerja sama antardesa.",
    "source": "PP No. 11 Tahun 2021 Pasal 7"
  },
  {
    "id": 469,
    "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
    "difficulty": "mudah",
    "question": "Berdasarkan Permendagri No. 18 Tahun 2018, pengurus Lembaga Kemasyarakatan Desa (LKD) seperti Ketua RT, RW, dan PKK dilarang...",
    "options": [
      "Mengadakan kegiatan gotong royong warga",
      "Menjadi pengurus atau berafiliasi dengan partai politik",
      "Menghadiri musyawarah perencanaan desa",
      "Mengikuti pelatihan peningkatan kapasitas kader"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 18 Tahun 2018 Pasal 8 ayat (5) tegas melarang pengurus LKD merangkap jabatan pada LKD lainnya dan dilarang menjadi anggota partai politik.",
    "source": "Permendagri No. 18 Tahun 2018 Pasal 8 ayat (5)"
  },
  {
    "id": 470,
    "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
    "difficulty": "sedang",
    "question": "Tahapan siklus pembangunan desa yang benar dan berurutan sesuai regulasi adalah...",
    "options": [
      "Pelaksanaan kegiatan - Perencanaan - Pengawasan - Evaluasi",
      "Perencanaan - Penganggaran - Pelaksanaan - Pertanggungjawaban/Evaluasi",
      "Penganggaran - Evaluasi - Perencanaan - Pelaksanaan",
      "Pertanggungjawaban - Pelaksanaan - Perencanaan - Penganggaran"
    ],
    "answer": 1,
    "explanation": "Siklus tata kelola pembangunan desa berurutan: Perencanaan (RPJM/RKP Desa) -> Penganggaran (APB Desa) -> Pelaksanaan Kegiatan -> Pertanggungjawaban dan Evaluasi.",
    "source": "Permendagri No. 114 Tahun 2014 & Permendesa 21/2020"
  },

  # =========================================================================
  # KATEGORI 7: BPD, kelembagaan desa, dan musyawarah (5 Soal: ID 471-475)
  # =========================================================================
  {
    "id": 471,
    "category": "BPD, kelembagaan desa, dan musyawarah",
    "difficulty": "mudah",
    "question": "Berdasarkan UU No. 6 Tahun 2014 Pasal 55 huruf a, BPD berwenang bersama Kepala Desa untuk...",
    "options": [
      "Membahas dan menyepakati Rancangan Peraturan Desa",
      "Menetapkan besaran gaji PNS di kantor kecamatan",
      "Mengadili perkara pidana warga desa di pengadilan",
      "Menjual aset tanah kas desa secara bebas"
    ],
    "answer": 0,
    "explanation": "Fungsi legislasi BPD adalah membahas dan menyepakati rancangan Peraturan Desa (Perdes) bersama Kepala Desa.",
    "source": "UU No. 6 Tahun 2014 Pasal 55 huruf a"
  },
  {
    "id": 472,
    "category": "BPD, kelembagaan desa, dan musyawarah",
    "difficulty": "sedang",
    "question": "Berdasarkan UU No. 6 Tahun 2014 Pasal 61 huruf a, BPD berhak meminta keterangan kepada Pemerintah Desa mengenai...",
    "options": [
      "Kehidupan rumah tangga pribadi perangkat desa",
      "Penyelenggaraan pemerintahan desa dan pengelolaan keuangan desa",
      "Daftar kekayaan pribadi warga desa yang bukan pejabat",
      "Hasil pemeriksaan kesehatan dokter warga desa"
    ],
    "answer": 1,
    "explanation": "BPD berhak meminta keterangan tertulis atau lisan dari Pemerintah Desa terkait penyelenggaraan pemerintahan desa dalam rangka fungsi pengawasan.",
    "source": "UU No. 6 Tahun 2014 Pasal 61 huruf a"
  },
  {
    "id": 473,
    "category": "BPD, kelembagaan desa, dan musyawarah",
    "difficulty": "sedang",
    "question": "Berdasarkan Permendagri No. 110 Tahun 2016, rapat BPD dinyatakan kuorum dan sah untuk mengambil keputusan jika dihadiri oleh paling sedikit...",
    "options": [
      "1/2 dari jumlah anggota BPD",
      "2/3 dari jumlah anggota BPD",
      "3/4 dari jumlah anggota BPD",
      "Seluruh anggota BPD (100%)"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 110 Tahun 2016 Pasal 40 mengatur bahwa rapat BPD dinyatakan sah apabila dihadiri oleh paling sedikit 2/3 (dua pertiga) dari jumlah anggota BPD.",
    "source": "Permendagri No. 110 Tahun 2016 Pasal 40"
  },
  {
    "id": 474,
    "category": "BPD, kelembagaan desa, dan musyawarah",
    "difficulty": "mudah",
    "question": "Dalam pengambilan keputusan di Musyawarah Desa, apabila upaya musyawarah mufakat tidak tercapai setelah diusahakan berulang kali, maka keputusan dapat diambil melalui...",
    "options": [
      "Penunjukan sepihak oleh Camat",
      "Pemungutan suara terbanyak (voting)",
      "Adu kekuatan fisik antarpendukung",
      "Pengundian koin uang logam"
    ],
    "answer": 1,
    "explanation": "Apabila musyawarah untuk mufakat tidak tercapai, keputusan diambil berdasarkan pemungutan suara terbanyak (voting) secara demokratis.",
    "source": "Permendagri No. 110 Tahun 2016"
  },
  {
    "id": 475,
    "category": "BPD, kelembagaan desa, dan musyawarah",
    "difficulty": "mudah",
    "question": "Tunjangan dan operasional pimpinan serta anggota BPD bersumber dari...",
    "options": [
      "Anggaran Pendapatan dan Belanja Desa (APB Desa)",
      "Sumbangan sukarela bulanan warga miskin",
      "Hasil pemotongan bantuan sosial PKH",
      "Pinjaman online atas nama desa"
    ],
    "answer": 0,
    "explanation": "PP No. 11 Tahun 2019 dan Permendagri 110/2016 menetapkan tunjangan kedudukan dan biaya operasional BPD dianggarkan resmi dalam APB Desa (bersumber dari ADD).",
    "source": "PP No. 11 Tahun 2019 Pasal 100"
  },

  # =========================================================================
  # KATEGORI 8: Bahasa Indonesia (7 Soal: ID 476-482)
  # =========================================================================
  {
    "id": 476,
    "category": "Bahasa Indonesia",
    "difficulty": "mudah",
    "question": "Manakah deretan kata serapan berikut yang seluruhnya baku sesuai Ejaan Bahasa Indonesia yang Disempurnakan (EYD V)?",
    "options": [
      "Analisa, sistim, kwalitas",
      "Analisis, sistem, kualitas",
      "Analisis, sistim, kwalitas",
      "Analisa, sistem, kualitas"
    ],
    "answer": 1,
    "explanation": "Bentuk baku yang tepat menurut EYD V dan KBBI adalah 'analisis' (bukan analisa), 'sistem' (bukan sistim), dan 'kualitas' (bukan kwalitas).",
    "source": "EYD Edisi V & KBBI Daring"
  },
  {
    "id": 477,
    "category": "Bahasa Indonesia",
    "difficulty": "sedang",
    "question": "Berdasarkan kaidah EYD V tentang penulisan bilangan, manakah penulisan kalimat yang tepat?",
    "options": [
      "Rapat desa itu dihadiri oleh 3 orang narasumber ahli.",
      "Rapat desa itu dihadiri oleh tiga orang narasumber ahli.",
      "Rapat desa itu dihadiri oleh 3 (tiga) orang narasumber ahli.",
      "Rapat desa itu dihadiri oleh ke-3 orang narasumber ahli."
    ],
    "answer": 1,
    "explanation": "Bilangan dalam teks yang dapat dinyatakan dengan satu atau dua kata ditulis dengan huruf ('tiga orang'), kecuali jika dipakai berurutan seperti dalam perincian naskah dinas formal.",
    "source": "EYD Edisi V Penulisan Bilangan dan Angka"
  },
  {
    "id": 478,
    "category": "Bahasa Indonesia",
    "difficulty": "mudah",
    "question": "Penulisan singkatan resmi nama peraturan perundang-undangan negara yang tepat adalah...",
    "options": [
      "U.U.D. 1945 dan P.E.R.D.E.S.",
      "UUD 1945 dan PERDES",
      "uud 1945 dan perdes",
      "Uud 1945 dan PerDes"
    ],
    "answer": 1,
    "explanation": "Singkatan nama resmi lembaga pemerintahan dan dokumen resmi negara terdiri atas huruf kapital tanpa tanda titik di antaranya (misal: UUD, UU, PP, PERDES).",
    "source": "EYD Edisi V Penulisan Singkatan dan Akronim"
  },
  {
    "id": 479,
    "category": "Bahasa Indonesia",
    "difficulty": "mudah",
    "question": "Cermati kalimat penutup surat dinas berikut: 'Demikian surat permohonan ini, atas perhatian dan bantuannya kami haturkan beribu-ribu terima kasih.' Perbaikan kalimat tersebut agar efektif dan lugas adalah...",
    "options": [
      "Demikian surat ini kami sampaikan, atas perhatian Bapak/Ibu kami haturkan banyak-banyak terima kasih.",
      "Demikian surat permohonan ini disampaikan. Atas perhatian Saudara, kami ucapkan terima kasih.",
      "Demikianlah surat kami sampaikan, kami ucapkan ribuan terima kasih yang mendalam.",
      "Atas perhatiannya kami haturkan banyak terima kasih."
    ],
    "answer": 1,
    "explanation": "Kalimat penutup surat dinas yang efektif harus hemat kata, lugas, dan santun. Bentuk 'kami ucapkan terima kasih' baku dan tidak berlebihan (tanpa 'beribu-ribu' atau 'banyak-banyak').",
    "source": "Pedoman Penulisan Surat Dinas Baku Bahasa Indonesia"
  },
  {
    "id": 480,
    "category": "Bahasa Indonesia",
    "difficulty": "sedang",
    "question": "Penggunaan huruf miring (italics) yang benar dalam naskah surat dinas pemerintahan adalah...",
    "options": [
      "Kepala Desa menjabat secara *ex-officio* sebagai Penasihat BUMDes.",
      "Kepala Desa menjabat secara EX-OFFICIO sebagai Penasihat BUMDes.",
      "Kepala Desa menjabat secara 'ex-officio' sebagai Penasihat BUMDes.",
      "Kepala Desa menjabat secara _ex-officio_ sebagai Penasihat BUMDes."
    ],
    "answer": 0,
    "explanation": "Huruf miring dipakai untuk menuliskan kata atau ungkapan dalam bahasa daerah atau bahasa asing yang belum diserap ke dalam bahasa Indonesia (seperti istilah Latin 'ex-officio').",
    "source": "EYD Edisi V Penggunaan Huruf Miring"
  },
  {
    "id": 481,
    "category": "Bahasa Indonesia",
    "difficulty": "mudah",
    "question": "Manakah penulisan kata depan 'di' dan awalan 'di-' berikut yang seluruhnya tepat?",
    "options": [
      "Surat itu ditanda tangani di balai desa.",
      "Surat itu ditandatangani dibalai desa.",
      "Surat itu ditandatangani di balai desa.",
      "Surat itu di tandatangani di-balai desa."
    ],
    "answer": 2,
    "explanation": "Awalan 'di-' pada kata kerja pasif ditulis serangkai ('ditandatangani'), sedangkan kata depan 'di' yang menunjukkan tempat ditulis terpisah ('di balai desa').",
    "source": "EYD Edisi V Penulisan Kata Depan"
  },
  {
    "id": 482,
    "category": "Bahasa Indonesia",
    "difficulty": "mudah",
    "question": "Pilihlah pasangan kata baku yang tepat sesuai kaidah EYD V!",
    "options": [
      "Standarisasi dan komoditi",
      "Standardisasi dan komoditas",
      "Standarisasi dan komoditas",
      "Standardisasi dan komoditi"
    ],
    "answer": 1,
    "explanation": "Bentuk kata serapan yang baku adalah 'standardisasi' (imbuhan -isasi dari standard) dan 'komoditas' (bukan komoditi).",
    "source": "EYD Edisi V & KBBI Daring"
  },

  # =========================================================================
  # KATEGORI 9: Matematika dan numerik (6 Soal: ID 483-488)
  # =========================================================================
  {
    "id": 483,
    "category": "Matematika dan numerik",
    "difficulty": "mudah",
    "question": "Total pagu Belanja Desa dalam APB Desa adalah Rp1.500.000.000,00. Jika anggaran yang dialokasikan untuk Bidang Pelaksanaan Pembangunan Desa adalah Rp600.000.000,00, berapa persentase anggaran pembangunan tersebut terhadap total belanja desa?",
    "options": [
      "35%",
      "40%",
      "45%",
      "50%"
    ],
    "answer": 1,
    "explanation": "Persentase = (Rp600.000.000,00 / Rp1.500.000.000,00) x 100% = 4/10 x 100% = 40%.",
    "source": "Aritmetika Sosial Persentase Anggaran"
  },
  {
    "id": 484,
    "category": "Matematika dan numerik",
    "difficulty": "sedang",
    "question": "Pemerintah Desa memberikan honorarium narasumber pelatihan aparatur desa sebesar Rp2.000.000,00 kepada seorang narasumber profesional (non-PNS dan ber-NPWP). Jika tarif PPh Pasal 21 adalah 5%, berapakah uang honor bersih yang diterima narasumber tersebut?",
    "options": [
      "Rp1.800.000,00",
      "Rp1.900.000,00",
      "Rp1.950.000,00",
      "Rp1.980.000,00"
    ],
    "answer": 1,
    "explanation": "Potongan PPh 21 = 5% x Rp2.000.000,00 = Rp100.000,00. Honor bersih = Rp2.000.000,00 - Rp100.000,00 = Rp1.900.000,00.",
    "source": "Perhitungan Pajak Penghasilan PPh 21"
  },
  {
    "id": 485,
    "category": "Matematika dan numerik",
    "difficulty": "mudah",
    "question": "Sebidang tanah lapangan olahraga milik desa memiliki luas 1,2 hektar. Berapakah luas tanah tersebut jika dikonversikan ke dalam satuan are?",
    "options": [
      "12 are",
      "120 are",
      "1.200 are",
      "12.000 are"
    ],
    "answer": 1,
    "explanation": "1 hektar (ha) = 100 are (1 are = 100 m²). Maka 1,2 hektar = 1,2 x 100 = 120 are.",
    "source": "Konversi Satuan Ukuran Luas"
  },
  {
    "id": 486,
    "category": "Matematika dan numerik",
    "difficulty": "sedang",
    "question": "Perangkat desa mengantarkan berkas LPPD ke kantor kecamatan berjarak 10 km dengan sepeda motor berkecepatan rata-rata 40 km/jam. Berapa menit waktu yang dibutuhkan untuk tiba di kantor kecamatan?",
    "options": [
      "10 menit",
      "15 menit",
      "20 menit",
      "25 menit"
    ],
    "answer": 1,
    "explanation": "Waktu tempuh = Jarak / Kecepatan = 10 km / 40 km/jam = 0,25 jam. Dikonversi ke menit: 0,25 x 60 menit = 15 menit.",
    "source": "Perhitungan Waktu, Kecepatan, dan Jarak"
  },
  {
    "id": 487,
    "category": "Matematika dan numerik",
    "difficulty": "sedang",
    "question": "Rekening kas desa di bank daerah memiliki saldo rata-rata mengendap sebesar Rp300.000.000,00. Bank memberikan bunga jasa giro bersih 0,3% per bulan setelah dipotong pajak. Berapakah pendapatan jasa giro yang masuk ke kas desa pada bulan tersebut?",
    "options": [
      "Rp600.000,00",
      "Rp900.000,00",
      "Rp1.200.000,00",
      "Rp1.500.000,00"
    ],
    "answer": 1,
    "explanation": "Jasa giro = 0,3% x Rp300.000.000,00 = 0,003 x 300.000.000 = Rp900.000,00.",
    "source": "Aritmetika Keuangan Perbankan"
  },
  {
    "id": 488,
    "category": "Matematika dan numerik",
    "difficulty": "sedang",
    "question": "Program bantuan material bedah rumah (RTLH) desa disalurkan secara bertahap dengan pola barisan aritmetika: Tahap 1 sebesar Rp5.000.000,00; Tahap 2 sebesar Rp7.500.000,00; Tahap 3 sebesar Rp10.000.000,00. Berapakah nilai bantuan yang disalurkan pada Tahap ke-5?",
    "options": [
      "Rp12.500.000,00",
      "Rp15.000.000,00",
      "Rp17.500.000,00",
      "Rp20.000.000,00"
    ],
    "answer": 1,
    "explanation": "Suku pertama (a) = 5.000.000, beda (b) = 2.500.000. Suku ke-5 (U5) = a + (5 - 1)b = 5.000.000 + 4 x 2.500.000 = 5.000.000 + 10.000.000 = Rp15.000.000,00.",
    "source": "Barisan dan Deret Aritmetika"
  },

  # =========================================================================
  # KATEGORI 10: Logika dan penalaran (5 Soal: ID 489-493)
  # =========================================================================
  {
    "id": 489,
    "category": "Logika dan penalaran",
    "difficulty": "sedang",
    "question": "Premis 1: Semua pengelola keuangan desa wajib menandatangani pakta integritas pencegahan korupsi.\nPremis 2: Sebagian staf pembantu umum desa bukan pengelola keuangan desa.\nKesimpulan yang sah adalah...",
    "options": [
      "Semua staf pembantu umum wajib menandatangani pakta integritas",
      "Sebagian staf pembantu umum desa tidak wajib menandatangani pakta integritas pencegahan korupsi pengelola keuangan",
      "Tidak ada staf pembantu umum yang boleh bertugas di kantor desa",
      "Semua pengelola keuangan adalah staf pembantu umum"
    ],
    "answer": 1,
    "explanation": "Silogisme kategorial: Karena sebagian staf bukan pengelola keuangan, maka sebagian staf tersebut tidak terkena kewajiban pakta integritas khusus pengelola keuangan desa.",
    "source": "Silogisme Kategorial Logika Deduktif"
  },
  {
    "id": 490,
    "category": "Logika dan penalaran",
    "difficulty": "sedang",
    "question": "Premis 1: Jika suatu desa berstatus Desa Mandiri dalam Indeks Desa Membangun (IDM), maka desa tersebut berhak menerima alokasi afirmasi Dana Desa.\nPremis 2: Desa Sukamaju berstatus Desa Mandiri dalam IDM.\nKesimpulan yang benar menurut kaidah logika Modus Ponens adalah...",
    "options": [
      "Desa Sukamaju tidak menerima alokasi afirmasi Dana Desa",
      "Desa Sukamaju berhak menerima alokasi afirmasi Dana Desa",
      "Desa Sukamaju harus menurunkan statusnya",
      "Semua desa di kecamatan menerima alokasi afirmasi"
    ],
    "answer": 1,
    "explanation": "Kaidah Modus Ponens: Jika P maka Q. P terjadi. Maka kesimpulannya Q (Desa Sukamaju berhak menerima alokasi afirmasi Dana Desa).",
    "source": "Logika Matematika Modus Ponens"
  },
  {
    "id": 491,
    "category": "Logika dan penalaran",
    "difficulty": "sedang",
    "question": "Premis 1: Jika dokumen RKP Desa disepakati tepat waktu sebelum akhir September, maka APB Desa dapat ditetapkan sebelum 31 Desember.\nPremis 2: Jika APB Desa dapat ditetapkan sebelum 31 Desember, maka pencairan Siltap perangkat desa awal tahun tidak mengalami penundaan.\nKesimpulan yang sah menurut silogisme hipotetis adalah...",
    "options": [
      "Jika dokumen RKP Desa disepakati tepat waktu sebelum akhir September, maka pencairan Siltap perangkat desa awal tahun tidak mengalami penundaan",
      "Pencairan Siltap pasti tertunda meskipun RKP Desa tepat waktu",
      "APB Desa tidak perlu ditetapkan sebelum 31 Desember",
      "Siltap perangkat desa ditiadakan jika RKP Desa terlambat"
    ],
    "answer": 0,
    "explanation": "Silogisme Hipotetis Rantai: Jika P maka Q. Jika Q maka R. Maka kesimpulannya Jika P maka R.",
    "source": "Silogisme Hipotetis Logika Proposisional"
  },
  {
    "id": 492,
    "category": "Logika dan penalaran",
    "difficulty": "sulit",
    "question": "Dalam rapat desa, 5 orang pejabat duduk berderet menghadap warga: Kepala Desa, Sekdes, Ketua BPD, Camat, dan Kasun. Aturan duduk:\n1. Camat duduk tepat di tengah (kursi nomor 3).\n2. Kepala Desa duduk di sebelah kanan Camat.\n3. Kasun duduk di ujung paling kiri (kursi nomor 1).\n4. Sekdes duduk di antara Kasun dan Camat.\nSiapakah yang duduk di kursi paling kanan (kursi nomor 5)?",
    "options": [
      "Ketua BPD",
      "Kepala Desa",
      "Sekdes",
      "Kasun"
    ],
    "answer": 0,
    "explanation": "Urutan kursi 1 sampai 5 dari kiri ke kanan:\nKursi 1: Kasun.\nKursi 3: Camat.\nKursi 2: Sekdes (di antara Kasun dan Camat).\nKursi 4: Kepala Desa (sebelah kanan Camat).\nMaka kursi nomor 5 diisi oleh Ketua BPD.",
    "source": "Penalaran Posisi Ruang dan Urutan Logis"
  },
  {
    "id": 493,
    "category": "Logika dan penalaran",
    "difficulty": "sedang",
    "question": "Dari 80 peternak penerima bibit ternak di desa, 50 orang memelihara sapi, 40 orang memelihara kambing, dan 15 orang memelihara sapi sekaligus kambing. Berapakah jumlah peternak yang tidak memelihara sapi maupun kambing?",
    "options": [
      "5 orang",
      "10 orang",
      "15 orang",
      "20 orang"
    ],
    "answer": 0,
    "explanation": "Total peternak yang memelihara sapi atau kambing = 50 + 40 - 15 = 75 orang. Maka yang tidak memelihara keduanya = 80 - 75 = 5 orang.",
    "source": "Diagram Venn Teori Himpunan"
  },

  # =========================================================================
  # KATEGORI 11: Pengetahuan umum (4 Soal: ID 494-497)
  # =========================================================================
  {
    "id": 494,
    "category": "Pengetahuan umum",
    "difficulty": "mudah",
    "question": "Kabupaten Tuban dikenal luas dengan sebutan atau julukan sebagai...",
    "options": [
      "Bumi Blambangan",
      "Bumi Minak Jinggo",
      "Bumi Wali",
      "Bumi Arema"
    ],
    "answer": 2,
    "explanation": "Kabupaten Tuban dijuluki sebagai 'Bumi Wali' karena banyaknya makam para wali dan ulama penyebar agama Islam terkemuka di tanah Jawa yang berada di wilayah Tuban.",
    "source": "Profil Identitas Daerah Kabupaten Tuban"
  },
  {
    "id": 495,
    "category": "Pengetahuan umum",
    "difficulty": "mudah",
    "question": "Makam Syekh Maulana Ibrahim Asmoro Qondi, ayahanda dari Sunan Ampel yang menjadi salah satu destinasi wisata religi utama di Tuban, terletak di...",
    "options": [
      "Desa Gesikharjo, Kecamatan Palang, Kabupaten Tuban",
      "Kecamatan Jatirogo",
      "Kecamatan Senori",
      "Kecamatan Montong"
    ],
    "answer": 0,
    "explanation": "Makam Syekh Maulana Ibrahim Asmoro Qondi terletak di Desa Gesikharjo, Kecamatan Palang, Kabupaten Tuban di tepi jalur Pantura.",
    "source": "Wisata Budaya dan Sejarah Religi Tuban"
  },
  {
    "id": 496,
    "category": "Pengetahuan umum",
    "difficulty": "mudah",
    "question": "Lembaga kekuasaan kehakiman di Indonesia yang memiliki wewenang menguji undang-undang terhadap Undang-Undang Dasar NRI 1945 (judicial review) adalah...",
    "options": [
      "Mahkamah Agung",
      "Mahkamah Konstitusi",
      "Komisi Yudisial",
      "Kejaksaan Agung"
    ],
    "answer": 1,
    "explanation": "Mahkamah Konstitusi (MK) berwenang mengadili pada tingkat pertama dan terakhir yang putusannya bersifat final untuk menguji undang-undang terhadap UUD NRI 1945.",
    "source": "UUD NRI 1945 Pasal 24C ayat (1)"
  },
  {
    "id": 497,
    "category": "Pengetahuan umum",
    "difficulty": "sedang",
    "question": "Berdasarkan Undang-Undang No. 24 Tahun 2009, rasio resmi perbandingan lebar dan panjang Bendera Sang Saka Merah Putih adalah...",
    "options": [
      "Lebar 1 bagian berbanding panjang 2 bagian (1 : 2)",
      "Lebar 2 bagian berbanding panjang 3 bagian (2 : 3)",
      "Lebar 3 bagian berbanding panjang 4 bagian (3 : 4)",
      "Lebar 1 bagian berbanding panjang 1 bagian (1 : 1)"
    ],
    "answer": 1,
    "explanation": "UU No. 24 Tahun 2009 Pasal 4 ayat (1) menyatakan Bendera Negara Sang Merah Putih berbentuk empat persegi panjang dengan ukuran lebar 2/3 (dua pertiga) dari panjang (perbandingan lebar : panjang = 2 : 3).",
    "source": "UU No. 24 Tahun 2009 Pasal 4 ayat (1)"
  },

  # =========================================================================
  # KATEGORI 12: Komputer dasar dan pelayanan publik (3 Soal: ID 498-500)
  # =========================================================================
  {
    "id": 498,
    "category": "Komputer dasar dan pelayanan publik",
    "difficulty": "sedang",
    "question": "Fitur pada aplikasi Microsoft Excel yang digunakan untuk mengunci baris judul kolom agar tetap terlihat saat lembar kerja digulirkan (scroll) jauh ke bawah adalah...",
    "options": [
      "Wrap Text",
      "Freeze Panes",
      "Merge & Center",
      "Conditional Formatting"
    ],
    "answer": 1,
    "explanation": "Freeze Panes pada tab View berfungsi membekukan (freeze) baris atau kolom tertentu sehingga tetap terlihat saat lembar kerja di-scroll.",
    "source": "Panduan Aplikasi Microsoft Excel Kearsipan"
  },
  {
    "id": 499,
    "category": "Komputer dasar dan pelayanan publik",
    "difficulty": "mudah",
    "question": "Rumus logika IF pada Microsoft Excel yang benar untuk memberikan keterangan 'LULUS' jika nilai seleksi di sel C5 sekurang-kurangnya 75, dan 'TIDAK LULUS' jika kurang dari 75 adalah...",
    "options": [
      "=IF(C5>=75, 'LULUS', 'TIDAK LULUS')",
      "=IF(C5>=75; \"LULUS\"; \"TIDAK LULUS\")",
      "=CHECK(C5=75, LULUS, TIDAK LULUS)",
      "=SUMIF(C5>=75, LULUS)"
    ],
    "answer": 1,
    "explanation": "Sintaks formula IF di Excel: =IF(logical_test; value_if_true; value_if_false). String teks diapit tanda petik dua ganda (\"LULUS\"; \"TIDAK LULUS\").",
    "source": "Dasar Formula Microsoft Excel"
  },
  {
    "id": 500,
    "category": "Komputer dasar dan pelayanan publik",
    "difficulty": "mudah",
    "question": "Berdasarkan Undang-Undang No. 25 Tahun 2009 tentang Pelayanan Publik, prinsip penyelenggaraan pelayanan di kantor desa yang melarang diskriminasi berdasarkan suku, ras, agama, golongan, status gender, atau latar belakang politik disebut...",
    "options": [
      "Asas Partisipatif",
      "Asas Non-Diskriminatif",
      "Asas Keterbukaan",
      "Asas Akuntabilitas"
    ],
    "answer": 1,
    "explanation": "UU No. 25 Tahun 2009 Pasal 4 huruf g menegaskan Asas Tidak Diskriminatif, yaitu perlakuan yang tidak membedakan jenis kelamin, suku, agama, ras, status sosial, maupun pandangan politik dalam pelayanan publik.",
    "source": "UU No. 25 Tahun 2009 tentang Pelayanan Publik Pasal 4 huruf g"
  }
]
