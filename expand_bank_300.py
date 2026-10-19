# -*- coding: utf-8 -*-
"""
Database Tambahan Soal 201 s.d. 300 untuk Simulasi CBT Perangkat Desa
Memperluas master bank soal dari 200 menjadi 300 butir soal.
Proporsional 3x dari kuota 12 kategori ujian resmi:
- Kat 1 (Pemerintahan desa): 20 soal (total pool: 60)
- Kat 2 (Perundang-undangan): 12 soal (total pool: 36)
- Kat 3 (Pancasila & Wawasan Kebangsaan): 10 soal (total pool: 30)
- Kat 4 (Administrasi & Surat): 10 soal (total pool: 30)
- Kat 5 (Keuangan & Aset Desa): 10 soal (total pool: 30)
- Kat 6 (Pembangunan & Pemberdayaan): 8 soal (total pool: 24)
- Kat 7 (BPD & Musyawarah): 5 soal (total pool: 15)
- Kat 8 (Bahasa Indonesia): 7 soal (total pool: 21)
- Kat 9 (Matematika & Numerik): 6 soal (total pool: 18)
- Kat 10 (Logika & Penalaran): 5 soal (total pool: 15)
- Kat 11 (Pengetahuan Umum): 4 soal (total pool: 12)
- Kat 12 (Komputer & Pelayanan): 3 soal (total pool: 9)
TOTAL: 100 soal baru (ID 201 - 300).
"""

QUESTIONS_201_300 = [
  # =========================================================================
  # KATEGORI 1: Pemerintahan desa, struktur organisasi, tugas dan fungsi (20 Soal: ID 201-220)
  # =========================================================================
  {
    "id": 201,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Berdasarkan Permendagri No. 84 Tahun 2015, dalam hal terjadi kekosongan jabatan Sekretaris Desa, Kepala Desa dapat menunjuk pelaksana tugas (Plt.) yang berasal dari...",
    "options": [
      "Anggota BPD yang memiliki kualifikasi administrasi",
      "Salah satu Kepala Urusan (Kaur) yang ada di sekretariat desa",
      "Ketua RT atau RW setempat yang ditunjuk",
      "Tokoh masyarakat desa yang disetujui camat"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 84 Tahun 2015 Pasal 15 mengatur bahwa kekosongan jabatan Sekretaris Desa dapat diisi oleh pelaksana tugas (Plt.) yang ditunjuk oleh Kepala Desa dari salah satu Kepala Urusan (Kaur).",
    "source": "Permendagri No. 84 Tahun 2015 Pasal 15"
  },
  {
    "id": 202,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "mudah",
    "question": "Berapakah batas usia minimal dan maksimal bagi calon Perangkat Desa pada saat mendaftar seleksi di Kabupaten Tuban?",
    "options": [
      "18 tahun sampai dengan 35 tahun",
      "20 tahun sampai dengan 42 tahun",
      "21 tahun sampai dengan 45 tahun",
      "25 tahun sampai dengan 50 tahun",
    ],
    "answer": 1,
    "explanation": "Berdasarkan UU No. 6/2014 Pasal 50 dan Perda Kab. Tuban No. 2/2016 jo. No. 16/2021, syarat usia pendaftaran calon perangkat desa adalah genap berusia 20 tahun dan paling tinggi 42 tahun pada saat mendaftar.",
    "source": "UU No. 6/2014 Pasal 50 & Perda Kab. Tuban No. 2/2016 jo. No. 16/2021"
  },
  {
    "id": 203,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Apabila Kepala Desa diberhentikan sementara karena menjadi terdakwa tindak pidana, siapa yang menjalankan tugas dan kewajiban Kepala Desa sehari-hari?",
    "options": [
      "Ketua BPD",
      "Sekretaris Desa",
      "Camat setempat",
      "Kasi Pemerintahan"
    ],
    "answer": 1,
    "explanation": "Berdasarkan UU No. 6 Tahun 2014 Pasal 45, jika Kepala Desa diberhentikan sementara, Sekretaris Desa melaksanakan tugas dan kewajiban Kepala Desa sampai dengan adanya putusan pengadilan yang berkekuatan hukum tetap.",
    "source": "UU No. 6 Tahun 2014 Pasal 45"
  },
  {
    "id": 204,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Perangkat Desa berhak mendapatkan cuti melahirkan bagi perangkat desa wanita. Berapa lama jangka waktu cuti melahirkan tersebut?",
    "options": [
      "1 bulan sebelum dan 1 bulan sesudah melahirkan",
      "1 bulan sebelum dan 2 bulan sesudah melahirkan",
      "3 bulan sesudah melahirkan secara penuh",
      "40 hari kalender"
    ],
    "answer": 1,
    "explanation": "Sesuai ketentuan ketenagakerjaan dan kepegawaian aparatur desa, cuti bersalin/melahirkan diberikan selama 1 bulan sebelum dan 2 bulan sesudah persalinan (total 3 bulan).",
    "source": "Permendagri No. 67/2017 & Perda Kab. Tuban No. 2/2016"
  },
  {
    "id": 205,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sulit",
    "question": "Sebelum memberhentikan Perangkat Desa karena pelanggaran larangan, Kepala Desa wajib memberikan surat peringatan (SP) secara bertahap, yaitu...",
    "options": [
      "Peringatan lisan 3 kali baru diberhentikan",
      "Peringatan tertulis I, II, dan III masing-masing tenggang waktu 30 hari kalender",
      "Peringatan tertulis I, II, dan III dengan tenggang waktu masing-masing 14 hari kerja",
      "Pemberitahuan tertulis sekali langsung kepada Camat"
    ],
    "answer": 1,
    "explanation": "Sesuai Permendagri No. 67/2017 dan regulasi teknis di Kabupaten Tuban, penjatuhan sanksi administrasi dilakukan melalui peringatan tertulis kesatu, kedua, dan ketiga dengan tenggang waktu masing-masing 30 hari kalender sebelum rekomendasi pemberhentian diajukan ke Camat.",
    "source": "Permendagri No. 67 Tahun 2017 Pasal 9"
  },
  {
    "id": 206,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "mudah",
    "question": "Kepala Dusun (Kasun) di wilayah Kabupaten Tuban juga sering dikenal dengan sebutan lokal tradisional...",
    "options": [
      "Carik",
      "Kamituwo",
      "Bayan",
      "Modin"
    ],
    "answer": 1,
    "explanation": "Di Kabupaten Tuban dan wilayah karesidenan Bojonegoro, Kepala Dusun secara tradisional dan kultural akrab disebut sebagai 'Kamituwo' (Carik = Sekdes, Modin = Kasi Pelayanan/Urusan Agama, Bayan = Kebayan/Keamanan).",
    "source": "Perda Kab. Tuban No. 2/2016 & Kearifan Lokal Pemerintahan Desa Tuban"
  },
  {
    "id": 207,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Perangkat Desa dilarang merangkap jabatan tertentu. Manakah rangkap jabatan yang secara tegas dilarang oleh UU Desa?",
    "options": [
      "Menjadi ketua panitia peringatan HUT RI di desa",
      "Menjadi pengurus RT atau RW di lingkungan tempat tinggalnya",
      "Menjadi anggota Dewan Perwakilan Rakyat (DPR/DPRD) atau pengurus partai politik",
      "Menjadi pengurus perkumpulan kelompok tani"
    ],
    "answer": 2,
    "explanation": "UU No. 6 Tahun 2014 Pasal 51 huruf f dan g menegaskan larangan perangkat desa menjadi pengurus partai politik dan menjadi anggota legislatif (DPR/DPD/DPRD).",
    "source": "UU No. 6 Tahun 2014 Pasal 51"
  },
  {
    "id": 208,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Berdasarkan UU No. 3 Tahun 2024, masa jabatan Kepala Desa yang terpilih setelah berlakunya undang-undang ini adalah...",
    "options": [
      "6 tahun dan dapat dipilih kembali untuk 3 periode",
      "8 tahun dan dapat dipilih kembali untuk 2 periode",
      "9 tahun dan hanya 1 periode",
      "5 tahun dan dapat dipilih kembali untuk 2 periode"
    ],
    "answer": 1,
    "explanation": "UU No. 3 Tahun 2024 Pasal 39 mengubah masa jabatan Kepala Desa menjadi 8 (delapan) tahun dan dapat dipilih paling banyak 2 (dua) kali masa jabatan secara berturut-turut atau tidak berturut-turut.",
    "source": "UU No. 3 Tahun 2024 Pasal 39"
  },
  {
    "id": 209,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Penjabat (Pj.) Kepala Desa yang diangkat untuk mengisi kekosongan jabatan Kepala Desa karena diberhentikan atau habis masa jabatannya harus berasal dari...",
    "options": [
      "Tokoh masyarakat desa terpilih",
      "Pegawai Negeri Sipil (PNS) dari pemerintah daerah kabupaten/kota",
      "Perangkat desa yang paling senior",
      "Anggota BPD bidang pemerintahan"
    ],
    "answer": 1,
    "explanation": "UU No. 6 Tahun 2014 Pasal 46 ayat (2) menyatakan bahwa Penjabat Kepala Desa diangkat oleh Bupati/Walikota dari Pegawai Negeri Sipil (PNS) di lingkungan Pemerintah Daerah.",
    "source": "UU No. 6 Tahun 2014 Pasal 46 ayat (2)"
  },
  {
    "id": 210,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "mudah",
    "question": "Pemberhentian Perangkat Desa karena telah mencapai batas usia 60 tahun tergolong ke dalam jenis...",
    "options": [
      "Pemberhentian sementara",
      "Pemberhentian tidak dengan hormat",
      "Pemberhentian dengan hormat",
      "Pemberhentian atas usul BPD"
    ],
    "answer": 2,
    "explanation": "Mencapai usia genap 60 tahun merupakan salah satu syarat pemberhentian perangkat desa dengan hormat karena purnatugas (pensiun).",
    "source": "UU No. 6/2014 Pasal 53 & Permendagri No. 67/2017"
  },
  {
    "id": 211,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Siapakah yang melantik dan mengambil sumpah jabatan Perangkat Desa yang baru lulus seleksi pengangkatan?",
    "options": [
      "Bupati Tuban",
      "Camat atas nama Bupati",
      "Kepala Desa",
      "Ketua BPD"
    ],
    "answer": 2,
    "explanation": "Berdasarkan Permendagri No. 67 Tahun 2017 Pasal 5 ayat (5), Kepala Desa melantik Perangkat Desa setelah mendapatkan rekomendasi tertulis dari Camat.",
    "source": "Permendagri No. 67 Tahun 2017 Pasal 5 ayat (5)"
  },
  {
    "id": 212,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Kepala Urusan Tata Usaha dan Umum berkedudukan di bawah naungan...",
    "options": [
      "Kepala Seksi Pemerintahan",
      "Sekretaris Desa",
      "BPD bidang kelembagaan",
      "Camat langsung"
    ],
    "answer": 1,
    "explanation": "Seluruh Kepala Urusan (Kaur) merupakan unsur staf sekretariat desa yang berkedudukan di bawah dan bertanggung jawab langsung kepada Sekretaris Desa.",
    "source": "Permendagri No. 84 Tahun 2015 Pasal 8"
  },
  {
    "id": 213,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sulit",
    "question": "Dalam Peraturan Bupati Tuban, materi ujian tulis seleksi pengangkatan perangkat desa meliputi kelompok materi...",
    "options": [
      "Hanya tes psikologi dan wawancara kades",
      "Materi ujian tulis, tes praktik komputer, dan pembobotan dedikasi/pengabdian",
      "Hanya tes kesehatan dan bebas narkoba",
      "Ujian lisan bahasa Jawa dan hafalan UU Desa"
    ],
    "answer": 1,
    "explanation": "Berdasarkan Perbup Tuban No. 11/2022, tahapan seleksi perangkat desa mencakup ujian tulis objektif, ujian praktik komputer, serta verifikasi kelengkapan dan pembobotan sertifikat/pengabdian.",
    "source": "Perbup Tuban No. 11 Tahun 2022"
  },
  {
    "id": 214,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Selain penghasilan tetap (siltap), Perangkat Desa di Kabupaten Tuban berhak memperoleh tunjangan kesehatan melalui program...",
    "options": [
      "Askes PNS Pusat",
      "BPJS Kesehatan dan BPJS Ketenagakerjaan",
      "Asuransi swasta yang dipilih sendiri",
      "Bantuan sosial tunai desa"
    ],
    "answer": 1,
    "explanation": "Perangkat Desa diikutsertakan dalam program jaminan sosial pemerintah melalui BPJS Kesehatan dan BPJS Ketenagakerjaan (JKK, JKM, JHT) yang premi pemberi kerjanya didukung alokasi APB Desa.",
    "source": "Permendagri No. 20/2018 & Perda Kab. Tuban No. 2/2016"
  },
  {
    "id": 215,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Mekanisme pengisian jabatan perangkat desa yang kosong melalui mutasi antar jabatan di lingkungan pemerintah desa dilakukan dengan syarat...",
    "options": [
      "Ditetapkan sepihak oleh Kepala Desa tanpa konsultasi",
      "Melalui konsultasi tertulis dan mendapatkan rekomendasi dari Camat",
      "Harus melalui ujian seleksi terbuka umum kembali",
      "Disetujui oleh minimal 2/3 warga desa melalui voting"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 67/2017 jo. Permendagri No. 84/2015 mengatur bahwa mutasi jabatan antar perangkat desa dapat dilakukan oleh Kepala Desa setelah dikonsultasikan dan memperoleh rekomendasi tertulis dari Camat.",
    "source": "Permendagri No. 67 Tahun 2017 Pasal 7"
  },
  {
    "id": 216,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "mudah",
    "question": "Syarat minimal pendidikan formal bagi calon perangkat desa menurut UU Desa dan Perda Kabupaten Tuban adalah...",
    "options": [
      "Sekolah Dasar (SD) atau sederajat",
      "Sekolah Menengah Pertama (SMP) atau sederajat",
      "Sekolah Menengah Atas (SMA) atau sederajat",
      "Diploma Tiga (D3) atau Sarjana (S1)"
    ],
    "answer": 2,
    "explanation": "UU No. 6 Tahun 2014 Pasal 50 ayat (1) huruf a mensyaratkan calon perangkat desa berpendidikan paling rendah sekolah menengah umum atau yang sederajat.",
    "source": "UU No. 6 Tahun 2014 Pasal 50"
  },
  {
    "id": 217,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Fungsi membantu Kepala Desa dalam melaksanakan urusan keagamaan, nikah/talak/rujuk (pembantu), dan sosial kemasyarakatan di tingkat desa diemban oleh...",
    "options": [
      "Kasi Pemerintahan",
      "Kasi Kesejahteraan",
      "Kasi Pelayanan",
      "Kaur Tata Usaha dan Umum"
    ],
    "answer": 2,
    "explanation": "Permendagri No. 84 Tahun 2015 menetapkan Kasi Pelayanan memiliki fungsi melaksanakan penyuluhan, motivasi, dan pelayanan sosial kemasyarakatan, keagamaan, dan ketenagakerjaan.",
    "source": "Permendagri No. 84 Tahun 2015 Pasal 13"
  },
  {
    "id": 218,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Kaur Keuangan dalam struktur Pengelolaan Keuangan Desa (PPKD) menjalankan fungsi definitif sebagai...",
    "options": [
      "Koordinator PPKD",
      "Pelaksana Kegiatan Anggaran (PKA)",
      "Bendahara Desa",
      "Auditor Internal Desa"
    ],
    "answer": 2,
    "explanation": "Permendagri No. 20 Tahun 2018 Pasal 7 ayat (1) menegaskan bahwa Kaur Keuangan melaksanakan fungsi kebendaharaan (Bendahara Desa).",
    "source": "Permendagri No. 20 Tahun 2018 Pasal 7"
  },
  {
    "id": 219,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sulit",
    "question": "Berapakah jumlah hari kerja efektif bagi kantor desa dalam menjalankan pelayanan masyarakat di lingkungan Pemerintah Kabupaten Tuban?",
    "options": [
      "4 hari kerja per minggu",
      "5 hari kerja per minggu (Senin sampai Jumat)",
      "6 hari kerja per minggu (Senin sampai Sabtu)",
      "7 hari kerja tanpa libur"
    ],
    "answer": 1,
    "explanation": "Berdasarkan regulasi jam kerja aparatur pemerintahan di Kabupaten Tuban, pelayanan kedinasan kantor desa mengikuti ketentuan 5 hari kerja (Senin s.d. Jumat) dengan jam pelayanan resmi yang ditentukan bupati.",
    "source": "Perbup Tuban tentang Hari dan Jam Kerja Aparatur Desa"
  },
  {
    "id": 220,
    "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
    "difficulty": "sedang",
    "question": "Pemberhentian sementara perangkat desa dicabut dan direhabilitasi nama baiknya oleh Kepala Desa apabila...",
    "options": [
      "Masyarakat dusun berdemonstrasi menuntut pemulihan",
      "Pengadilan memutus bebas atau tidak terbukti bersalah dan putusan telah inkracht",
      "Telah lewat waktu 1 tahun sejak penonaktifan",
      "Membayar ganti rugi kepada kas desa"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 67 Tahun 2017 Pasal 8 ayat (3) menegaskan bahwa perangkat desa yang diberhentikan sementara setelah diputus bebas oleh pengadilan yang berkekuatan hukum tetap, harus direhabilitasi dan diaktifkan kembali.",
    "source": "Permendagri No. 67 Tahun 2017 Pasal 8"
  },

  # =========================================================================
  # KATEGORI 2: Peraturan perundang-undangan dan tata kelola (12 Soal: ID 221-232)
  # =========================================================================
  {
    "id": 221,
    "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
    "difficulty": "sedang",
    "question": "Berapa lama jangka waktu evaluasi Rancangan Peraturan Desa tentang APB Desa oleh Bupati/Camat sebelum ditetapkan menjadi Perdes?",
    "options": [
      "Paling lama 7 hari kerja",
      "Paling lama 20 hari kerja",
      "Paling lama 30 hari kalender",
      "Paling lama 60 hari kalender"
    ],
    "answer": 1,
    "explanation": "Berdasarkan Permendagri No. 20 Tahun 2018 Pasal 38 ayat (2), bupati/walikota melakukan evaluasi rancangan Perdes APB Desa paling lama 20 (dua puluh) hari kerja sejak diterima.",
    "source": "Permendagri No. 20 Tahun 2018 Pasal 38"
  },
  {
    "id": 222,
    "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
    "difficulty": "mudah",
    "question": "Peraturan Desa yang telah diundangkan wajib dicatat dan dimuat dalam media resmi perundangan desa yang disebut...",
    "options": [
      "Berita Desa",
      "Lembaran Desa",
      "Papan Pengumuman Desa",
      "Jurnal Desa"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 111 Tahun 2014 Pasal 18 mengatur bahwa Peraturan Desa diundangkan dalam Lembaran Desa, sedangkan Peraturan Kepala Desa (Perkades) diundangkan dalam Berita Desa.",
    "source": "Permendagri No. 111 Tahun 2014 Pasal 18"
  },
  {
    "id": 223,
    "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
    "difficulty": "sedang",
    "question": "Siapakah pejabat yang berwenang mengundangkan Peraturan Desa dan Peraturan Kepala Desa?",
    "options": [
      "Kepala Desa",
      "Ketua BPD",
      "Sekretaris Desa",
      "Camat"
    ],
    "answer": 2,
    "explanation": "Berdasarkan Permendagri No. 111 Tahun 2014 Pasal 19, pengundangan Peraturan Desa dalam Lembaran Desa dan Peraturan Kepala Desa dalam Berita Desa dilakukan oleh Sekretaris Desa.",
    "source": "Permendagri No. 111 Tahun 2014 Pasal 19"
  },
  {
    "id": 224,
    "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
    "difficulty": "sulit",
    "question": "Jika hasil evaluasi bupati terhadap Rancangan Perdes APB Desa menyatakan tidak sesuai peraturan perundang-undangan, Kepala Desa bersama BPD wajib memperbaikinya dalam waktu...",
    "options": [
      "Paling lambat 7 hari kerja sejak diterimanya hasil evaluasi",
      "Paling lambat 14 hari kerja",
      "Paling lambat 30 hari kalender",
      "Paling lambat akhir tahun anggaran berjalan"
    ],
    "answer": 0,
    "explanation": "Permendagri No. 20 Tahun 2018 Pasal 39 ayat (1) menyatakan Kepala Desa bersama BPD melakukan penyempurnaan rancangan Perdes APB Desa paling lama 7 (tujuh) hari kerja sejak diterimanya hasil evaluasi.",
    "source": "Permendagri No. 20 Tahun 2018 Pasal 39"
  },
  {
    "id": 225,
    "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
    "difficulty": "sedang",
    "question": "Asas penyelenggaraan pemerintahan desa yang menjadi landasan keteraturan, keserasian, dan keseimbangan dalam pengendalian tata kelola desa disebut asas...",
    "options": [
      "Asas Tertib Penyelenggaraan Pemerintahan",
      "Asas Sentralisasi Kekuasaan",
      "Asas Diskresi Mutlak Kepala Desa",
      "Asas Kepentingan Golongan"
    ],
    "answer": 0,
    "explanation": "Berdasarkan penjelasan Pasal 24 huruf b UU No. 6 Tahun 2014, Asas Tertib Penyelenggaraan Pemerintahan adalah asas yang menjadi landasan keteraturan, keserasian, dan keseimbangan dalam pengendalian penyelenggaraan pemerintahan desa.",
    "source": "UU No. 6 Tahun 2014 Pasal 24 huruf b"
  },
  {
    "id": 226,
    "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
    "difficulty": "sedang",
    "question": "Peraturan perundang-undangan manakah yang membatalkan Peraturan Desa apabila Perdes tersebut bertentangan dengan kepentingan umum atau peraturan yang lebih tinggi?",
    "options": [
      "Keputusan Kepala Desa",
      "Surat Edaran Camat",
      "Keputusan Bupati/Walikota",
      "Pernyataan Sikap BPD"
    ],
    "answer": 2,
    "explanation": "Sesuai UU No. 6 Tahun 2014 dan Permendagri No. 111 Tahun 2014 Pasal 24, pembatalan Peraturan Desa ditetapkan dengan Keputusan Bupati/Walikota.",
    "source": "Permendagri No. 111 Tahun 2014 Pasal 24"
  },
  {
    "id": 227,
    "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
    "difficulty": "mudah",
    "question": "Produk hukum Kepala Desa yang bersifat penetapan konkret, individual, dan final disebut...",
    "options": [
      "Peraturan Desa",
      "Peraturan Kepala Desa",
      "Keputusan Kepala Desa",
      "Instruksi Kepala Desa"
    ],
    "answer": 2,
    "explanation": "Keputusan Kepala Desa (SK Kades) memuat kebijakan yang bersifat penetapan (beschikking) konkret, individual, dan final.",
    "source": "Permendagri No. 111 Tahun 2014 Pasal 15"
  },
  {
    "id": 228,
    "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
    "difficulty": "sedang",
    "question": "Rancangan Peraturan Desa tentang APB Desa, Pungutan Desa, Tata Ruang, dan RKP Desa wajib dikonsultasikan kepada masyarakat desa melalui forum...",
    "options": [
      "Rapat koordinasi mingguan perangkat desa",
      "Musyawarah Desa (Musdes)",
      "Pemberitahuan lewat pengeras suara masjid",
      "Pemberitahuan melalui surat dinas camat"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 111/2014 dan UU 6/2014 Pasal 54 mewajibkan hal-hal strategis dan pembebanan masyarakat dibahas dan disepakati dalam forum Musyawarah Desa.",
    "source": "Permendagri No. 111 Tahun 2014 Pasal 7"
  },
  {
    "id": 229,
    "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
    "difficulty": "sedang",
    "question": "Berdasarkan UU No. 12 Tahun 2011, hierarki perundang-undangan yang tepat dari yang tertinggi ke terendah adalah...",
    "options": [
      "UUD 1945 -> UU/Perppu -> PP -> Perpres -> Perda Provinsi -> Perda Kab/Kota",
      "UUD 1945 -> PP -> UU -> Perpres -> Perda Kab/Kota -> Perdes",
      "UUD 1945 -> Tap MPR -> Perda Provinsi -> UU -> PP -> Perpres",
      "UUD 1945 -> UU -> Perda Provinsi -> PP -> Perpres"
    ],
    "answer": 0,
    "explanation": "Pasal 7 UU 12/2011: UUD 1945, Ketetapan MPR, UU/Perppu, PP, Perpres, Perda Provinsi, Perda Kabupaten/Kota.",
    "source": "UU No. 12 Tahun 2011 Pasal 7"
  },
  {
    "id": 230,
    "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
    "difficulty": "sedang",
    "question": "Apakah Peraturan Desa (Perdes) boleh mengatur sanksi pidana kurungan bagi warga yang melanggar?",
    "options": [
      "Boleh asalkan kurungan paling lama 3 bulan",
      "Boleh apabila disetujui secara bulat oleh BPD",
      "Tidak boleh, karena sanksi pidana hanya dapat diatur oleh Undang-Undang dan Peraturan Daerah",
      "Boleh khusus untuk perkara pencurian hasil pertanian"
    ],
    "answer": 2,
    "explanation": "UU No. 12 Tahun 2011 Pasal 15 menegaskan materi muatan sanksi pidana hanya dapat dimuat dalam Undang-Undang, Peraturan Daerah Provinsi, atau Peraturan Daerah Kabupaten/Kota. Perdes tidak memiliki wewenang memuat sanksi pidana kurungan.",
    "source": "UU No. 12 Tahun 2011 Pasal 15"
  },
  {
    "id": 231,
    "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
    "difficulty": "sedang",
    "question": "Bupati dapat mendelegasikan wewenang evaluasi Rancangan Peraturan Desa tentang APB Desa kepada...",
    "options": [
      "Kepala Inspektorat Daerah",
      "Camat di wilayah kecamatan bersangkutan",
      "Kepala Dinas PMD Kabupaten",
      "Sekretaris Daerah langsung"
    ],
    "answer": 1,
    "explanation": "Berdasarkan Permendagri No. 20 Tahun 2018 Pasal 38 ayat (1), bupati/walikota dapat melimpahkan wewenang evaluasi rancangan Peraturan Desa tentang APB Desa kepada Camat.",
    "source": "Permendagri No. 20 Tahun 2018 Pasal 38 ayat (1)"
  },
  {
    "id": 232,
    "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
    "difficulty": "mudah",
    "question": "Siapakah yang menandatangani Peraturan Desa (Perdes) sehingga resmi menjadi payung hukum desa?",
    "options": [
      "Ketua BPD bersama Sekretaris Desa",
      "Kepala Desa",
      "Camat atas nama Bupati",
      "Kepala Urusan Tata Usaha dan Umum"
    ],
    "answer": 1,
    "explanation": "Peraturan Desa ditetapkan dan ditandatangani oleh Kepala Desa setelah mendapat persetujuan bersama dengan BPD.",
    "source": "Permendagri No. 111 Tahun 2014 Pasal 17"
  },

  # =========================================================================
  # KATEGORI 3: Pancasila, UUD 1945, dan wawasan kebangsaan (10 Soal: ID 233-242)
  # =========================================================================
  {
    "id": 233,
    "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
    "difficulty": "mudah",
    "question": "Kegiatan musyawarah mufakat di desa dalam menentukan alokasi pembangunan jalan pertanian merupakan perwujudan pengamalan Pancasila sila ke...",
    "options": [
      "Sila Pertama",
      "Sila Kedua",
      "Sila Ketiga",
      "Sila Keempat"
    ],
    "answer": 3,
    "explanation": "Musyawarah mufakat untuk mencapai mufakat dalam semangat kekeluargaan merupakan implementasi Sila Keempat: Kerakyatan yang dipimpin oleh hikmat kebijaksanaan dalam permusyawaratan/perwakilan.",
    "source": "Ketetapan MPR No. I/MPR/2003 tentang Butir Pancasila"
  },
  {
    "id": 234,
    "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
    "difficulty": "sedang",
    "question": "Pasal 18B ayat (2) UUD NRI Tahun 1945 menegaskan pengakuan negara terhadap...",
    "options": [
      "Pemerintah daerah otonom seluas-luasnya",
      "Kesatuan-kesatuan masyarakat hukum adat beserta hak-hak tradisionalnya sepanjang masih hidup dan sesuai prinsip NKRI",
      "Kewenangan mutlak kepala desa mengelola tanah",
      "Hak veto pemerintah desa terhadap peraturan daerah"
    ],
    "answer": 1,
    "explanation": "Pasal 18B ayat (2) UUD 1945: 'Negara mengakui dan menghormati kesatuan-kesatuan masyarakat hukum adat beserta hak-hak tradisionalnya sepanjang masih hidup dan sesuai dengan perkembangan masyarakat dan prinsip NKRI'.",
    "source": "UUD NRI Tahun 1945 Pasal 18B ayat (2)"
  },
  {
    "id": 235,
    "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
    "difficulty": "mudah",
    "question": "Sikap tidak membeda-bedakan warga miskin maupun kaya dalam memberikan pelayanan administrasi surat desa merupakan pencerminan sila...",
    "options": [
      "Sila Kedua dan Sila Kelima",
      "Hanya Sila Pertama",
      "Sila Ketiga saja",
      "Bukan nilai Pancasila"
    ],
    "answer": 0,
    "explanation": "Perlakuan adil tanpa diskriminasi menjunjung tinggi martabat kemanusiaan (Sila Ke-2) dan mewujudkan keadilan sosial bagi seluruh warga (Sila Ke-5).",
    "source": "Pedoman Pengamalan Pancasila BPIP"
  },
  {
    "id": 236,
    "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
    "difficulty": "sedang",
    "question": "Kedaulatan berada di tangan rakyat dan dilaksanakan menurut Undang-Undang Dasar adalah bunyi dari UUD 1945...",
    "options": [
      "Pasal 1 ayat (1)",
      "Pasal 1 ayat (2)",
      "Pasal 1 ayat (3)",
      "Pasal 2 ayat (1)"
    ],
    "answer": 1,
    "explanation": "Pasal 1 ayat (2) UUD NRI Tahun 1945 berbunyi: 'Kedaulatan berada di tangan rakyat dan dilaksanakan menurut Undang-Undang Dasar.'",
    "source": "UUD NRI Tahun 1945 Pasal 1 ayat (2)"
  },
  {
    "id": 237,
    "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
    "difficulty": "sedang",
    "question": "Dalam Pembukaan UUD 1945, tujuan nasional negara Republik Indonesia tercantum secara jelas pada alinea...",
    "options": [
      "Alinea Pertama",
      "Alinea Kedua",
      "Alinea Ketiga",
      "Alinea Keempat"
    ],
    "answer": 3,
    "explanation": "Alinea Keempat Pembukaan UUD 1945 memuat 4 tujuan negara: melindungi segenap bangsa, memajukan kesejahteraan umum, mencerdaskan kehidupan bangsa, dan ikut melaksanakan ketertiban dunia.",
    "source": "Pembukaan UUD NRI Tahun 1945 Alinea IV"
  },
  {
    "id": 238,
    "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
    "difficulty": "mudah",
    "question": "Kedudukan Pancasila sebagai sumber dari segala sumber hukum negara diatur secara eksplisit dalam...",
    "options": [
      "UU No. 12 Tahun 2011 Pasal 2",
      "Permendagri No. 84 Tahun 2015",
      "Peraturan Daerah Provinsi",
      "Keputusan Kepala Desa"
    ],
    "answer": 0,
    "explanation": "UU No. 12 Tahun 2011 Pasal 2 menegaskan bahwa Pancasila merupakan sumber segala sumber hukum negara Republik Indonesia.",
    "source": "UU No. 12 Tahun 2011 Pasal 2"
  },
  {
    "id": 239,
    "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
    "difficulty": "sedang",
    "question": "Konsep Wawasan Nusantara dalam konteks kehidupan desa menuntut perangkat desa untuk memandang wilayah desa dan keragamannya sebagai...",
    "options": [
      "Wilayah otonom yang dapat memisahkan diri dari NKRI",
      "Satu kesatuan utuh politik, ekonomi, sosial budaya, dan pertahanan keamanan dalam bingkai NKRI",
      "Entitas independen tanpa tunduk hukum nasional",
      "Milik kelompok mayoritas dusun terbesar"
    ],
    "answer": 1,
    "explanation": "Wawasan Nusantara mengajarkan persatuan bangsa dan kesatuan wilayah Indonesia sebagai satu kesatuan utuh dalam segala gatra kehidupan.",
    "source": "Modul Wawasan Kebangsaan Lemhannas RI"
  },
  {
    "id": 240,
    "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
    "difficulty": "mudah",
    "question": "Pasal 30 ayat (1) UUD NRI Tahun 1945 menegaskan hak dan kewajiban setiap warga negara dalam...",
    "options": [
      "Mendapatkan pekerjaan yang layak",
      "Usaha pertahanan dan keamanan negara",
      "Memperoleh subsidi pangan dari pemerintah",
      "Membentuk serikat pekerja"
    ],
    "answer": 1,
    "explanation": "Pasal 30 ayat (1) UUD 1945: 'Tiap-tiap warga negara berhak dan wajib ikut serta dalam usaha pertahanan dan keamanan negara.'",
    "source": "UUD NRI Tahun 1945 Pasal 30 ayat (1)"
  },
  {
    "id": 241,
    "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
    "difficulty": "sedang",
    "question": "Sistem pertahanan keamanan negara yang melibatkan seluruh rakyat dengan TNI dan Polri sebagai kekuatan utama disebut...",
    "options": [
      "Sistem Pertahanan Terbuka",
      "Sistem Pertahanan Keamanan Rakyat Semesta (Sishankamrata)",
      "Sistem Keamanan Blok Dusun",
      "Sistem Garda Desa Swakarsa"
    ],
    "answer": 1,
    "explanation": "Pasal 30 ayat (2) UUD 1945 mengatur usaha hankamneg dilaksanakan melalui sistem pertahanan dan keamanan rakyat semesta.",
    "source": "UUD NRI Tahun 1945 Pasal 30 ayat (2)"
  },
  {
    "id": 242,
    "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
    "difficulty": "sedang",
    "question": "Makna lambang pohon beringin pada perisai Garuda Pancasila melambangkan...",
    "options": [
      "Ketuhanan Yang Maha Esa",
      "Kemanusiaan yang adil dan beradab",
      "Persatuan Indonesia",
      "Keadilan sosial bagi seluruh rakyat Indonesia"
    ],
    "answer": 2,
    "explanation": "Pohon beringin merupakan simbol Sila Ketiga: Persatuan Indonesia, yang melambangkan keteduhan dan tempat bernaung seluruh bangsa Indonesia yang majemuk.",
    "source": "PP No. 66 Tahun 1951 tentang Lambang Negara"
  },

  # =========================================================================
  # KATEGORI 4: Administrasi pemerintahan, surat-menyurat, pengarsipan (10 Soal: ID 243-252)
  # =========================================================================
  {
    "id": 243,
    "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
    "difficulty": "mudah",
    "question": "Permendagri No. 47 Tahun 2016 mengatur tata administrasi pemerintahan desa yang dikelompokkan ke dalam berapa jenis buku administrasi?",
    "options": [
      "3 jenis buku administrasi",
      "5 jenis buku administrasi",
      "8 jenis buku administrasi",
      "12 jenis buku administrasi"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 47 Tahun 2016 mengatur 5 jenis administrasi desa: Administrasi Umum, Penduduk, Keuangan, Pembangunan, dan Lainnya.",
    "source": "Permendagri No. 47 Tahun 2016 Pasal 3"
  },
  {
    "id": 244,
    "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
    "difficulty": "sedang",
    "question": "Buku yang mencatat data keluar masuknya surat dinas resmi di kantor desa beserta tanggal pengiriman dan tanda terima disebut...",
    "options": [
      "Buku Agenda dan Buku Ekspedisi",
      "Buku Induk Penduduk",
      "Buku Kas Pembantu",
      "Buku Rencana Anggaran Biaya"
    ],
    "answer": 0,
    "explanation": "Buku Agenda mencatat surat masuk/keluar secara kronologis, dan Buku Ekspedisi mencatat pembuktian pengiriman/penerimaan fisik surat.",
    "source": "Permendagri No. 47 Tahun 2016 tentang Administrasi Pemerintahan Desa"
  },
  {
    "id": 245,
    "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
    "difficulty": "mudah",
    "question": "Penulisan alamat tujuan surat resmi dinas desa yang sesuai dengan pedoman tata naskah dinas yang benar adalah...",
    "options": [
      "Kepada Yth. Bapak Camat Tuban di Tempat",
      "Yth. Camat Tuban\nJalan Veteran No. 12\nTuban",
      "Kepada Yth. Bapak/Ibu Camat Tuban di Tuban",
      "Yth. Bapak Camat Tuban, Jalan Veteran No. 12, Tuban"
    ],
    "answer": 1,
    "explanation": "Tata naskah dinas baku tidak menggunakan kata 'Kepada' sebelum 'Yth.', tidak menggunakan sebutan 'Bapak/Ibu' jika diikuti nama jabatan, dan tidak menggunakan frasa 'di Tempat'.",
    "source": "Permendagri No. 54/2009 & Permendagri No. 1/2023 Tata Naskah Dinas"
  },
  {
    "id": 246,
    "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
    "difficulty": "sedang",
    "question": "Singkatan 'a.n.' (atas nama) pada penandatanganan naskah dinas digunakan apabila...",
    "options": [
      "Pejabat yang berwenang melimpahkan wewenang penandatanganan kepada bawahannya sesuai bidang tugasnya",
      "Kepala Desa sedang cuti panjang dan menunjuk warga desa",
      "Surat ditujukan kepada instansi swasta",
      "Surat tersebut bersifat rahasia negara"
    ],
    "answer": 0,
    "explanation": "Atas nama (a.n.) digunakan jika pejabat definitif melimpahkan mandat penandatanganan kepada pejabat di bawahnya secara resmi.",
    "source": "Permendagri tentang Tata Naskah Dinas Pemerintahan Daerah & Desa"
  },
  {
    "id": 247,
    "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
    "difficulty": "sedang",
    "question": "Cap atau stempel dinas Pemerintah Desa berbentuk lingkaran memuat lambang dan nama instansi yang tintanya resmi menggunakan warna...",
    "options": [
      "Hitam",
      "Merah",
      "Ungu / Biru",
      "Hijau tua"
    ],
    "answer": 2,
    "explanation": "Sesuai ketentuan tata naskah dinas instansi pemerintahan daerah dan desa, tinta cap dinas menggunakan warna ungu (violet) atau biru.",
    "source": "Permendagri tentang Tata Naskah Dinas Instansi Pemerintah"
  },
  {
    "id": 248,
    "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
    "difficulty": "sedang",
    "question": "Buku administrasi yang wajib dimiliki oleh desa untuk mencatat tanah kas desa, tanah bengkok, dan tanah fasilitas umum lainnya adalah...",
    "options": [
      "Buku Data Tanah Kas Desa / Tanah di Desa",
      "Buku Mutasi Penduduk",
      "Buku Register Pengaduan",
      "Buku Harian Piket"
    ],
    "answer": 0,
    "explanation": "Buku Tanah di Desa merupakan salah satu buku wajib dalam Administrasi Umum menurut Permendagri No. 47 Tahun 2016.",
    "source": "Permendagri No. 47 Tahun 2016 Lampiran I"
  },
  {
    "id": 249,
    "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
    "difficulty": "sedang",
    "question": "Arsip dinas desa yang masih frekuen digunakan dalam kegiatan operasional sehari-hari disebut...",
    "options": [
      "Arsip Statis",
      "Arsip Inaktif",
      "Arsip Aktif",
      "Arsip Musnah"
    ],
    "answer": 2,
    "explanation": "Arsip aktif adalah arsip yang frekuensi penggunaannya tinggi dan terus-menerus diperlukan dalam pelaksanaan fungsi instansi.",
    "source": "UU No. 43 Tahun 2009 tentang Kearsipan"
  },
  {
    "id": 250,
    "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
    "difficulty": "mudah",
    "question": "Surat resmi yang dikeluarkan oleh Kepala Desa untuk menerangkan status kependudukan seorang warga (misal domisili, belum menikah, atau kurang mampu) disebut...",
    "options": [
      "Surat Edaran",
      "Surat Perjalanan Dinas",
      "Surat Keterangan",
      "Surat Keputusan"
    ],
    "answer": 2,
    "explanation": "Surat Keterangan adalah naskah dinas yang berisi penjelasan atau keterangan resmi tentang suatu keadaan atau peristiwa faktual seseorang.",
    "source": "Pedoman Tata Naskah Dinas Desa Permendagri"
  },
  {
    "id": 251,
    "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
    "difficulty": "sedang",
    "question": "Dokumen resmi yang dibuat sebagai bukti terjadinya suatu peristiwa, rapat, serah terima barang/jabatan, atau pemeriksaan fisik disebut...",
    "options": [
      "Nota Dinas",
      "Lembar Disposisi",
      "Berita Acara",
      "Surat Tugas"
    ],
    "answer": 2,
    "explanation": "Berita Acara merupakan naskah dinas yang berisi pernyataan sah mengenai pelaksanaan suatu kegiatan atau serah terima pekerjaan/jabatan.",
    "source": "Permendagri Tata Naskah Dinas Pemerintahan"
  },
  {
    "id": 252,
    "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
    "difficulty": "sedang",
    "question": "Siapakah penanggung jawab tertinggi pengelolaan seluruh arsip dan administrasi ketatausahaan di lingkungan Pemerintah Desa?",
    "options": [
      "Kaur Keuangan",
      "Sekretaris Desa",
      "Ketua RT tertua",
      "Petugas Pos Kecamatan"
    ],
    "answer": 1,
    "explanation": "Sekretaris Desa bertugas membantu Kepala Desa dalam bidang administrasi pemerintahan dan memimpin sekretariat desa selaku penanggung jawab ketatausahaan dan kearsipan.",
    "source": "Permendagri No. 84 Tahun 2015 Pasal 7"
  },

  # =========================================================================
  # KATEGORI 5: Keuangan desa, APB Desa, aset desa (10 Soal: ID 253-262)
  # =========================================================================
  {
    "id": 253,
    "category": "Keuangan desa, APB Desa, dan aset desa",
    "difficulty": "sedang",
    "question": "Rekening Kas Desa (RKD) dibuka pada bank persepsi oleh Pemerintah Desa dengan spesimen tanda tangan bersama antara...",
    "options": [
      "Ketua BPD dan Camat",
      "Kepala Desa dan Kaur Keuangan (Bendahara Desa)",
      "Sekretaris Desa dan Bendahara BPD",
      "Kepala Desa dan Kasi Pemerintahan"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 20 Tahun 2018 Pasal 14 ayat (3) menetapkan spesimen tanda tangan pembukaan RKD adalah Kepala Desa dan Kaur Keuangan.",
    "source": "Permendagri No. 20 Tahun 2018 Pasal 14"
  },
  {
    "id": 254,
    "category": "Keuangan desa, APB Desa, dan aset desa",
    "difficulty": "sedang",
    "question": "Batas waktu paling lambat penetapan Peraturan Desa tentang APB Desa untuk tahun anggaran berikutnya adalah tanggal...",
    "options": [
      "30 November tahun berjalan",
      "31 Desember tahun berjalan",
      "10 Januari tahun anggaran berkenaan",
      "31 Maret tahun berkenaan"
    ],
    "answer": 1,
    "explanation": "Berdasarkan Permendagri No. 20 Tahun 2018 Pasal 37 ayat (2), Perdes tentang APB Desa ditetapkan paling lambat tanggal 31 Desember tahun anggaran berjalan.",
    "source": "Permendagri No. 20 Tahun 2018 Pasal 37"
  },
  {
    "id": 255,
    "category": "Keuangan desa, APB Desa, dan aset desa",
    "difficulty": "sedang",
    "question": "Berdasarkan PP No. 11 Tahun 2019, alokasi belanja desa dalam APB Desa untuk penghasilan tetap dan tunjangan Kepala Desa, Perangkat Desa, operasional Pemdes dan BPD diatur paling banyak...",
    "options": [
      "30% dari total belanja desa",
      "50% dari total belanja desa",
      "70% dari total belanja desa",
      "Tanpa batasan persentase"
    ],
    "answer": 0,
    "explanation": "PP No. 11/2019 Pasal 100 mengatur paling banyak 30% belanja APB Desa untuk siltap, tunjangan, operasional kades, perangkat, BPD, dan insentif RT/RW.",
    "source": "PP No. 11 Tahun 2019 Pasal 100 ayat (1) huruf a"
  },
  {
    "id": 256,
    "category": "Keuangan desa, APB Desa, dan aset desa",
    "difficulty": "sedang",
    "question": "Sesuai Permendagri No. 1 Tahun 2016, jangka waktu sewa tanah kas desa atau aset desa lainnya ditetapkan paling lama...",
    "options": [
      "1 tahun saja",
      "3 tahun dan dapat diperpanjang",
      "10 tahun penuh",
      "25 tahun sesuai hak guna bangunan"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 1 Tahun 2016 Pasal 11 ayat (3) menegaskan bahwa jangka waktu sewa aset desa paling lama 3 (tiga) tahun dan dapat diperpanjang.",
    "source": "Permendagri No. 1 Tahun 2016 Pasal 11"
  },
  {
    "id": 257,
    "category": "Keuangan desa, APB Desa, dan aset desa",
    "difficulty": "sedang",
    "question": "Surat Permintaan Pembayaran (SPP) diajukan oleh Pelaksana Kegiatan Anggaran (Kaur/Kasi) kepada Kepala Desa melalui...",
    "options": [
      "Ketua BPD untuk diotorisasi",
      "Sekretaris Desa untuk diverifikasi kelengkapannya",
      "Camat untuk disahkan",
      "Inspektorat Kabupaten"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 20 Tahun 2018 Pasal 51 mengatur Sekretaris Desa bertindak sebagai verifikator atas SPP dan dokumen pendukung yang diajukan Kaur/Kasi.",
    "source": "Permendagri No. 20 Tahun 2018 Pasal 51"
  },
  {
    "id": 258,
    "category": "Keuangan desa, APB Desa, dan aset desa",
    "difficulty": "mudah",
    "question": "Sisa Lebih Pembiayaan Anggaran (Silpa) tahun sebelumnya dalam APB Desa tahun berjalan dikelompokkan ke dalam struktur...",
    "options": [
      "Pendapatan Asli Desa",
      "Penerimaan Pembiayaan",
      "Pengeluaran Pembiayaan",
      "Belanja Tak Terduga"
    ],
    "answer": 1,
    "explanation": "Silpa tahun anggaran sebelumnya merupakan pos Penerimaan Pembiayaan yang digunakan untuk mendanai kegiatan tahun berjalan.",
    "source": "Permendagri No. 20 Tahun 2018 Pasal 27"
  },
  {
    "id": 259,
    "category": "Keuangan desa, APB Desa, dan aset desa",
    "difficulty": "sedang",
    "question": "Berapakah jumlah bidang kelompok belanja dalam struktur Anggaran Pendapatan dan Belanja Desa (APB Desa)?",
    "options": [
      "3 bidang",
      "4 bidang",
      "5 bidang",
      "7 bidang"
    ],
    "answer": 2,
    "explanation": "Permendagri No. 20/2018 menetapkan 5 bidang belanja desa: (1) Penyelenggaraan Pemdes, (2) Pembangunan, (3) Pembinaan Kemasyarakatan, (4) Pemberdayaan Masyarakat, dan (5) Penanggulangan Bencana/Keadaan Mendesak.",
    "source": "Permendagri No. 20 Tahun 2018 Pasal 16"
  },
  {
    "id": 260,
    "category": "Keuangan desa, APB Desa, dan aset desa",
    "difficulty": "sulit",
    "question": "Penghapusan aset desa berupa barang milik desa karena rusak berat atau hilang harus ditetapkan dengan...",
    "options": [
      "Keputusan Kepala Desa setelah mendapat persetujuan BPD",
      "Surat Pernyataan Sekretaris Desa",
      "Keputusan Camat",
      "Surat Perjanjian Sewa"
    ],
    "answer": 0,
    "explanation": "Permendagri No. 1 Tahun 2016 Pasal 19 mengatur bahwa penghapusan aset desa dilakukan melalui Keputusan Kepala Desa setelah mendapat persetujuan BPD.",
    "source": "Permendagri No. 1 Tahun 2016 Pasal 19"
  },
  {
    "id": 261,
    "category": "Keuangan desa, APB Desa, dan aset desa",
    "difficulty": "sedang",
    "question": "Aplikasi komputer resmi terpadu yang dikembangkan BPKP dan Kemendagri untuk tata kelola penatausahaan keuangan desa adalah...",
    "options": [
      "SIMDA",
      "SISKEUDES",
      "SIPADES",
      "PRODESKEL"
    ],
    "answer": 1,
    "explanation": "Siskeudes (Sistem Keuangan Desa) adalah aplikasi resmi BPKP-Kemendagri untuk pengelolaan APB Desa.",
    "source": "Pedoman Pengelolaan Keuangan Desa Kemendagri & BPKP"
  },
  {
    "id": 262,
    "category": "Keuangan desa, APB Desa, dan aset desa",
    "difficulty": "sedang",
    "question": "Dana Desa yang bersumber dari APBN disalurkan dari Rekening Kas Umum Negara (RKUN) ke desa melalui...",
    "options": [
      "Rekening Kas Umum Daerah (RKUD) Kabupaten/Kota",
      "Rekening pribadi Kepala Desa",
      "Kantor Pos terdekat",
      "Rekening bersama BPD"
    ],
    "answer": 0,
    "explanation": "Penyaluran Dana Desa dilakukan melalui pemindahbukuan dari RKUN ke RKUD kabupaten/kota sebelum ditransfer ke RKD masing-masing desa.",
    "source": "PP No. 60 Tahun 2014 & PMK Pengelolaan Dana Desa"
  },

  # =========================================================================
  # KATEGORI 6: Pembangunan desa, perencanaan, pemberdayaan (8 Soal: ID 263-270)
  # =========================================================================
  {
    "id": 263,
    "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
    "difficulty": "sedang",
    "question": "Berdasarkan Permendesa PDTT No. 21 Tahun 2020, penyusunan Rencana Kerja Pemerintah Desa (RKP Desa) mulai dilaksanakan pada bulan...",
    "options": [
      "Januari tahun berjalan",
      "Juli tahun berjalan",
      "September tahun berjalan",
      "Desember tahun berjalan"
    ],
    "answer": 1,
    "explanation": "Permendesa PDTT No. 21 Tahun 2020 Pasal 22 menetapkan Kepala Desa menyusun RKP Desa dengan mengikutsertakan masyarakat mulai bulan Juli tahun berjalan.",
    "source": "Permendesa PDTT No. 21 Tahun 2020 Pasal 22"
  },
  {
    "id": 264,
    "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
    "difficulty": "mudah",
    "question": "Dokumen perencanaan pembangunan desa yang memuat rencana arah kebijakan pembangunan untuk jangka waktu 8 tahun adalah...",
    "options": [
      "RKP Desa",
      "RPJM Desa",
      "APB Desa",
      "Profil Desa"
    ],
    "answer": 1,
    "explanation": "UU No. 3 Tahun 2024 menyelaraskan masa jabatan Kepala Desa 8 tahun, sehingga RPJM Desa disusun untuk periode 8 tahun.",
    "source": "UU No. 3 Tahun 2024 & Permendesa No. 21/2020"
  },
  {
    "id": 265,
    "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
    "difficulty": "sedang",
    "question": "Pelaksanaan proyek pembangunan fisik di desa diutamakan dengan metode swakelola dan prinsip Padat Karya Tunai Desa (PKTD). Tujuan utama PKTD adalah...",
    "options": [
      "Memberikan keuntungan maksimal bagi kontraktor swasta",
      "Menyerap tenaga kerja warga setempat terutama keluarga prasejahtera dan menambah pendapatan masyarakat desa",
      "Mempercepat waktu pengerjaan proyek tanpa melibatkan warga",
      "Mengurangi transparansi penggunaan anggaran"
    ],
    "answer": 1,
    "explanation": "PKTD bertujuan membuka lapangan kerja sementara bagi warga lokal, meningkatkan daya beli, dan mengentaskan kemiskinan perdesaan.",
    "source": "Buku Saku Padat Karya Tunai Desa Kemendesa PDTT"
  },
  {
    "id": 266,
    "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
    "difficulty": "sedang",
    "question": "Modal awal pendirian Badan Usaha Milik Desa (BUMDes) bersumber dari...",
    "options": [
      "Pinjaman bank komersial tanpa jaminan",
      "Kekayaan desa yang dipisahkan yang dianggarkan melalui APB Desa",
      "Sumbangan sukarela perangkat desa",
      "Iuran wajib seluruh warga desa per bulan"
    ],
    "answer": 1,
    "explanation": "PP No. 11 Tahun 2021 Pasal 39 menegaskan modal awal BUMDes bersumber dari APB Desa sebagai kekayaan desa yang dipisahkan.",
    "source": "PP No. 11 Tahun 2021 tentang BUMDes Pasal 39"
  },
  {
    "id": 267,
    "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
    "difficulty": "sedang",
    "question": "Kader di desa yang bertugas memfasilitasi dan mengawal integrasi pencegahan stunting pada 1.000 Hari Pertama Kehidupan (HPK) disebut...",
    "options": [
      "Kader Pemberdayaan Masyarakat Desa (KPMD)",
      "Kader Pembangunan Manusia (KPM)",
      "Pendamping Lokal Desa (PLD)",
      "Petugas Lapangan KB (PLKB)"
    ],
    "answer": 1,
    "explanation": "Kader Pembangunan Manusia (KPM) adalah kader desa yang memantau dan mendorong layanan konvergensi pencegahan stunting di desa.",
    "source": "Petunjuk Teknis Konvergensi Stunting Desa Kemendesa PDTT"
  },
  {
    "id": 268,
    "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
    "difficulty": "mudah",
    "question": "Tim yang dibentuk oleh Kepala Desa untuk membantu pelaksanaan kegiatan pengadaan barang/jasa pembangunan fisik di desa disebut...",
    "options": [
      "Panitia Pengawas BPD",
      "Tim Pelaksana Kegiatan (TPK)",
      "Komisi Disiplin Aparatur",
      "Dewan Pertimbangan Desa"
    ],
    "answer": 1,
    "explanation": "Pengadaan barang dan jasa di desa dilaksanakan oleh Tim Pelaksana Kegiatan (TPK) yang dibentuk oleh Kepala Desa dari unsur perangkat desa dan masyarakat.",
    "source": "Perka LKPP No. 12/2019 tentang Pengadaan Barang/Jasa di Desa"
  },
  {
    "id": 269,
    "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
    "difficulty": "sedang",
    "question": "Berapakah porsi pembagian hasil laba bersih usaha BUMDes yang disetorkan sebagai Pendapatan Asli Desa (PADes)?",
    "options": [
      "Ditetapkan dalam Anggaran Dasar / Anggaran Rumah Tangga (AD/ART) BUMDes dan disepakati dalam Musdes",
      "Wajib 100% tanpa cadangan modal",
      "Maksimal 10% saja",
      "Ditetapkan sepihak oleh direktur BUMDes"
    ],
    "answer": 0,
    "explanation": "Pembagian laba usaha BUMDes untuk PADes, cadangan modal, dan pengelola diatur dalam AD/ART dan diputuskan melalui forum Musyawarah Desa.",
    "source": "PP No. 11 Tahun 2021 tentang BUMDes"
  },
  {
    "id": 270,
    "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
    "difficulty": "sedang",
    "question": "Tujuan utama program SDGs Desa yang diatur dalam Permendesa No. 21 Tahun 2020 adalah...",
    "options": [
      "Menghapus keberadaan tradisi lokal desa",
      "Mewujudkan pembangunan desa yang berkelanjutan, tanpa kemiskinan, tanpa kelaparan, dan peduli lingkungan",
      "Mengganti seluruh lahan pertanian menjadi kawasan industri",
      "Mewajibkan warga desa bekerja di luar negeri"
    ],
    "answer": 1,
    "explanation": "SDGs Desa mengadaptasi 18 tujuan global untuk percepatan pencapaian desa tanpa kemiskinan, desa sehat, peduli pendidikan, dan berkelanjutan.",
    "source": "Permendesa PDTT No. 21 Tahun 2020"
  },

  # =========================================================================
  # KATEGORI 7: BPD, kelembagaan desa, musyawarah (5 Soal: ID 271-275)
  # =========================================================================
  {
    "id": 271,
    "category": "BPD, kelembagaan desa, dan musyawarah",
    "difficulty": "sedang",
    "question": "Berdasarkan UU No. 3 Tahun 2024, masa keanggotaan Badan Permusyawaratan Desa (BPD) adalah...",
    "options": [
      "5 tahun",
      "6 tahun",
      "8 tahun dan dapat dipilih kembali",
      "Seumur hidup"
    ],
    "answer": 2,
    "explanation": "UU No. 3 Tahun 2024 Pasal 56 menyelaraskan masa keanggotaan BPD menjadi 8 (delapan) tahun terhitung sejak tanggal pengucapan sumpah/janji.",
    "source": "UU No. 3 Tahun 2024 Pasal 56"
  },
  {
    "id": 272,
    "category": "BPD, kelembagaan desa, dan musyawarah",
    "difficulty": "mudah",
    "question": "Berapakah jumlah anggota BPD di suatu desa menurut peraturan perundang-undangan?",
    "options": [
      "Genap antara 4 sampai 8 orang",
      "Ganjil paling sedikit 5 orang dan paling banyak 9 orang",
      "Bebas sesuai kesepakatan warga dusun",
      "Harus sama persis dengan jumlah perangkat desa"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 110 Tahun 2016 Pasal 5 ayat (1) menyatakan jumlah anggota BPD berjumlah ganjil, paling sedikit 5 (lima) orang dan paling banyak 9 (sembilan) orang.",
    "source": "Permendagri No. 110 Tahun 2016 Pasal 5"
  },
  {
    "id": 273,
    "category": "BPD, kelembagaan desa, dan musyawarah",
    "difficulty": "sedang",
    "question": "Penyampaian Laporan Keterangan Penyelenggaraan Pemerintahan Desa (LKPPD) oleh Kepala Desa kepada BPD dilakukan secara tertulis dalam jangka waktu...",
    "options": [
      "Paling lambat 30 hari setelah tahun anggaran berakhir",
      "Paling lambat 3 (tiga) bulan setelah berakhirnya tahun anggaran",
      "Setiap akhir bulan berjalan",
      "Hanya pada akhir masa jabatan Kepala Desa"
    ],
    "answer": 1,
    "explanation": "Berdasarkan Permendagri No. 46 Tahun 2016 Pasal 8 ayat (1), LKPPD disampaikan secara tertulis kepada BPD paling lambat 3 bulan setelah tahun anggaran berakhir.",
    "source": "Permendagri No. 46 Tahun 2016 Pasal 8"
  },
  {
    "id": 274,
    "category": "BPD, kelembagaan desa, dan musyawarah",
    "difficulty": "sedang",
    "question": "Manakah lembaga di bawah ini yang tergolong sebagai Lembaga Kemasyarakatan Desa (LKD) menurut Permendagri No. 18 Tahun 2018?",
    "options": [
      "Badan Permusyawaratan Desa (BPD)",
      "Karang Taruna dan Tim Penggerak PKK",
      "Koramil dan Polsek",
      "Koperasi Simpan Pinjam swasta"
    ],
    "answer": 1,
    "explanation": "Permendagri No. 18/2018 Pasal 3 menyebut jenis LKD meliputi: RT, RW, PKK, Karang Taruna, Posyandu, dan LPMD.",
    "source": "Permendagri No. 18 Tahun 2018 Pasal 3"
  },
  {
    "id": 275,
    "category": "BPD, kelembagaan desa, dan musyawarah",
    "difficulty": "sedang",
    "question": "Forum musyawarah tertinggi di desa yang diselenggarakan oleh BPD untuk menyepakati hal strategis desa disebut...",
    "options": [
      "Musyawarah Dusun (Musdus)",
      "Musyawarah Desa (Musdes)",
      "Musrenbangdes",
      "Rapat Dengar Pendapat Umum"
    ],
    "answer": 1,
    "explanation": "Musdes diselenggarakan oleh BPD untuk hal strategis (penataan desa, BUMDes, kerja sama, aset desa) per UU No. 6/2014 Pasal 54.",
    "source": "UU No. 6 Tahun 2014 Pasal 54 & Permendesa No. 16/2019"
  },

  # =========================================================================
  # KATEGORI 8: Bahasa Indonesia (7 Soal: ID 276-282)
  # =========================================================================
  {
    "id": 276,
    "category": "Bahasa Indonesia",
    "difficulty": "mudah",
    "question": "Manakah kelompok kata berikut yang semuanya merupakan kata baku menurut KBBI dan EYD Edisi V?",
    "options": [
      "Ijin, sistim, kwitansi, antri",
      "Izin, sistem, kuitansi, antre",
      "Ijin, sistem, kwitansi, antre",
      "Izin, sistim, kuitansi, antri"
    ],
    "answer": 1,
    "explanation": "Bentuk baku menurut EYD V dan KBBI adalah izin (bukan ijin), sistem (bukan sistim), kuitansi (bukan kwitansi), dan antre (bukan antri).",
    "source": "EYD Edisi V & Kamus Besar Bahasa Indonesia (KBBI)"
  },
  {
    "id": 277,
    "category": "Bahasa Indonesia",
    "difficulty": "sedang",
    "question": "Penulisan gelar akademik dan nama pejabat yang benar pada naskah dinas adalah...",
    "options": [
      "Drs, Ahmad Fauzi. M,Si.",
      "Drs. Ahmad Fauzi, M.Si.",
      "Drs. Ahmad Fauzi M.Si",
      "Drs Ahmad Fauzi, M,Si."
    ],
    "answer": 1,
    "explanation": "Gelar depan diikuti tanda titik (Drs.), antara nama dan gelar belakang dipisahkan tanda koma, dan tiap singkatan gelar belakang diakhiri tanda titik (M.Si.).",
    "source": "Pedoman Umum Ejaan Bahasa Indonesia (EYD V)"
  },
  {
    "id": 278,
    "category": "Bahasa Indonesia",
    "difficulty": "sedang",
    "question": "Kalimat manakah di bawah ini yang paling efektif dan bebas dari pemborosan kata (pleonasme)?",
    "options": [
      "Seluruh para perangkat desa sekalian hadir dalam rapat.",
      "Semua perangkat desa hadir dalam rapat pleno.",
      "Para perangkat desa semua saling bantu-membantu.",
      "Perangkat desa hadir kembali mengulang kegiatan tersebut."
    ],
    "answer": 1,
    "explanation": "Pilihan B efektif. Pilihan A pleonastis ('seluruh para sekalian'), C pleonastis ('semua saling bantu-membantu').",
    "source": "Tata Bahasa Baku Bahasa Indonesia"
  },
  {
    "id": 279,
    "category": "Bahasa Indonesia",
    "difficulty": "sedang",
    "question": "Kata 'legalitas' dalam konteks administrasi hukum pemerintahan desa memiliki makna sinonim dengan...",
    "options": [
      "Kebijaksanaan",
      "Keabsahan hukum",
      "Popularitas pejabat",
      "Efisiensi anggaran"
    ],
    "answer": 1,
    "explanation": "Legalitas berasal dari kata legal yang berarti keabsahan atau kesesuaian dengan hukum dan peraturan yang berlaku.",
    "source": "KBBI Kemendikbudristek"
  },
  {
    "id": 280,
    "category": "Bahasa Indonesia",
    "difficulty": "mudah",
    "question": "Penulisan tanggal surat dinas desa yang benar dan baku adalah...",
    "options": [
      "Tuban, 18-10-2026",
      "Tuban, 18 Oktober 2026",
      "Tuban, 18 Okt. 2026",
      "Tuban: 18/Oktober/2026"
    ],
    "answer": 1,
    "explanation": "Dalam tata naskah dinas, nama tempat diikuti tanda koma, tanggal dengan angka, nama bulan ditulis utuh dengan huruf kapital awal, dan tahun angka tanpa titik akhir.",
    "source": "Permendagri Tata Naskah Dinas & EYD V"
  },
  {
    "id": 281,
    "category": "Bahasa Indonesia",
    "difficulty": "sedang",
    "question": "Penulisan kata serapan yang baku di bawah ini adalah...",
    "options": [
      "Standarisasi, kordinasi, frekwensi",
      "Standardisasi, koordinasi, frekuensi",
      "Standardisasi, kordinasi, frekwensi",
      "Standarisasi, koordinasi, frekwensi"
    ],
    "answer": 1,
    "explanation": "Bentuk baku: standardisasi (dari standardization), koordinasi (dua 'o'), dan frekuensi (dengan huruf 'k-u' bukan 'w').",
    "source": "EYD Edisi V Pedoman Pembentukan Istilah"
  },
  {
    "id": 282,
    "category": "Bahasa Indonesia",
    "difficulty": "sedang",
    "question": "Perhatikan kalimat: 'Keputusan ini berlaku sejak tanggal ditetapkan.' Kata 'sejak' dalam kalimat tersebut berfungsi sebagai...",
    "options": [
      "Kata hubung (konjungsi) penanda waktu awal",
      "Kata benda abstrak",
      "Kata sifat",
      "Kata seru"
    ],
    "answer": 0,
    "explanation": "Kata 'sejak' merupakan preposisi/konjungsi temporal yang menandai titik tolak permulaan waktu berlakunya suatu penetapan.",
    "source": "Tata Bahasa Baku Bahasa Indonesia"
  },

  # =========================================================================
  # KATEGORI 9: Matematika dan numerik (6 Soal: ID 283-288)
  # =========================================================================
  {
    "id": 283,
    "category": "Matematika dan numerik",
    "difficulty": "sedang",
    "question": "Desa Sukomakmur memiliki total APB Desa sebesar Rp 1.200.000.000,00. Jika 65% dialokasikan untuk bidang pelaksanaan pembangunan desa, berapakah nilai nominal anggaran pembangunan tersebut?",
    "options": [
      "Rp 720.000.000,00",
      "Rp 780.000.000,00",
      "Rp 820.000.000,00",
      "Rp 850.000.000,00"
    ],
    "answer": 1,
    "explanation": "Perhitungan: 65% x Rp 1.200.000.000 = 0,65 x 1.200.000.000 = Rp 780.000.000,00.",
    "source": "Matematika Terapan Pengelolaan APB Desa"
  },
  {
    "id": 284,
    "category": "Matematika dan numerik",
    "difficulty": "sedang",
    "question": "Sebidang tanah kas desa seluas 2,5 hektar akan dibagikan untuk garapan 5 kelompok tani secara merata. Berapa meter persegi (m²) luas tanah yang diterima masing-masing kelompok tani?",
    "options": [
      "2.500 m²",
      "5.000 m²",
      "7.500 m²",
      "10.000 m²"
    ],
    "answer": 1,
    "explanation": "1 hektar = 10.000 m². Total luas = 2,5 x 10.000 = 25.000 m². Tiap kelompok menerima = 25.000 m² / 5 = 5.000 m².",
    "source": "Konversi Satuan Agraria Standar Nasional"
  },
  {
    "id": 285,
    "category": "Matematika dan numerik",
    "difficulty": "sedang",
    "question": "Sebuah proyek jalan rabat beton sepanjang 600 meter dapat diselesaikan oleh 12 orang pekerja dalam 20 hari. Jika Kepala Desa ingin proyek selesai dalam 15 hari, berapa jumlah total pekerja yang dibutuhkan?",
    "options": [
      "14 orang",
      "16 orang",
      "18 orang",
      "20 orang"
    ],
    "answer": 1,
    "explanation": "Perbandingan berbalik nilai: (Pekerja1 x Hari1) = (Pekerja2 x Hari2). (12 x 20) = (P2 x 15) -> 240 = 15 x P2 -> P2 = 240 / 15 = 16 orang.",
    "source": "Aritmatika Sosial dan Perbandingan Berbalik Nilai"
  },
  {
    "id": 286,
    "category": "Matematika dan numerik",
    "difficulty": "mudah",
    "question": "Pemerintah Desa membeli 4 unit laptop kantor seharga Rp 7.500.000,00 per unit. Toko memberikan potongan harga (diskon) sebesar 8%. Berapakah total biaya yang harus dibayarkan dari kas desa?",
    "options": [
      "Rp 27.600.000,00",
      "Rp 28.000.000,00",
      "Rp 28.500.000,00",
      "Rp 29.400.000,00"
    ],
    "answer": 0,
    "explanation": "Harga total kotor = 4 x 7.500.000 = Rp 30.000.000. Diskon 8% = 0,08 x 30.000.000 = Rp 2.400.000. Total bayar = 30.000.000 - 2.400.000 = Rp 27.600.000,00.",
    "source": "Matematika Dasar Aritmatika Sosial"
  },
  {
    "id": 287,
    "category": "Matematika dan numerik",
    "difficulty": "sedang",
    "question": "Perhatikan deret bilangan berikut: 3, 7, 15, 31, 63, ... Angka berikutnya pada deret tersebut adalah...",
    "options": [
      "95",
      "127",
      "128",
      "144"
    ],
    "answer": 1,
    "explanation": "Pola deret: (+4, +8, +16, +32, +64) atau rumus (2n + 1). 63 + 64 = 127.",
    "source": "Tes Potensi Akademik Deret Angka Numerik"
  },
  {
    "id": 288,
    "category": "Matematika dan numerik",
    "difficulty": "mudah",
    "question": "Jarak antara balai desa ke kantor kecamatan adalah 18 km. Jika perangkat desa mengendarai sepeda motor dengan kecepatan rata-rata 45 km/jam, berapa menit waktu yang diperlukan untuk sampai?",
    "options": [
      "20 menit",
      "24 menit",
      "30 menit",
      "36 menit"
    ],
    "answer": 1,
    "explanation": "Waktu = Jarak / Kecepatan = 18 km / 45 km/jam = 0,4 jam. 0,4 x 60 menit = 24 menit.",
    "source": "Matematika Dasar Kecepatan dan Waktu"
  },

  # =========================================================================
  # KATEGORI 10: Logika dan penalaran (5 Soal: ID 289-293)
  # =========================================================================
  {
    "id": 289,
    "category": "Logika dan penalaran",
    "difficulty": "sedang",
    "question": "Premis 1: Semua perangkat desa wajib masuk kerja tepat waktu.\nPremis 2: Sebagian warga desa Sukamaju adalah perangkat desa.\nKesimpulan yang paling tepat secara silogisme logis adalah...",
    "options": [
      "Semua warga desa Sukamaju wajib masuk kerja tepat waktu",
      "Sebagian warga desa Sukamaju wajib masuk kerja tepat waktu",
      "Perangkat desa tidak ada yang berasal dari Sukamaju",
      "Warga Sukamaju bebas dari kewajiban disiplin"
    ],
    "answer": 1,
    "explanation": "Kombinasi premis universal (Semua) dan partikular (Sebagian) menghasilkan kesimpulan partikular: 'Sebagian warga desa Sukamaju wajib masuk kerja tepat waktu'.",
    "source": "Logika Silogisme Kategorial Formal"
  },
  {
    "id": 290,
    "category": "Logika dan penalaran",
    "difficulty": "sedang",
    "question": "Jika musim kemarau panjang tiba, maka debit air sumur warga berkurang. Saat ini debit air sumur warga tidak berkurang. Kesimpulan yang sah berdasarkan modus tollens adalah...",
    "options": [
      "Musim kemarau panjang sedang tiba",
      "Musim kemarau panjang tidak tiba",
      "Warga desa menggunakan pompa air",
      "Hujan lebat terjadi setiap malam"
    ],
    "answer": 1,
    "explanation": "Modus Tollens: Jika P maka Q. Negasi Q (~Q), maka kesimpulannya adalah negasi P (~P): 'Musim kemarau panjang tidak tiba'.",
    "source": "Logika Proposisional Modus Tollens"
  },
  {
    "id": 291,
    "category": "Logika dan penalaran",
    "difficulty": "sedang",
    "question": "Dalam jadwal piket pelayanan desa: Ali piket sebelum Budi. Cici piket setelah Dedi tetapi sebelum Ali. Siapakah yang piket pada giliran pertama?",
    "options": [
      "Ali",
      "Budi",
      "Cici",
      "Dedi"
    ],
    "answer": 3,
    "explanation": "Urutan piket: Dedi -> Cici -> Ali -> Budi. Giliran pertama adalah Dedi.",
    "source": "Tes Penalaran Analitis Posisi dan Urutan"
  },
  {
    "id": 292,
    "category": "Logika dan penalaran",
    "difficulty": "sedang",
    "question": "Dari 50 warga penerima bantuan: 30 warga menerima bantuan beras, 25 warga menerima bantuan minyak goreng, dan 10 warga menerima kedua-duanya. Berapakah warga yang hanya menerima bantuan beras saja?",
    "options": [
      "10 warga",
      "15 warga",
      "20 warga",
      "25 warga"
    ],
    "answer": 2,
    "explanation": "Himpunan: Warga yang hanya menerima beras = Total penerima beras - Penerima keduanya = 30 - 10 = 20 warga.",
    "source": "Logika Matematika Teori Himpunan Venn"
  },
  {
    "id": 293,
    "category": "Logika dan penalaran",
    "difficulty": "sedang",
    "question": "Semua kantor pemerintah desa memiliki papan transparansi APB Desa. Gedung X tidak memiliki papan transparansi APB Desa. Kesimpulan yang benar adalah...",
    "options": [
      "Gedung X adalah kantor BPD",
      "Gedung X bukan kantor pemerintah desa",
      "Gedung X adalah kantor desa yang sedang direnovasi",
      "Papan transparansi sedang dicetak"
    ],
    "answer": 1,
    "explanation": "Jika semua P adalah Q, dan X bukan Q, maka pasti X bukan P ('Gedung X bukan kantor pemerintah desa').",
    "source": "Silogisme Penalaran Deduktif"
  },

  # =========================================================================
  # KATEGORI 11: Pengetahuan umum Tuban & Nasional (4 Soal: ID 294-297)
  # =========================================================================
  {
    "id": 294,
    "category": "Pengetahuan umum",
    "difficulty": "mudah",
    "question": "Secara administratif, Kabupaten Tuban di sebelah utara berbatasan langsung dengan...",
    "options": [
      "Kabupaten Lamongan",
      "Laut Jawa",
      "Kabupaten Bojonegoro",
      "Kabupaten Rembang"
    ],
    "answer": 1,
    "explanation": "Batas wilayah Kabupaten Tuban: Utara: Laut Jawa; Timur: Kab. Lamongan; Selatan: Kab. Bojonegoro; Barat: Kab. Rembang dan Kab. Blora (Jawa Tengah).",
    "source": "Profil Wilayah dan Geografi Pemerintah Kabupaten Tuban"
  },
  {
    "id": 295,
    "category": "Pengetahuan umum",
    "difficulty": "mudah",
    "question": "Salah satu objek wisata alam gua yang terkenal di pusat kota Kabupaten Tuban yang terletak di bawah pasar perbelanjaan adalah...",
    "options": [
      "Gua Ngerong",
      "Gua Akbar",
      "Gua Maharani",
      "Gua Suci"
    ],
    "answer": 1,
    "explanation": "Gua Akbar adalah gua karst alami bersejarah yang terletak persis di bawah Pasar Baru Tuban di pusat kota Tuban.",
    "source": "Dinas Kebudayaan, Kepemudaan dan Olahraga serta Pariwisata Kab. Tuban"
  },
  {
    "id": 296,
    "category": "Pengetahuan umum",
    "difficulty": "sedang",
    "question": "Berapakah jumlah kecamatan yang ada di wilayah administratif Kabupaten Tuban?",
    "options": [
      "18 kecamatan",
      "20 kecamatan",
      "22 kecamatan",
      "25 kecamatan"
    ],
    "answer": 1,
    "explanation": "Kabupaten Tuban terdiri atas 20 kecamatan, 17 kelurahan, dan 311 desa.",
    "source": "Badan Pusat Statistik (BPS) Kabupaten Tuban Dalam Angka"
  },
  {
    "id": 297,
    "category": "Pengetahuan umum",
    "difficulty": "mudah",
    "question": "Makam tokoh penyebar agama Islam yang merupakan ayah dari Sunan Drajat dan Sunan Bonang, yang berada di Desa Gesikharjo, Kecamatan Palang, Tuban adalah...",
    "options": [
      "Sunan Kalijaga",
      "Syekh Maulana Ibrahim Asmoroqondi",
      "Sunan Muria",
      "Syekh Subakir"
    ],
    "answer": 1,
    "explanation": "Makam Syekh Maulana Ibrahim Asmoroqondi (ayah Sunan Ampel / kakek Sunan Bonang) terletak di Gesikharjo, Kecamatan Palang, Kabupaten Tuban.",
    "source": "Sejarah Kebudayaan Islam Tuban & Situs Cagar Budaya Jatim"
  },

  # =========================================================================
  # KATEGORI 12: Komputer dasar dan pelayanan publik (3 Soal: ID 298-300)
  # =========================================================================
  {
    "id": 298,
    "category": "Komputer dasar dan pelayanan publik",
    "difficulty": "sedang",
    "question": "Dalam Microsoft Excel, rumus yang tepat untuk menghitung jumlah sel yang memenuhi kriteria tertentu (misalnya menghitung warga penerima bansos kategori 'LANSIA') adalah...",
    "options": [
      "=SUMIF(...)",
      "=COUNTIF(...)",
      "=AVERAGEIF(...)",
      "=LOOKUP(...)"
    ],
    "answer": 1,
    "explanation": "Fungsi =COUNTIF digunakan untuk mencacah/menghitung frekuensi banyaknya sel yang memenuhi syarat/kriteria tertentu.",
    "source": "Modul Komputer Perkantoran Microsoft Excel"
  },
  {
    "id": 299,
    "category": "Komputer dasar dan pelayanan publik",
    "difficulty": "mudah",
    "question": "Kombinasi tombol keyboard (shortcut) yang digunakan untuk membatalkan tindakan pengeditan terakhir (undo) pada komputer adalah...",
    "options": [
      "Ctrl + C",
      "Ctrl + V",
      "Ctrl + Z",
      "Ctrl + Y"
    ],
    "answer": 2,
    "explanation": "Ctrl + Z berfungsi untuk Undo (membatalkan perintah terakhir), sedangkan Ctrl + Y untuk Redo.",
    "source": "Dasar Pengoperasian Komputer Keyboard Shortcuts"
  },
  {
    "id": 300,
    "category": "Komputer dasar dan pelayanan publik",
    "difficulty": "sedang",
    "question": "Berdasarkan prinsip pelayanan publik prima dan UU No. 25 Tahun 2009, maklumat pelayanan yang dipasang di kantor desa berfungsi sebagai...",
    "options": [
      "Daftar nama perangkat desa yang sedang cuti",
      "Pernyataan kesanggupan dan janji tertulis penyelenggara pelayanan untuk melaksanakan pelayanan sesuai standar yang ditetapkan",
      "Surat peringatan bagi warga yang terlambat membayar pajak",
      "Himbauan untuk tidak mengurus surat secara mandiri"
    ],
    "answer": 1,
    "explanation": "Maklumat pelayanan adalah pernyataan kesanggupan dan kewajiban penyelenggara pelayanan publik untuk melaksanakan pelayanan sesuai Standar Pelayanan (SP).",
    "source": "UU No. 25 Tahun 2009 tentang Pelayanan Publik Pasal 22"
  }
]
