# -*- coding: utf-8 -*-
"""
Database Soal 501 s.d. 550: Pendidikan Agama & Moderasi Beragama
Khusus Seleksi Calon Perangkat Desa (Kaur, Kasi Pelayanan/Kesra, Kasun, Sekdes)
Materi Lengkap:
1. Fiqih Sosial & Fardhu Kifayah Pengurusan Jenazah di Desa (Q501-Q510)
2. Zakat Fitrah, Zakat Pertanian, Asnaf 8, dan Regulasi Wakaf Desa UU 41/2004 (Q511-Q518)
3. Tugas Modin / Kasi Pelayanan & Hukum Perkawinan Islam UU 16/2019 (Q519-Q526)
4. Moderasi Beragama, Toleransi Kebinekaan, & PBM No. 9 & 8 Th 2006 (Q527-Q534)
5. Etika Kepemimpinan Islami & Integritas Pelayanan Publik Bebas Risywah (Q535-Q542)
6. Sejarah Walisongo, Sunan Bonang Tuban, Sunan Drajat, Sunan Ampel (Q543-Q550)
Total: 50 butir soal terverifikasi (ID 501 - 550).
"""

QUESTIONS_501_550 = [
    # =========================================================================
    # BAGIAN 1: FIQIH SOSIAL & FARDHU KIFAYAH PENGURUSAN JENAZAH (Q501 - Q510)
    # =========================================================================
    {
        "id": 501,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "mudah",
        "question": "Pengurusan jenazah seorang muslim (memandikan, mengafani, menyalatkan, dan menguburkan) dalam hukum fikih Islam berstatus...",
        "options": [
            "Fardhu 'ain bagi seluruh penduduk desa tanpa terkecuali",
            "Fardhu kifayah, yaitu kewajiban yang gugur bagi warga lain apabila telah dilaksanakan oleh sebagian orang",
            "Sunnah muakkadah yang dianjurkan bagi perangkat desa saja",
            "Mubah tergantung kesepakatan musyawarah warga rukun tetangga"
        ],
        "answer": 1,
        "explanation": "Hukum mengurus jenazah muslim (memandikan, mengafani, menyalatkan, dan memakamkan) adalah Fardhu Kifayah. Artinya, kewajiban ini dibebankan kepada umat/masyarakat secara kolektif; jika sudah ada sebagian warga (seperti modin dan keluarga) yang melaksanakannya dengan baik, maka gugurlah dosa seluruh warga lainnya di wilayah tersebut.",
        "source": "Kitab Fathul Qarib al-Mujib & Fikih Islam Sulaiman Rasjid, Bab Tajhiz al-Janaiz"
    },
    {
        "id": 502,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "sedang",
        "question": "Dalam pelaksanaan sholat jenazah, urutan bacaan yang dibaca setelah Takbir Kedua adalah...",
        "options": [
            "Membaca Surat Al-Fatihah",
            "Membaca doa pengampunan khusus untuk jenazah (Allahummaghfir lahu/laha)",
            "Membaca shalawat kepada Nabi Muhammad SAW",
            "Membaca doa untuk keluarga yang ditinggalkan lalu salam"
        ],
        "answer": 2,
        "explanation": "Rukun sholat jenazah terdiri dari 4 takbir tanpa ruku dan sujud: Takbir 1 membaca Surat Al-Fatihah; Takbir 2 membaca Shalawat kepada Nabi Muhammad SAW (minimal: Allahumma shalli 'ala sayyidina Muhammad); Takbir 3 membaca doa bagi jenazah (Allahummaghfir lahu...); Takbir 4 membaca doa penutup (Allahumma la tahrimna ajrahu...) disusul salam.",
        "source": "Fikih Praktis Ibadah Jenazah Kemenag RI & Kitab Matan Taqrib Fiqih Syafi'i"
    },
    {
        "id": 503,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "sedang",
        "question": "Ketika menjadi imam sholat jenazah untuk jenazah laki-laki, posisi berdiri imam yang sesuai dengan sunnah Rasulullah SAW adalah...",
        "options": [
            "Sejajar dengan bagian kepala atau dada jenazah",
            "Sejajar dengan bagian perut atau pinggang jenazah",
            "Sejajar dengan kedua lutut jenazah",
            "Sejajar dengan ujung kedua telapak kaki jenazah"
        ],
        "answer": 0,
        "explanation": "Berdasarkan hadits riwayat Abu Daud dan Tirmidzi dari Anas bin Malik dan Samurah bin Jundub, sunnah posisi imam saat menyalatkan jenazah laki-laki adalah berdiri lurus searah kepala/dada jenazah. Sedangkan jika jenazah perempuan, posisi imam berdiri searah bagian tengah tubuh (pinggang/perut) jenazah.",
        "source": "HR. Abu Daud No. 3194 & Tirmidzi No. 1034, Bab Posisi Imam Sholat Jenazah"
    },
    {
        "id": 504,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "mudah",
        "question": "Berapakah jumlah lapisan kain kafan yang disunnahkan untuk membungkus jenazah laki-laki muslim?",
        "options": [
            "1 lapis kain sarung",
            "3 lapis kain kafan putih bersih",
            "5 lapis kain kafan bersusun",
            "7 lapis kain kafan berwarna hijau"
        ],
        "answer": 1,
        "explanation": "Berdasarkan hadits riwayat Bukhari dan Muslim dari Ummul Mukminin Aisyah RA, jenazah laki-laki disunnahkan dikafani dengan 3 lapis kain putih tanpa gamis dan sorban. Sementara untuk jenazah perempuan disunnahkan 5 lapis (kain basahan/sarung, baju kurung, kerudung, dan 2 lembar kain penutup seluruh tubuh).",
        "source": "HR. Bukhari No. 1264 & Muslim No. 941; Fiqih Jenazah Kemenag RI"
    },
    {
        "id": 505,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "sulit",
        "question": "Seorang warga desa meninggal dunia dalam musibah kecelakaan perahu di laut dan jasadnya belum ditemukan setelah operasi pencarian resmi SAR ditutup. Tindakan ibadah yang dilaksanakan oleh warga desa bersama modin/tokoh agama adalah...",
        "options": [
            "Melaksanakan sholat khusuf di balai desa",
            "Melaksanakan sholat gaib berjamaah untuk mendoakan almarhum",
            "Membuat nisan kosong tanpa doa jenazah",
            "Mengganti kewajiban sholat dengan membayar fidyah 1 sha' beras"
        ],
        "answer": 1,
        "explanation": "Bila seorang muslim wafat di tempat yang jauh atau jenazahnya tidak berada di hadapan jamaah (misal hilang di perairan/musibah bencana alam setelah pencarian dinyatakan selesai), disyariatkan melaksanakan Sholat Gaib sebagaimana Rasulullah SAW menyalatkan jenazah Raja Najasyi (Ash-hamah) di Madinah saat wafat di Habasyah.",
        "source": "HR. Bukhari No. 1318 & Muslim No. 951; Keputusan Bahtsul Masail NU & Tarjih Muhammadiyah"
    },
    {
        "id": 506,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "sedang",
        "question": "Berikut ini pihak yang paling berhak dan utama memandikan jenazah laki-laki dewasa yang wafat di desa secara syar'i adalah...",
        "options": [
            "Kasi Pelayanan bersama Kepala Desa",
            "Istri atau kerabat laki-laki terdekat yang paham tata cara memandikan dan amanah menjaga aib jenazah",
            "Tetangga laki-laki yang berusia paling tua di lingkungan RT",
            "Bidan desa atau tenaga kesehatan puskesmas pembantu"
        ],
        "answer": 1,
        "explanation": "Dalam syariat Islam, pihak yang paling utama memandikan jenazah adalah istri almarhum atau anggota keluarga laki-laki terdekat (ayah, anak kandung, saudara laki-laki) yang memahami tata cara bersuci/thaharah serta terpercaya (amanah) untuk menutup aib fisik almarhum, didampingi oleh petugas rohani (modin/amil).",
        "source": "Kitab Al-Majmu' Syarah al-Muhadzdzab Imam An-Nawawi, Juz 5"
    },
    {
        "id": 507,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "mudah",
        "question": "Saat proses pemakaman jenazah muslim di tempat pemakaman umum (TPU) desa, posisi jenazah di dalam liang lahad diletakkan dengan cara...",
        "options": [
            "Terlentang membujur ke arah barat dengan mata memandang ke atas",
            "Dimiringkan ke sisi lambung kanan menghadap arah kiblat dan tali kain kafan dilepas",
            "Duduk menghadap pintu masuk pemakaman",
            "Tengkurap dengan kepala menghadap ke timur"
        ],
        "answer": 1,
        "explanation": "Sunnah dan rukun dalam penguburan jenazah muslim adalah meletakkan jenazah miring di atas lambung kanan menghadap ke arah kiblat. Tali pengikat kafan pada bagian kepala dan tubuh dilepas, serta pipi kanan disentuhkan ke tanah/lahad.",
        "source": "Fathul Mu'in Hamisy I'anatut Thalibin, Bab Ahkam al-Janaiz"
    },
    {
        "id": 508,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "sedang",
        "question": "Bagaimanakah ketentuan syariat Islam terhadap orang yang meninggal dunia dalam keadaan mati syahid di medan perang membela negara/agama?",
        "options": [
            "Wajib dimandikan tujuh kali dan dikafani lima lapis",
            "Tidak dimandikan dan tidak dishalatkan, melainkan langsung dimakamkan bersama pakaian yang dikenakannya",
            "Hanya dishalatkan tanpa perlu dikubur di liang lahad",
            "Cukup ditayamumkan oleh modin lalu dishalatkan seperti jenazah biasa"
        ],
        "answer": 1,
        "explanation": "Jenazah muslim yang wafat sebagai Syahid Ma'rakah (syahid medan perang membela kebenaran/negara) memiliki kekhususan syariat: tidak dimandikan dan tidak dishalatkan, melainkan langsung dimakamkan dengan pakaian yang berlumuran darah yang melekat di tubuhnya sebagai saksi kemuliaan di hari kiamat.",
        "source": "HR. Bukhari No. 1343 tentang Syuhada Perang Uhud; Kitab Al-Umm Imam Asy-Syafi'i"
    },
    {
        "id": 509,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "mudah",
        "question": "Tujuan utama anjuran ber-ta'ziyah (melayat) ke rumah duka keluarga warga desa yang sedang tertimpa musibah kematian adalah...",
        "options": [
            "Menuntut pembagian warisan tanah kas desa secepatnya",
            "Menghibur dan menguatkan hati keluarga yang berduka (tasliyah), mendoakan jenazah, serta membantu meringankan beban mereka",
            "Mengadakan pesta perayaan perpisahan warga",
            "Meminta pertanggungjawaban panitia rukun kematian tingkat dusun"
        ],
        "answer": 1,
        "explanation": "Ta'ziyah secara bahasa bermakna tasliyah (menghibur). Tujuannya adalah meringankan duka nestapa keluarga yang ditinggalkan, menasihati agar bersabar dan ridha terhadap takdir Allah SWT, mendoakan ampunan bagi si mayit, serta dianjurkan membuatkan makanan bagi keluarga duka (sebagaimana hadits riwayat Abu Daud: 'Buatkanlah makanan untuk keluarga Ja'far').",
        "source": "HR. Abu Daud No. 3132 & Tirmidzi No. 998; Kitab Riyadhus Shalihin Imam An-Nawawi"
    },
    {
        "id": 510,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "sedang",
        "question": "Sebelum proses pemakaman jenazah selesai dan keluarga duka meninggalkan area pemakaman, perangkat desa atau tokoh agama setempat biasanya menyampaikan pengumuman terkait hak adami si mayit, yaitu...",
        "options": [
            "Menyita rumah almarhum untuk kas rukun tetangga",
            "Meminta permohonan maaf dan mengimbau siapa pun yang memiliki urusan piutang/tanggungan dengan almarhum agar menghubungi ahli warisnya",
            "Membacakan riwayat slip gaji almarhum selama bekerja",
            "Menginstruksikan seluruh pelayat membayar iuran wajib pemakaman tunai"
        ],
        "answer": 1,
        "explanation": "Hak adami (utang piutang dan sengketa antarmanusia) merupakan tanggungan yang sangat berat bagi orang yang telah meninggal dunia. Perangkat desa/modin bertugas mengumumkan kepada warga agar memaafkan kesalahan almarhum dan meminta pihak yang memiliki sangkutan hak/piutang segera menyelesaikan bersama ahli waris almarhum secara musyawarah.",
        "source": "HR. Tirmidzi No. 1078 ('Jiwa seorang mukmin terkatung-katung karena utangnya sampai dilunasi'); Norma Adat Desa Muslim"
    },

    # =========================================================================
    # BAGIAN 2: ZAKAT FITRAH, ZAKAT MAL, DAN WAKAF DESA (Q511 - Q518)
    # =========================================================================
    {
        "id": 511,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "mudah",
        "question": "Besaran takaran Zakat Fitrah per jiwa bagi umat Islam di Indonesia yang dibayarkan berupa makanan pokok beras adalah setara dengan...",
        "options": [
            "1 mud atau sekitar 0,6 kg beras",
            "1 sha' atau setara dengan 2,5 kg / 3,5 liter beras berkualitas baik",
            "5 wasaq atau sekitar 653 kg gabah kering panen",
            "10 liter beras ketan putih"
        ],
        "answer": 1,
        "explanation": "Kewajiban zakat fitrah adalah 1 sha' makanan pokok (kurma, gandum, atau beras di Indonesia). Berdasarkan Keputusan Komisi Fatwa MUI dan Surat Keputusan Ketua BAZNAS, 1 sha' beras setara dengan 2,5 kg atau 3,5 liter beras per jiwa yang dikonsumsi sehari-hari.",
        "source": "SK Ketua BAZNAS No. 10 Tahun 2024 & Fatwa MUI tentang Standar Ukuran Zakat Fitrah"
    },
    {
        "id": 512,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "sedang",
        "question": "Waktu terbaik (afdhal) untuk membayarkan Zakat Fitrah kepada panitia amil/UPZ desa adalah...",
        "options": [
            "Pada awal bulan Sya'ban sebelum memasuki bulan puasa",
            "Mulai terbit fajar tanggal 1 Syawal hingga sebelum dimulainya Sholat Idul Fitri",
            "Setelah sholat Idul Fitri pada siang hari hari raya",
            "Pada tanggal 10 Dzulhijjah bersamaan dengan penyembelihan hewan qurban"
        ],
        "answer": 1,
        "explanation": "Waktu afdhal pembayaran zakat fitrah adalah sejak terbit fajar 1 Syawal hingga sebelum pelaksanaan Sholat Idul Fitri. Bila dibayarkan setelah sholat Idul Fitri selesai tanpa uzur syar'i, pembayarannya dihukumi sedekah biasa dan tidak terhitung sebagai zakat fitrah yang sempurna.",
        "source": "HR. Abu Daud No. 1609 & Ibnu Majah No. 1827; Fiqih Syafi'iyah"
    },
    {
        "id": 513,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "sedang",
        "question": "Berdasarkan Al-Qur'an Surat At-Taubah ayat 60, siapakah yang berhak menerima penyaluran zakat (asnaf delapan)?",
        "options": [
            "Perangkat desa, BPD, pengurus RT, dan anggota linmas",
            "Fakir, miskin, amil, muallaf, riqab (hamba sahaya), gharimin (orang berutang), fisabilillah, dan ibnu sabil (musafir)",
            "Keluarga kepala desa, donatur masjid, dan aparat keamanan kecamatan",
            "Penyelenggara lelang tanah kas desa dan kontraktor pembangunan balai desa"
        ],
        "answer": 1,
        "explanation": "Surat At-Taubah ayat 60 secara tegas menetapkan 8 golongan mustahiq zakat (Asnaf Tsamaniyah): 1. Fakir, 2. Miskin, 3. Amil zakat, 4. Muallaf, 5. Riqab, 6. Gharimin, 7. Fisabilillah, dan 8. Ibnu Sabil. Zakat tidak boleh dialokasikan di luar 8 asnaf ini.",
        "source": "Al-Qur'an Surat At-Taubah Ayat 60 & UU No. 23 Tahun 2011 tentang Pengelolaan Zakat"
    },
    {
        "id": 514,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "sulit",
        "question": "Seorang petani di desa memanen padi dari sawah tadah hujan (mengandalkan air hujan alami tanpa biaya bahan bakar pompa/irigasi). Berapakah persentase zakat hasil pertanian yang wajib dikeluarkannya bila panennya telah mencapai nisab 5 wasaq (sekitar 653 kg gabah kering)?",
        "options": [
            "2,5% dari total penjualan gabah",
            "5% dari hasil panen kotor",
            "10% dari total hasil panen padi",
            "20% dari keuntungan bersih setelah dikurangi modal"
        ],
        "answer": 2,
        "explanation": "Berdasarkan hadits Rasulullah SAW riwayat Bukhari: hasil tanaman pertanian yang diairi dengan air hujan alami/mata air (tanpa biaya) wajib dikeluarkan zakatnya sebesar 10% (sepersepuluh). Sedangkan jika diairi menggunakan sarana irigasi berbiaya (pompa air/diesel/genset), zakatnya adalah 5% (seperdua puluh).",
        "source": "HR. Bukhari No. 1483 & Kitab Bidayatul Mujtahid Ibnu Rusyd"
    },
    {
        "id": 515,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "sedang",
        "question": "Berdasarkan UU Nomor 41 Tahun 2004 tentang Wakaf, apakah status hukum tanah wakaf yang diperuntukkan bagi masjid, pemakaman, atau madrasah di desa?",
        "options": [
            "Dapat diperjualbelikan oleh ahli waris wakif jika kas keluarga menipis",
            "Dapat disita oleh pengadilan untuk melunasi utang pribadi nadzir",
            "Kekal manfaatnya untuk kepentingan umum dan dilarang keras untuk dijual, diwariskan, dihibahkan, ditukar, atau disita",
            "Otomatis beralih menjadi tanah bengkok Kepala Desa"
        ],
        "answer": 2,
        "explanation": "Pasal 40 UU No. 41 Tahun 2004 tentang Wakaf menegaskan bahwa harta benda wakaf dilarang: a. dijadikan jaminan; b. disita; c. dihibahkan; d. dijual; e. diwariskan; f. ditukar; atau g. dialihkan dalam bentuk pengalihan hak lainnya. Pelanggaran atas pasal ini memiliki konsekuensi pidana.",
        "source": "UU No. 41 Tahun 2004 tentang Wakaf Pasal 40 & PP No. 42 Tahun 2006"
    },
    {
        "id": 516,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "sedang",
        "question": "Pejabat yang berwenang membuat Akta Ikrar Wakaf (AIW) untuk legalitas tanah wakaf di wilayah perdesaan adalah...",
        "options": [
            "Kepala Seksi Pelayanan dan Sekretaris BPD",
            "Pejabat Pembuat Akta Ikrar Wakaf (PPAIW), yang dijabat oleh Kepala Kantor Urusan Agama (KUA) Kecamatan setempat",
            "Ketua Lembaga Pemberdayaan Masyarakat (LPM)",
            "Pengurus Karang Taruna Desa"
        ],
        "answer": 1,
        "explanation": "Menurut UU No. 41 Tahun 2004 dan PMA No. 73 Tahun 2013, ikrar wakaf wajib dituangkan dalam Akta Ikrar Wakaf (AIW) di hadapan PPAIW (Pejabat Pembuat Akta Ikrar Wakaf), yaitu Kepala Kantor Urusan Agama (KUA) kecamatan setempat, disaksikan oleh minimal 2 orang saksi.",
        "source": "UU No. 41 Tahun 2004 Pasal 37 jo. Peraturan Menteri Agama No. 73 Tahun 2013"
    },
    {
        "id": 517,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "sedang",
        "question": "Pihak yang ditunjuk oleh wakif untuk menerima, memelihara, dan mengelola harta benda wakaf di desa (seperti takmir masjid desa) disebut...",
        "options": [
            "Mauquf 'alaih",
            "Nadzir",
            "Musytari",
            "Murtahin"
        ],
        "answer": 1,
        "explanation": "Dalam rukun wakaf terdapat 4 unsur: 1. Wakif (pihak yang mewakafkan), 2. Mauquf bih (harta yang diwakafkan), 3. Mauquf 'alaih (pihak penerima manfaat/peruntukan wakaf), dan 4. Nadzir (pihak yang menerima amanah memelihara dan mengelola harta benda wakaf).",
        "source": "UU No. 41 Tahun 2004 tentang Wakaf Pasal 6 & Fiqih Muamalah Kontemporer"
    },
    {
        "id": 518,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "mudah",
        "question": "Tradisi sedekah bumi atau tasyakuran desa yang rutin diselenggarakan oleh masyarakat pedesaan Jawa (seperti di Kabupaten Tuban) menurut kacamata dakwah Islam yang moderat dimaknai sebagai...",
        "options": [
            "Upacara peribadatan syirik yang wajib dilarang keras oleh kepala desa",
            "Sarana bersyukur kepada Allah SWT atas limpahan rezeki hasil bumi, mempererat silaturahmi antarwarga, dan sedekah makanan yang diisi doa bersama",
            "Ajang pesta pemborosan anggaran kas desa",
            "Kewajiban konstitusi negara yang mengikat secara hukum pidana"
        ],
        "answer": 1,
        "explanation": "Pendekatan dakwah kultural para Walisongo (termasuk Sunan Bonang) mentransformasikan tradisi sedekah bumi menjadi sarana syukur kepada Allah SWT (Rabbul 'Alamin), mempererat kerukunan/silaturahmi, berbagi sedekah makanan kepada sesama, dan tahlil/doa bersama untuk keselamatan desa dari bencana.",
        "source": "Pedoman Dakwah Kultural MUI & Sejarah Akulturasi Islam Nusantara"
    },

    # =========================================================================
    # BAGIAN 3: TUGAS MODIN/KESRA & HUKUM PERKAWINAN ISLAM (Q519 - Q526)
    # =========================================================================
    {
        "id": 519,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "mudah",
        "question": "Dalam struktur perangkat desa di Jawa Timur, tugas pelayanan sosial keagamaan, pengurusan jenazah, pembinaan nikah, dan doa desa secara tradisional diemban oleh perangkat atau staf pembantu yang dikenal dengan sebutan...",
        "options": [
            "Bayan atau Jogoboyo",
            "Modin (Kasi Pelayanan / Urusan Kesra)",
            "Ulu-ulu atau Kamituwo",
            "Pamong Tani Desa"
        ],
        "answer": 1,
        "explanation": "Secara kultural dan sosiologis di Jawa, 'Modin' (Lebe/Kaum) adalah sebutan untuk perangkat desa yang mengurusi urusan keagamaan, pernikahan, kematian (rohani), dan sosial kemasyarakatan. Dalam nomenklatur modern Permendagri No. 84/2015, tugas ini diintegrasikan ke dalam fungsi Kepala Seksi Pelayanan.",
        "source": "Permendagri No. 84 Tahun 2015 Pasal 9 ayat (4) & Sosiologi Hukum Desa Tuban"
    },
    {
        "id": 520,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "sedang",
        "question": "Berdasarkan Undang-Undang Nomor 16 Tahun 2019 tentang Perubahan atas UU No. 1 Tahun 1974 tentang Perkawinan, batas usia minimal perkawinan bagi pria dan wanita adalah...",
        "options": [
            "Pria 18 tahun dan wanita 16 tahun",
            "Pria dan wanita sama-sama minimal berusia 19 tahun",
            "Pria 21 tahun dan wanita 18 tahun",
            "Pria 20 tahun dan wanita 17 tahun"
        ],
        "answer": 1,
        "explanation": "Pasal 7 ayat (1) UU No. 16 Tahun 2019 mengubah batas usia perkawinan, yaitu perkawinan hanya diizinkan apabila pria dan wanita sudah mencapai usia 19 (sembilan belas) tahun. Perangkat desa bertugas melakukan edukasi guna mencegah perkawinan usia anak di desa.",
        "source": "UU No. 16 Tahun 2019 tentang Perubahan atas UU No. 1 Tahun 1974 tentang Perkawinan Pasal 7"
    },
    {
        "id": 521,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "sedang",
        "question": "Rukun nikah dalam hukum syariat Islam yang wajib dipenuhi agar akad perkawinan sah terdiri atas...",
        "options": [
            "Calon mempelai pria, calon mempelai wanita, wali nikah, dua orang saksi laki-laki yang adil, serta ijab dan kabul",
            "Kepala desa, ketua BPD, saksi satu orang, mahar berupa mobil, dan pesta resepsi",
            "Penghulu KUA, camat, surat perjanjian pranikah, dan seragam dinas",
            "Undangan minimal 100 orang warga RT, tumpeng, dan hiburan rakyat"
        ],
        "answer": 0,
        "explanation": "Rukun nikah menurut Kompilasi Hukum Islam (KHI) Pasal 14 dan jumhur ulama mazhab Syafi'i ada 5: 1. Calon mempelai pria, 2. Calon mempelai wanita, 3. Wali nikah dari pihak wanita, 4. Dua orang saksi laki-laki yang adil dan baligh, 5. Ijab dan Kabul (shighat akad).",
        "source": "Instruksi Presiden No. 1 Tahun 1991 tentang Kompilasi Hukum Islam (KHI) Pasal 14"
    },
    {
        "id": 522,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "sulit",
        "question": "Jika seorang ayah kandung dari calon mempelai wanita telah meninggal dunia, siapakah urutan wali nasab berikutnya yang paling berhak menjadi wali nikah?",
        "options": [
            "Paman kandung dari pihak ibu",
            "Kakek kandung dari pihak ayah (ayah dari ayah) atau saudara laki-laki kandung (seayah seibu)",
            "Tetangga tertua yang dituakan di rukun tetangga",
            "Suami dari saudara perempuan calon pengantin wanita"
        ],
        "answer": 1,
        "explanation": "Urutan prioritas wali nasab dalam KHI Pasal 21 dan fikih Syafi'i: 1. Ayah kandung, 2. Kakek (ayah dari ayah) ke atas, 3. Saudara laki-laki kandung seayah seibu, 4. Saudara laki-laki seayah, 5. Anak laki-laki dari saudara kandung, 6. Paman (saudara ayah), dst. Kerabat dari pihak ibu bukan merupakan wali nasab pernikahan.",
        "source": "Kompilasi Hukum Islam (KHI) Pasal 21 & Kitab Fathul Qarib al-Mujib"
    },
    {
        "id": 523,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "sedang",
        "question": "Pernikahan yang dilaksanakan hanya secara agama/adat tanpa dicatatkan pada Kantor Urusan Agama (KUA) atau Kantor Catatan Sipil sering disebut nikah siri. Mengapa perangkat desa berkewajiban mengedukasi warga agar mencatatkan pernikahan secara resmi?",
        "options": [
            "Agar pemerintah desa mendapat komisi retribusi dari KUA",
            "Untuk menjamin kepastian hukum hak keperdataan istri dan anak (seperti akta kelahiran, hak nafkah, dan hak waris)",
            "Karena nikah resmi membebaskan warga dari kewajiban gotong royong",
            "Agar seluruh mas kawin diserahkan ke kas rukun kampung"
        ],
        "answer": 1,
        "explanation": "Pencatatan perkawinan (UU No. 1/1974 Pasal 2 ayat 2) sangat krusial untuk melindungi hak-hak hukum perempuan dan anak. Tanpa akta nikah resmi, anak akan kesulitan mendapatkan akta kelahiran berkekuatan hukum penuh, hak nafkah, perwalian hukum, serta pembagian hak waris bila terjadi perceraian atau kematian.",
        "source": "UU No. 1 Tahun 1974 Pasal 2 ayat (2) & Putusan MK No. 46/PUU-VIII/2010"
    },
    {
        "id": 524,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "mudah",
        "question": "Dalam administrasi desa, dokumen surat pengantar yang diterbitkan oleh pemerintah desa (Kasi Pelayanan/Sekdes) untuk warga yang hendak melangsungkan pernikahan di KUA dikenal sebagai model formulir...",
        "options": [
            "Surat Keterangan Kematian (Model A)",
            "Surat Pengantar Perkawinan (Model N1) dan Permohonan Kehendak Nikah",
            "Surat Pernyataan Bebas Narkoba",
            "Surat Izin Usaha Perdagangan (SIUP)"
        ],
        "answer": 1,
        "explanation": "Berdasarkan Peraturan Menteri Agama No. 20 Tahun 2019 tentang Pencatatan Pernikahan, calon pengantin wajib melampirkan Surat Pengantar Perkawinan dari Kepala Desa/Lurah (Formulir Model N1, N2, N4) sebagai bukti status kependudukan dan persetujuan kehendak nikah.",
        "source": "PMA No. 20 Tahun 2019 tentang Pencatatan Pernikahan Pasal 4 & Permendagri No. 47/2016"
    },
    {
        "id": 525,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "sedang",
        "question": "Apabila calon mempelai wanita tidak memiliki wali nasab sama sekali atau walinya 'adhol' (enggan menikahkan tanpa alasan syar'i setelah diputus oleh Pengadilan Agama), maka akad nikah dilaksanakan dengan perwalian dari...",
        "options": [
            "Wali Hakim (Kepala KUA atas pelimpahan kewenangan Menteri Agama)",
            "Kepala Seksi Pemerintahan Desa",
            "Ketua RT setempat",
            "Calon mertua laki-laki"
        ],
        "answer": 0,
        "explanation": "KHI Pasal 23 mengatur bahwa bila wali nasab tidak ada, gaib, atau berstatus adhal (enggan) berdasarkan penetapan/putusan Pengadilan Agama, maka hak perwalian berpindah kepada Wali Hakim (Sultan/Menteri Agama yang didelegasikan kepada Kepala KUA Kecamatan setempat).",
        "source": "Kompilasi Hukum Islam (KHI) Pasal 23 & PMA No. 20 Tahun 2019"
    },
    {
        "id": 526,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "mudah",
        "question": "Harta yang diperoleh suami dan istri secara bersama-sama selama ikatan perkawinan berlangsung dalam hukum Islam di Indonesia dan perundang-undangan dikenal sebagai...",
        "options": [
            "Harta bawaan masing-masing",
            "Harta bersama (gono-gini)",
            "Harta pusaka tinggi adat",
            "Harta hibah wasiat wajibah"
        ],
        "answer": 1,
        "explanation": "Menurut Pasal 35 UU No. 1/1974 dan KHI Pasal 85, harta benda yang diperoleh selama perkawinan menjadi harta bersama (harta gono-gini). Sedangkan harta bawaan masing-masing suami atau istri sebelum menikah dan harta hibah/warisan tetap di bawah penguasaan masing-masing.",
        "source": "UU No. 1 Tahun 1974 Pasal 35 & Kompilasi Hukum Islam (KHI) Bab XIII"
    },

    # =========================================================================
    # BAGIAN 4: MODERASI BERAGAMA & KERUKUNAN UMAT BERAGAMA (Q527 - Q534)
    # =========================================================================
    {
        "id": 527,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "sedang",
        "question": "Prinsip dasar 'Moderasi Beragama' (Wasathiyah) yang digaungkan oleh Kementerian Agama dan harus ditegakkan di lingkungan desa mencakup 4 pilar utama, yaitu...",
        "options": [
            "Komitmen kebangsaan, toleransi, anti-kekerasan, dan akomodatif terhadap kebudayaan lokal",
            "Keseragaman keyakinan, pemusatan tempat ibadah, asimilasi etnis paksa, dan kepatuhan mutlak",
            "Penghapusan ritual adat, privatisasi agama total, penutupan forum dialog, dan sentralisme kas",
            "Pemisahan wilayah mukim berdasarkan suku, pemungutan pajak keyakinan, dan peradilan adat tertutup"
        ],
        "answer": 0,
        "explanation": "Empat indikator utama Moderasi Beragama menurut Kemenag RI: 1. Komitmen kebangsaan (penerimaan Pancasila & UUD 1945), 2. Toleransi (menghormati perbedaan keyakinan), 3. Anti-kekerasan (menolak ekstremisme/radikalisme), dan 4. Akomodatif terhadap kebudayaan lokal yang selaras dengan nilai agama.",
        "source": "Buku Moderasi Beragama Kementerian Agama RI (2019) & Perpres No. 58 Tahun 2023"
    },
    {
        "id": 528,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "mudah",
        "question": "Landasan Al-Qur'an yang menegaskan bahwa keragaman manusia diciptakan bersuku-suku dan berbangsa-bangsa agar saling mengenal dan bekerja sama terdapat dalam...",
        "options": [
            "Surat Al-Baqarah ayat 282",
            "Surat Al-Hujurat ayat 13",
            "Surat Al-Ikhlas ayat 1-4",
            "Surat Al-Fil ayat 1-5"
        ],
        "answer": 1,
        "explanation": "Surat Al-Hujurat ayat 13 menyatakan: 'Wahai manusia! Sungguh, Kami telah menciptakan kamu dari seorang laki-laki dan seorang perempuan, kemudian Kami jadikan kamu berbangsa-bangsa dan bersuku-suku agar kamu saling mengenal (li ta'arafu). Sungguh, yang paling mulia di antara kamu di sisi Allah ialah orang yang paling bertakwa.'",
        "source": "Al-Qur'an Surat Al-Hujurat Ayat 13 & Tafsir Al-Misbah Quraish Shihab"
    },
    {
        "id": 529,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "sedang",
        "question": "Surat Al-Kafirun ayat terakhir yang berbunyi 'Lakum diinukum waliyadiin' (Untukmu agamamu, dan untukku agamaku) merupakan panduan fundamental umat beragama dalam hal...",
        "options": [
            "Mencampuradukkan ritual peribadatan antaragama demi kompromi politik",
            "Menjaga kemurnian akidah pribadi tanpa menghina, mencela, atau memaksakan keyakinan kepada pemeluk agama lain (toleransi beragama)",
            "Melarang umat lain bermukim di desa yang mayoritas muslim",
            "Membatasi hak warga non-muslim dalam mendapatkan pelayanan surat kependudukan"
        ],
        "answer": 1,
        "explanation": "Surat Al-Kafirun mengajarkan batasan toleransi: dalam hal akidah dan ibadah mahdhah tidak boleh ada kompromi/sinkretisme, namun dalam muamalah dan relasi sosial kemasyarakatan wajib menjunjung tinggi saling menghormati, tidak memaksakan kehendak, dan menjaga kedamaian antarumat beragama.",
        "source": "Al-Qur'an Surat Al-Kafirun Ayat 6 & Tafsir Ibnu Katsir"
    },
    {
        "id": 530,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "sulit",
        "question": "Dokumen konstitusi tertulis pertama dalam sejarah peradaban Islam yang digagas oleh Nabi Muhammad SAW untuk menyatukan masyarakat majemuk Madinah (kaum muslimin Muhajirin, Anshar, serta kaum Yahudi dan Nasrani) dalam satu kesatuan bangsa dikenal sebagai...",
        "options": [
            "Perjanjian Hudaibiyah",
            "Piagam Madinah (Mitsaq al-Madinah)",
            "Fathu Makkah",
            "Bai'at 'Aqabah Pertama"
        ],
        "answer": 1,
        "explanation": "Piagam Madinah (Mitsaq al-Madinah) tahun 622 M adalah piagam konstitusional pertama di dunia yang menjamin kebebasan beragama, kesetaraan hak dan kewajiban warga negara, persatuan mempertahankan wilayah, serta penegakan keadilan tanpa diskriminasi bagi masyarakat Madinah yang majemuk.",
        "source": "Sirah Nabawiyah Ibnu Hisyam & Tarikh Thabari, Bab Konstitusi Madinah"
    },
    {
        "id": 531,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "sedang",
        "question": "Peraturan Bersama Menteri Agama dan Menteri Dalam Negeri (PBM) Nomor 9 dan Nomor 8 Tahun 2006 mengatur tentang pedoman pelaksanaan tugas kepala daerah/perangkat dalam hal...",
        "options": [
            "Pemilihan kepala desa serentak",
            "Pemeliharaan kerukunan umat beragama, pemberdayaan Forum Kerukunan Umat Beragama (FKUB), dan pendirian rumah ibadat",
            "Pengelolaan aset tanah kas desa untuk perkebunan sawit",
            "Penataan pos bantuan hukum terpadu tingkat kecamatan"
        ],
        "answer": 1,
        "explanation": "PBM No. 9 dan 8 Tahun 2006 merupakan regulasi kunci yang mewajibkan kepala daerah dan jajaran pemerintahan hingga tingkat desa menjaga kerukunan umat beragama, memfasilitasi FKUB, serta mengatur persyaratan teknis dan administratif pendirian rumah ibadat demi ketenteraman bersama.",
        "source": "Peraturan Bersama Menteri Agama dan Menteri Dalam Negeri No. 9 dan 8 Tahun 2006"
    },
    {
        "id": 532,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "sedang",
        "question": "Sikap 'Tasamuh' dalam konsep ukhuwah Islamiyah dan kemasyarakatan perdesaan mengandung makna...",
        "options": [
            "Sikap acuh tak acuh terhadap kebersihan lingkungan",
            "Sikap tenggang rasa, lapang dada, dan saling menghormati perbedaan latar belakang keyakinan maupun suku",
            "Sikap memaksakan pendapat kelompok sendiri dalam musdes",
            "Sikap mengutamakan kepentingan pribadi di atas kepentingan umum"
        ],
        "answer": 1,
        "explanation": "Tasamuh berarti toleransi, kelapangan dada, dan tenggang rasa. Sikap tasamuh menjadi modal sosial paling berharga bagi masyarakat desa di Indonesia dalam merajut kerukunan, mencegah polarisasi, dan menjaga keharmonisan antarwarga.",
        "source": "Pedoman Moderasi Beragama Kemenag RI & Risalah Ahlussunnah wal Jama'ah"
    },
    {
        "id": 533,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "sedang",
        "question": "Tiga pilar persaudaraan (Tri Ukhuwah) yang diajarkan oleh ulama Indonesia (seperti KH. Achmad Siddiq) untuk menjaga keutuhan Negara Kesatuan Republik Indonesia adalah...",
        "options": [
            "Ukhuwah Islamiyah (persaudaraan seagama), Ukhuwah Wathaniyah (persaudaraan sebangsa setanah air), dan Ukhuwah Insaniyah/Basyariyah (persaudaraan sesama manusia)",
            "Ukhuwah partai, ukhuwah ormas, dan ukhuwah marga",
            "Ukhuwah niaga, ukhuwah profesi, dan ukhuwah dinas",
            "Ukhuwah sekuler, ukhuwah liberal, dan ukhuwah feodal"
        ],
        "answer": 0,
        "explanation": "Tri Ukhuwah adalah konsep agung harmoni sosial: 1. Ukhuwah Islamiyah (persaudaraan sesama muslim), 2. Ukhuwah Wathaniyah (persaudaraan sebangsa melintasi sekat agama/suku), dan 3. Ukhuwah Insaniyah/Basyariyah (persaudaraan universal sesama umat manusia).",
        "source": "Konsep Tri Ukhuwah Muktamar NU Ke-27 Situbondo (1984) & Pemikiran Gus Dur"
    },
    {
        "id": 534,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "sedang",
        "question": "Jika terjadi perselisihan atau kesalahpahaman antarkelompok warga di desa akibat isu keagamaan di media sosial, langkah preventif terbaik yang wajib diambil perangkat desa adalah...",
        "options": [
            "Membiarkan perselisihan membesar agar warga terbiasa berkonflik",
            "Mengadakan dialog tabayyun (klarifikasi/mediasi) secara persuasif bersama BPD, Babinsa, Bhabinkamtibmas, dan tokoh agama setempat",
            "Mendukung salah satu pihak yang paling banyak memberikan suara saat pilkades",
            "Mengusir pihak minoritas dari lingkungan desa"
        ],
        "answer": 1,
        "explanation": "Prinsip Tabayyun (klarifikasi fakta) sesuai Al-Qur'an Surat Al-Hujurat ayat 6 merupakan metode islami yang dipadukan dengan kearifan musyawarah desa. Perangkat desa bersama Tiga Pilar (Kepala Desa, Babinsa, Bhabinkamtibmas) dan tokoh agama wajib memediasi secara netral dan adil demi ketenteraman umum.",
        "source": "Al-Qur'an Surat Al-Hujurat Ayat 6 & Pedoman Penanganan Konflik Sosial Permendagri No. 42/2015"
    },

    # =========================================================================
    # BAGIAN 5: ETIKA KEPEMIMPINAN ISLAMI & INTEGRITAS AMANAH PUBLIK (Q535 - Q542)
    # =========================================================================
    {
        "id": 535,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "mudah",
        "question": "Empat sifat mulia Nabi Muhammad SAW yang wajib dijadikan teladan etika kepemimpinan moral oleh seorang perangkat desa adalah...",
        "options": [
            "Siddiq (jujur), Amanah (dapat dipercaya), Tabligh (transparan/menyampaikan), dan Fathonah (cerdas/bijaksana)",
            "Kadzib, Khianat, Kitman, dan Baladah",
            "Egois, Ambisius, Otoriter, dan Tertutup",
            "Riya', Sum'ah, 'Ujub, dan Takabbur"
        ],
        "answer": 0,
        "explanation": "Empat sifat wajib bagi Rasulullah SAW: 1. Siddiq (integritas, berkata dan berbuat benar), 2. Amanah (dapat dipercaya mengelola aset dan uang desa), 3. Tabligh (transparan dalam informasi publik desa), 4. Fathonah (cerdas mencari solusi permasalahan masyarakat). Lawan sifat ini adalah sifat mustahil bagi rasul.",
        "source": "Aqidatul Awam Syaikh Ahmad al-Marzuqi & Etika Kepemimpinan Pelayanan Publik"
    },
    {
        "id": 536,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "mudah",
        "question": "Hadits Nabi Muhammad SAW yang menegaskan bahwa 'Kullukum ra'in wa kullukum mas'ulun 'an ra'iyyatihi' mengandung makna mendalam bahwa...",
        "options": [
            "Setiap orang boleh berbuat sesuka hatinya tanpa aturan",
            "Setiap kalian adalah pemimpin dan setiap pemimpin pasti akan dimintai pertanggungjawaban atas kepemimpinannya di hadapan Allah SWT",
            "Hanya kepala desa yang akan ditanya pertanggungjawabannya di akhirat",
            "Perangkat desa tidak memiliki beban moral terhadap warga"
        ],
        "answer": 1,
        "explanation": "Hadits riwayat Bukhari dan Muslim: 'Kullukum ra'in wa kullukum mas'ulun 'an ra'iyyatihi...'. Pemimpin masyarakat bertanggung jawab atas rakyatnya, kepala keluarga bertanggung jawab atas keluarganya, dan setiap pemegang amanah akan dimintai hisab atas kewajibannya.",
        "source": "HR. Bukhari No. 893 & HR. Muslim No. 1829"
    },
    {
        "id": 537,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "sedang",
        "question": "Hukum menerima suap, uang pelicin, atau gratifikasi terselubung (risywah) bagi seorang perangkat desa dalam pelayanan administrasi warga adalah...",
        "options": [
            "Halal karena dianggap sebagai tanda ucapan terima kasih warga",
            "Haram mutlak dan dilaknat oleh Allah SWT serta Rasul-Nya",
            "Makruh bila nilainya di bawah seratus ribu rupiah",
            "Mubah bila disetor ke kas pengurus karang taruna"
        ],
        "answer": 1,
        "explanation": "Rasulullah SAW bersabda: 'La'natu Allahi 'ala ar-rasyi wal murtasyi' (Laknat Allah atas orang yang menyuap dan orang yang menerima suap). Dalam administrasi negara hal ini dikategorikan pungli/gratifikasi/tindak pidana korupsi yang melanggar UU No. 20/2001.",
        "source": "HR. Abu Daud No. 3580 & Tirmidzi No. 1337; Fatwa MUI No. 4/Munas VI/MUI/2000"
    },
    {
        "id": 538,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "sedang",
        "question": "Bagaimanakah sikap seorang perangkat desa yang beriman ketika mendapati perbedaan pilihan politik atau perselisihan pendapat dalam musyawarah rencana pembangunan desa?",
        "options": [
            "Menyerang pribadi peserta yang berbeda pandangan",
            "Mengedepankan adab musyawarah (syura), menghargai pendapat orang lain, dan berlapang dada menerima keputusan mufakat bersama",
            "Memboikot musyawarah desa",
            "Memutuskan sepihak tanpa melibatkan BPD dan warga"
        ],
        "answer": 1,
        "explanation": "Al-Qur'an Surat Asy-Syura ayat 38 memuji orang-orang yang menyelesaikan urusan mereka secara musyawarah ('wa amruhum syura bainahum'). Sikap lapang dada dan menghormati hasil mufakat adalah perwujudan akhlakul karimah seorang pelayan masyarakat.",
        "source": "Al-Qur'an Surat Asy-Syura Ayat 38 & Surat Ali 'Imran Ayat 159"
    },
    {
        "id": 539,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "sulit",
        "question": "Dalam kisah sahabat Umar bin Khattab RA saat menjadi Khalifah, beliau mematikan lampu minyak milik negara dan menggantinya dengan lampu minyak miliknya sendiri ketika berbincang tentang urusan pribadi dengan putranya. Hikmah utama kisah ini bagi penyelenggara keuangan desa adalah...",
        "options": [
            "Pentingnya hidup dalam kegelapan agar hemat listrik",
            "Ketegasan dalam memisahkan fasilitas/keuangan dinas negara dari kepentingan pribadi dan keluarga (kehati-hatian atas harta publik)",
            "Larangan membeli minyak lampu di pasar desa",
            "Keharusan memotong anggaran alat tulis kantor desa"
        ],
        "answer": 1,
        "explanation": "Keteladanan Khalifah Umar bin Khattab RA tersebut merupakan pelajaran tertinggi tentang integritas birokrasi: tidak menyalahgunakan satu sen pun uang atau fasilitas milik masyarakat/desa untuk urusan dan kepentingan pribadi keluarga.",
        "source": "Kitab Manaqib Amirul Mukminin Umar bin Khattab Ibnul Jauzi & Tarikh Khulafa As-Suyuthi"
    },
    {
        "id": 540,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "mudah",
        "question": "Prinsip amar ma'ruf nahi munkar dalam kehidupan bermasyarakat di desa wajib dijalankan dengan cara...",
        "options": [
            "Tindakan main hakim sendiri dan merusak fasilitas warga",
            "Hikmah, teladan yang baik (mau'izhah hasanah), dialog santun, serta koordinasi dengan aparat penegak hukum yang berwenang",
            "Membentuk kelompok milisi liar di tingkat RT",
            "Menyebarkan ujaran kebencian di pengeras suara masjid"
        ],
        "answer": 1,
        "explanation": "Al-Qur'an Surat An-Nahl ayat 125 menegaskan: 'Serulah (manusia) kepada jalan Tuhanmu dengan hikmah dan pengajaran yang baik, dan berdebatlah dengan mereka dengan cara yang baik.' Nahi munkar tidak boleh dilakukan dengan cara yang menimbulkan kemungkaran baru yang lebih besar.",
        "source": "Al-Qur'an Surat An-Nahl Ayat 125 & Fiqih Dakwah Syekh Jum'ah Amin"
    },
    {
        "id": 541,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "sedang",
        "question": "Seorang perangkat desa yang mengemban tugas mengelola Dana Bantuan Sosial (Bansos) bagi warga miskin desa namun menyunat atau memotong bantuan tersebut untuk keuntungan pribadinya, dalam pandangan agama dikategorikan sebagai tindakan...",
        "options": [
            "Ijtihad yang diperbolehkan demi kelancaran operasional",
            "Khianat atas amanah dan memakan harta anak yatim/fakir miskin secara batil yang diancam azab pedih",
            "Urusan perdata ringan yang cukup ditegur secara lisan",
            "Amalan sedekah paksa"
        ],
        "answer": 1,
        "explanation": "Memotong bansos fakir miskin adalah bentuk Ghulul (pengkhianatan terhadap amanah publik) dan memakan harta sesama secara zalim (Surat An-Nisa ayat 29). Di akhirat pelakunya akan memikul sendiri beban kezalimannya di hadapan Allah SWT.",
        "source": "Al-Qur'an Surat An-Nisa Ayat 29 & Surat Ali 'Imran Ayat 161 (Bab Ghulul)"
    },
    {
        "id": 542,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "mudah",
        "question": "Penerapan nilai 'Jujur dan Terpercaya' (Siddiq dan Amanah) oleh seorang Sekretaris Desa tecermin secara konkret dalam tindakan...",
        "options": [
            "Menyembunyikan buku ekspedisi agar tidak dibaca oleh BPD",
            "Mencatat seluruh surat masuk, surat keluar, dan realisasi anggaran belanja desa sesuai fakta riil tanpa manipulasi laporan kuitansi",
            "Menandatangani kuitansi kosong yang disodorkan pihak ketiga",
            "Mengganti tanggal keputusan kepala desa agar tidak kedaluwarsa"
        ],
        "answer": 1,
        "explanation": "Integritas moral perangkat desa dibuktikan dengan kesesuaian antara fakta lapangan dan catatan administrasi (jujur), serta tidak merekayasa nota kuitansi atau memalsukan dokumen demi keuntungan diri sendiri atau kelompok.",
        "source": "Permendagri No. 47 Tahun 2016 tentang Administrasi Desa & Kode Etik Pamong Desa"
    },

    # =========================================================================
    # BAGIAN 6: SEJARAH WALISONGO, SUNAN BONANG TUBAN & SYIAR NUSANTARA (Q543 - Q550)
    # =========================================================================
    {
        "id": 543,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "mudah",
        "question": "Salah satu tokoh Walisongo yang berdakwah di pesisir utara Jawa Timur dan makam keramatnya berada di Kelurahan Kutorejo, Kabupaten Tuban (sebelah barat Masjid Agung Tuban) adalah...",
        "options": [
            "Sunan Kudus (Ja'far Shadiq)",
            "Sunan Bonang (Raden Makhdum Ibrahim)",
            "Sunan Muria (Raden Umar Said)",
            "Sunan Gunung Jati (Syarif Hidayatullah)"
        ],
        "answer": 1,
        "explanation": "Sunan Bonang memiliki nama asli Raden Makhdum Ibrahim, putra dari Sunan Ampel dan Nyai Ageng Manila. Makam beliau terletak di jantung Kota Tuban (Kelurahan Kutorejo), menjadikan Kabupaten Tuban termasyhur dengan sebutan 'Bumi Wali'.",
        "source": "Babad Tuban & Sejarah Walisongo Agus Sunyoto (Atlas Walisongo)"
    },
    {
        "id": 544,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "sedang",
        "question": "Karya sastra suluk legendaris gubahan Sunan Bonang yang memuat wejangan tasawuf mendalam tentang makrifatullah dan pengendalian hawa nafsu adalah...",
        "options": [
            "Serat Centhini",
            "Suluk Wijil",
            "Kitab Sutasoma",
            "Babad Tanah Jawi"
        ],
        "answer": 1,
        "explanation": "Suluk Wijil adalah karya sastra mistik/tasawuf fenomenal karangan Sunan Bonang yang menceritakan dialog spiritual Sunan Bonang dengan Wijil, seorang bekas abdi dalem Majapahit, berisi ajaran tasawuf falsafi yang disajikan dengan bahasa Jawa yang santun dan filosofis.",
        "source": "Atlas Walisongo Agus Sunyoto & Naskah Manuskrip Suluk Wijil Koleksi Perpustakaan Nasional"
    },
    {
        "id": 545,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "mudah",
        "question": "Dalam menyampaikan dakwah Islam kepada masyarakat Jawa pada masanya, Sunan Bonang sangat bijaksana memanfaatkan media seni budaya, salah satunya dengan...",
        "options": [
            "Mewajibkan warga menghafal naskah dalam bahasa Arab tanpa terjemah",
            "Menggubah instrumen gamelan bonang (gong kecil berkoleksi nada khas) dan tembang Tombo Ati untuk memikat hati masyarakat",
            "Merobohkan candi peninggalan kerajaan kuno",
            "Melarang seluruh bentuk tembang dan karawitan Jawa"
        ],
        "answer": 1,
        "explanation": "Sunan Bonang memodifikasi alat musik gamelan Jawa dengan menambahkan instrumen 'bonang' (gong perunggu kecil berpencon) yang menghasilkan alunan nada mistis-meditatif, serta menggubah tembang Tombo Ati (Obat Hati) yang sarat muatan zikir, sholat malam, tadarus, dan pergaulan orang saleh.",
        "source": "Ensiklopedi Islam Nusantara & Sejarah Kebudayaan Islam Kemenag RI"
    },
    {
        "id": 546,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "sedang",
        "question": "Falsafah dakwah 'Moh Limo' (menolak 5 perkara maksiat: Moh Main, Moh Ngombe, Moh Madat, Moh Maling, Moh Madon) yang sangat berpengaruh dalam membersihkan moral masyarakat desa digagas oleh tokoh Walisongo, yaitu...",
        "options": [
            "Sunan Kalijaga",
            "Sunan Ampel (Raden Rahmat)",
            "Sunan Giri",
            "Sunan Muria"
        ],
        "answer": 1,
        "explanation": "Sunan Ampel (Raden Rahmat), ayahanda dari Sunan Bonang dan Sunan Drajat, meletakkan dasar ajaran moral 'Moh Limo': 1. Moh Main (tidak berjudi), 2. Moh Ngombe (tidak minum arak/mabuk), 3. Moh Madat (tidak memakai candu/narkoba), 4. Moh Maling (tidak mencuri/korupsi), 5. Moh Madon (tidak berzina).",
        "source": "Babad Ampel Denta & Atlas Walisongo"
    },
    {
        "id": 547,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "sedang",
        "question": "Sunan Drajat (Raden Qasim), adik kandung Sunan Bonang yang berdakwah di pesisir Lamongan (bersebelahan dengan Tuban), terkenal dengan 'Catur Piwulang' (empat ajaran luhur) untuk pemberdayaan masyarakat miskin. Ajaran 'Wenehono teken marang wong kang wuto' bermakna...",
        "options": [
            "Berilah tongkat petunjuk kepada orang yang buta (berilah ilmu bimbingan kepada mereka yang bodoh/tersesat)",
            "Berilah makanan kepada orang yang kenyang",
            "Berilah pakaian mewah kepada pejabat desa",
            "Berilah payung hanya kepada keluarga bangsawan"
        ],
        "answer": 0,
        "explanation": "Catur Piwulang Sunan Drajat: 1. Wenehono teken marang wong kang wuto (berilah petunjuk/ilmu pada yang buta), 2. Wenehono mangan marang wong kang luwe (berilah makan pada yang lapar), 3. Wenehono busana marang wong kang wudo (berilah pakaian/martabat pada yang telanjang), 4. Wenehono payung marang wong kang kodanan (berilah perlindungan pada yang kehujanan).",
        "source": "Manuskrip Sunan Drajat Museum Drajat Lamongan & Sejarah Islam Pesisir Jawa Timur"
    },
    {
        "id": 548,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "sedang",
        "question": "Metode dakwah para Walisongo di Nusantara yang memadukan ajaran Islam dengan kearifan adat lokal tanpa kekerasan dikenal dalam istilah sejarah kebudayaan sebagai...",
        "options": [
            "Invasi militer feodal",
            "Akulturasi budaya dan asimilasi damai (inkulturasi dakwah)",
            "Kolonisasi administratif",
            "Westernisasi nilai perdesaan"
        ],
        "answer": 1,
        "explanation": "Pendekatan dakwah Walisongo adalah akulturasi damai: nilai-nilai tauhid dan syariat dimasukkan secara halus ke dalam adat istiadat, wayang, tembang, arsitektur masjid (atap tumpang meru), dan tradisi desa tanpa menghancurkan kearifan lokal yang sudah mengakar.",
        "source": "Buku Menengok Dinamika Islam Nusantara Prof. Azyumardi Azra & Atlas Walisongo"
    },
    {
        "id": 549,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "mudah",
        "question": "Mengapa Kabupaten Tuban dijuluki sebagai 'Bumi Wali' atau 'Kota Wali'?",
        "options": [
            "Karena di Kabupaten Tuban terdapat makam salah satu Walisongo utama yaitu Sunan Bonang, serta makam banyak waliyullah/wali penyebar Islam terkemuka seperti Syekh Subakir, Syekh Maulana Ishaq, dan Sunan Bejagung",
            "Karena seluruh kepala desa di Kabupaten Tuban bergelar wali nikah",
            "Karena Kabupaten Tuban merupakan penghasil minyak goreng terbesar",
            "Karena hukum adat di Tuban menggantikan hukum positif Indonesia"
        ],
        "answer": 0,
        "explanation": "Tuban bergelar 'Bumi Wali' karena posisinya sebagai pelabuhan utama kerajaan Majapahit kuno yang menjadi pintu gerbang masuknya para juru dakwah Islam, ditandai dengan makam Sunan Bonang di pusat kota, Makam Sunan Bejagung (Syekh Asy'ari), Makam Syekh Maulana Ishaq di pesisir, serta puluhan makam auliya lainnya.",
        "source": "Profil Pariwisata Religi Kabupaten Tuban & Sejarah Tuban Bumi Wali Disparbudpora"
    },
    {
        "id": 550,
        "category": "Pendidikan agama dan moderasi beragama",
        "difficulty": "sedang",
        "question": "Nilai keteladanan terbesar dari para wali penyebar agama Islam di tanah Jawa yang patut diteladani oleh seluruh jajaran perangkat desa dalam memimpin warga perdesaan adalah...",
        "options": [
            "Mengejar kekayaan materi dan tanah bengkok seluas-luasnya",
            "Keikhlasan melayani, kesederhanaan hidup, keadilan sosial bagi kaum lemah, serta keteduhan dalam mengayomi seluruh lapisan masyarakat tanpa diskriminasi",
            "Mewajibkan warga desa menyetor upeti bulanan",
            "Menutup akses desa bagi warga dari luar daerah"
        ],
        "answer": 1,
        "explanation": "Para Walisongo meneladankan kepemimpinan kenabian (khidmah lil ummah): mereka merakyat, melayani masyarakat dengan tulus, membela kaum papa (mustadh'afin), hidup bersahaja, serta membawa kedamaian dan ketenteraman bagi seluruh warga desa.",
        "source": "Atlas Walisongo Agus Sunyoto & Refleksi Nilai Kepemimpinan Luhur Nusantara"
    }
]
