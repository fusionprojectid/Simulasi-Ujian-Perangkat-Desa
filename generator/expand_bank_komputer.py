# -*- coding: utf-8 -*-
"""
Database Soal 551 s.d. 585: Komputer Dasar, Pengolah Kata, Spreadsheet, Jaringan, dan Keamanan Digital
Khusus Standar Kompetensi Teknis Calon Perangkat Desa (Kabupaten Tuban & Standar Nasional)
Label: Latihan Buatan — Standar Kompetensi Komputer Perangkat Desa
Materi:
1. Pengolah Kata (MS Word / LibreOffice Writer) untuk Tata Naskah Dinas Desa (Q551-Q558)
2. Spreadsheet (MS Excel / Calc) untuk Administrasi Penduduk & Keuangan Desa (Q559-Q570)
3. Manajemen Berkas, Format PDF, dan Kompresi Arsip Digital Desa (Q571-Q573)
4. Jaringan, Email Kedinasan, dan Internet Desa (Q574-Q577)
5. Keamanan Siber, Proteksi Sandi, Backup, dan UU Perlindungan Data Pribadi (Q578-Q581)
6. Hardware, Troubleshooting Kantor Desa, Siskeudes, dan Netiket Digital (Q582-Q585)
Total: 35 butir soal latihan buatan (ID 551 - 585).
"""

QUESTIONS_551_585 = [
    # =========================================================================
    # BAGIAN 1: PENGOLAH KATA (MS WORD) UNTUK TATA NASKAH DINAS DESA (Q551 - Q558)
    # =========================================================================
    {
        "id": 551,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "sedang",
        "question": "Dalam penyusunan Buku Profil Desa atau Laporan Pertanggungjawaban APBDes yang akan dijilid bolak-balik, fitur pengaturan margin pada aplikasi pengolah kata yang tepat untuk memberi ruang ekstra penjilidan di bagian dalam halaman adalah...",
        "options": [
            "Orientation Landscape",
            "Gutter Margin / Mirror Margins",
            "Columns Two with Line Between",
            "Hanging Indent 1.5 cm"
        ],
        "answer": 1,
        "explanation": "Gutter margin memberikan ruang tambahan pada sisi margin penjilidan (biasanya sisi kiri untuk halaman ganjil dan sisi kanan untuk halaman genap pada cetak bolak-balik / Mirror Margins) agar teks tidak terpotong atau tertutup lem/staples saat dokumen resmi desa dijilid.",
        "source": "Latihan Buatan — Standar Kompetensi Komputer Perangkat Desa (Modul Pengolah Kata)"
    },
    {
        "id": 552,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "mudah",
        "question": "Pada pembuatan Kop Surat resmi Pemerintah Desa di Microsoft Word, cara yang paling rapi dan standar untuk membuat garis pemisah tebal ganda (double line) di bawah identitas kop surat adalah...",
        "options": [
            "Menekan tombol garis bawah (underscore) berulang-ulang sampai ujung kertas",
            "Menggunakan fitur Shapes garis bebas ditarik manual dengan tetikus (mouse)",
            "Menggunakan fitur 'Borders and Shading' pada menu Home/Paragraph lalu memilih garis Bottom Border",
            "Membuat tabel 10 baris lalu mewarnai salah satu sel dengan warna hitam pekat"
        ],
        "answer": 2,
        "explanation": "Cara resmi dan rapi membuat garis kop surat adalah menggunakan fitur 'Borders and Shading' pada paragraf kop, lalu memilih garis tebal atau ganda pada posisi Bottom Border. Menggambar manual dengan Shapes rentan bergeser saat dibuka di komputer lain, dan mengetik underscore manual menghasilkan garis yang tidak rata.",
        "source": "Latihan Buatan — Standar Kompetensi Komputer Perangkat Desa (Tata Naskah Dinas)"
    },
    {
        "id": 553,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "sedang",
        "question": "Ketika menyusun dokumen RKP Desa yang memuat halaman sampul tanpa nomor, kata pengantar bernomor romawi kecil (i, ii), dan isi materi bernomor angka biasa (1, 2, 3), fitur pemutus halaman yang wajib digunakan adalah...",
        "options": [
            "Page Break biasa (Ctrl + Enter)",
            "Section Break (Next Page)",
            "Line Break (Shift + Enter)",
            "Column Break"
        ],
        "answer": 1,
        "explanation": "Section Break (Next Page) membagi dokumen menjadi beberapa seksi independen sehingga pengaturan tata letak, orientasi (portrait/landscape), dan format nomor halaman (romawi vs angka Arab, serta 'Unlink from Previous') dapat berbeda antar-bagian dokumen.",
        "source": "Latihan Buatan — Standar Kompetensi Komputer Perangkat Desa (Modul Pengolah Kata)"
    },
    {
        "id": 554,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "mudah",
        "question": "Surat keputusan kepala desa dan administrasi desa di Indonesia umumnya dicetak menggunakan kertas ukuran Folio / F4. Ukuran lebar dan tinggi standar untuk kertas Folio/F4 pada pengaturan 'Custom Page Size' adalah...",
        "options": [
            "21,0 cm x 29,7 cm",
            "21,5 cm x 33,0 cm (8,5 x 13 inci)",
            "21,59 cm x 35,56 cm (Legal)",
            "14,8 cm x 21,0 cm (A5)"
        ],
        "answer": 1,
        "explanation": "Ukuran standar kertas Folio / F4 (HVS Folio) di Indonesia adalah lebar 21,5 cm dan tinggi 33,0 cm (atau 8,5 x 13 inci). Pilihan Legal memiliki panjang 35,56 cm (lebih panjang 2,5 cm dari F4), sehingga jika memilih format Legal pada kertas F4, bagian bawah dokumen akan terpotong saat dicetak.",
        "source": "Latihan Buatan — Standar Kompetensi Komputer Perangkat Desa (Pengaturan Kertas Dokumen)"
    },
    {
        "id": 555,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "mudah",
        "question": "Perangkat keras penyimpanan data generasi baru yang menggunakan chip memori flash tanpa komponen mekanis berputar, menghasilkan kecepatan baca-tulis jauh lebih tinggi dan tahan guncangan dibandingkan harddisk konvensional (HDD) adalah...",
        "options": [
            "Floppy Disk",
            "SSD (Solid State Drive)",
            "CD-ROM",
            "Pita Kaset Magnetik"
        ],
        "answer": 1,
        "explanation": "SSD (Solid State Drive) adalah media penyimpanan sekunder berbasis chip semikonduktor flash yang bekerja secara elektrik tanpa piringan mekanis berputar seperti HDD konvensional, memberikan kecepatan booting sistem dan akses file kantor desa yang jauh lebih cepat serta tahan benturan.",
        "source": "Standar Kompetensi Komputer Perangkat Desa (Perangkat Keras Penyimpanan)"
    },
    {
        "id": 556,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "mudah",
        "question": "Kaidah tata naskah dinas pemerintah mengharuskan badan paragraf surat atau peraturan desa memiliki perataan teks yang rapi di sisi kiri dan sisi kanan. Perataan teks ini disebut...",
        "options": [
            "Align Left (Rata Kiri)",
            "Center (Rata Tengah)",
            "Align Right (Rata Kanan)",
            "Justify (Rata Kanan-Kiri)"
        ],
        "answer": 3,
        "explanation": "Perataan teks Justify (Ctrl + J) menghasilkan naskah yang rata pada batas margin kiri dan margin kanan secara simetris, sehingga dokumen dinas terlihat formal, tertib, dan profesional sesuai Peraturan Menteri Dalam Negeri tentang Tata Naskah Dinas.",
        "source": "Latihan Buatan — Standar Kompetensi Komputer Perangkat Desa (Format Tata Naskah)"
    },
    {
        "id": 557,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "sulit",
        "question": "Dalam proses pembahasan bersama draf rancangan Peraturan Desa antara Kepala Desa dan BPD, fitur aplikasi pengolah kata yang berfungsi merekam setiap perubahan kalimat, pencoretan, atau usulan penambahan teks oleh para pihak disebut...",
        "options": [
            "Word Count",
            "Track Changes (Review)",
            "Macro Recorder",
            "Hyphenation"
        ],
        "answer": 1,
        "explanation": "Fitur Track Changes (di bawah tab Review) memungkinkan seluruh suntingan, penambahan kata, penghapusan klausa, dan komentar terekam dengan penanda warna berbeda, memudahkan tim legal atau pimpinan desa meninjau usulan perubahan sebelum draf disahkan menjadi Perdes final.",
        "source": "Latihan Buatan — Standar Kompetensi Komputer Perangkat Desa (Review Regulasi Desa)"
    },
    {
        "id": 558,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "sedang",
        "question": "Saat membuat tabel Register Penduduk Desa yang memanjang hingga 5 halaman, staf desa ingin agar judul kolom (No, NIK, Nama, Alamat) otomatis muncul di baris paling atas pada setiap halaman berikutnya. Fitur yang harus diaktifkan adalah...",
        "options": [
            "Ketik ulang judul tabel secara manual di awal setiap halaman",
            "Split Cells pada menu layout tabel",
            "Repeat Header Rows pada tab Table Tools > Layout",
            "Merge and Center baris pertama"
        ],
        "answer": 2,
        "explanation": "Fitur 'Repeat Header Rows' memastikan baris kepala tabel (header) otomatis diulang di bagian atas setiap halaman berikutnya saat tabel memotong batas halaman (page break). Ini mencegah kesalahan pembacaan kolom data penduduk tanpa perlu mengetik manual.",
        "source": "Latihan Buatan — Standar Kompetensi Komputer Perangkat Desa (Pengelolaan Tabel)"
    },

    # =========================================================================
    # BAGIAN 2: SPREADSHEET (MS EXCEL / CALC) DATA DESA (Q559 - Q570)
    # =========================================================================
    {
        "id": 559,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "mudah",
        "question": "Fungsi matematika dasar pada lembar kerja Excel yang digunakan untuk menjumlahkan seluruh nilai realisasi belanja bidang pembangunan desa dari sel D5 sampai sel D25 adalah...",
        "options": [
            "=TOTAL(D5:D25)",
            "=SUM(D5:D25)",
            "=PLUS(D5:D25)",
            "=ADD(D5:D25)"
        ],
        "answer": 1,
        "explanation": "Fungsi =SUM(number1, [number2], ...) adalah formula standar Excel untuk menjumlahkan sekumpulan angka dalam rentang sel (range) tertentu, dalam contoh ini =SUM(D5:D25).",
        "source": "Latihan Buatan — Standar Kompetensi Komputer Perangkat Desa (Formula Spreadsheet)"
    },
    {
        "id": 560,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "mudah",
        "question": "Untuk menghitung rata-rata pendapatan per kepala keluarga warga prasejahtera dari data sel E2 sampai E50, formula yang benar adalah...",
        "options": [
            "=MEAN(E2:E50)",
            "=AVERAGE(E2:E50)",
            "=RATARATA(E2:E50)",
            "=MEDIAN(E2:E50)"
        ],
        "answer": 1,
        "explanation": "Fungsi =AVERAGE(range) digunakan untuk menghitung nilai rata-rata hitung (arithmetic mean) dari sekumpulan nilai dalam sel numerik.",
        "source": "Latihan Buatan — Standar Kompetensi Komputer Perangkat Desa (Formula Spreadsheet)"
    },
    {
        "id": 561,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "sedang",
        "question": "Kaur Perencanaan ingin membuat status otomatis penerima bantuan: jika penghasilan di sel C2 kurang dari atau sama dengan 1.500.000 maka berstatus 'Penerima BLT', jika lebih besar berstatus 'Bukan Penerima'. Penulisan rumus IF yang tepat adalah...",
        "options": [
            "=IF(C2 <= 1500000; 'Penerima BLT'; 'Bukan Penerima')",
            "=IF(C2 <= 1500000, \"Penerima BLT\", \"Bukan Penerima\")",
            "=CHECK(C2 <= 1500000; Penerima BLT; Bukan Penerima)",
            "=CONDITION(C2; 1500000; \"Penerima BLT\"; \"Bukan\")"
        ],
        "answer": 1,
        "explanation": "Struktur baku fungsi IF adalah =IF(logical_test, [value_if_true], [value_if_false]). Teks keterangan wajib diapit tanda petik dua ganda (\"), dan pemisah argumen menggunakan koma atau titik koma sesuai konfigurasi regional sistem.",
        "source": "Latihan Buatan — Standar Kompetensi Komputer Perangkat Desa (Formula Logika Excel)"
    },
    {
        "id": 562,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "sedang",
        "question": "Fungsi spreadsheet yang digunakan untuk menghitung banyaknya warga yang berstatus pekerjaan 'Petani' dari kolom pekerjaan (C2:C100) adalah...",
        "options": [
            "=COUNT(C2:C100)",
            "=COUNTIF(C2:C100, \"Petani\")",
            "=SUMIF(C2:C100, \"Petani\")",
            "=COUNTA(C2:C100, \"Petani\")"
        ],
        "answer": 1,
        "explanation": "=COUNTIF(range, criteria) menghitung jumlah sel yang memenuhi kriteria tertentu (dalam hal ini sel yang bernilai teks \"Petani\"). Fungsi COUNT hanya menghitung angka, sedangkan SUMIF menjumlahkan nilai angka bersyarat.",
        "source": "Latihan Buatan — Standar Kompetensi Komputer Perangkat Desa (Formula Statistik Excel)"
    },
    {
        "id": 563,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "sulit",
        "question": "Kasi Pemerintahan ingin mencari nama warga secara otomatis pada tabel master kependudukan berdasarkan input NIK. Jika NIK dicari pada kolom pertama tabel referensi A2:D500 dan Nama Warga berada di kolom ke-2, rumus pencarian vertikal yang tepat adalah...",
        "options": [
            "=HLOOKUP(F2, A2:D500, 2, FALSE)",
            "=VLOOKUP(F2, A2:D500, 2, FALSE)",
            "=SEARCH(F2, A2:D500, 2)",
            "=FIND(F2, A2:D500, Nama)"
        ],
        "answer": 1,
        "explanation": "Fungsi =VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup]) mencari nilai kunci (NIK di F2) pada kolom paling kiri tabel (A2:D500), lalu mengembalikan nilai pada kolom indeks ke-2 (Nama Warga). Parameter FALSE digunakan untuk pencarian nilai persis (exact match).",
        "source": "Latihan Buatan — Standar Kompetensi Komputer Perangkat Desa (Formula VLOOKUP)"
    },
    {
        "id": 564,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "sedang",
        "question": "Simbol yang digunakan dalam formula Excel untuk mengunci alamat sel agar baris dan kolomnya tidak berubah saat formula disalin (di-copy) ke sel lain (referensi absolut) adalah...",
        "options": [
            "Tanda Persen (%)",
            "Tanda Dolar ($)",
            "Tanda Bintang (*)",
            "Tanda Pagar (#)"
        ],
        "answer": 1,
        "explanation": "Tanda dolar ($), misalnya $A$1, mengunci sel secara absolut baik baris maupun kolomnya sehingga nilainya tetap merujuk pada sel tersebut saat ditarik/disalin ke sel lain. Menekan tombol F4 pada keyboard dapat menambahkan tanda dolar secara otomatis.",
        "source": "Latihan Buatan — Standar Kompetensi Komputer Perangkat Desa (Referensi Absolut)"
    },
    {
        "id": 565,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "mudah",
        "question": "Saat hendak memaparkan materi Musrenbangdes di balai desa menggunakan proyektor LCD dari laptop, jenis kabel dan port antarmuka standar modern yang dapat mentransmisikan sinyal video definisi tinggi (HD) sekaligus audio suara secara bersamaan melalui satu kabel adalah...",
        "options": [
            "VGA (Video Graphics Array)",
            "HDMI (High-Definition Multimedia Interface)",
            "Kabel RCA Kuning",
            "Port Serial COM1"
        ],
        "answer": 1,
        "explanation": "HDMI (High-Definition Multimedia Interface) adalah antarmuka digital standar modern yang mengirimkan sinyal video resolusi tinggi beserta sinyal audio digital secara simultan dalam satu kabel, menggantikan kabel analog VGA yang hanya membawa sinyal gambar tanpa suara.",
        "source": "Standar Perangkat Komputer dan Audio Visual Modern"
    },
    {
        "id": 566,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "sedang",
        "question": "Untuk membatasi agar staf pendaftaran hanya dapat menginput pilihan nama dusun yang sah (misalnya: Dusun Krajan, Dusun Mulyo, Dusun Rejo) melalui menu pilihan tarik-turun (dropdown), fitur Excel yang digunakan adalah...",
        "options": [
            "Conditional Formatting",
            "Data Validation dengan kriteria 'List'",
            "AutoFilter",
            "Text to Columns"
        ],
        "answer": 1,
        "explanation": "Data Validation (menu Data > Data Validation) dengan kriteria 'List' memungkinkan pembuat formulir membatasi isian sel hanya pada daftar pilihan yang ditentukan dalam bentuk dropdown list, mencegah salah ketik nama wilayah administratif.",
        "source": "Latihan Buatan — Standar Kompetensi Komputer Perangkat Desa (Validasi Data)"
    },
    {
        "id": 567,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "mudah",
        "question": "Untuk menyaring daftar pemilih pilkades agar hanya menampilkan warga yang bertempat tinggal di RT 02 RW 01, tombol perintah pada tab Data yang harus diaktifkan adalah...",
        "options": [
            "Filter (berlogo corong penyaring)",
            "Sort A to Z",
            "Consolidate",
            "Remove Duplicates"
        ],
        "answer": 0,
        "explanation": "Perintah Filter (ikon corong pada tab Data atau Ctrl+Shift+L) memunculkan tombol panah pada kepala kolom untuk menyaring data berdasarkan kriteria tertentu (misal hanya mencentang RT 02 RW 01).",
        "source": "Latihan Buatan — Standar Kompetensi Komputer Perangkat Desa (Filter Data)"
    },
    {
        "id": 568,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "mudah",
        "question": "Ketika staf desa membuka beberapa program sekaligus (seperti Siskeudes, Word, Excel, dan Browser) di komputer, tombol pintasan (keyboard shortcut) yang paling cepat dan praktis untuk berpindah-pindah antarjendela aplikasi yang sedang aktif adalah...",
        "options": [
            "Ctrl + Alt + Del",
            "Alt + Tab",
            "Ctrl + Shift + Esc",
            "Windows + E"
        ],
        "answer": 1,
        "explanation": "Menekan kombinasi Alt + Tab pada keyboard menampilkan jendela peralihan cepat (Task Switcher) untuk beralih secara langsung dari satu aplikasi aktif ke aplikasi lainnya tanpa perlu mengklik ikon aplikasi di taskbar dengan mouse.",
        "source": "Navigasi Cepat Sistem Operasi Windows"
    },
    {
        "id": 569,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "sedang",
        "question": "Berdasarkan Peraturan Menteri Komunikasi dan Informatika RI, nama domain internet tingkat kedua resmi yang khusus dialokasikan dan digunakan untuk situs web resmi instansi pemerintahan desa di Indonesia adalah...",
        "options": [
            ".com",
            ".desa.go.id atau .desa.id",
            ".org",
            ".co.id"
        ],
        "answer": 1,
        "explanation": "Sesuai regulasi domain instansi pemerintah Republik Indonesia (Permenkominfo), domain resmi bagi entitas pemerintahan desa adalah .desa.go.id (dan pengelolaan domain desa .desa.id), guna memastikan keabsahan dan kredibilitas informasi resmi desa bagi publik.",
        "source": "Permenkominfo tentang Tata Kelola Nama Domain Instansi Pemerintah"
    },
    {
        "id": 570,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "mudah",
        "question": "Dalam penggunaan komputer sehari-hari, perbedaan mendasar antara Peramban Web (Web Browser) seperti Google Chrome atau Microsoft Edge dengan Mesin Pencari (Search Engine) seperti Google Search atau Bing adalah...",
        "options": [
            "Web browser adalah perangkat keras sedangkan mesin pencari adalah monitor layar",
            "Web browser adalah aplikasi perangkat lunak untuk membuka dan menjelajah situs web di internet, sedangkan mesin pencari adalah layanan berbasis web untuk mencari informasi atau tautan situs",
            "Mesin pencari adalah jenis kabel jaringan sedangkan web browser adalah printer",
            "Tidak ada perbedaan, keduanya adalah sistem operasi komputer"
        ],
        "answer": 1,
        "explanation": "Web Browser (Chrome, Firefox, Edge) adalah aplikasi/program yang diinstal di komputer pengguna untuk mengakses dan merender kode halaman web, sedangkan Search Engine (Google, Bing) adalah program/layanan web yang mengindeks dan mencari informasi di seluruh penjuru internet berdasarkan kata kunci tertentu.",
        "source": "Konsep Dasar Teknologi Informasi & Internet"
    },

    # =========================================================================
    # BAGIAN 3: MANAJEMEN BERKAS, PDF, & KOMPRESI ARSIP DIGITAL (Q571 - Q573)
    # =========================================================================
    {
        "id": 571,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "mudah",
        "question": "Untuk mewujudkan tata kelola kearsipan digital desa yang tertib dan mudah dicari kembali, pola penamaan berkas dokumen SK Kepala Desa yang paling tepat dan baku adalah...",
        "options": [
            "sk baru fix banget.docx",
            "dokumen1_final(2).pdf",
            "2026_SK-Kades_No-05_Pengangkatan-Kaur-Keuangan.pdf",
            "SK KADES TERBARU REVISI OK.doc"
        ],
        "answer": 2,
        "explanation": "Standar penamaan file digital arsip kedinasan harus memuat unsur: Tahun, Jenis Dokumen/Instansi, Nomor Surat, dan Ringkasan Isi Dokumen tanpa spasi berantakan, serta disimpan dalam format PDF non-editable. Contoh: 2026_SK-Kades_No-05_Pengangkatan-Kaur-Keuangan.pdf.",
        "source": "Latihan Buatan — Standar Kompetensi Komputer Perangkat Desa (Manajemen Kearsipan Digital)"
    },
    {
        "id": 572,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "mudah",
        "question": "Alasan utama mengapa dokumen resmi Pemerintah Desa (seperti Perdes, Peraturan Bersama Kades, dan Surat Edaran) harus dikonversi ke format PDF sebelum didistribusikan kepada publik atau via WhatsApp adalah...",
        "options": [
            "Format PDF hanya bisa dibuka di komputer server kecamatan",
            "Format PDF mempertahankan tata letak (layout), font, tanda tangan, dan tidak mudah diedit sembarangan di berbagai perangkat",
            "Format PDF otomatis menghapus cap stempel desa sehingga aman",
            "Format PDF membuat ukuran file menjadi lebih besar 100 kali lipat"
        ],
        "answer": 1,
        "explanation": "Format PDF (Portable Document Format) dirancang agar tampilan dokumen (tata letak, jenis font, garis, tabel, dan tanda tangan) tampil konsisten di semua jenis komputer dan ponsel cerdas serta tidak mudah diubah-ubah secara tidak sah.",
        "source": "Latihan Buatan — Standar Kompetensi Komputer Perangkat Desa (Format Dokumen Standar)"
    },
    {
        "id": 573,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "sedang",
        "question": "Saat akan mengirimkan 15 berkas lampiran persyaratan verifikasi calon perangkat desa melalui pos elektronik (email), tindakan teknis terbaik agar berkas tidak tercecer dan hemat ukuran transmisi adalah...",
        "options": [
            "Mengirim 15 email terpisah masing-masing satu lampiran",
            "Memasukkan seluruh berkas ke dalam satu folder lalu mengompresinya menjadi berkas arsip (.ZIP atau .RAR)",
            "Memfoto layar komputer menggunakan kamera ponsel lalu mengirim gambarnya",
            "Menghapus lampiran-lampiran yang dirasa kurang penting"
        ],
        "answer": 1,
        "explanation": "Mengompresi berkas ke dalam format ZIP/RAR menggabungkan banyak file menjadi satu paket utuh serta memperkecil ukuran data transmisi (kompresi lossless), sehingga pengiriman melalui email dinas menjadi praktis dan rapi.",
        "source": "Latihan Buatan — Standar Kompetensi Komputer Perangkat Desa (Pengelolaan Berkas Digital)"
    },

    # =========================================================================
    # BAGIAN 4: JARINGAN, EMAIL KEDINASAN, & INTERNET DESA (Q574 - Q577)
    # =========================================================================
    {
        "id": 574,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "sedang",
        "question": "Di kantor desa yang memiliki beberapa komputer staf dan printer bersama, sistem jaringan komputer lokal yang menghubungkan perangkat-perangkat tersebut dalam satu ruangan kantor dinamakan...",
        "options": [
            "LAN (Local Area Network)",
            "WAN (Wide Area Network)",
            "MAN (Metropolitan Area Network)",
            "VPN (Virtual Private Network)"
        ],
        "answer": 0,
        "explanation": "LAN (Local Area Network) adalah jaringan komputer yang mencakup wilayah geografis terbatas seperti ruangan kantor, balai desa, atau satu gedung perkantoran, memungkinkan berbagi file data dan perangkat printer bersama.",
        "source": "Latihan Buatan — Standar Kompetensi Komputer Perangkat Desa (Jaringan Komputer Dasar)"
    },
    {
        "id": 575,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "sedang",
        "question": "Demi keamanan sistem administrasi dan server desa, kebijakan pengaturan jaringan nirkabel (Wi-Fi) di Balai Desa yang paling tepat adalah...",
        "options": [
            "Membuat satu jaringan Wi-Fi tanpa password agar semua warga bebas memakainya",
            "Memisahkan jaringan Wi-Fi untuk Pelayanan Administrasi Desa dengan Wi-Fi Publik/Tamu (Guest Network)",
            "Mematikan Wi-Fi selamanya dan hanya memakai disket untuk bertukar data",
            "Menyamakan password router Wi-Fi dengan tanggal lahir Kepala Desa"
        ],
        "answer": 1,
        "explanation": "Memisahkan jaringan (segregasi jaringan) antara Wi-Fi internal staf pelayanan dengan Wi-Fi publik warga/tamu (Guest Network) mencegah pihak luar mengakses komputer administrasi, printer dinas, data kependudukan, atau menyebarkan malware.",
        "source": "Latihan Buatan — Standar Kompetensi Komputer Perangkat Desa (Keamanan Jaringan Kantor)"
    },
    {
        "id": 576,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "mudah",
        "question": "Saat mengirim surat elektronik (email) dinas kepada Camat mengenai laporan realisasi bansos, bagian 'Subject' pada formulir email wajib diisi dengan...",
        "options": [
            "Dikosongkan saja agar terlihat misterius",
            "Kata 'HALO' atau 'TOLONG DIBACA'",
            "Judul yang ringkas, jelas, dan memuat perihal surat (misal: 'Laporan Realisasi Penyaluran BLT-DD Tahap I Desa Sukamaju')",
            "Menyalin seluruh isi badan surat ke kolom subject"
        ],
        "answer": 2,
        "explanation": "Kolom Subject adalah judul atau perihal surat elektronik. Pengisian subject yang jelas, informatif, dan formal memudahkan penerima mengenali isi pesan dinas dan mengarsipkannya dengan tepat.",
        "source": "Latihan Buatan — Standar Kompetensi Komputer Perangkat Desa (Etika Komunikasi Digital)"
    },
    {
        "id": 577,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "sedang",
        "question": "Pada formulir pengiriman email kedinasan, fungsi kolom BCC (Blind Carbon Copy) adalah...",
        "options": [
            "Mengirim email utama kepada penerima surat",
            "Mengirim tembusan surat di mana alamat penerima tembusan tersebut tidak terlihat oleh penerima lainnya",
            "Menghapus email secara otomatis setelah 24 jam",
            "Mengubah format teks email menjadi sandi rahasia"
        ],
        "answer": 1,
        "explanation": "BCC (Blind Carbon Copy) digunakan untuk mengirim tembusan tanpa memperlihatkan alamat email penerima BCC tersebut kepada penerima lain (baik To maupun CC). Ini penting saat mengirim pemberitahuan massal untuk melindungi privasi alamat email warga.",
        "source": "Latihan Buatan — Standar Kompetensi Komputer Perangkat Desa (Komunikasi Email Kedinasan)"
    },

    # =========================================================================
    # BAGIAN 5: KEAMANAN SIBER, PRIVASI DATA, & UU PDP (Q578 - Q581)
    # =========================================================================
    {
        "id": 578,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "sedang",
        "question": "Seorang staf desa menerima pesan WhatsApp atau email yang mengatasnamakan Bank Jatim atau Kementerian Desa dengan tautan (link) untuk 'Verifikasi Akun Siskeudes'. Setelah diklik, muncul halaman login palsu yang meminta kata sandi. Modus kejahatan siber ini disebut...",
        "options": [
            "Phishing",
            "Defragmentasi",
            "Overclocking",
            "Troubleshooting"
        ],
        "answer": 0,
        "explanation": "Phishing adalah bentuk penipuan rekayasa sosial (social engineering) di mana pelaku menyamar sebagai entitas terpercaya untuk mencuri informasi sensitif seperti username, kata sandi, kode OTP, atau informasi rekening perbankan melalui situs atau tautan palsu.",
        "source": "Latihan Buatan — Standar Kompetensi Komputer Perangkat Desa (Kesadaran Keamanan Siber)"
    },
    {
        "id": 579,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "mudah",
        "question": "Standar pembuatan kata sandi (password) yang kuat dan aman untuk akun Sistem Keuangan Desa (Siskeudes) atau email kedinasan desa adalah...",
        "options": [
            "Menggunakan angka berurutan seperti '12345678'",
            "Menggunakan nama desa diikuti angka 'desaku2026'",
            "Kombinasi minimal 8-12 karakter yang memuat huruf besar, huruf kecil, angka, dan simbol khusus unik",
            "Menggunakan tanggal lahir anak kepala desa"
        ],
        "answer": 2,
        "explanation": "Password kuat harus memadukan huruf kapital, huruf kecil, angka, dan karakter khusus/simbol (misal: !@#$%), memiliki panjang minimal 8-12 karakter, serta tidak menggunakan data pribadi yang mudah ditebak untuk mencegah serangan brute force.",
        "source": "Latihan Buatan — Standar Kompetensi Komputer Perangkat Desa (Manajemen Kredensial)"
    },
    {
        "id": 580,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "sedang",
        "question": "Untuk melindungi database kependudukan dan keuangan desa dari ancaman virus Ransomware (pengunci data) atau kerusakan harddisk fisik, strategi pencadangan (backup) data terbaik adalah...",
        "options": [
            "Tidak perlu backup jika sudah memakai antivirus gratisan",
            "Menerapkan aturan backup 3-2-1: menyimpan minimal 3 salinan data, pada 2 media penyimpanan berbeda (harddisk internal & eksternal), dan 1 salinan disimpan di tempat terpisah/cloud",
            "Menyalin file ke folder yang sama di desktop komputer",
            "Mencetak seluruh isi database ke kertas setiap sore hari"
        ],
        "answer": 1,
        "explanation": "Aturan backup 3-2-1 adalah standar industri manajemen kontinuitas data: 3 salinan data, 2 jenis media berbeda (misal: harddisk kantor dan harddisk eksternal offline), serta 1 salinan disimpan off-site (di luar lokasi/cloud tersandikan) guna mengantisipasi bencana fisik maupun ransomware.",
        "source": "Latihan Buatan — Standar Kompetensi Komputer Perangkat Desa (Strategi Pencadangan Data)"
    },
    {
        "id": 581,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "sedang",
        "question": "Berdasarkan Undang-Undang Nomor 27 Tahun 2022 tentang Perlindungan Data Pribadi (UU PDP), tindakan perangkat desa mengunggah foto Kartu Keluarga dan KTP warga yang memuat NIK secara terbuka ke grup media sosial Facebook desa adalah...",
        "options": [
            "Tindakan terpuji demi transparansi total informasi desa",
            "Pelanggaran hukum terhadap pelindungan data pribadi spesifik/spesifik warga yang dapat dikenai sanksi pidana dan administratif",
            "Boleh dilakukan asalkan disukai oleh kepala dusun",
            "Kewajiban rutin bulanan yang diatur dalam Permendagri"
        ],
        "answer": 1,
        "explanation": "Pasal dalam UU No. 27 Tahun 2022 (UU PDP) menegaskan bahwa NIK dan data kependudukan adalah data pribadi yang wajib dilindungi kerahasiaannya. Mengunggah data kependudukan tanpa izin pemilik dan tanpa hak ke ruang publik melanggar hukum dan membahayakan warga dari kejahatan pinjaman online ilegal atau pencurian identitas.",
        "source": "Latihan Buatan — UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi & Etika Layanan"
    },

    # =========================================================================
    # BAGIAN 6: HARDWARE, TROUBLESHOOTING, SISKEUDES, & NETIKET (Q582 - Q585)
    # =========================================================================
    {
        "id": 582,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "mudah",
        "question": "Ketika printer kantor desa mengalami 'Paper Jam' (kertas tersangkut di dalam roller printer), tindakan pertama yang benar untuk mengatasinya adalah...",
        "options": [
            "Menarik paksa kertas ke arah berlawanan sekuat tenaga menggunakan obeng",
            "Mematikan printer terlebih dahulu, membuka penutup roller, lalu menarik kertas tersangkut secara perlahan searah jalur keluar kertas",
            "Menyiram roller printer dengan air hangat",
            "Menekan tombol cetak 20 kali berturut-turut"
        ],
        "answer": 1,
        "explanation": "Penanganan paper jam harus diawali dengan mematikan daya printer, membuka penutup akses roller, lalu menarik kertas perlahan searah alur jalannya kertas agar gir atau sensor penarik kertas tidak patah atau rusak.",
        "source": "Latihan Buatan — Standar Kompetensi Komputer Perangkat Desa (Pemeliharaan Perangkat Keras)"
    },
    {
        "id": 583,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "mudah",
        "question": "Perangkat keras tambahan yang berfungsi sebagai penyimpan daya cadangan sementara agar komputer server/kerja desa tidak langsung mati saat listrik PLN padam mendadak disebut...",
        "options": [
            "Modem",
            "UPS (Uninterruptible Power Supply)",
            "Scanner",
            "Motherboard"
        ],
        "answer": 1,
        "explanation": "UPS (Uninterruptible Power Supply) menyediakan cadangan daya baterai sementara ketika arus listrik utama terputus, memberikan waktu bagi operator desa untuk menyimpan dokumen dan mematikan (shut down) komputer secara aman.",
        "source": "Latihan Buatan — Standar Kompetensi Komputer Perangkat Desa (Perangkat Keras Komputer)"
    },
    {
        "id": 584,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "sedang",
        "question": "Aplikasi resmi berbasis komputer yang dikembangkan bersama oleh Kemendagri dan BPKP untuk membantu pemerintah desa dalam perencanaan, penganggaran, penatausahaan, dan pelaporan keuangan desa secara akuntabel dinamakan...",
        "options": [
            "SISKEUDES (Sistem Keuangan Desa)",
            "DAPODIK (Data Pokok Pendidikan)",
            "SIMDA Barang Milik Daerah",
            "E-KTP Mobile Client"
        ],
        "answer": 0,
        "explanation": "SISKEUDES (Sistem Keuangan Desa) adalah aplikasi resmi yang dikembangkan oleh BPKP bersama Kemendagri guna memfasilitasi tata kelola keuangan desa sesuai ketentuan Permendagri No. 20 Tahun 2018.",
        "source": "Latihan Buatan — Petunjuk Teknis SISKEUDES Kemendagri & BPKP RI"
    },
    {
        "id": 585,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "mudah",
        "question": "Dalam etika berkomunikasi digital (netiket) pelayanan desa, penggunaan HURUF KAPITAL SEMUA (ALL CAPS) dalam pesan obrolan atau surat elektronik sebaiknya dihindari karena...",
        "options": [
            "Membuat ukuran file email menjadi terlalu besar",
            "Dapat dipersepsikan oleh pembaca sebagai teriakan, kemarahan, atau nada bicara yang tidak sopan",
            "Dilarang oleh sistem operasi Windows",
            "Membuat tinta printer cepat habis saat dicetak"
        ],
        "answer": 1,
        "explanation": "Dalam konvensi netiket digital, mengetik teks seluruhnya dengan huruf besar/kapital dianggap setara dengan berteriak atau bersikap agresif/marah, sehingga tidak pantas digunakan dalam komunikasi resmi pelayanan masyarakat.",
        "source": "Latihan Buatan — Standar Kompetensi Komputer Perangkat Desa (Etika Netiket Digital)"
    }
]
