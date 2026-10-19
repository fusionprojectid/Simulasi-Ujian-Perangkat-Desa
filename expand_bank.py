# -*- coding: utf-8 -*-
"""
Script penambahan 100 soal baru (ID 101 - 200) ke dalam bank soal database
Total Bank Soal: 200 Soal Proporsional.
"""
import json

NEW_QUESTIONS = [
    # =========================================================================
    # Kategori 1: Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa (20 Soal Tambahan: ID 101 - 120)
    # =========================================================================
    {
        "id": 101,
        "number": 101,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "sedang",
        "question": "Berdasarkan Permendagri Nomor 84 Tahun 2015, tugas utama Kepala Seksi (Kasi) Pemerintahan di lingkungan pemerintah desa adalah membantu Kepala Desa dalam...",
        "options": [
            "Manajemen tata praja pemerintahan, administrasi kependudukan, pembinaan ketenteraman dan ketertiban, serta pertanahan",
            "Pengelolaan inventarisasi belanja barang dan pencatatan buku kas umum desa",
            "Penyusunan rancangan anggaran pendapatan dan belanja desa tahunan",
            "Pembinaan posyandu dan urusan perlindungan ibu dan anak"
        ],
        "answer": 0,
        "explanation": "Pasal 9 ayat (2) Permendagri No. 84 Tahun 2015 mengatur bahwa Kepala Seksi Pemerintahan mempunyai fungsi melaksanakan manajemen tata praja pemerintahan, menyusun rancangan regulasi desa, pembinaan ketenteraman dan ketertiban, pelaksanaan upaya perlindungan masyarakat, kependudukan, penataan dan pengelolaan wilayah, serta pendataan dan pengelolaan profil desa.",
        "source": "Permendagri No. 84 Tahun 2015 Pasal 9 ayat (2)",
        "sourceType": "regulasi"
    },
    {
        "id": 102,
        "number": 102,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "sedang",
        "question": "Kepala Seksi (Kasi) Kesejahteraan bertugas membantu Kepala Desa dalam urusan pembangunan sarana prasarana perdesaan, pembangunan bidang kesehatan, serta...",
        "options": [
            "Pembangunan bidang pendidikan, kebudayaan, dan pembinaan keagamaan di desa",
            "Penetapan sanksi denda adat dan pemakzulan kepala dusun",
            "Penagihan pajak bumi dan bangunan sektor perkebunan swasta",
            "Pengelolaan pembukuan buku kas pembantu kegiatan belanja modal"
        ],
        "answer": 0,
        "explanation": "Berdasarkan Permendagri No. 84 Tahun 2015 Pasal 9 ayat (3), Kepala Seksi Kesejahteraan bertugas melaksanakan pembangunan sarana prasarana perdesaan, pembangunan bidang pendidikan, kesehatan, serta sosialisasi dan motivasi masyarakat di bidang budaya, ekonomi, politik, lingkungan hidup, dan keagamaan.",
        "source": "Permendagri No. 84 Tahun 2015 Pasal 9 ayat (3)",
        "sourceType": "regulasi"
    },
    {
        "id": 103,
        "number": 103,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "sedang",
        "question": "Pelaksanaan tugas operasional pelayanan masyarakat, pencatatan pernikahan/kematian, pembinaan kemasyarakatan, dan pemberdayaan perempuan menjadi tugas pokok dari...",
        "options": [
            "Kepala Seksi Pelayanan",
            "Kepala Urusan Keuangan",
            "Sekretaris BPD",
            "Koordinator Satgas Linmas"
        ],
        "answer": 0,
        "explanation": "Pasal 9 ayat (4) Permendagri No. 84 Tahun 2015 menyebutkan Kepala Seksi Pelayanan memiliki fungsi melaksanakan penyuluhan dan motivasi terhadap hak dan kewajiban masyarakat, meningkatkan partisipasi masyarakat, pelayanan masyarakat, dan pembinaan kemasyarakatan.",
        "source": "Permendagri No. 84 Tahun 2015 Pasal 9 ayat (4)",
        "sourceType": "regulasi"
    },
    {
        "id": 104,
        "number": 104,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "sedang",
        "question": "Kepala Urusan Tata Usaha dan Umum berkedudukan sebagai staf sekretariat desa yang membidangi...",
        "options": [
            "Tata naskah dinas, penomoran surat, kearsipan, ekspedisi, dan penyediaan perlengkapan kantor desa",
            "Pelaksanaan lelang terbuka tanah bengkok milik desa",
            "Penyidikan perkara tindak pidana ringan di wilayah desa",
            "Pengawasan kepatuhan hukum anggota dewan permusyawaratan desa"
        ],
        "answer": 0,
        "explanation": "Berdasarkan Permendagri No. 84 Tahun 2015 Pasal 8 ayat (2), Kaur Tata Usaha dan Umum bertugas dalam urusan ketatausahaan seperti tata naskah dinas, administrasi surat menyurat, arsip, ekspedisi, serta penataan perlengkapan dan kebersihan kantor desa.",
        "source": "Permendagri No. 84 Tahun 2015 Pasal 8 ayat (2)",
        "sourceType": "regulasi"
    },
    {
        "id": 105,
        "number": 105,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "sedang",
        "question": "Urusan penatausahaan administrasi keuangan, penerimaan kas, pembukuan bukti transaksi, dan penyusunan laporan pertanggungjawaban realisasi kas dipegang oleh...",
        "options": [
            "Kepala Urusan Keuangan",
            "Kepala Seksi Pemerintahan",
            "Sekretaris Kecamatan",
            "Ketua Lembaga Pemberdayaan Masyarakat"
        ],
        "answer": 0,
        "explanation": "Kaur Keuangan berkedudukan di bawah Sekretariat Desa dan bertugas melaksanakan urusan keuangan seperti pengurusan administrasi keuangan, pembukuan, dan penerimaan serta pengeluaran kas desa.",
        "source": "Permendagri No. 84 Tahun 2015 Pasal 8 ayat (3); Permendagri No. 20 Tahun 2018",
        "sourceType": "regulasi"
    },
    {
        "id": 106,
        "number": 106,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "sedang",
        "question": "Menyusun draf rencana APB Desa, menginventarisasi data-data pembangunan, serta melakukan evaluasi dan monitoring program pembangunan desa adalah tugas dari...",
        "options": [
            "Kepala Urusan Perencanaan",
            "Kepala Dusun Wilayah II",
            "Pendamping Lokal Desa",
            "Inspektorat Kabupaten"
        ],
        "answer": 0,
        "explanation": "Pasal 8 ayat (4) Permendagri No. 84 Tahun 2015 mengatur Kaur Perencanaan bertugas menyusun rencana APB Desa, menginventarisasi data pembangunan, monitoring dan evaluasi, serta penyusunan laporan pembangunan.",
        "source": "Permendagri No. 84 Tahun 2015 Pasal 8 ayat (4)",
        "sourceType": "regulasi"
    },
    {
        "id": 107,
        "number": 107,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "mudah",
        "question": "Berdasarkan Putusan Mahkamah Konstitusi (MK) Nomor 128/PUU-XIII/2015 terkait syarat pendaftaran calon Perangkat Desa, ketentuan yang telah dibatalkan adalah...",
        "options": [
            "Kewajiban bertempat tinggal di desa setempat paling kurang 1 (satu) tahun sebelum pendaftaran",
            "Syarat batas usia minimal 20 tahun dan maksimal 42 tahun",
            "Syarat memiliki ijazah minimal SMU atau sederajat",
            "Kewajiban berkelakuan baik yang dibuktikan dengan SKCK"
        ],
        "answer": 0,
        "explanation": "Putusan Mahkamah Konstitusi Nomor 128/PUU-XIII/2015 membatalkan syarat bahwa calon perangkat desa harus terdaftar sebagai penduduk desa setempat minimal 1 tahun, sehingga seluruh warga negara Indonesia berhak mendaftar di mana pun.",
        "source": "Putusan Mahkamah Konstitusi RI No. 128/PUU-XIII/2015; Permendagri No. 67 Tahun 2017",
        "sourceType": "regulasi"
    },
    {
        "id": 108,
        "number": 108,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "mudah",
        "question": "Sesuai Undang-Undang Nomor 7 Tahun 2017 tentang Pemilu dan UU Desa, keterlibatan Perangkat Desa dalam tahapan kampanye pemilu dan pilkada diatur dengan ketentuan...",
        "options": [
            "Dilarang keras ikut serta dan/atau terlibat sebagai pelaksana atau tim kampanye",
            "Boleh ikut serta asalkan memakai pakaian bebas di luar jam dinas kantor",
            "Boleh menjadi juru kampanye resmi jika calon kepala daerah masih kerabat",
            "Wajib memobilisasi warga desa untuk memilih salah satu pasangan calon"
        ],
        "answer": 0,
        "explanation": "Pasal 280 ayat (2) UU No. 7 Tahun 2017 dan UU Desa secara mutlak melarang perangkat desa diikutsertakan atau melibatkan diri sebagai tim/pelaksana kampanye pemilu demi menjaga netralitas aparatur.",
        "source": "UU No. 7 Tahun 2017 tentang Pemilu Pasal 280; UU No. 6 Tahun 2014 Pasal 51",
        "sourceType": "regulasi"
    },
    {
        "id": 109,
        "number": 109,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "sedang",
        "question": "Apabila terjadi kekosongan formasi jabatan perangkat desa (misalnya meninggal dunia atau berhenti), Kepala Desa dapat menunjuk Pelaksana Tugas (Plt) yang berasal dari...",
        "options": [
            "Perangkat desa lain yang masih aktif di desa setempat",
            "Warga sipil mana saja yang ditunjuk secara lisan oleh kades",
            "Anggota BPD yang sedang menjabat aktif",
            "Ketua RT atau Ketua RW setempat tanpa surat penugasan"
        ],
        "answer": 0,
        "explanation": "Permendagri No. 67 Tahun 2017 Pasal 9 mengatur bahwa untuk mengisi kekosongan jabatan perangkat desa, Kepala Desa menunjuk Pelaksana Tugas (Plt) dari perangkat desa yang masih aktif sampai terisinya pejabat definitif.",
        "source": "Permendagri No. 67 Tahun 2017 Pasal 9",
        "sourceType": "regulasi"
    },
    {
        "id": 110,
        "number": 110,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "sedang",
        "question": "Surat resmi yang diterbitkan oleh Kepala Desa untuk menugaskan seorang perangkat desa merangkap sebagai Pelaksana Tugas (Plt) adalah...",
        "options": [
            "Surat Perintah Tugas (Surat Perintah Pelaksana Tugas)",
            "Surat Izin Mengemudi Dinas",
            "Surat Rekomendasi Politik",
            "Surat Keterangan Berkelakuan Baik"
        ],
        "answer": 0,
        "explanation": "Penunjukan Plt perangkat desa ditetapkan oleh Kepala Desa menggunakan Surat Perintah Tugas yang tembusannya disampaikan kepada Camat.",
        "source": "Petunjuk Teknis Administrasi Kepegawaian Desa Permendagri No. 67 Tahun 2017",
        "sourceType": "regulasi"
    },
    {
        "id": 111,
        "number": 111,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "sedang",
        "question": "Pemberian cuti bagi Perangkat Desa menurut ketentuan peraturan perundang-undangan menjadi wewenang dan ditetapkan oleh...",
        "options": [
            "Kepala Desa",
            "Ketua BPD",
            "Dinas Tenaga Kerja Provinsi",
            "Gubernur Jawa Timur"
        ],
        "answer": 0,
        "explanation": "Kepala Desa berwenang memberikan izin cuti (tahunan, sakit, bersalin, alasan penting, atau ibadah keagamaan) kepada perangkat desa sesuai regulasi pembinaan aparatur desa.",
        "source": "Permendagri No. 83 Tahun 2015 jo. Permendagri No. 67 Tahun 2017",
        "sourceType": "regulasi"
    },
    {
        "id": 112,
        "number": 112,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "sedang",
        "question": "Seorang Perangkat Desa yang mendaftar dan mencalonkan diri dalam Pemilihan Kepala Desa (Pilkades) wajib...",
        "options": [
            "Mengajukan cuti terhitung sejak ditetapkan sebagai calon kepala desa sampai selesainya proses pemilihan",
            "Mengundurkan diri secara permanen dan kehilangan hak kembali sebagai perangkat desa",
            "Tetap bertugas seperti biasa tanpa perlu melapor kepada siapa pun",
            "Menyerahkan seluruh gajinya kepada panitia pilkades"
        ],
        "answer": 0,
        "explanation": "Sesuai Permendagri No. 112 Tahun 2014 jo. Permendagri No. 65 Tahun 2017, perangkat desa yang mencalonkan diri dalam Pilkades wajib mengambil cuti sejak ditetapkan sebagai calon kades hingga penetapan hasil akhir.",
        "source": "Permendagri No. 112 Tahun 2014 tentang Pemilihan Kepala Desa",
        "sourceType": "regulasi"
    },
    {
        "id": 113,
        "number": 113,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "sulit",
        "question": "Jika seorang Perangkat Desa mendaftar sebagai calon anggota legislatif (DPR/DPD/DPRD), kewajiban hukum yang harus dipenuhi adalah...",
        "options": [
            "Mengundurkan diri secara tetap sejak ditetapkan sebagai calon dalam Daftar Calon Tetap (DCT)",
            "Cukup mengambil cuti di luar tanggungan negara selama 3 bulan",
            "Boleh merangkap jabatan asalkan gaji perangkat desa disumbangkan ke panti asuhan",
            "Meminta izin lisan kepada camat tanpa surat keputusan pemberhentian"
        ],
        "answer": 0,
        "explanation": "UU Pemilu dan UU Desa Pasal 51 mewajibkan perangkat desa mengundurkan diri secara permanen dan diberhentikan dengan hormat oleh Kepala Desa saat maju sebagai calon legislatif.",
        "source": "UU No. 7 Tahun 2017; UU No. 6 Tahun 2014 Pasal 51 huruf f",
        "sourceType": "regulasi"
    },
    {
        "id": 114,
        "number": 114,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "sedang",
        "question": "Kepala Desa dapat melakukan mutasi jabatan antarperangkat desa (misalnya Kepala Urusan menjadi Kepala Seksi) dengan syarat...",
        "options": [
            "Telah melalui proses evaluasi kinerja dan memperoleh rekomendasi tertulis dari Camat",
            "Cukup disepakati dalam obrolan informal bersama keluarga kepala desa",
            "Menunggu izin tertulis dari Menteri Dalam Negeri di Jakarta",
            "Memungut biaya administrasi mutasi dari perangkat desa yang bersangkutan"
        ],
        "answer": 0,
        "explanation": "Berdasarkan Permendagri No. 67 Tahun 2017 Pasal 7 ayat (5), mutasi jabatan perangkat desa dilakukan berdasarkan pertimbangan kompetensi/kebutuhan organisasi setelah berkonsultasi dan memperoleh rekomendasi tertulis Camat.",
        "source": "Permendagri No. 67 Tahun 2017 Pasal 7 ayat (5)",
        "sourceType": "regulasi"
    },
    {
        "id": 115,
        "number": 115,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "mudah",
        "question": "Pemberian sanksi administratif berupa teguran tertulis kepada Perangkat Desa diterbitkan oleh...",
        "options": [
            "Kepala Desa",
            "Ketua RW setempat",
            "Panitia Seleksi Perangkat Desa",
            "Lembaga Bantuan Hukum Kabupaten"
        ],
        "answer": 0,
        "explanation": "Kepala Desa berwenang melakukan pembinaan kedisiplinan dan menjatuhkan sanksi administratif (teguran lisan maupun tertulis) kepada perangkat desa.",
        "source": "Permendagri No. 67 Tahun 2017 Pasal 7",
        "sourceType": "regulasi"
    },
    {
        "id": 116,
        "number": 116,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "sedang",
        "question": "Dokumen resmi yang menjadi bukti penyerahan barang inventaris, arsip berkas dinas, dan laporan keuangan pada saat pergantian perangkat desa adalah...",
        "options": [
            "Berita Acara Serah Terima Jabatan (BASTJ)",
            "Kuitansi Tanda Terima Uang Saku",
            "Surat Pernyataan Pelepasan Hak Waris",
            "Surat Keterangan Catatan Kepolisian"
        ],
        "answer": 0,
        "explanation": "Serah terima aset, dokumen, dan kewenangan kedinasan dari perangkat desa lama kepada pengganti atau Plt wajib dituangkan dalam Berita Acara Serah Terima Jabatan yang ditandatangani kedua belah pihak dan diketahui Kepala Desa.",
        "source": "Pedoman Tata Administrasi Penatausahaan Jabatan Desa",
        "sourceType": "administrasi"
    },
    {
        "id": 117,
        "number": 117,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "sulit",
        "question": "Apabila Perangkat Desa dijatuhi vonis pidana penjara minimal 5 tahun berdasarkan putusan pengadilan yang telah berkekuatan hukum tetap (inkrah), Kepala Desa wajib menerbitkan SK pemberhentian paling lambat dalam waktu...",
        "options": [
            "14 (empat belas) hari kerja setelah salinan putusan diterima",
            "3 (tiga) bulan kalender",
            "Menunggu sampai masa jabatan kepala desa berakhir",
            "1 (satu) tahun setelah vonis dijatuhkan"
        ],
        "answer": 0,
        "explanation": "Berdasarkan Permendagri No. 67 Tahun 2017 Pasal 6, paling lambat 14 hari kerja setelah putusan pengadilan berkekuatan hukum tetap diterima, Kepala Desa wajib memberhentikan tetap perangkat desa tersebut.",
        "source": "Permendagri No. 67 Tahun 2017 Pasal 6 ayat (5)",
        "sourceType": "regulasi"
    },
    {
        "id": 118,
        "number": 118,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "mudah",
        "question": "Pemberian nomor induk aparatur pemerintah desa atau Nomor Registrasi Perangkat Desa diterbitkan oleh...",
        "options": [
            "Pemerintah Daerah Kabupaten melalui Dinas PMD / Bupati",
            "Kantor Pelayanan Pajak Pratama",
            "Badan Pusat Statistik Provinsi",
            "Kantor Imigrasi Wilayah"
        ],
        "answer": 0,
        "explanation": "Pemerintah Daerah Kabupaten menerbitkan Nomor Induk Perangkat Desa (NIPD) atau kode registrasi perangkat desa sebagai basis data pembinaan aparatur desa dan penyaluran siltap.",
        "source": "Kebijakan Tata Kelola Administrasi Aparatur Desa Pemkab Tuban / Kemendagri",
        "sourceType": "regulasi"
    },
    {
        "id": 119,
        "number": 119,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "sedang",
        "question": "Pemberhentian sementara perangkat desa dicabut dan yang bersangkutan direhabilitasi/diaktifkan kembali apabila...",
        "options": [
            "Pengadilan memutus bebas atau tidak terbukti bersalah dan putusan telah berkekuatan hukum tetap (inkrah)",
            "Keluarga perangkat desa membayar uang jaminan ke balai desa",
            "Mendapat dukungan petisi dari sebagian warga dusun",
            "Tersangka melarikan diri ke luar kota dan tidak tertangkap"
        ],
        "answer": 0,
        "explanation": "Pasal 6 ayat (4) Permendagri No. 67 Tahun 2017 menegaskan jika perangkat desa yang diberhentikan sementara dinyatakan tidak terbukti bersalah berdasarkan putusan pengadilan yang inkrah, Kepala Desa wajib merehabilitasi dan mengaktifkan kembali jabatannya.",
        "source": "Permendagri No. 67 Tahun 2017 Pasal 6 ayat (4)",
        "sourceType": "regulasi"
    },
    {
        "id": 120,
        "number": 120,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "sedang",
        "question": "Hubungan kerja antara Kepala Dusun (Pelaksana Kewilayahan) dengan Kepala Desa adalah...",
        "options": [
            "Bersifat subordinasi hierarkis, di mana Kepala Dusun membantu kades mengoordinasikan penyelenggaraan pemerintahan di wilayah dusunnya",
            "Setara dan independen seperti hubungan antarnegara bagian",
            "Kepala Dusun berhak membatalkan keputusan kepala desa di wilayah dusunnya",
            "Kepala Dusun hanya melapor kepada BPD tanpa berkoordinasi dengan kades"
        ],
        "answer": 0,
        "explanation": "Kepala Dusun merupakan satuan tugas kewilayahan yang membantu Kepala Desa dalam pelaksanaan tugas dan kewenangannya di wilayah kerjanya, serta bertanggung jawab kepada Kepala Desa.",
        "source": "Permendagri No. 84 Tahun 2015 Pasal 10",
        "sourceType": "regulasi"
    },

    # =========================================================================
    # Kategori 2: Peraturan perundang-undangan dan tata kelola pemerintahan (12 Soal Tambahan: ID 121 - 132)
    # =========================================================================
    {
        "id": 121,
        "number": 121,
        "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
        "difficulty": "mudah",
        "question": "Asas penyelenggaraan pemerintahan desa yang membuka diri terhadap hak masyarakat untuk memperoleh informasi yang benar, jujur, dan tidak diskriminatif disebut asas...",
        "options": [
            "Keterbukaan",
            "Sentralistik",
            "Kerahasiaan Jabatan",
            "Konsensus Elit"
        ],
        "answer": 0,
        "explanation": "Penjelasan Pasal 24 UU No. 6 Tahun 2014 menjelaskan bahwa Asas Keterbukaan adalah asas yang membuka diri terhadap hak masyarakat untuk memperoleh informasi yang benar, jujur, dan tidak diskriminatif tentang penyelenggaraan pemerintahan desa.",
        "source": "UU No. 6 Tahun 2014 Pasal 24 huruf d",
        "sourceType": "regulasi"
    },
    {
        "id": 122,
        "number": 122,
        "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
        "difficulty": "sedang",
        "question": "Kewenangan yang dimiliki desa berdasarkan hak asal-usul yang diakui oleh negara disebut kewenangan...",
        "options": [
            "Rekognisi",
            "Delegasi Penuh",
            "Mandat Khusus",
            "Dekonsentrasi"
        ],
        "answer": 0,
        "explanation": "Asas Rekognisi adalah pengakuan terhadap hak asal-usul desa, adat istiadat, dan hak tradisional yang masih hidup dalam masyarakat desa.",
        "source": "UU No. 6 Tahun 2014 Pasal 3 huruf a dan Pasal 19",
        "sourceType": "regulasi"
    },
    {
        "id": 123,
        "number": 123,
        "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
        "difficulty": "sedang",
        "question": "Kewenangan desa untuk mengatur dan mengurus kepentingan masyarakat setempat yang diputuskan sendiri oleh desa dinamakan...",
        "options": [
            "Kewenangan lokal berskala desa",
            "Kewenangan imperatif kementerian",
            "Kewenangan koersif kepolisian",
            "Kewenangan yudisial mahkamah agung"
        ],
        "answer": 0,
        "explanation": "Berdasarkan UU Desa, kewenangan desa meliputi kewenangan berdasarkan hak asal-usul dan kewenangan lokal berskala desa (subsidiaritas).",
        "source": "UU No. 6 Tahun 2014 Pasal 19 huruf b",
        "sourceType": "regulasi"
    },
    {
        "id": 124,
        "number": 124,
        "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
        "difficulty": "sedang",
        "question": "Produk hukum berupa Peraturan Bersama Kepala Desa (Permakades) diterbitkan apabila...",
        "options": [
            "Dua desa atau lebih menyepakati kerja sama antardesa dalam pembangunan sarana bersama atau pelayanan lintas batas",
            "Kepala desa ingin mengganti seluruh pengurus RT tanpa musyawarah",
            "Kepala desa membatalkan surat keputusan camat",
            "Desa mengalami kekosongan anggaran belanja modal"
        ],
        "answer": 0,
        "explanation": "Permendagri No. 111 Tahun 2014 Pasal 2 mengatur bahwa Peraturan Bersama Kepala Desa adalah peraturan yang ditetapkan oleh dua atau lebih Kepala Desa dalam rangka kerja sama antardesa.",
        "source": "Permendagri No. 111 Tahun 2014 Pasal 2",
        "sourceType": "regulasi"
    },
    {
        "id": 125,
        "number": 125,
        "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
        "difficulty": "sulit",
        "question": "Bupati/Walikota berwenang membatalkan Peraturan Desa (Perdes) apabila...",
        "options": [
            "Perdes tersebut bertentangan dengan kepentingan umum dan/atau peraturan perundang-undangan yang lebih tinggi",
            "Bupati berasal dari partai politik yang berbeda dengan Kepala Desa",
            "Kepala desa tidak menghadiri acara seremonial di pendopo kabupaten",
            "Anggota BPD tidak menyukai gaya kepemimpinan sekretaris desa"
        ],
        "answer": 0,
        "explanation": "Berdasarkan UU No. 6 Tahun 2014 Pasal 69 jo. Permendagri No. 111 Tahun 2014, bupati membatalkan Perdes apabila bertentangan dengan kepentingan umum dan peraturan perundang-undangan yang lebih tinggi.",
        "source": "UU No. 6 Tahun 2014 Pasal 69 ayat (4); Permendagri No. 111 Tahun 2014",
        "sourceType": "regulasi"
    },
    {
        "id": 126,
        "number": 126,
        "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
        "difficulty": "sedang",
        "question": "Fungsi Camat dalam sistem pembinaan dan pengawasan (Binwas) terhadap desa adalah...",
        "options": [
            "Memfasilitasi penyusunan peraturan desa, tata kelola keuangan, dan memberikan evaluasi rancangan APB Desa",
            "Mengambil alih seluruh pengelolaan keuangan kas desa secara langsung",
            "Menunjuk langsung calon perangkat desa tanpa melalui ujian seleksi",
            "Menjabat sebagai ketua musyawarah desa di setiap desa wilayahnya"
        ],
        "answer": 0,
        "explanation": "PP No. 43/2014 Pasal 154 mengatur Camat melakukan pembinaan dan pengawasan desa, memfasilitasi administrasi tata pemerintahan desa, dan mengevaluasi rancangan Perdes APB Desa.",
        "source": "PP No. 43 Tahun 2014 Pasal 154",
        "sourceType": "regulasi"
    },
    {
        "id": 127,
        "number": 127,
        "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
        "difficulty": "sedang",
        "question": "Peraturan Daerah Kabupaten Tuban Nomor 16 Tahun 2021 merupakan perubahan kedua atas...",
        "options": [
            "Peraturan Daerah Kabupaten Tuban Nomor 2 Tahun 2016 tentang Perangkat Desa",
            "Peraturan Daerah Kabupaten Tuban Nomor 1 Tahun 2005 tentang Pedagang Kaki Lima",
            "Peraturan Daerah Kabupaten Tuban Nomor 7 Tahun 2011 tentang Pajak Daerah",
            "Peraturan Daerah Kabupaten Tuban Nomor 9 Tahun 2013 tentang Bangunan Gedung"
        ],
        "answer": 0,
        "explanation": "Perda Tuban No. 16 Tahun 2021 secara resmi merupakan Perubahan Kedua atas Peraturan Daerah Kabupaten Tuban Nomor 2 Tahun 2016 tentang Perangkat Desa.",
        "source": "JDIH Kabupaten Tuban: Perda Kab. Tuban No. 16 Tahun 2021",
        "sourceType": "regulasi"
    },
    {
        "id": 128,
        "number": 128,
        "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
        "difficulty": "sedang",
        "question": "Media publikasi resmi tempat pengundangan Peraturan Kepala Desa (Perkades) dan Peraturan Bersama Kepala Desa (Permakades) adalah...",
        "options": [
            "Berita Desa",
            "Lembaran Daerah Kabupaten",
            "Surat Kabar Komersial Nasional",
            "Papan Pengumuman Pos Kamling"
        ],
        "answer": 0,
        "explanation": "Berdasarkan Permendagri No. 111 Tahun 2014 Pasal 21, Perdes diundangkan dalam Lembaran Desa, sedangkan Perkades dan Permakades diundangkan dalam Berita Desa oleh Sekretaris Desa.",
        "source": "Permendagri No. 111 Tahun 2014 Pasal 21",
        "sourceType": "regulasi"
    },
    {
        "id": 129,
        "number": 129,
        "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
        "difficulty": "mudah",
        "question": "Pernyataan komitmen tertulis dari penyelenggara pelayanan publik di kantor desa yang memuat janji penyelenggaraan pelayanan sesuai standar pelayanan disebut...",
        "options": [
            "Maklumat Pelayanan",
            "Piagam Penghargaan",
            "Surat Teguran Dinas",
            "Nota Kesepahaman Rahasia"
        ],
        "answer": 0,
        "explanation": "UU No. 25 Tahun 2009 tentang Pelayanan Publik mewajibkan setiap unit penyelenggara pelayanan menyusun dan mempublikasikan Maklumat Pelayanan sebagai wujud kepastian hak masyarakat.",
        "source": "UU No. 25 Tahun 2009 tentang Pelayanan Publik",
        "sourceType": "regulasi"
    },
    {
        "id": 130,
        "number": 130,
        "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
        "difficulty": "sedang",
        "question": "Asas yang mengutamakan keahlian berlandaskan kode etik dan ketentuan peraturan perundang-undangan dalam bekerja sebagai perangkat desa disebut asas...",
        "options": [
            "Profesionalitas",
            "Kekeluargaan Semata",
            "Senioritas Mutlak",
            "Spontanitas"
        ],
        "answer": 0,
        "explanation": "Asas Profesionalitas dalam UU Desa mengutamakan keahlian yang berlandaskan kode etik dan ketentuan peraturan perundang-undangan.",
        "source": "UU No. 6 Tahun 2014 Pasal 24 huruf f",
        "sourceType": "regulasi"
    },
    {
        "id": 131,
        "number": 131,
        "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
        "difficulty": "sulit",
        "question": "Klarifikasi dan evaluasi rancangan peraturan desa tentang APB Desa oleh Bupati/Walikota melalui Camat dilakukan dalam jangka waktu paling lama...",
        "options": [
            "20 (dua puluh) hari kerja sejak rancangan diterima",
            "60 (enam puluh) hari kalender",
            "6 (enam) bulan berjalan",
            "3 (tiga) hari kerja"
        ],
        "answer": 0,
        "explanation": "Berdasarkan Permendagri No. 20 Tahun 2018 Pasal 38, evaluasi rancangan Perdes APB Desa oleh bupati/camat dilaksanakan paling lama 20 hari kerja sejak rancangan diterima.",
        "source": "Permendagri No. 20 Tahun 2018 Pasal 38",
        "sourceType": "regulasi"
    },
    {
        "id": 132,
        "number": 132,
        "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
        "difficulty": "sedang",
        "question": "Prinsip tata kelola pemerintahan desa yang menekankan keseimbangan antara hak dan kewajiban penyelenggara desa disebut asas...",
        "options": [
            "Proporsionalitas",
            "Oportunitas",
            "Legalitas Bebas",
            "Subordinasi Penuh"
        ],
        "answer": 0,
        "explanation": "Asas Proporsionalitas adalah asas yang mengutamakan keseimbangan antara hak dan kewajiban penyelenggara pemerintahan desa.",
        "source": "UU No. 6 Tahun 2014 Pasal 24 huruf e",
        "sourceType": "regulasi"
    },

    # =========================================================================
    # Kategori 3: Pancasila, UUD 1945, dan wawasan kebangsaan (10 Soal Tambahan: ID 133 - 142)
    # =========================================================================
    {
        "id": 133,
        "number": 133,
        "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
        "difficulty": "mudah",
        "question": "Jaminan konstitusional bahwa negara menjamin kemerdekaan tiap-tiap penduduk untuk memeluk agamanya masing-masing dan beribadat menurut agamanya tertuang dalam UUD 1945...",
        "options": [
            "Pasal 29 ayat (2)",
            "Pasal 33 ayat (1)",
            "Pasal 34 ayat (2)",
            "Pasal 36A"
        ],
        "answer": 0,
        "explanation": "Pasal 29 ayat (2) UUD 1945 menegaskan: 'Negara menjamin kemerdekaan tiap-tiap penduduk untuk memeluk agamanya masing-masing dan untuk beribadat menurut agamanya dan kepercayaannya itu.'",
        "source": "UUD NRI Tahun 1945 Pasal 29 ayat (2)",
        "sourceType": "wawasan"
    },
    {
        "id": 134,
        "number": 134,
        "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
        "difficulty": "sedang",
        "question": "Gemar melakukan kegiatan kemanusiaan, seperti membantu evakuasi korban banjir dan menyantuni anak yatim desa, merupakan perwujudan pengamalan Pancasila Sila...",
        "options": [
            "Kedua: Kemanusiaan yang Adil dan Beradab",
            "Ketiga: Persatuan Indonesia",
            "Keempat: Kerakyatan yang Dipimpin oleh Hikmat Kebijaksanaan",
            "Pertama: Ketuhanan Yang Maha Esa"
        ],
        "answer": 0,
        "explanation": "Mengembangkan sikap saling mencintai sesama manusia dan gemar melakukan kegiatan kemanusiaan merupakan butir pengamalan Sila Kedua Pancasila.",
        "source": "Pedoman Penghayatan dan Pengamalan Pancasila Sila Ke-2",
        "sourceType": "wawasan"
    },
    {
        "id": 135,
        "number": 135,
        "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
        "difficulty": "mudah",
        "question": "Rela berkorban untuk kepentingan bangsa dan negara di atas kepentingan pribadi atau kelompok di tingkat desa mencerminkan nilai luhur Sila...",
        "options": [
            "Ketiga: Persatuan Indonesia",
            "Pertama",
            "Kedua",
            "Kelima"
        ],
        "answer": 0,
        "explanation": "Rela berkorban demi kepentingan negara dan bangsa bila diperlukan adalah perwujudan langsung Sila Ketiga: Persatuan Indonesia.",
        "source": "Pedoman Pengamalan Pancasila Sila Ke-3",
        "sourceType": "wawasan"
    },
    {
        "id": 136,
        "number": 136,
        "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
        "difficulty": "mudah",
        "question": "Dalam forum musyawarah desa, tidak boleh memaksakan kehendak kepada orang lain dan wajib menghormati perbedaan pendapat. Hal ini sesuai dengan Sila...",
        "options": [
            "Keempat: Kerakyatan yang Dipimpin oleh Hikmat Kebijaksanaan dalam Permusyawaratan/Perwakilan",
            "Kedua",
            "Ketiga",
            "Kelima"
        ],
        "answer": 0,
        "explanation": "Tidak memaksakan kehendak dan mengutamakan musyawarah mufakat merupakan inti dari Sila Keempat Pancasila.",
        "source": "Pedoman Pengamalan Pancasila Sila Ke-4",
        "sourceType": "wawasan"
    },
    {
        "id": 137,
        "number": 137,
        "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
        "difficulty": "sedang",
        "question": "Mengembangkan pola hidup sederhana, menghargai hasil karya orang lain, serta tidak melakukan pemerasan terhadap warga desa adalah cerminan Sila...",
        "options": [
            "Kelima: Keadilan Sosial bagi Seluruh Rakyat Indonesia",
            "Pertama",
            "Ketiga",
            "Keempat"
        ],
        "answer": 0,
        "explanation": "Suka menghargai hasil karya orang lain dan tidak bergaya hidup mewah atau boros adalah butir pengamalan Sila Kelima Pancasila.",
        "source": "Pedoman Pengamalan Pancasila Sila Ke-5",
        "sourceType": "wawasan"
    },
    {
        "id": 138,
        "number": 138,
        "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
        "difficulty": "sedang",
        "question": "Ketentuan Pasal 18B ayat (2) UUD 1945 mengatur pengakuan negara terhadap...",
        "options": [
            "Kesatuan-kesatuan masyarakat hukum adat beserta hak-hak tradisionalnya sepanjang masih hidup dan sesuai perkembangan masyarakat dan prinsip NKRI",
            "Sistem monarki absolut di seluruh pulau-pulau terluar",
            "Kekuasaan militer dalam menentukan batas batas desa",
            "Hak veto kepala desa dalam membatalkan undang-undang"
        ],
        "answer": 0,
        "explanation": "Pasal 18B ayat (2) UUD 1945 menyatakan negara mengakui dan menghormati kesatuan masyarakat hukum adat beserta hak tradisionalnya.",
        "source": "UUD NRI Tahun 1945 Pasal 18B ayat (2)",
        "sourceType": "wawasan"
    },
    {
        "id": 139,
        "number": 139,
        "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
        "difficulty": "mudah",
        "question": "Landasan konstitusional demokrasi ekonomi Indonesia yang menyatakan bahwa perekonomian disusun sebagai usaha bersama berdasar atas asas kekeluargaan tercantum dalam UUD 1945...",
        "options": [
            "Pasal 33 ayat (1)",
            "Pasal 27 ayat (2)",
            "Pasal 31 ayat (1)",
            "Pasal 34 ayat (3)"
        ],
        "answer": 0,
        "explanation": "Pasal 33 ayat (1) UUD 1945 berbunyi: 'Perekonomian disusun sebagai usaha bersama berdasar atas asas kekeluargaan.'",
        "source": "UUD NRI Tahun 1945 Pasal 33 ayat (1)",
        "sourceType": "wawasan"
    },
    {
        "id": 140,
        "number": 140,
        "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
        "difficulty": "sedang",
        "question": "Unsur konstitutif mutlak berdirinya suatu negara hukum menurut hukum tata negara internasional meliputi...",
        "options": [
            "Rakyat, wilayah tertentu, dan pemerintah yang berdaulat",
            "Pasukan tentara perang adidaya, cadangan emas melimpah, dan gedung pencakar langit",
            "Keanggotaan tetap Dewan Keamanan PBB dan kepemilikan senjata nuklir",
            "Perjanjian utang piutang luar negeri dan sistem perbankan global"
        ],
        "answer": 0,
        "explanation": "Unsur konstitutif berdirinya negara adalah rakyat, wilayah tertentu, dan pemerintah yang berdaulat, sedangkan pengakuan negara lain merupakan unsur deklaratif.",
        "source": "Konvensi Montevideo 1933; Pengantar Ilmu Hukum Tata Negara",
        "sourceType": "wawasan"
    },
    {
        "id": 141,
        "number": 141,
        "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
        "difficulty": "sedang",
        "question": "Lima nilai dasar Bela Negara yang dikembangkan Kementerian Pertahanan Republik Indonesia meliputi: Cinta tanah air, sadar berbangsa dan bernegara, rela berkorban untuk bangsa dan negara, mempunyai kemampuan awal bela negara, serta...",
        "options": [
            "Setia pada Pancasila sebagai ideologi negara",
            "Siap memegang senjata laras panjang setiap hari",
            "Memutuskan hubungan perdagangan internasional",
            "Menolak seluruh produk teknologi buatan luar negeri"
        ],
        "answer": 0,
        "explanation": "Lima nilai dasar bela negara adalah: 1. Cinta Tanah Air, 2. Kesadaran Berbangsa dan Bernegara, 3. Setia pada Pancasila sebagai Ideologi Negara, 4. Rela Berkorban untuk Bangsa dan Negara, 5. Kemampuan Awal Bela Negara.",
        "source": "Kementerian Pertahanan RI: Modul Pembinaan Kesadaran Bela Negara",
        "sourceType": "wawasan"
    },
    {
        "id": 142,
        "number": 142,
        "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
        "difficulty": "sedang",
        "question": "Pokok Pikiran Pertama yang termaktub dalam Pembukaan UUD 1945 adalah...",
        "options": [
            "Negara melindungi segenap bangsa Indonesia dan seluruh tumpah darah Indonesia dengan berdasar atas persatuan (Pokok Pikiran Persatuan)",
            "Negara hendak mewujudkan keadilan sosial bagi seluruh rakyat",
            "Negara yang berkedaulatan rakyat berdasar kerakyatan dan permusyawaratan",
            "Negara berdasar atas Ketuhanan Yang Maha Esa menurut dasar kemanusiaan yang adil dan beradab"
        ],
        "answer": 0,
        "explanation": "Pokok Pikiran Pertama Pembukaan UUD 1945 adalah Pokok Pikiran Persatuan (negara kesatuan yang melindungi segenap bangsa dan tumpah darah).",
        "source": "Penjelasan UUD NRI Tahun 1945",
        "sourceType": "wawasan"
    },

    # =========================================================================
    # Kategori 4: Administrasi pemerintahan, surat-menyurat, dan pengarsipan (10 Soal Tambahan: ID 143 - 152)
    # =========================================================================
    {
        "id": 143,
        "number": 143,
        "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
        "difficulty": "sedang",
        "question": "Buku yang digunakan pemerintah desa untuk mencatat peristiwa mutasi kelahiran, kematian, perpindahan penduduk, dan kedatangan penduduk adalah...",
        "options": [
            "Buku Rencana Mutasi Penduduk Desa",
            "Buku Kas Pembantu Pajak",
            "Buku Ekspedisi Rahasia",
            "Buku Agenda Peraturan Desa"
        ],
        "answer": 0,
        "explanation": "Permendagri No. 47 Tahun 2016 mengatur Buku Mutasi Penduduk sebagai bagian dari Administrasi Penduduk untuk mencatat mutasi lahir, mati, pindah, dan datang.",
        "source": "Permendagri No. 47 Tahun 2016 tentang Administrasi Pemerintahan Desa",
        "sourceType": "administrasi"
    },
    {
        "id": 144,
        "number": 144,
        "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
        "difficulty": "sedang",
        "question": "Menurut Permendagri Nomor 47 Tahun 2016, buku administrasi yang wajib mencatat seluruh rencana pelaksanaan kegiatan pembangunan desa adalah...",
        "options": [
            "Buku Rencana Kerja Pembangunan Desa",
            "Buku Kas Pembantu Kegiatan",
            "Buku Ekspedisi Naskah Dinas",
            "Buku Agenda Surat Masuk"
        ],
        "answer": 0,
        "explanation": "Berdasarkan Permendagri No. 47 Tahun 2016 Lampiran IV, Buku Rencana Kerja Pembangunan Desa adalah buku dalam kelompok Administrasi Pembangunan yang berfungsi mencatat seluruh rencana kerja pembangunan yang akan dilaksanakan di desa pada tahun berjalan.",
        "source": "Permendagri No. 47 Tahun 2016 Lampiran IV",
        "sourceType": "administrasi"
    },
    {
        "id": 145,
        "number": 145,
        "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
        "difficulty": "sedang",
        "question": "Penulisan alamat tujuan surat dinas yang benar dan baku sesuai kaidah tata naskah dinas adalah...",
        "options": [
            "Yth. Camat Merakurak\ndi Tuban",
            "Kepada Yth. Bapak Camat Merakurak\ndi Tempat",
            "Kepada Yth: Camat Merakurak\ndi Tuban.",
            "Yth; Sdr Camat Merakurak\ndi tempat-"
        ],
        "answer": 0,
        "explanation": "Kaidah baku: tidak menggunakan kata pleonasme 'Kepada Yth' (cukup 'Yth.'), tidak menggunakan sebutan 'Bapak' jika diikuti nama jabatan, dan penulisan tempat spesifik bukan 'di Tempat'.",
        "source": "Pedoman Tata Naskah Dinas Instansi Pemerintah & EYD V",
        "sourceType": "kebahasaan"
    },
    {
        "id": 146,
        "number": 146,
        "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
        "difficulty": "mudah",
        "question": "Naskah dinas yang berisi pemberitahuan resmi dari Kepala Desa kepada warga masyarakat atau instansi bawahan mengenai petunjuk teknis tertentu disebut...",
        "options": [
            "Surat Edaran",
            "Surat Gugatan",
            "Surat Kuasa Khusus",
            "Kuitansi Penerimaan"
        ],
        "answer": 0,
        "explanation": "Surat Edaran adalah naskah dinas yang memuat pemberitahuan atau penjelasan teknis tentang hal tertentu yang dianggap mendesak dan penting.",
        "source": "Tata Naskah Dinas Pemerintah Desa",
        "sourceType": "administrasi"
    },
    {
        "id": 147,
        "number": 147,
        "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
        "difficulty": "sedang",
        "question": "Tata cara penulisan tembusan surat dinas resmi di bagian kiri bawah yang benar adalah...",
        "options": [
            "Tembusan:\n1. Bupati Tuban\n2. Camat Jenu",
            "Tembusan disampaikan kepada Yth:\n1. Bapak Bupati Tuban",
            "TEMBUSAN SURAT;\nKepada Yth Bupati",
            "Cc: Bupati Tuban, Camat Jenu"
        ],
        "answer": 0,
        "explanation": "Format baku tembusan: ditulis 'Tembusan:' tanpa kata 'disampaikan kepada Yth.' atau 'Kepada', diikuti penomoran hierarki jabatan pejabat penerima.",
        "source": "Pedoman Tata Naskah Dinas Pemerintah Daerah",
        "sourceType": "administrasi"
    },
    {
        "id": 148,
        "number": 148,
        "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
        "difficulty": "sedang",
        "question": "Pembubuhan cap/stempel dinas pemerintah desa yang benar pada naskah dinas bertanda tangan Kepala Desa adalah...",
        "options": [
            "Dibubuhkan di sebelah kiri tanda tangan dengan sedikit mengenai tanda tangan pejabat yang bersangkutan",
            "Dibubuhkan menutupi seluruh tanda tangan sehingga tanda tangan tidak terbaca",
            "Dibubuhkan di sudut kanan paling atas kertas surat",
            "Dibubuhkan di belakang kertas surat"
        ],
        "answer": 0,
        "explanation": "Sesuai tata naskah dinas, cap dinas dibubuhkan di sebelah kiri tanda tangan dengan menyinggung sedikit (mengenai) garis tanda tangan pejabat penandatangan.",
        "source": "Pedoman Tata Naskah Dinas Pemerintah Kabupaten/Desa",
        "sourceType": "administrasi"
    },
    {
        "id": 149,
        "number": 149,
        "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
        "difficulty": "sedang",
        "question": "Naskah dinas yang membuktikan terjadinya suatu kejadian, musyawarah, peristiwa kerusakan aset, atau transaksi serah terima pekerjaan yang ditandatangani para pihak dan saksi disebut...",
        "options": [
            "Berita Acara",
            "Surat Perintah Kerja",
            "Nota Dinas",
            "Surat Izin Cuti"
        ],
        "answer": 0,
        "explanation": "Berita Acara adalah naskah dinas yang berisi pernyataan tentang terjadinya suatu peristiwa, rapat, transaksi, atau serah terima barang/jabatan.",
        "source": "Pedoman Umum Tata Naskah Dinas",
        "sourceType": "administrasi"
    },
    {
        "id": 150,
        "number": 150,
        "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
        "difficulty": "sedang",
        "question": "Sistem penyimpanan arsip desa berdasarkan kesamaan subjek atau permasalahan surat (misalnya keuangan, pemerintahan, kesejahteraan, kepegawaian) disebut sistem...",
        "options": [
            "Pola Klasifikasi Masalah / Subjek",
            "Pola Abjad Murni Tanpa Kode",
            "Pola Nomor Acak Komputer",
            "Pola Tanggal Acak"
        ],
        "answer": 0,
        "explanation": "Pola klasifikasi masalah (subjek) mengelompokkan arsip dinas berdasarkan pokok urusan/masalah kedinasan menggunakan kode klasifikasi standar.",
        "source": "UU No. 43 Tahun 2009 tentang Kearsipan; Permendagri Klasifikasi Arsip",
        "sourceType": "administrasi"
    },
    {
        "id": 151,
        "number": 151,
        "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
        "difficulty": "mudah",
        "question": "Surat dinas internal yang digunakan oleh Kepala Seksi atau Kepala Urusan untuk menyampaikan laporan atau permohonan disposisi kepada Sekretaris Desa atau Kepala Desa disebut...",
        "options": [
            "Nota Dinas",
            "Surat Edaran Umum",
            "Surat Kuasa Direksi",
            "Lembaran Daerah"
        ],
        "answer": 0,
        "explanation": "Nota Dinas adalah naskah dinas internal antarpejabat dalam satu instansi pemerintah desa untuk menyampaikan telaahan, permohonan, atau laporan singkat.",
        "source": "Tata Naskah Dinas Pemerintahan Desa",
        "sourceType": "administrasi"
    },
    {
        "id": 152,
        "number": 152,
        "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
        "difficulty": "sedang",
        "question": "Penggunaan bahasa dalam surat dinas pemerintahan wajib memenuhi kriteria...",
        "options": [
            "Baku, lugas, santun, tidak berbelit-belit, dan tidak menimbulkan multitafsir",
            "Puitis, penuh kiasan, dan sarat majas hiperbola",
            "Singkat dalam bentuk bahasa gaul atau singkatan tidak resmi",
            "Menggunakan dialek bahasa gaul daerah agar terkesan akrab"
        ],
        "answer": 0,
        "explanation": "Bahasa dinas harus baku, jelas, ringkas, tegas, santun, objektif, dan terbebas dari tafsir ganda.",
        "source": "Kaidah Bahasa Naskah Dinas Resmi",
        "sourceType": "kebahasaan"
    },

    # =========================================================================
    # Kategori 5: Keuangan desa, APB Desa, dan aset desa (10 Soal Tambahan: ID 153 - 162)
    # =========================================================================
    {
        "id": 153,
        "number": 153,
        "category": "Keuangan desa, APB Desa, dan aset desa",
        "difficulty": "sedang",
        "question": "Kelompok Pendapatan Asli Desa (PADes) dalam APB Desa terdiri atas pos...",
        "options": [
            "Hasil usaha (BUMDes), hasil aset desa, swadaya dan partisipasi, gotong royong, serta lain-lain PADes yang sah",
            "Bantuan dana dari Bank Dunia dan pinjaman bank swasta asing",
            "Dana Alokasi Khusus dan Dana Bagi Hasil Cukai Tembakau",
            "Gaji ke-13 pegawai negeri sipil daerah kabupaten"
        ],
        "answer": 0,
        "explanation": "Pasal 12 Permendagri No. 20 Tahun 2018 menetapkan PADes terdiri atas: hasil usaha, hasil aset, swadaya/partisipasi/gotong royong, dan lain-lain pendapatan asli desa yang sah.",
        "source": "Permendagri No. 20 Tahun 2018 Pasal 12",
        "sourceType": "regulasi"
    },
    {
        "id": 154,
        "number": 154,
        "category": "Keuangan desa, APB Desa, dan aset desa",
        "difficulty": "mudah",
        "question": "Rekening kas yang dibuka oleh pemerintah desa pada bank yang ditunjuk bupati untuk menampung seluruh penerimaan dan pengeluaran desa dinamakan...",
        "options": [
            "Rekening Kas Desa (RKD)",
            "Rekening Giro Pribadi Kades",
            "Rekening Tabungan BPD",
            "Rekening Dana Investasi Swasta"
        ],
        "answer": 0,
        "explanation": "Pasal 1 angka 17 Permendagri No. 20 Tahun 2018 mendefinisikan RKD sebagai rekening tempat menyimpan uang pemerintahan desa yang menampung seluruh penerimaan dan pengeluaran desa.",
        "source": "Permendagri No. 20 Tahun 2018 Pasal 1 angka 17",
        "sourceType": "regulasi"
    },
    {
        "id": 155,
        "number": 155,
        "category": "Keuangan desa, APB Desa, dan aset desa",
        "difficulty": "sedang",
        "question": "Dokumen yang diajukan oleh Pelaksana Kegiatan Anggaran (Kaur/Kasi) kepada Kepala Desa melalui Sekretaris Desa untuk mencairkan anggaran pelaksanaan kegiatan disebut...",
        "options": [
            "Surat Permintaan Pembayaran (SPP)",
            "Surat Perjanjian Utang Piutang",
            "Surat Keterangan Tidak Mampu",
            "Faktur Pengiriman Ekspor"
        ],
        "answer": 0,
        "explanation": "SPP (Surat Permintaan Pembayaran) adalah dokumen pengajuan pencairan belanja kegiatan yang diajukan PKA setelah memenuhi syarat verifikasi administrasi.",
        "source": "Permendagri No. 20 Tahun 2018 Tata Cara Pengeluaran",
        "sourceType": "regulasi"
    },
    {
        "id": 156,
        "number": 156,
        "category": "Keuangan desa, APB Desa, dan aset desa",
        "difficulty": "sedang",
        "question": "SiLPA (Sisa Lebih Perhitungan Anggaran) tahun anggaran sebelumnya yang terdapat dalam rekening kas desa dicatat pada pos...",
        "options": [
            "Penerimaan Pembiayaan",
            "Pengeluaran Belanja Pegawai",
            "Pendapatan Asli Desa",
            "Dana Darurat Nasional"
        ],
        "answer": 0,
        "explanation": "SiLPA tahun sebelumnya merupakan salah satu komponen Penerimaan Pembiayaan dalam struktur APB Desa yang dapat dianggarkan kembali pada tahun berjalan.",
        "source": "Permendagri No. 20 Tahun 2018 Pasal 25",
        "sourceType": "regulasi"
    },
    {
        "id": 157,
        "number": 157,
        "category": "Keuangan desa, APB Desa, dan aset desa",
        "difficulty": "sedang",
        "question": "Alokasi anggaran untuk penyertaan modal desa ke BUMDes dicatat dalam struktur APB Desa pada kelompok...",
        "options": [
            "Pengeluaran Pembiayaan",
            "Belanja Operasional Kantor",
            "Belanja Barang dan Jasa",
            "Pendapatan Hibah"
        ],
        "answer": 0,
        "explanation": "Penyertaan modal desa ke BUMDes tergolong dalam pos Pengeluaran Pembiayaan pada APB Desa.",
        "source": "Permendagri No. 20 Tahun 2018 Pasal 27",
        "sourceType": "regulasi"
    },
    {
        "id": 158,
        "number": 158,
        "category": "Keuangan desa, APB Desa, dan aset desa",
        "difficulty": "sedang",
        "question": "Pengadaan barang dan jasa di desa menurut Peraturan LKPP Nomor 12 Tahun 2019 diutamakan dilakukan dengan prinsip...",
        "options": [
            "Swakelola dengan mengoptimalkan tenaga kerja dan material lokal desa",
            "Tender internasional melalui perusahaan luar negeri",
            "Penunjukan langsung kontraktor swasta besar dari ibu kota",
            "Pembelian tanpa kuitansi atau bukti pembayaran"
        ],
        "answer": 0,
        "explanation": "Perka LKPP No. 12 Tahun 2019 menegaskan pengadaan di desa diutamakan swakelola dengan memanfaatkan partisipasi masyarakat dan material lokal guna mendorong pemberdayaan ekonomi desa.",
        "source": "Peraturan LKPP No. 12 Tahun 2019 tentang Pengadaan Barang/Jasa di Desa",
        "sourceType": "regulasi"
    },
    {
        "id": 159,
        "number": 159,
        "category": "Keuangan desa, APB Desa, dan aset desa",
        "difficulty": "sulit",
        "question": "Tukar menukar (ruislag) tanah kas desa hanya dapat dilakukan untuk kepentingan umum dan wajib memperoleh...",
        "options": [
            "Kesepakatan Musyawarah Desa dan izin tertulis dari Bupati/Walikota serta Gubernur",
            "Persetujuan lisan dari camat tanpa berita acara",
            "Surat keterangan waris dari kepala dusun",
            "Izin dari pengadilan agama setempat"
        ],
        "answer": 0,
        "explanation": "Permendagri No. 1 Tahun 2016 Pasal 32 mengatur ruislag tanah kas desa hanya untuk kepentingan umum setelah disepakati dalam musdes dan mendapat persetujuan tertulis Bupati serta Gubernur.",
        "source": "Permendagri No. 1 Tahun 2016 tentang Pengelolaan Aset Desa Pasal 32",
        "sourceType": "regulasi"
    },
    {
        "id": 160,
        "number": 160,
        "category": "Keuangan desa, APB Desa, dan aset desa",
        "difficulty": "mudah",
        "question": "Prinsip pengelolaan keuangan desa yang mewajibkan informasi anggaran APB Desa dipublikasikan melalui papan pengumuman/baliho desa adalah wujud dari asas...",
        "options": [
            "Transparan",
            "Sentralistik",
            "Eksklusif",
            "Monopolistik"
        ],
        "answer": 0,
        "explanation": "Asas Transparan mewajibkan keterbukaan informasi publik mengenai penerimaan, penggunaan, dan pertanggungjawaban dana desa kepada seluruh masyarakat.",
        "source": "Permendagri No. 20 Tahun 2018 Pasal 2",
        "sourceType": "regulasi"
    },
    {
        "id": 161,
        "number": 161,
        "category": "Keuangan desa, APB Desa, dan aset desa",
        "difficulty": "sedang",
        "question": "Buku kas yang digunakan oleh Kaur Keuangan (Bendahara Desa) untuk mencatat pemotongan dan penyetoran pajak (PPN dan PPh) belanja desa adalah...",
        "options": [
            "Buku Pembantu Pajak",
            "Buku Bank Desa",
            "Buku Inventaris Bengkok",
            "Buku Register Nikah"
        ],
        "answer": 0,
        "explanation": "Buku Pembantu Pajak digunakan khusus untuk menatausahakan penerimaan potongan pajak dan penyetorannya ke kas negara melalui sistem e-billing.",
        "source": "Permendagri No. 20 Tahun 2018 Petunjuk Teknis Pembukuan",
        "sourceType": "regulasi"
    },
    {
        "id": 162,
        "number": 162,
        "category": "Keuangan desa, APB Desa, dan aset desa",
        "difficulty": "sedang",
        "question": "Laporan realisasi pelaksanaan APB Desa semester pertama wajib disampaikan oleh Kepala Desa kepada Bupati melalui Camat paling lambat...",
        "options": [
            "Akhir bulan Juli tahun anggaran berjalan",
            "Akhir bulan Desember tahun berikutnya",
            "Tanggal 1 Januari tahun anggaran baru",
            "Menunggu pemeriksaan akhir BPK"
        ],
        "answer": 0,
        "explanation": "Pasal 68 Permendagri No. 20 Tahun 2018 mengatur laporan semester pertama disampaikan paling lambat akhir bulan Juli tahun berjalan.",
        "source": "Permendagri No. 20 Tahun 2018 Pasal 68",
        "sourceType": "regulasi"
    },

    # =========================================================================
    # Kategori 6: Pembangunan desa, perencanaan, dan pemberdayaan masyarakat (8 Soal Tambahan: ID 163 - 170)
    # =========================================================================
    {
        "id": 163,
        "number": 163,
        "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
        "difficulty": "sedang",
        "question": "Ketua Tim Penyusun Rencana Pembangunan Jangka Menengah Desa (RPJM Desa) dan Rencana Kerja Pemerintah Desa (RKP Desa) dijabat oleh...",
        "options": [
            "Sekretaris Desa",
            "Ketua BPD",
            "Kepala Seksi Pelayanan",
            "Camat setempat"
        ],
        "answer": 0,
        "explanation": "Berdasarkan Permendesa PDTT No. 21 Tahun 2020 jo. Permendagri No. 114 Tahun 2014, Kepala Desa membentuk Tim Penyusun dengan susunan: Kepala Desa sebagai pembina, Sekretaris Desa sebagai ketua tim, dan Kaur Perencanaan sebagai sekretaris tim.",
        "source": "Permendesa PDTT No. 21 Tahun 2020; Permendagri No. 114 Tahun 2014",
        "sourceType": "regulasi"
    },
    {
        "id": 164,
        "number": 164,
        "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
        "difficulty": "sedang",
        "question": "Daftar Usulan RKP Desa (DU-RKP Desa) memuat usulan kegiatan pembangunan desa yang...",
        "options": [
            "Menjadi kewenangan pemerintah kabupaten/provinsi/pusat dan tidak dapat didanai oleh APB Desa untuk diperjuangkan di Musrenbang Kecamatan",
            "Dibiayai dari sumbangan pribadi perangkat desa",
            "Kegiatan yang ditolak secara mutlak oleh warga dusun",
            "Kegiatan rahasia yang tidak boleh diketahui masyarakat"
        ],
        "answer": 0,
        "explanation": "DU-RKP Desa berisi daftar prioritas usulan pembangunan skala supradesa yang diteruskan ke Musrenbangcam untuk diusulkan ke APBD Kabupaten/Provinsi.",
        "source": "Permendesa PDTT No. 21 Tahun 2020",
        "sourceType": "regulasi"
    },
    {
        "id": 165,
        "number": 165,
        "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
        "difficulty": "sedang",
        "question": "Jabatan Penasihat dalam struktur organisasi Badan Usaha Milik Desa (BUMDes) secara ex-officio dijabat oleh...",
        "options": [
            "Kepala Desa",
            "Ketua Karang Taruna",
            "Kapolsek setempat",
            "Manajer bank daerah"
        ],
        "answer": 0,
        "explanation": "Sesuai PP No. 11 Tahun 2021 tentang BUMDes, Kepala Desa secara ex-officio menjabat sebagai Penasihat BUMDes yang mewakili pemerintah desa sebagai pemilik modal utama.",
        "source": "Peraturan Pemerintah No. 11 Tahun 2021 tentang BUMDes",
        "sourceType": "regulasi"
    },
    {
        "id": 166,
        "number": 166,
        "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
        "difficulty": "sedang",
        "question": "Pelaksanaan program Pos Pelayanan Terpadu (Posyandu) di desa merupakan bagian dari bidang pembangunan desa pada urusan...",
        "options": [
            "Kesehatan masyarakat, pencegahan stunting, dan perlindungan ibu-anak",
            "Pembangunan infrastruktur jembatan beton",
            "Pengadaan seragam dinas pamong desa",
            "Penertiban izin tambang galian pasir"
        ],
        "answer": 0,
        "explanation": "Posyandu merupakan LKD yang bermitra dengan pemerintah desa dalam pemenuhan layanan kesehatan dasar warga, gizi balita, dan pencegahan stunting.",
        "source": "Permendagri No. 18 Tahun 2018 tentang Lembaga Kemasyarakatan Desa",
        "sourceType": "regulasi"
    },
    {
        "id": 167,
        "number": 167,
        "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
        "difficulty": "mudah",
        "question": "Pemasangan papan transparansi proyek kegiatan fisik di lokasi pekerjaan desa bertujuan untuk...",
        "options": [
            "Menjamin keterbukaan publik mengenai volume pekerjaan, sumber dana, dan pelaksana kegiatan",
            "Menambah keindahan dekorasi taman desa",
            "Menakut-nakuti pedagang kaki lima di sekitar proyek",
            "Memenuhi syarat pendaftaran hak cipta pribadi pelaksana"
        ],
        "answer": 0,
        "explanation": "Pemasangan papan informasi proyek adalah kewajiban transparansi publik agar masyarakat dapat memantau volume, biaya, dan sumber dana pembangunan desa.",
        "source": "Prinsip Akuntabilitas Publik Pengadaan Desa",
        "sourceType": "administrasi"
    },
    {
        "id": 168,
        "number": 168,
        "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
        "difficulty": "sedang",
        "question": "Instrumen pemetaan sosial yang digunakan desa untuk mengidentifikasi kondisi keluarga miskin, ibu hamil, anak stunting, dan warga disabilitas disebut...",
        "options": [
            "Pendataan SDGs Desa dan Pemetaan Sosial Partisipatif",
            "Pemeriksaan Intelijen Daerah",
            "Sensus Pajak Penghasilan Pejabat",
            "Audit Forensik Independen"
        ],
        "answer": 0,
        "explanation": "Pemetaan sosial partisipatif dan pendataan SDGs Desa memotret data riil kemiskinan dan kebutuhan warga per rukun tetangga sebagai basis intervensi program.",
        "source": "Permendesa PDTT No. 21 Tahun 2020",
        "sourceType": "regulasi"
    },
    {
        "id": 169,
        "number": 169,
        "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
        "difficulty": "mudah",
        "question": "Peran Kader Pemberdayaan Masyarakat Desa (KPMD) adalah...",
        "options": [
            "Memfasilitasi warga desa dalam proses penggalian gagasan, musyawarah dusun, dan pelaksanaan pemberdayaan",
            "Menagih iuran retribusi sampah secara paksa",
            "Menggantikan tugas kepolisian dalam menindak tilang lalu lintas",
            "Membentuk partai politik baru di tingkat rukun warga"
        ],
        "answer": 0,
        "explanation": "KPMD bertugas mendampingi warga dalam menumbuhkan prakarsa dan partisipasi aktif dalam musyawarah perencanaan dan pembangunan desa.",
        "source": "Permendagri No. 114 Tahun 2014; Permendesa PDTT No. 21 Tahun 2020",
        "sourceType": "regulasi"
    },
    {
        "id": 170,
        "number": 170,
        "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
        "difficulty": "sedang",
        "question": "Status perkembangan desa menurut Indeks Desa Membangun (IDM) terdiri dari tingkatan...",
        "options": [
            "Desa Sangat Tertinggal, Desa Tertinggal, Desa Berkembang, Desa Maju, dan Desa Mandiri",
            "Desa Pemula, Desa Pratama, Desa Madya, dan Desa Utama",
            "Desa Miskin, Desa Cukup, dan Desa Kaya",
            "Desa Kelas 1, Desa Kelas 2, dan Desa Kelas 3"
        ],
        "answer": 0,
        "explanation": "Permendesa No. 2 Tahun 2016 mengklasifikasikan status desa ke dalam 5 tingkatan: Sangat Tertinggal, Tertinggal, Berkembang, Maju, dan Mandiri.",
        "source": "Permendesa PDTT No. 2 Tahun 2016 tentang IDM",
        "sourceType": "regulasi"
    },

    # =========================================================================
    # Kategori 7: BPD, kelembagaan desa, dan musyawarah (5 Soal Tambahan: ID 171 - 175)
    # =========================================================================
    {
        "id": 171,
        "number": 171,
        "category": "BPD, kelembagaan desa, dan musyawarah",
        "difficulty": "mudah",
        "question": "Hak yang dimiliki oleh anggota Badan Permusyawaratan Desa (BPD) menurut Pasal 61 UU Nomor 6 Tahun 2014 adalah...",
        "options": [
            "Mengajukan usul rancangan Perdes, mengajukan pertanyaan, serta menyampaikan usul dan pendapat",
            "Mengelola kas belanja modal fisik desa secara langsung",
            "Mengganti kepala desa tanpa proses pemilihan kepala desa",
            "Menetapkan surat perintah penangkapan warga yang melanggar hukum"
        ],
        "answer": 0,
        "explanation": "Berdasarkan Pasal 61 UU No. 6 Tahun 2014, anggota BPD berhak: mengajukan usul rancangan Perdes, mengajukan pertanyaan, menyampaikan usul dan pendapat, memilih dan dipilih, serta memperoleh tunjangan operasional.",
        "source": "UU No. 6 Tahun 2014 Pasal 61",
        "sourceType": "regulasi"
    },
    {
        "id": 172,
        "number": 172,
        "category": "BPD, kelembagaan desa, dan musyawarah",
        "difficulty": "sedang",
        "question": "Hubungan kelembagaan antara Pemerintah Desa dengan Badan Permusyawaratan Desa (BPD) adalah...",
        "options": [
            "Hubungan kemitraan yang setara dalam merumuskan kebijakan desa untuk kesejahteraan masyarakat",
            "Hubungan atasan dan bawahan langsung di mana BPD adalah bawahan kades",
            "Hubungan konfrontasi politik permanen demi menjatuhkan kepemimpinan pemdes",
            "Hubungan ketergantungan mutlak di mana kades tidak boleh menerbitkan surat apa pun tanpa izin BPD"
        ],
        "answer": 0,
        "explanation": "Pemerintah Desa dan BPD merupakan mitra kerja yang setara dalam merumuskan Perdes dan mengawal aspirasi warga menuju desa maju dan mandiri.",
        "source": "Permendagri No. 110 Tahun 2016",
        "sourceType": "regulasi"
    },
    {
        "id": 173,
        "number": 173,
        "category": "BPD, kelembagaan desa, dan musyawarah",
        "difficulty": "sedang",
        "question": "Musyawarah Desa Khusus (Musdessus) diselenggarakan untuk...",
        "options": [
            "Menangani hal-hal yang bersifat khusus dan mendesak, seperti verifikasi dan penetapan keluarga penerima Bantuan Langsung Tunai (BLT) Desa",
            "Merayakan hari ulang tahun kepala desa terpilih",
            "Menghukum warga yang tidak membayar iuran ronda malam",
            "Membagikan tanah kas desa kepada sanak famili aparat desa"
        ],
        "answer": 0,
        "explanation": "Musdessus diselenggarakan oleh BPD bersama Pemdes secara insidental untuk menyepakati hal strategis yang mendesak, seperti validasi dan penetapan KPM BLT Dana Desa.",
        "source": "Permendesa PDTT Pedoman Musyawarah Desa",
        "sourceType": "regulasi"
    },
    {
        "id": 174,
        "number": 174,
        "category": "BPD, kelembagaan desa, dan musyawarah",
        "difficulty": "sedang",
        "question": "Mekanisme pengambilan keputusan dalam rapat BPD yang utama adalah...",
        "options": [
            "Musyawarah untuk mufakat, dan apabila tidak tercapai mufakat, keputusan diambil berdasarkan suara terbanyak (voting)",
            "Keputusan mutlak di tangan ketua BPD seorang diri",
            "Menunggu instruksi tertulis dari bupati kabupaten",
            "Mengundi nama anggota yang hadir menggunakan koin"
        ],
        "answer": 0,
        "explanation": "Pasal 42 Permendagri No. 110 Tahun 2016 mengatur keputusan rapat BPD diambil berdasarkan musyawarah mufakat, dan jika tidak tercapai diambil berdasarkan suara terbanyak.",
        "source": "Permendagri No. 110 Tahun 2016 Pasal 42",
        "sourceType": "regulasi"
    },
    {
        "id": 175,
        "number": 175,
        "category": "BPD, kelembagaan desa, dan musyawarah",
        "difficulty": "mudah",
        "question": "Masa keanggotaan Badan Permusyawaratan Desa (BPD) menurut ketentuan perundang-undangan desa adalah...",
        "options": [
            "Mengikuti regulasi periode masa jabatan yang berlaku dan dapat dipilih kembali sesuai aturan perundang-undangan",
            "Seumur hidup tanpa pergantian",
            "Hanya 1 tahun kalender",
            "Ditetapkan setiap bulan oleh camat"
        ],
        "answer": 0,
        "explanation": "Pasal 56 UU No. 6 Tahun 2014 jo. UU No. 3 Tahun 2024 mengatur masa keanggotaan BPD yang diselaraskan dengan masa jabatan pemerintahan desa.",
        "source": "UU No. 6 Tahun 2014 jo. UU No. 3 Tahun 2024",
        "sourceType": "regulasi"
    },

    # =========================================================================
    # Kategori 8: Bahasa Indonesia (7 Soal Tambahan: ID 176 - 182)
    # =========================================================================
    {
        "id": 176,
        "number": 176,
        "category": "Bahasa Indonesia",
        "difficulty": "sedang",
        "question": "Manakah deretan bentuk gabungan kata yang penulisannya baku menurut kaidah EYD V?",
        "options": [
            "Kerja sama, tanda tangan, tanggung jawab",
            "Kerjasama, tandatangan, tanggungjawab",
            "Kerja-sama, tanda-tangan, tanggung-jawab",
            "Kerjasama, tanda tangan, tanggungjawab"
        ],
        "answer": 0,
        "explanation": "Gabungan kata yang tidak mendapat awalan dan akhiran sekaligus ditulis terpisah: kerja sama, tanda tangan, tanggung jawab. Ditulis serangkai bila mendapat awalan dan akhiran sekaligus: menandatangani, pertanggungjawaban.",
        "source": "EYD V Kaidah Penulisan Gabungan Kata",
        "sourceType": "kebahasaan"
    },
    {
        "id": 177,
        "number": 177,
        "category": "Bahasa Indonesia",
        "difficulty": "mudah",
        "question": "Penulisan kata depan 'di' yang tepat pada teks administrasi desa adalah...",
        "options": [
            "Rapat koordinasi dilaksanakan di balai desa.",
            "Surat undangan ini di serahkan kepada ketua RT.",
            "Dokumen tersebut disimpan didalam lemari besi.",
            "Bantuan sembako dibagikan di-dusun krajan."
        ],
        "answer": 0,
        "explanation": "Kata depan 'di' yang menunjukkan tempat ditulis terpisah (di balai desa, di kantor), sedangkan awalan 'di-' sebagai pembentuk kata kerja pasif ditulis serangkai (diserahkan, disimpan, dibagikan).",
        "source": "EYD V Kaidah Kata Depan",
        "sourceType": "kebahasaan"
    },
    {
        "id": 178,
        "number": 178,
        "category": "Bahasa Indonesia",
        "difficulty": "sedang",
        "question": "Penulisan partikel 'pun' yang benar menurut EYD V terdapat pada kalimat...",
        "options": [
            "Meskipun hujan deras mengguyur desa, warga pun tetap antusias menghadiri musyawarah.",
            "Wargapun ikut bergotong royong membersihkan saluran air.",
            "Apapun yang terjadi, kades harus tetap tenang.",
            "Meski pun hari libur, staf desa tetap siaga di balai desa."
        ],
        "answer": 0,
        "explanation": "Partikel 'pun' yang bermakna 'juga' ditulis terpisah (warga pun). Bentuk penghubung tetap seperti 'meskipun', 'walaupun', 'adapun' ditulis serangkai.",
        "source": "EYD V Penulisan Partikel",
        "sourceType": "kebahasaan"
    },
    {
        "id": 179,
        "number": 179,
        "category": "Bahasa Indonesia",
        "difficulty": "sedang",
        "question": "Perhatikan kalimat pengumuman: 'Yang membawa kendaraan harap dimasukkan ke dalam tempat parkir.'\nPerbaikan kalimat di atas agar menjadi kalimat yang logis dan efektif adalah...",
        "options": [
            "Pengendara dimohon memarkir kendaraannya di tempat parkir.",
            "Kendaraan yang dibawa harap dimasukkan bersama orangnya ke tempat parkir.",
            "Bagi yang bawa kendaraan mohon untuk segera ditaruh dalam parkiran.",
            "Kepada para pengendara-pengendara kendaraan wajib menaruh motornya."
        ],
        "answer": 0,
        "explanation": "Kalimat asli tidak logis karena subjek yang membawa (orangnya) yang dimasukkan ke tempat parkir. Perbaikan yang santun, logis, dan efektif adalah 'Pengendara dimohon memarkir kendaraannya di tempat parkir.'",
        "source": "Kaidah Kalimat Efektif dan Nalar Bahasa Indonesia",
        "sourceType": "kebahasaan"
    },
    {
        "id": 180,
        "number": 180,
        "category": "Bahasa Indonesia",
        "difficulty": "mudah",
        "question": "Lawan kata (antonim) dari kata 'akuntabel' dalam konteks tata kelola pemerintahan adalah...",
        "options": [
            "Tertutup / tidak dapat dipertanggungjawabkan",
            "Kredibel dan terpercaya",
            "Transparan dan terbuka",
            "Cermat dan berhati-hati"
        ],
        "answer": 0,
        "explanation": "Akuntabel bermakna dapat dipertanggungjawabkan secara terbuka dan sah. Lawan katanya adalah tertutup atau tidak dapat dipertanggungjawabkan.",
        "source": "Kamus Besar Bahasa Indonesia (KBBI) V",
        "sourceType": "kebahasaan"
    },
    {
        "id": 181,
        "number": 181,
        "category": "Bahasa Indonesia",
        "difficulty": "sedang",
        "question": "Penulisan singkatan resmi lembaga dan naskah hukum dalam bahasa Indonesia yang benar adalah...",
        "options": [
            "BPD, APB Desa, Perbup, dan SPP",
            "B.P.D., A.P.B.Des., dan S.P.P.",
            "bpd, apb-desa, per-bup, dan spp",
            "Bpd., Apbdes., dan Spp."
        ],
        "answer": 0,
        "explanation": "Singkatan yang terdiri atas huruf awal setiap kata nama lembaga pemerintah atau dokumen resmi ditulis dengan huruf kapital tanpa titik: BPD, APB Desa, SPP, Perbup.",
        "source": "EYD V Singkatan dan Akronim",
        "sourceType": "kebahasaan"
    },
    {
        "id": 182,
        "number": 182,
        "category": "Bahasa Indonesia",
        "difficulty": "sedang",
        "question": "Bacalah kalimat simpulan berikut: 'Dengan demikian, keberadaan BUMDes terbukti mampu meningkatkan pendapatan asli desa serta membuka lapangan kerja baru bagi pemuda setempat.'\nKata penghubung penanda simpulan dalam kalimat tersebut adalah...",
        "options": [
            "Dengan demikian",
            "Keberadaan",
            "Serta",
            "Bagi pemuda"
        ],
        "answer": 0,
        "explanation": "Frasa 'Dengan demikian' merupakan konjungsi antarkalimat yang berfungsi mengantarkan simpulan logis dari pernyataan-pernyataan sebelumnya.",
        "source": "Tata Bahasa Baku Bahasa Indonesia",
        "sourceType": "kebahasaan"
    },

    # =========================================================================
    # Kategori 9: Matematika dan numerik (6 Soal Tambahan: ID 183 - 188)
    # =========================================================================
    {
        "id": 183,
        "number": 183,
        "category": "Matematika dan numerik",
        "difficulty": "mudah",
        "question": "Badan Usaha Milik Desa (BUMDes) membukukan laba bersih tahunan sebesar Rp80.000.000,00. Sesuai Peraturan Desa, sebesar 40% dari laba bersih wajib disetorkan sebagai Pendapatan Asli Desa (PADes). Berapakah nominal rupiah yang disetorkan ke kas desa?",
        "options": [
            "Rp32.000.000,00",
            "Rp24.000.000,00",
            "Rp36.000.000,00",
            "Rp40.000.000,00"
        ],
        "answer": 0,
        "explanation": "Perhitungan: 40% x Rp80.000.000,00 = 0,4 x 80.000.000 = Rp32.000.000,00.",
        "source": "Aritmetika Sosial / Pembagian Laba BUMDes",
        "sourceType": "numerik"
    },
    {
        "id": 184,
        "number": 184,
        "category": "Matematika dan numerik",
        "difficulty": "sedang",
        "question": "Pembangunan saluran drainase pasangan batu memiliki panjang 50 meter, lebar penampang 0,4 meter, dan tinggi pasangan 0,15 meter. Berapakah volume pasangan batu tersebut dalam satuan meter kubik (m³)?",
        "options": [
            "3,0 m³",
            "2,5 m³",
            "4,0 m³",
            "6,0 m³"
        ],
        "answer": 0,
        "explanation": "Volume balok/saluran = panjang x lebar x tinggi = 50 m x 0,4 m x 0,15 m = 3,0 m³.",
        "source": "Geometri Pengukuran Fisik Konstruksi Desa",
        "sourceType": "numerik"
    },
    {
        "id": 185,
        "number": 185,
        "category": "Matematika dan numerik",
        "difficulty": "mudah",
        "question": "Jumlah penduduk suatu desa adalah 2.500 jiwa. Berdasarkan survei sosial, sebanyak 14% warga tergolong penerima bantuan jaminan sosial terpadu. Berapakah jumlah jiwa warga penerima bantuan tersebut?",
        "options": [
            "350 jiwa",
            "325 jiwa",
            "375 jiwa",
            "400 jiwa"
        ],
        "answer": 0,
        "explanation": "Perhitungan: 14% x 2.500 = (14 / 100) x 2.500 = 14 x 25 = 350 jiwa.",
        "source": "Statistika Sosial Kependudukan",
        "sourceType": "numerik"
    },
    {
        "id": 186,
        "number": 186,
        "category": "Matematika dan numerik",
        "difficulty": "sedang",
        "question": "Tentukan angka berikutnya dalam pola deret geometri berikut:\n3, 6, 12, 24, 48, ...",
        "options": [
            "96",
            "72",
            "84",
            "108"
        ],
        "answer": 0,
        "explanation": "Setiap suku dikalikan dengan 2 (rasio = 2):\n3 x 2 = 6; 6 x 2 = 12; 12 x 2 = 24; 24 x 2 = 48; 48 x 2 = 96.",
        "source": "Deret Geometri / Pola Bilangan",
        "sourceType": "numerik"
    },
    {
        "id": 187,
        "number": 187,
        "category": "Matematika dan numerik",
        "difficulty": "sedang",
        "question": "Seorang staf desa mengantarkan berkas dokumen dinas dari kantor desa ke kantor camat yang berjarak 18 kilometer menggunakan sepeda motor dinas dengan kecepatan rata-rata 36 km/jam. Berapa menit lama perjalanan yang ditempuh staf tersebut?",
        "options": [
            "30 menit",
            "20 menit",
            "45 menit",
            "50 menit"
        ],
        "answer": 0,
        "explanation": "Waktu = Jarak ÷ Kecepatan = 18 km ÷ 36 km/jam = 0,5 jam. Konversi ke menit = 0,5 x 60 menit = 30 menit.",
        "source": "Aritmetika Pengukuran Waktu dan Kecepatan",
        "sourceType": "numerik"
    },
    {
        "id": 188,
        "number": 188,
        "category": "Matematika dan numerik",
        "difficulty": "sedang",
        "question": "Pemerintah Desa membeli 10 unit meja kerja kantor dengan harga total Rp5.000.000,00. Karena membeli secara tunai dalam jumlah banyak, toko memberikan diskon sebesar 12%. Berapakah total uang yang harus dibayarkan?",
        "options": [
            "Rp4.400.000,00",
            "Rp4.200.000,00",
            "Rp4.600.000,00",
            "Rp4.500.000,00"
        ],
        "answer": 0,
        "explanation": "Besar diskon = 12% x Rp5.000.000 = Rp600.000. Total bayar = Rp5.000.000 - Rp600.000 = Rp4.400.000,00.",
        "source": "Aritmetika Sosial / Potongan Harga Pengadaan",
        "sourceType": "numerik"
    },

    # =========================================================================
    # Kategori 10: Logika dan penalaran (5 Soal Tambahan: ID 189 - 193)
    # =========================================================================
    {
        "id": 189,
        "number": 189,
        "category": "Logika dan penalaran",
        "difficulty": "sedang",
        "question": "Premis 1: Pencairan dana desa tahap I dapat dilakukan melalui transaksi transfer bank atau cek tunai di kantor cabang.\nPremis 2: Sistem jaringan transfer online bank sedang mengalami gangguan teknis fatal.\nKesimpulan yang sah adalah...",
        "options": [
            "Pencairan dana desa tahap I dilakukan melalui cek tunai di kantor cabang.",
            "Dana desa tahap I tidak dapat dicairkan sama sekali untuk selamanya.",
            "Kepala desa harus membatalkan seluruh program pembangunan desa.",
            "Pencairan dialihkan ke rekening tabungan pribadi sekretaris desa."
        ],
        "answer": 0,
        "explanation": "Berdasarkan silogisme disjungtif (p atau q; bukan p; maka q): karena transfer bank terganggu, maka pencairan menggunakan cek tunai.",
        "source": "Logika Silogisme Disjungtif",
        "sourceType": "logika"
    },
    {
        "id": 190,
        "number": 190,
        "category": "Logika dan penalaran",
        "difficulty": "sedang",
        "question": "Perhatikan analogi hubungan kata berikut:\nKEPALA DESA : DESA = CAMAT : ...\nKata yang paling tepat untuk melengkapi analogi tersebut adalah...",
        "options": [
            "KECAMATAN",
            "KABUPATEN",
            "DUSUN",
            "PROVINSI"
        ],
        "answer": 0,
        "explanation": "Kepala Desa memimpin wilayah Desa, sebagaimana Camat memimpin wilayah kerja Kecamatan.",
        "source": "Penalaran Hubungan Analogi Kata",
        "sourceType": "logika"
    },
    {
        "id": 191,
        "number": 191,
        "category": "Logika dan penalaran",
        "difficulty": "sedang",
        "question": "Dari 80 pelaku UMKM di desa binaan, tercatat 45 orang mengikuti pelatihan pembukuan keuangan, 35 orang mengikuti pelatihan pemasaran digital, dan 15 orang mengikuti kedua pelatihan tersebut. Berapakah pelaku UMKM yang HANYA mengikuti pelatihan pembukuan keuangan saja?",
        "options": [
            "30 orang",
            "20 orang",
            "35 orang",
            "45 orang"
        ],
        "answer": 0,
        "explanation": "Jumlah yang hanya mengikuti pembukuan keuangan = Total pembukuan - Peserta kedua pelatihan = 45 - 15 = 30 orang.",
        "source": "Logika Himpunan / Diagram Venn",
        "sourceType": "logika"
    },
    {
        "id": 192,
        "number": 192,
        "category": "Logika dan penalaran",
        "difficulty": "sedang",
        "question": "Warga mengeluhkan debu dari truk proyek pembangunan pabrik yang melewati jalan desa. Sebagai aparatur desa yang profesional, tindakan mediasi yang paling tepat adalah...",
        "options": [
            "Memfasilitasi musyawarah antara perwakilan warga dan penanggung jawab proyek untuk menyepakati jadwal penyiraman jalan serta batasan jam lintas truk",
            "Menutup akses jalan secara sepihak dan merusak truk proyek yang melintas",
            "Membiarkan keluhan warga tanpa respons karena pabrik mendatangkan pemasukan pribadi",
            "Menyalahkan warga yang rumahnya berada di pinggir jalan raya"
        ],
        "answer": 0,
        "explanation": "Penyelesaian masalah sosial di desa mengedepankan mediasi kekeluargaan yang solutif dan berkepala dingin guna mengakomodasi kepentingan warga dan ketertiban umum.",
        "source": "Manajemen Resolusi Konflik Kemasyarakatan Desa",
        "sourceType": "administrasi"
    },
    {
        "id": 193,
        "number": 193,
        "category": "Logika dan penalaran",
        "difficulty": "sulit",
        "question": "Empat orang staf pelayanan kantor desa (Ratna, Sinta, Taufik, dan Usman) melayani 4 loket. Diketahui:\n1. Ratna tidak berada di loket 1 maupun loket 4.\n2. Taufik berada di loket tepat di sebelah kanan loket Ratna.\n3. Usman berada di loket 4.\nDi loket manakah Sinta bertugas?",
        "options": [
            "Loket 1",
            "Loket 2",
            "Loket 3",
            "Loket 4"
        ],
        "answer": 0,
        "explanation": "Analisis posisi:\n- Loket 4 diisi Usman (ketentuan 3).\n- Ratna tidak di loket 1 dan 4, maka Ratna di loket 2 atau 3.\n- Jika Ratna di loket 3, sebelah kanannya (loket 4) adalah Taufik, bertentangan dengan ketentuan bahwa Usman di loket 4.\n- Maka Ratna pasti di loket 2, dan Taufik di loket 3 (sebelah kanan Ratna).\n- Tersisa loket 1 yang ditempati oleh Sinta.",
        "source": "Penalaran Analitis Posisi Lokasi",
        "sourceType": "logika"
    },

    # =========================================================================
    # Kategori 11: Pengetahuan umum (4 Soal Tambahan: ID 194 - 197)
    # =========================================================================
    {
        "id": 194,
        "number": 194,
        "category": "Pengetahuan umum",
        "difficulty": "mudah",
        "question": "Secara geografis, wilayah Kabupaten Tuban di sebelah utara berbatasan langsung dengan...",
        "options": [
            "Laut Jawa",
            "Kabupaten Bojonegoro",
            "Kabupaten Lamongan",
            "Kabupaten Rembang (Jawa Tengah)"
        ],
        "answer": 0,
        "explanation": "Batas wilayah Kabupaten Tuban: Sebelah utara berbatasan dengan Laut Jawa, sebelah timur dengan Kabupaten Lamongan, sebelah selatan dengan Kabupaten Bojonegoro, dan sebelah barat dengan Kabupaten Rembang (Jawa Tengah).",
        "source": "Profil Geografis Kabupaten Tuban (tubankab.go.id)",
        "sourceType": "umum"
    },
    {
        "id": 195,
        "number": 195,
        "category": "Pengetahuan umum",
        "difficulty": "mudah",
        "question": "Kesenian tari tradisional khas Kabupaten Tuban yang populer dan sarat dengan nilai kebersamaan masyarakat pedesaan adalah...",
        "options": [
            "Tari Tayub / Sindir Tuban",
            "Tari Pendet",
            "Tari Saman",
            "Tari Jaipong"
        ],
        "answer": 0,
        "explanation": "Seni Tayub (Sindiran) merupakan kesenian tari tradisional yang sangat mengakar dalam kebudayaan masyarakat pedesaan di Kabupaten Tuban.",
        "source": "Dinas Kebudayaan dan Pariwisata Kabupaten Tuban",
        "sourceType": "umum"
    },
    {
        "id": 196,
        "number": 196,
        "category": "Pengetahuan umum",
        "difficulty": "mudah",
        "question": "Konsep pembagian kekuasaan negara menjadi tiga cabang (Eksekutif, Legislatif, dan Yudikatif) dikenal dengan teori...",
        "options": [
            "Trias Politika",
            "Dwi Fungsi",
            "Monarki Parlementer",
            "Birokrasi Weberian"
        ],
        "answer": 0,
        "explanation": "Trias Politika (yang dipopulerkan oleh Montesquieu) membagi kekuasaan negara ke dalam cabang legislatif, eksekutif, dan yudikatif.",
        "source": "Ilmu Negara dan Teori Konstitusi",
        "sourceType": "umum"
    },
    {
        "id": 197,
        "number": 197,
        "category": "Pengetahuan umum",
        "difficulty": "mudah",
        "question": "Lagu kebangsaan 'Indonesia Raya' diciptakan oleh Wage Rudolf Supratman dan pertama kali dikumandangkan secara resmi pada peristiwa bersejarah...",
        "options": [
            "Kongres Pemuda II tanggal 28 Oktober 1928",
            "Proklamasi Kemerdekaan 17 Agustus 1945",
            "Sidang Pertama BPUPKI 29 Mei 1945",
            "Peristiwa Rengasdengklok 16 Agustus 1945"
        ],
        "answer": 0,
        "explanation": "Lagu Indonesia Raya pertama kali diperdengarkan dengan gesekan biola WR Supratman pada Kongres Pemuda II tanggal 28 Oktober 1928 di Jakarta.",
        "source": "Sejarah Nasional Indonesia; UU No. 24 Tahun 2009",
        "sourceType": "umum"
    },

    # =========================================================================
    # Kategori 12: Komputer dasar dan pelayanan publik (3 Soal Tambahan: ID 198 - 200)
    # =========================================================================
    {
        "id": 198,
        "number": 198,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "mudah",
        "question": "Kombinasi tombol pintas (keyboard shortcut) pada komputer yang berfungsi untuk menyimpan dokumen secara cepat pada pengolah kata atau angka adalah...",
        "options": [
            "Ctrl + S",
            "Ctrl + P",
            "Ctrl + C",
            "Ctrl + Z"
        ],
        "answer": 0,
        "explanation": "Kombinasi tombol `Ctrl + S` (Save) digunakan untuk menyimpan file dokumen secara cepat pada komputer Windows.",
        "source": "Dasar Pengoperasian Komputer Perkantoran",
        "sourceType": "teknologi"
    },
    {
        "id": 199,
        "number": 199,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "sedang",
        "question": "Fungsi rumus logika pada Microsoft Excel yang digunakan untuk menghasilkan keterangan berdasarkan pengujian kondisi tertentu (contoh: jika nilai sel C2 >= 75 maka 'Lulus', jika tidak maka 'Remedial') adalah...",
        "options": [
            "=IF(C2>=75; \"Lulus\"; \"Remedial\")",
            "=SUM(C2:75)",
            "=COUNT(C2; \"Lulus\")",
            "=AVERAGE(C2:Lulus)"
        ],
        "answer": 0,
        "explanation": "Fungsi `=IF(kondisi; nilai_jika_benar; nilai_jika_salah)` adalah rumus logika spreadsheet untuk menguji kriteria kelulusan atau status data.",
        "source": "Kompetensi Praktik Komputer / Microsoft Excel",
        "sourceType": "teknologi"
    },
    {
        "id": 200,
        "number": 200,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "sedang",
        "question": "Dalam rangka menjaga keamanan sistem informasi keuangan desa (Siskeudes), tindakan keamanan digital yang wajib ditaati oleh operator desa adalah...",
        "options": [
            "Tidak membagikan kata sandi akun kepada pihak yang tidak berhak, memperbarui sandi berkala, dan membuat salinan cadangan (backup) data berkala",
            "Menuliskan kata sandi di kertas dan menempelkannya di layar monitor balai desa",
            "Membiarkan komputer aplikasi keuangan terbuka tanpa kunci saat ditinggal istirahat",
            "Mengunduh program permainan bajakan dari internet di komputer kas desa"
        ],
        "answer": 0,
        "explanation": "Keamanan data administrasi desa mensyaratkan kerahasiaan kata sandi, penggantian berkala, backup rutin, dan tidak menggunakan perangkat kantor untuk aktivitas berbahaya.",
        "source": "Standar Operasional Keamanan Data & Informasi Desa; BPKP",
        "sourceType": "teknologi"
    }
]

print(f"Total soal tambahan baru: {len(NEW_QUESTIONS)} butir.")
