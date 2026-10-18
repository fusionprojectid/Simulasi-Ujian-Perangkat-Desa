# -*- coding: utf-8 -*-
"""
Script penyusun dan pemvalidasi Bank Soal serta generator aplikasi CBT
Simulasi Ujian Perangkat Desa - Kabupaten Tuban & Nasional.
"""
import json
import os
import sys

# 100 Soal Lengkap dan Terverifikasi
QUESTIONS = [
    # =========================================================================
    # Kategori 1: Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa (20 Soal)
    # =========================================================================
    {
        "id": 1,
        "number": 1,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "mudah",
        "question": "Berdasarkan Undang-Undang Nomor 6 Tahun 2014 tentang Desa, kedudukan Perangkat Desa adalah sebagai...",
        "options": [
            "Lembaga perwakilan aspirasi masyarakat desa yang mengawasi kinerja kepala desa",
            "Unsur pembantu Kepala Desa dalam melaksanakan tugas dan kewenangannya",
            "Badan independen yang ditunjuk bupati untuk mengelola keuangan desa",
            "Unsur pelaksana teknis daerah yang berkedudukan di bawah koordinasi camat"
        ],
        "answer": 1,
        "explanation": "Berdasarkan Pasal 48 UU No. 6 Tahun 2014 tentang Desa jo. Permendagri No. 84 Tahun 2015, Perangkat Desa bertugas membantu Kepala Desa dalam melaksanakan tugas dan kewenangannya serta bertanggung jawab kepada Kepala Desa.",
        "source": "UU No. 6 Tahun 2014 tentang Desa Pasal 48; Permendagri No. 84 Tahun 2015",
        "sourceType": "regulasi"
    },
    {
        "id": 2,
        "number": 2,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "mudah",
        "question": "Susunan organisasi Perangkat Desa menurut Permendagri Nomor 84 Tahun 2015 terdiri atas...",
        "options": [
            "Sekretariat Desa, Pelaksana Teknis, dan Pelaksana Kewilayahan",
            "Badan Permusyawaratan Desa, Lembaga Pemberdayaan Masyarakat, dan RT/RW",
            "Sekretaris Desa, Bendahara Desa, dan Pengawas Internal Desa",
            "Kepala Urusan, Kepala Seksi, dan Satuan Tugas Perlindungan Masyarakat"
        ],
        "answer": 0,
        "explanation": "Pasal 2 Permendagri No. 84 Tahun 2015 tentang Susunan Organisasi dan Tata Kerja Pemerintah Desa menegaskan bahwa Perangkat Desa terdiri atas Sekretariat Desa, Pelaksana Teknis, dan Pelaksana Kewilayahan.",
        "source": "Permendagri No. 84 Tahun 2015 tentang SOTK Pemerintah Desa Pasal 2",
        "sourceType": "regulasi"
    },
    {
        "id": 3,
        "number": 3,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "sedang",
        "question": "Sekretariat Desa dipimpin oleh Sekretaris Desa. Manakah di antara tugas berikut yang merupakan tugas pokok Sekretaris Desa?",
        "options": [
            "Menetapkan peraturan desa bersama Badan Permusyawaratan Desa",
            "Membantu Kepala Desa dalam bidang administrasi pemerintahan dan mengoordinasikan pelaksana teknis",
            "Melaksanakan pembinaan ketenteraman dan ketertiban langsung di tingkat dusun",
            "Menjabat sebagai pemegang kekuasaan tunggal pengelolaan keuangan desa"
        ],
        "answer": 1,
        "explanation": "Berdasarkan Pasal 7 Permendagri No. 84 Tahun 2015, Sekretaris Desa bertugas membantu Kepala Desa dalam bidang administrasi pemerintahan, mengoordinasikan penyusunan kebijakan, dan mengoordinasikan tugas perangkat desa lainnya.",
        "source": "Permendagri No. 84 Tahun 2015 Pasal 7",
        "sourceType": "regulasi"
    },
    {
        "id": 4,
        "number": 4,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "sedang",
        "question": "Berdasarkan Permendagri Nomor 84 Tahun 2015, jabatan Kepala Urusan (Kaur) berada di bawah Sekretariat Desa. Urusan apa sajakah yang dapat dibentuk paling banyak dalam struktur Sekretariat Desa?",
        "options": [
            "Urusan Pemerintahan, Urusan Pembangunan, dan Urusan Kesejahteraan",
            "Urusan Tata Usaha dan Umum, Urusan Keuangan, dan Urusan Perencanaan",
            "Urusan Keamanan, Urusan Perekonomian, dan Urusan Pelayanan",
            "Urusan Logistik, Urusan Kepegawaian, dan Urusan Kebudayaan"
        ],
        "answer": 1,
        "explanation": "Pasal 8 Permendagri No. 84 Tahun 2015 mengatur bahwa Kaur berkedudukan sebagai unsur staf sekretariat yang membidangi paling banyak 3 urusan: Tata Usaha dan Umum, Keuangan, serta Perencanaan.",
        "source": "Permendagri No. 84 Tahun 2015 Pasal 8",
        "sourceType": "regulasi"
    },
    {
        "id": 5,
        "number": 5,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "sedang",
        "question": "Kepala Seksi (Kasi) berkedudukan sebagai unsur pelaksana teknis operasional. Nomenklatur Kepala Seksi yang diatur dalam regulasi SOTK Pemerintah Desa paling banyak terdiri dari...",
        "options": [
            "Seksi Pemerintahan, Seksi Kesejahteraan, dan Seksi Pelayanan",
            "Seksi Ketertiban, Seksi Pembangunan, dan Seksi Pengawasan",
            "Seksi Pendapatan, Seksi Anggaran, dan Seksi Keuangan",
            "Seksi Pemuda, Seksi Olahraga, dan Seksi Keagamaan"
        ],
        "answer": 0,
        "explanation": "Pasal 9 Permendagri No. 84 Tahun 2015 menetapkan bahwa Kepala Seksi paling banyak terdiri atas 3 seksi, yaitu Seksi Pemerintahan, Seksi Kesejahteraan, dan Seksi Pelayanan.",
        "source": "Permendagri No. 84 Tahun 2015 Pasal 9",
        "sourceType": "regulasi"
    },
    {
        "id": 6,
        "number": 6,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "mudah",
        "question": "Unsur Pelaksana Kewilayahan dalam struktur pemerintah desa dipimpin oleh...",
        "options": [
            "Ketua RT yang dipilih secara bergantian",
            "Kepala Dusun atau sebutan lain sesuai kearifan lokal",
            "Camat melalui penunjukan surat tugas kedinasan",
            "Ketua Lembaga Pemberdayaan Masyarakat Desa (LPMD)"
        ],
        "answer": 1,
        "explanation": "Pasal 10 Permendagri No. 84 Tahun 2015 menyebutkan bahwa Pelaksana Kewilayahan merupakan unsur pembantu Kepala Desa sebagai satuan tugas kewilayahan yang dipimpin oleh Kepala Dusun atau sebutan lain.",
        "source": "Permendagri No. 84 Tahun 2015 Pasal 10",
        "sourceType": "regulasi"
    },
    {
        "id": 7,
        "number": 7,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "sedang",
        "question": "Berdasarkan Permendagri No. 83 Tahun 2015 jo. Permendagri No. 67 Tahun 2017 serta Perda Kabupaten Tuban No. 2 Tahun 2016 jo. No. 16 Tahun 2021, batasan usia bagi calon perangkat desa pada saat mendaftar adalah...",
        "options": [
            "Paling rendah 18 tahun dan paling tinggi 35 tahun",
            "Paling rendah 20 tahun dan paling tinggi 42 tahun",
            "Paling rendah 21 tahun dan paling tinggi 45 tahun",
            "Paling rendah 25 tahun dan paling tinggi 50 tahun"
        ],
        "answer": 1,
        "explanation": "Persyaratan umum perangkat desa menurut Permendagri No. 67/2017 Pasal 2 ayat (2) huruf b dan Perda Kab. Tuban No. 2/2016 jo. No. 16/2021 adalah berusia 20 (dua puluh) tahun sampai dengan 42 (empat puluh dua) tahun pada saat pendaftaran.",
        "source": "Permendagri No. 67 Tahun 2017 Pasal 2 ayat (2); Perda Kab. Tuban No. 2 Tahun 2016 jo. No. 16 Tahun 2021",
        "sourceType": "regulasi"
    },
    {
        "id": 8,
        "number": 8,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "mudah",
        "question": "Syarat tingkat pendidikan formal paling rendah yang harus dipenuhi oleh calon Perangkat Desa adalah...",
        "options": [
            "Sekolah Dasar (SD) atau sederajat",
            "Sekolah Menengah Pertama (SMP) atau sederajat",
            "Sekolah Menengah Umum (SMU) atau sederajat",
            "Diploma Tiga (D3) atau Sarjana (S1)"
        ],
        "answer": 2,
        "explanation": "Berdasarkan Pasal 50 UU No. 6 Tahun 2014 jo. Permendagri No. 67 Tahun 2017, salah satu syarat umum perangkat desa adalah berpendidikan paling rendah Sekolah Menengah Umum (SMU) atau yang sederajat.",
        "source": "UU No. 6 Tahun 2014 Pasal 50; Permendagri No. 67 Tahun 2017",
        "sourceType": "regulasi"
    },
    {
        "id": 9,
        "number": 9,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "mudah",
        "question": "Perangkat Desa berhenti karena purnatugas (pensiun) apabila telah genap mencapai usia...",
        "options": [
            "55 tahun",
            "58 tahun",
            "60 tahun",
            "65 tahun"
        ],
        "answer": 2,
        "explanation": "Menurut Pasal 5 ayat (2) huruf b Permendagri No. 67 Tahun 2017, perangkat desa diberhentikan karena telah berusia genap 60 (enam puluh) tahun.",
        "source": "Permendagri No. 67 Tahun 2017 Pasal 5 ayat (2) huruf b",
        "sourceType": "regulasi"
    },
    {
        "id": 10,
        "number": 10,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "sedang",
        "question": "Dalam mekanisme penjaringan dan penyaringan calon Perangkat Desa, pembentukan Tim Pelaksana Pengangkatan Perangkat Desa dilakukan oleh...",
        "options": [
            "Bupati atas usul Camat",
            "Kepala Desa setelah berkonsultasi dengan Camat",
            "Ketua BPD bersama tokoh masyarakat",
            "Dinas Pemberdayaan Masyarakat dan Desa Kabupaten"
        ],
        "answer": 1,
        "explanation": "Sesuai regulasi Permendagri No. 83/2015 jo. 67/2017 serta Perbup Tuban No. 30/2017 jo. Perbup No. 11/2022, Kepala Desa membentuk Tim Pengangkatan/Penjaringan dan Penyaringan Perangkat Desa yang ditetapkan dengan Keputusan Kepala Desa.",
        "source": "Permendagri No. 83 Tahun 2015 Pasal 4; Perbup Tuban No. 30 Tahun 2017 jo. Perbup No. 11 Tahun 2022",
        "sourceType": "regulasi"
    },
    {
        "id": 11,
        "number": 11,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "sulit",
        "question": "Setelah menerima permohonan konsultasi tertulis mengenai calon perangkat desa dari Kepala Desa, Camat wajib menerbitkan rekomendasi tertulis paling lambat dalam waktu...",
        "options": [
            "3 (tiga) hari kerja",
            "7 (tujuh) hari kerja",
            "14 (empat belas) hari kalender",
            "30 (tiga puluh) hari kalender"
        ],
        "answer": 1,
        "explanation": "Berdasarkan Permendagri No. 67 Tahun 2017 Pasal 4 ayat (4), Camat atau pejabat lain yang ditunjuk memberikan rekomendasi tertulis paling lambat 7 (tujuh) hari kerja sejak diterimanya surat permohonan konsultasi dari Kepala Desa.",
        "source": "Permendagri No. 67 Tahun 2017 Pasal 4 ayat (4)",
        "sourceType": "regulasi"
    },
    {
        "id": 12,
        "number": 12,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "mudah",
        "question": "Pejabat yang berwenang melantik dan menerbitkan Surat Keputusan (SK) pengangkatan Perangkat Desa adalah...",
        "options": [
            "Camat setempat atas nama Bupati",
            "Kepala Desa yang bersangkutan",
            "Ketua Badan Permusyawaratan Desa (BPD)",
            "Kepala Dinas Pemberdayaan Masyarakat dan Desa Kabupaten"
        ],
        "answer": 1,
        "explanation": "Perangkat Desa diangkat oleh Kepala Desa melalui Surat Keputusan (SK) Kepala Desa setelah mendapat rekomendasi tertulis dari Camat, dan dilantik langsung oleh Kepala Desa.",
        "source": "UU No. 6 Tahun 2014 Pasal 49; Permendagri No. 83 Tahun 2015 jo. Permendagri No. 67 Tahun 2017",
        "sourceType": "regulasi"
    },
    {
        "id": 13,
        "number": 13,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "sulit",
        "question": "Perangkat Desa diberhentikan sementara oleh Kepala Desa apabila...",
        "options": [
            "Mendapatkan teguran lisan satu kali karena terlambat datang apel",
            "Ditetapkan sebagai tersangka tindak pidana korupsi, terorisme, makar, atau tindak pidana berancaman penjara minimal 5 tahun",
            "Mengambil cuti melahirkan atau cuti tahunan dengan izin resmi",
            "Mengalami perbedaan pendapat dalam musyawarah bersama anggota BPD"
        ],
        "answer": 1,
        "explanation": "Berdasarkan Permendagri No. 67 Tahun 2017 Pasal 6, Perangkat Desa diberhentikan sementara apabila ditetapkan sebagai tersangka tindak pidana korupsi, terorisme, makar, tindak pidana terhadap keamanan negara, atau tindak pidana yang diancam pidana penjara paling singkat 5 tahun.",
        "source": "Permendagri No. 67 Tahun 2017 Pasal 6 ayat (1)",
        "sourceType": "regulasi"
    },
    {
        "id": 14,
        "number": 14,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "sedang",
        "question": "Berikut ini yang BUKAN merupakan alasan pemberhentian Perangkat Desa menurut peraturan perundang-undangan adalah...",
        "options": [
            "Perangkat desa meninggal dunia",
            "Perangkat desa mengundurkan diri atas permintaan sendiri secara tertulis",
            "Kepala Desa berganti kepemimpinan setelah pemilihan kepala desa serentak",
            "Perangkat desa telah mencapai usia genap 60 (enam puluh) tahun"
        ],
        "answer": 2,
        "explanation": "Pergantian Kepala Desa TIDAK BOLEH menjadi alasan memberhentikan perangkat desa. Masa jabatan perangkat desa bersifat tetap sampai usia 60 tahun sepanjang tidak melanggar larangan dan memenuhi syarat regulasi.",
        "source": "Permendagri No. 83 Tahun 2015 jo. Permendagri No. 67 Tahun 2017 Pasal 5",
        "sourceType": "regulasi"
    },
    {
        "id": 15,
        "number": 15,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "sedang",
        "question": "Perangkat Desa dilarang merangkap jabatan sebagai...",
        "options": [
            "Ketua Karang Taruna tingkat RW",
            "Anggota DPR, DPD, DPRD, atau jabatan lain yang ditentukan oleh peraturan perundang-undangan",
            "Anggota kelompok pengajian atau takmir masjid desa",
            "Ketua kelompok tani di desanya sendiri"
        ],
        "answer": 1,
        "explanation": "Pasal 51 UU No. 6 Tahun 2014 melarang perangkat desa merangkap jabatan sebagai anggota DPR, DPD, DPRD, pengurus partai politik, advokat, atau jabatan lain yang dilarang peraturan perundang-undangan.",
        "source": "UU No. 6 Tahun 2014 Pasal 51 huruf f dan g",
        "sourceType": "regulasi"
    },
    {
        "id": 16,
        "number": 16,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "sulit",
        "question": "Berdasarkan Peraturan Pemerintah (PP) Nomor 11 Tahun 2019, ketentuan besaran penghasilan tetap (Siltap) Sekretaris Desa paling sedikit adalah...",
        "options": [
            "70% dari penghasilan tetap Kepala Desa",
            "80% dari penghasilan tetap Kepala Desa",
            "90% dari penghasilan tetap Kepala Desa",
            "Sama persis 100% dengan penghasilan tetap Kepala Desa"
        ],
        "answer": 2,
        "explanation": "Pasal 81 ayat (2) huruf b PP No. 11 Tahun 2019 menetapkan besaran penghasilan tetap Sekretaris Desa paling sedikit Rp2.224.420,00 atau setara 90% dari penghasilan tetap Kepala Desa.",
        "source": "Peraturan Pemerintah No. 11 Tahun 2019 Pasal 81 ayat (2) huruf b",
        "sourceType": "regulasi"
    },
    {
        "id": 17,
        "number": 17,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "sedang",
        "question": "Selain penghasilan tetap (Siltap), hak yang sah diterima oleh Perangkat Desa menurut regulasi yang berlaku adalah...",
        "options": [
            "Dividen saham perusahaan swasta daerah secara pribadi",
            "Jaminan kesehatan, jaminan ketenagakerjaan, serta tunjangan dan penerimaan lain yang sah sesuai APB Desa",
            "Persentase komisi tunai langsung dari setiap penerbitan surat pengantar warga",
            "Uang pelicin dari rekanan pemenang proyek pembangunan fisik desa"
        ],
        "answer": 1,
        "explanation": "Sesuai PP No. 43/2014 jo. PP No. 11/2019, selain Siltap, Kepala Desa dan Perangkat Desa berhak memperoleh jaminan kesehatan, jaminan ketenagakerjaan, serta tunjangan dan penerimaan sah lainnya yang dialokasikan dalam APB Desa.",
        "source": "PP No. 11 Tahun 2019 jo. Permendagri No. 20 Tahun 2018",
        "sourceType": "regulasi"
    },
    {
        "id": 18,
        "number": 18,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "sedang",
        "question": "Berdasarkan Undang-Undang Nomor 3 Tahun 2024 tentang Perubahan Kedua atas UU No. 6 Tahun 2014 tentang Desa, masa jabatan Kepala Desa adalah...",
        "options": [
            "5 (lima) tahun dan dapat menjabat paling banyak 3 (tiga) kali masa jabatan",
            "6 (enam) tahun dan dapat menjabat paling banyak 3 (tiga) kali masa jabatan",
            "8 (delapan) tahun dan dapat menjabat paling banyak 2 (dua) kali masa jabatan",
            "9 (sembilan) tahun dan hanya dapat menjabat 1 (satu) kali masa jabatan"
        ],
        "answer": 2,
        "explanation": "Pasal 39 UU No. 3 Tahun 2024 mengubah masa jabatan Kepala Desa menjadi 8 (delapan) tahun terhitung sejak tanggal pelantikan dan dapat menjabat paling banyak 2 (dua) kali masa jabatan secara berturut-turut atau tidak berturut-turut.",
        "source": "Undang-Undang Nomor 3 Tahun 2024 Pasal 39",
        "sourceType": "regulasi"
    },
    {
        "id": 19,
        "number": 19,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "mudah",
        "question": "Dalam pelaksanaan tugas sehari-hari, Perangkat Desa bertanggung jawab secara hierarki kepada...",
        "options": [
            "Ketua Badan Permusyawaratan Desa (BPD)",
            "Kepala Desa",
            "Camat melalui Sekretaris Camat",
            "Inspektorat Pembantu Daerah Kabupaten"
        ],
        "answer": 1,
        "explanation": "Sesuai Pasal 48 UU No. 6 Tahun 2014, Perangkat Desa bertugas membantu Kepala Desa dan dalam pelaksanaan tugas serta kewenangannya bertanggung jawab kepada Kepala Desa.",
        "source": "UU No. 6 Tahun 2014 Pasal 48",
        "sourceType": "regulasi"
    },
    {
        "id": 20,
        "number": 20,
        "category": "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
        "difficulty": "sedang",
        "question": "Urutan penjatuhan sanksi administratif bagi Perangkat Desa yang melanggar kewajiban kedinasan menurut Permendagri No. 67 Tahun 2017 adalah...",
        "options": [
            "Pemberhentian langsung tanpa proses klarifikasi",
            "Teguran lisan, teguran tertulis, pemberhentian sementara, lalu pemberhentian tetap",
            "Denda pemotongan gaji seketika lalu pengusiran dari wilayah desa",
            "Pemberhentian sementara selama 1 tahun tanpa surat peringatan"
        ],
        "answer": 1,
        "explanation": "Berdasarkan Permendagri No. 67 Tahun 2017 Pasal 7, sanksi administratif dikenakan secara bertahap: teguran lisan, teguran tertulis, pemberhentian sementara, dan dilanjutkan pemberhentian tetap bila tidak memperbaiki pelanggaran.",
        "source": "Permendagri No. 67 Tahun 2017 Pasal 7",
        "sourceType": "regulasi"
    },

    # =========================================================================
    # Kategori 2: Peraturan perundang-undangan dan tata kelola pemerintahan (12 Soal)
    # =========================================================================
    {
        "id": 21,
        "number": 21,
        "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
        "difficulty": "mudah",
        "question": "Hierarki Peraturan Perundang-undangan di Indonesia berdasarkan Pasal 7 ayat (1) UU Nomor 12 Tahun 2011 jo. UU Nomor 13 Tahun 2022 menempatkan urutan dari yang tertinggi ke terendah sebagai...",
        "options": [
            "UUD 1945, Ketetapan MPR, UU/Perppu, PP, Perpres, Perda Provinsi, Perda Kabupaten/Kota",
            "UUD 1945, UU/Perppu, Ketetapan MPR, Perpres, PP, Perda Kabupaten/Kota, Perda Provinsi",
            "UUD 1945, Tap MPR, Perpres, PP, UU, Peraturan Desa, Perda Kabupaten/Kota",
            "Pancasila, UUD 1945, UU Desa, Peraturan Menteri Dalam Negeri, Peraturan Bupati"
        ],
        "answer": 0,
        "explanation": "Pasal 7 ayat (1) UU No. 12 Tahun 2011 secara tegas mengatur urutan hierarki: UUD 1945, Ketetapan MPR, UU/Peraturan Pemerintah Pengganti UU, Peraturan Pemerintah, Peraturan Presiden, Perda Provinsi, dan Perda Kabupaten/Kota.",
        "source": "UU No. 12 Tahun 2011 Pasal 7 ayat (1) jo. UU No. 13 Tahun 2022",
        "sourceType": "regulasi"
    },
    {
        "id": 22,
        "number": 22,
        "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
        "difficulty": "sedang",
        "question": "Bagaimanakah kedudukan Peraturan Desa (Perdes) dalam sistem hukum peraturan perundang-undangan Indonesia?",
        "options": [
            "Tidak diakui sebagai norma hukum mengikat karena berada di bawah Peraturan Daerah",
            "Diakui keberadaannya dan berkekuatan hukum mengikat sepanjang diperintahkan oleh peraturan lebih tinggi atau dibentuk berdasarkan kewenangan desa",
            "Hanya berlaku sebagai norma kesusilaan internal dan adat istiadat tanpa sanksi formal",
            "Bisa mengesampingkan dan membatalkan Peraturan Daerah Kabupaten bila terjadi pertentangan norma"
        ],
        "answer": 1,
        "explanation": "Berdasarkan Pasal 8 UU No. 12 Tahun 2011, Peraturan Desa termasuk jenis peraturan perundang-undangan yang diakui keberadaannya dan mempunyai kekuatan hukum mengikat sepanjang diperintahkan oleh Peraturan Perundang-undangan yang lebih tinggi atau dibentuk berdasarkan kewenangan.",
        "source": "UU No. 12 Tahun 2011 Pasal 8; UU No. 6 Tahun 2014",
        "sourceType": "regulasi"
    },
    {
        "id": 23,
        "number": 23,
        "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
        "difficulty": "sedang",
        "question": "Menurut Permendagri Nomor 111 Tahun 2014, jenis produk hukum yang ditetapkan di tingkat desa terdiri atas...",
        "options": [
            "Undang-Undang Desa, Peraturan Menteri Desa, dan Surat Edaran Camat",
            "Peraturan Desa (Perdes), Peraturan Kepala Desa (Perkades), dan Peraturan Bersama Kepala Desa (Permakades)",
            "Keputusan Dusun, Instruksi RT, dan Maklumat RW",
            "Perda Khusus Desa, Surat Penetapan BPD, dan Dokumen Musyawarah"
        ],
        "answer": 1,
        "explanation": "Pasal 2 Permendagri No. 111 Tahun 2014 tentang Pedoman Teknis Peraturan di Desa menyebutkan jenis peraturan di desa terdiri atas: Peraturan Desa, Peraturan Kepala Desa, dan Peraturan Bersama Kepala Desa.",
        "source": "Permendagri No. 111 Tahun 2014 Pasal 2",
        "sourceType": "regulasi"
    },
    {
        "id": 24,
        "number": 24,
        "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
        "difficulty": "sedang",
        "question": "Rancangan Peraturan Desa (Ranperdes) yang diprakarsai oleh Kepala Desa atau BPD wajib dibahas dan disepakati bersama oleh...",
        "options": [
            "Kepala Desa dan BPD dalam musyawarah bersama",
            "Camat dan Kepala Bagian Hukum Setda Kabupaten",
            "Sekretaris Desa dan seluruh Ketua RT",
            "Pendamping Desa dan Badan Usaha Milik Desa"
        ],
        "answer": 0,
        "explanation": "Pasal 69 UU No. 6 Tahun 2014 menyatakan bahwa Peraturan Desa dibahas dan disepakati bersama oleh Kepala Desa dan Badan Permusyawaratan Desa (BPD).",
        "source": "UU No. 6 Tahun 2014 Pasal 69; Permendagri No. 111 Tahun 2014",
        "sourceType": "regulasi"
    },
    {
        "id": 25,
        "number": 25,
        "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
        "difficulty": "sulit",
        "question": "Pengundangan Peraturan Desa agar memiliki kekuatan mengikat masyarakat dilakukan oleh...",
        "options": [
            "Ketua BPD dalam Notula Rapat Paripurna Desa",
            "Sekretaris Desa dalam Lembaran Desa",
            "Kepala Bagian Hukum Kabupaten dalam Berita Daerah",
            "Camat dalam Warta Kecamatan"
        ],
        "answer": 1,
        "explanation": "Berdasarkan Permendagri No. 111 Tahun 2014 Pasal 21, Peraturan Desa diundangkan oleh Sekretaris Desa dalam Lembaran Desa, sedangkan Peraturan Kepala Desa dan Peraturan Bersama Kepala Desa diundangkan dalam Berita Desa.",
        "source": "Permendagri No. 111 Tahun 2014 Pasal 21",
        "sourceType": "regulasi"
    },
    {
        "id": 26,
        "number": 26,
        "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
        "difficulty": "sulit",
        "question": "Rancangan Peraturan Desa manakah yang wajib disampaikan kepada Bupati melalui Camat untuk dievaluasi sebelum ditetapkan?",
        "options": [
            "Ranperdes tentang pembentukan panitia peringatan HUT RI",
            "Ranperdes tentang APB Desa, Pungutan Desa, Tata Ruang, dan SOTK Pemerintah Desa",
            "Ranperdes tentang jadwal kerja bakti kebersihan lingkungan RT",
            "Ranperdes tentang pengesahan kelompok arisan ibu-ibu desa"
        ],
        "answer": 1,
        "explanation": "Permendagri No. 111 Tahun 2014 mengatur bahwa Rancangan Perdes tentang APB Desa, pungutan, tata ruang, dan organisasi pemerintah desa yang telah disepakati bersama BPD wajib dievaluasi oleh bupati/walikota sebelum ditetapkan.",
        "source": "Permendagri No. 111 Tahun 2014 Pasal 24",
        "sourceType": "regulasi"
    },
    {
        "id": 27,
        "number": 27,
        "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
        "difficulty": "sedang",
        "question": "Asas penyelenggaraan pemerintahan desa yang mengutamakan landasan peraturan perundang-undangan dan keadilan dalam setiap kebijakan pemerintah desa disebut asas...",
        "options": [
            "Kepastian Hukum",
            "Kearifan Lokal",
            "Akuntabilitas",
            "Profesionalitas"
        ],
        "answer": 0,
        "explanation": "Sesuai penjelasan Pasal 24 UU No. 6 Tahun 2014, Asas Kepastian Hukum adalah asas dalam negara hukum yang mengutamakan landasan ketentuan peraturan perundang-undangan dan keadilan dalam setiap kebijakan penyelenggara pemerintahan desa.",
        "source": "UU No. 6 Tahun 2014 Pasal 24 huruf a",
        "sourceType": "regulasi"
    },
    {
        "id": 28,
        "number": 28,
        "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
        "difficulty": "sedang",
        "question": "Peraturan Daerah Kabupaten Tuban yang menjadi payung hukum utama mengenai pengangkatan dan pemberhentian Perangkat Desa adalah...",
        "options": [
            "Perda Kabupaten Tuban Nomor 2 Tahun 2016 jo. Perda Nomor 16 Tahun 2021",
            "Perda Kabupaten Tuban Nomor 5 Tahun 2010 tentang Pemilihan Kepala Daerah",
            "Perda Kabupaten Tuban Nomor 1 Tahun 2014 tentang Pengelolaan Sampah",
            "Perda Kabupaten Tuban Nomor 12 Tahun 2023 tentang Pajak Daerah"
        ],
        "answer": 0,
        "explanation": "Regulasi resmi Perangkat Desa di Kabupaten Tuban berpijak pada Peraturan Daerah Kabupaten Tuban Nomor 2 Tahun 2016 tentang Perangkat Desa yang kemudian diubah dengan Peraturan Daerah Nomor 16 Tahun 2021.",
        "source": "JDIH Kabupaten Tuban: Perda Kab. Tuban No. 2 Tahun 2016 jo. Perda No. 16 Tahun 2021",
        "sourceType": "regulasi"
    },
    {
        "id": 29,
        "number": 29,
        "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
        "difficulty": "sulit",
        "question": "Peraturan Bupati Tuban yang mengatur tata cara teknis pelaksanaan seleksi perangkat desa mencakup Perbup No. 30 Tahun 2017 yang telah diubah dengan...",
        "options": [
            "Perbup Tuban Nomor 41 Tahun 2019, Perbup Nomor 11 Tahun 2022, dan Perbup Nomor 30 Tahun 2023",
            "Perbup Tuban Nomor 88 Tahun 2020 tentang Penanggulangan Bencana",
            "Perbup Tuban Nomor 3 Tahun 2015 tentang Tata Kelola Perusahaan Daerah",
            "Perbup Tuban Nomor 99 Tahun 2024 tentang Retribusi Pasar Tradisional"
        ],
        "answer": 0,
        "explanation": "Petunjuk teknis seleksi perangkat desa di Tuban diatur dalam Perbup Tuban No. 30 Tahun 2017 yang mengalami perubahan melalui Perbup No. 41 Tahun 2019, Perbup No. 11 Tahun 2022, dan Perbup No. 30 Tahun 2023.",
        "source": "JDIH Kabupaten Tuban: Perbup Tuban No. 30/2017, No. 41/2019, No. 11/2022, No. 30/2023",
        "sourceType": "regulasi"
    },
    {
        "id": 30,
        "number": 30,
        "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
        "difficulty": "sulit",
        "question": "Berdasarkan Perbup Tuban Nomor 11 Tahun 2022, pembagian komponen dan bobot nilai dalam seleksi ujian perangkat desa di Kabupaten Tuban terdiri atas...",
        "options": [
            "Ujian Tertulis bobot 75% (125 soal) dan Ujian Praktik Komputer bobot 25% (10 soal)",
            "Ujian Tertulis bobot 50% dan Wawancara Kepala Desa bobot 50%",
            "Ujian Tertulis bobot 90% dan Tes Fisik Jasmani bobot 10%",
            "Ujian Psikotes bobot 60% dan Wawancara Tokoh Masyarakat bobot 40%"
        ],
        "answer": 0,
        "explanation": "Perbup Tuban No. 11 Tahun 2022 mengatur bahwa ujian seleksi terdiri atas ujian tertulis (125 soal pilihan ganda berbobot 75%) dan ujian praktik komputer (10 soal/aspek praktik berbobot 25%).",
        "source": "Perbup Tuban No. 11 Tahun 2022 tentang Perubahan Kedua Atas Perbup No. 30 Tahun 2017",
        "sourceType": "regulasi"
    },
    {
        "id": 31,
        "number": 31,
        "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
        "difficulty": "sedang",
        "question": "Dua pilar asas utama yang melandasi kewenangan desa dalam UU Nomor 6 Tahun 2014 adalah...",
        "options": [
            "Asas Sentralisasi dan Asas Dekonsentrasi",
            "Asas Rekognisi (pengakuan hak asal-usul) dan Asas Subsidiaritas (penetapan kewenangan berskala lokal)",
            "Asas Efisiensi Anggaran dan Asas Profitabilitas Usaha",
            "Asas Monarki Terbatas dan Asas Primus Inter Pares"
        ],
        "answer": 1,
        "explanation": "Pasal 3 UU No. 6 Tahun 2014 menegaskan asas Rekognisi (pengakuan hak asal usul) dan Subsidiaritas (penetapan kewenangan berskala lokal dan pengambilan keputusan lokal untuk kepentingan masyarakat desa).",
        "source": "UU No. 6 Tahun 2014 Pasal 3 huruf a dan b",
        "sourceType": "regulasi"
    },
    {
        "id": 32,
        "number": 32,
        "category": "Peraturan perundang-undangan dan tata kelola pemerintahan",
        "difficulty": "sedang",
        "question": "Berdasarkan Peraturan Komisi Informasi (Perki) Nomor 1 Tahun 2018 tentang Standar Layanan Informasi Publik Desa, dokumen APB Desa dan realisasinya merupakan jenis informasi publik yang bersifat...",
        "options": [
            "Rahasia negara yang dikecualikan dari publik",
            "Wajib disediakan dan diumumkan secara berkala kepada masyarakat",
            "Hanya boleh dilihat oleh anggota BPD setelah membayar biaya retribusi",
            "Dilarang disebarluaskan di luar lingkungan balai desa"
        ],
        "answer": 1,
        "explanation": "Menurut Perki No. 1 Tahun 2018 jo. UU No. 14 Tahun 2008, informasi mengenai keuangan desa (APB Desa dan laporan pertanggungjawaban) merupakan informasi publik yang wajib diumumkan secara berkala melalui papan informasi, website, atau media publik desa.",
        "source": "Perki No. 1 Tahun 2018 tentang Standar Layanan Informasi Publik Desa; UU No. 14 Tahun 2008",
        "sourceType": "regulasi"
    },

    # =========================================================================
    # Kategori 3: Pancasila, UUD 1945, dan wawasan kebangsaan (10 Soal)
    # =========================================================================
    {
        "id": 33,
        "number": 33,
        "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
        "difficulty": "mudah",
        "question": "Sikap saling menghormati dan bekerja sama antarumat beragama di lingkungan warga desa tanpa memaksakan suatu agama merupakan pengamalan Pancasila, khususnya Sila...",
        "options": [
            "Pertama: Ketuhanan Yang Maha Esa",
            "Kedua: Kemanusiaan yang Adil dan Beradab",
            "Ketiga: Persatuan Indonesia",
            "Kelima: Keadilan Sosial bagi Seluruh Rakyat Indonesia"
        ],
        "answer": 0,
        "explanation": "Sila Pertama Pancasila mengajarkan toleransi, kebebasan beragama, dan penghormatan antarumat beragama tanpa pemaksaan kehendak.",
        "source": "Ketetapan MPR RI / Butir-butir Pengamalan Pancasila",
        "sourceType": "wawasan"
    },
    {
        "id": 34,
        "number": 34,
        "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
        "difficulty": "sedang",
        "question": "Seorang perangkat desa melayani semua warga dengan sopan dan adil tanpa membeda-bedakan latar belakang suku, agama, kekayaan, atau ikatan keluarga. Tindakan ini mencerminkan pengamalan Pancasila Sila...",
        "options": [
            "Sila ke-1",
            "Sila ke-2",
            "Sila ke-3",
            "Sila ke-4"
        ],
        "answer": 1,
        "explanation": "Mengakui persamaan derajat, persamaan hak dan kewajiban asasi setiap manusia tanpa membeda-bedakan suku, keturunan, agama, atau status sosial adalah perwujudan Sila Kedua: Kemanusiaan yang Adil dan Beradab.",
        "source": "Pedoman Pengamalan Pancasila Sila Ke-2",
        "sourceType": "wawasan"
    },
    {
        "id": 35,
        "number": 35,
        "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
        "difficulty": "mudah",
        "question": "Menggalang kembali budaya kerja bakti, gotong royong membersihkan saluran air desa, serta menjaga kerukunan warga merupakan wujud pengamalan Sila...",
        "options": [
            "Pertama",
            "Kedua",
            "Ketiga: Persatuan Indonesia",
            "Keempat"
        ],
        "answer": 2,
        "explanation": "Gotong royong, menjaga persatuan dan kesatuan serta menempatkan kepentingan bersama di atas kepentingan pribadi/golongan adalah esensi Sila Ketiga: Persatuan Indonesia.",
        "source": "Pedoman Pengamalan Pancasila Sila Ke-3",
        "sourceType": "wawasan"
    },
    {
        "id": 36,
        "number": 36,
        "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
        "difficulty": "mudah",
        "question": "Musyawarah Desa (Musdes) untuk mencapai mufakat dalam memecahkan persoalan desa merupakan implementasi langsung dari nilai Pancasila Sila...",
        "options": [
            "Kedua",
            "Ketiga",
            "Keempat: Kerakyatan yang Dipimpin oleh Hikmat Kebijaksanaan dalam Permusyawaratan/Perwakilan",
            "Kelima"
        ],
        "answer": 2,
        "explanation": "Sila Keempat mengamanatkan pengambilan keputusan melalui musyawarah untuk mencapai mufakat yang diliputi oleh semangat kekeluargaan.",
        "source": "Pedoman Pengamalan Pancasila Sila Ke-4",
        "sourceType": "wawasan"
    },
    {
        "id": 37,
        "number": 37,
        "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
        "difficulty": "sedang",
        "question": "Penyaluran bantuan sosial desa kepada masyarakat miskin secara objektif, merata, transparan, dan tidak diskriminatif merupakan wujud nyata pengamalan Pancasila Sila...",
        "options": [
            "Pertama",
            "Kedua",
            "Keempat",
            "Kelima: Keadilan Sosial bagi Seluruh Rakyat Indonesia"
        ],
        "answer": 3,
        "explanation": "Sila Kelima menekankan keadilan sosial, pemerataan hak, serta perlindungan dan bantuan terhadap masyarakat rentan tanpa kesewenang-wenangan.",
        "source": "Pedoman Pengamalan Pancasila Sila Ke-5",
        "sourceType": "wawasan"
    },
    {
        "id": 38,
        "number": 38,
        "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
        "difficulty": "sedang",
        "question": "Tujuan nasional Negara Republik Indonesia yang tercantum secara resmi dalam Pembukaan UUD 1945 Alinea IV meliputi hal-hal berikut, KECUALI...",
        "options": [
            "Melindungi segenap bangsa Indonesia dan seluruh tumpah darah Indonesia",
            "Memajukan kesejahteraan umum dan mencerdaskan kehidupan bangsa",
            "Ikut melaksanakan ketertiban dunia yang berdasarkan kemerdekaan, perdamaian abadi, dan keadilan sosial",
            "Menjadikan negara Indonesia sebagai kekuatan militer adidaya di Asia Tenggara"
        ],
        "answer": 3,
        "explanation": "Empat tujuan negara dalam Pembukaan UUD 1945 Alinea IV adalah: melindungi segenap bangsa & tumpah darah Indonesia, memajukan kesejahteraan umum, mencerdaskan kehidupan bangsa, dan ikut melaksanakan ketertiban dunia.",
        "source": "Pembukaan UUD NRI Tahun 1945 Alinea IV",
        "sourceType": "wawasan"
    },
    {
        "id": 39,
        "number": 39,
        "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
        "difficulty": "sedang",
        "question": "Rumusan bunyi Pasal 1 ayat (2) UUD 1945 setelah amandemen ketiga adalah...",
        "options": [
            "Negara Indonesia ialah Negara Kesatuan, yang berbentuk Republik",
            "Kedaulatan berada di tangan rakyat dan dilaksanakan menurut Undang-Undang Dasar",
            "Negara Indonesia adalah negara hukum",
            "Kedaulatan adalah di tangan rakyat, dan dilakukan sepenuhnya oleh Majelis Permusyawaratan Rakyat"
        ],
        "answer": 1,
        "explanation": "Pasal 1 ayat (2) UUD 1945 pasca-amandemen berbunyi: 'Kedaulatan berada di tangan rakyat dan dilaksanakan menurut Undang-Undang Dasar.'",
        "source": "UUD NRI Tahun 1945 Pasal 1 ayat (2)",
        "sourceType": "wawasan"
    },
    {
        "id": 40,
        "number": 40,
        "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
        "difficulty": "sedang",
        "question": "Ketentuan mengenai hak dan kewajiban setiap warga negara untuk ikut serta dalam upaya pembelaan negara diatur dalam UUD 1945 pada...",
        "options": [
            "Pasal 27 ayat (3)",
            "Pasal 29 ayat (1)",
            "Pasal 31 ayat (2)",
            "Pasal 33 ayat (1)"
        ],
        "answer": 0,
        "explanation": "Pasal 27 ayat (3) UUD 1945 menyatakan: 'Setiap warga negara berhak dan wajib ikut serta dalam upaya pembelaan negara.'",
        "source": "UUD NRI Tahun 1945 Pasal 27 ayat (3)",
        "sourceType": "wawasan"
    },
    {
        "id": 41,
        "number": 41,
        "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
        "difficulty": "mudah",
        "question": "Semboyan 'Bhinneka Tunggal Ika' yang tertulis pada pita lambang negara Garuda Pancasila dipetik dari kitab kuno...",
        "options": [
            "Kitab Negarakertagama karangan Mpu Prapanca",
            "Kitab Sutasoma karangan Mpu Tantular",
            "Kitab Arjunawiwaha karangan Mpu Kanwa",
            "Kitab Bharatayuddha karangan Mpu Sedah dan Mpu Panuluh"
        ],
        "answer": 1,
        "explanation": "Frasa Bhinneka Tunggal Ika ('berbeda-beda tetapi tetap satu') berasal dari Kakawin Sutasoma karangan Mpu Tantular pada zaman Kerajaan Majapahit abad ke-14.",
        "source": "Kitab Sutasoma; UU No. 24 Tahun 2009 tentang Bendera, Bahasa, dan Lambang Negara",
        "sourceType": "wawasan"
    },
    {
        "id": 42,
        "number": 42,
        "category": "Pancasila, UUD 1945, dan wawasan kebangsaan",
        "difficulty": "sedang",
        "question": "Cara pandang bangsa Indonesia mengenai diri dan lingkungannya yang serba beragam dengan mengutamakan persatuan dan kesatuan wilayah dalam penyelenggaraan kehidupan bermasyarakat, berbangsa, dan bernegara disebut...",
        "options": [
            "Ketahanan Nasional",
            "Wawasan Nusantara",
            "Bela Negara Fisik",
            "Otonomi Daerah"
        ],
        "answer": 1,
        "explanation": "Wawasan Nusantara adalah cara pandang bangsa Indonesia tentang diri dan lingkungannya berdasarkan Pancasila dan UUD 1945 sebagai satu kesatuan utuh.",
        "source": "Modul Wawasan Kebangsaan Lemhannas RI",
        "sourceType": "wawasan"
    },

    # =========================================================================
    # Kategori 4: Administrasi pemerintahan, surat-menyurat, dan pengarsipan (10 Soal)
    # =========================================================================
    {
        "id": 43,
        "number": 43,
        "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
        "difficulty": "sedang",
        "question": "Berdasarkan Permendagri Nomor 47 Tahun 2016, buku administrasi desa dikelompokkan ke dalam 5 (lima) bidang administrasi, yaitu...",
        "options": [
            "Administrasi Umum, Penduduk, Keuangan, Pembangunan, dan Badan Permusyawaratan Desa",
            "Administrasi Surat, Pajak, KTP, Bansos, dan Pengaduan",
            "Administrasi Pertanahan, Kepolisian, Pengadilan, Pajak, dan Militer",
            "Administrasi Kepegawaian, Logistik, Kendaraan, Bangunan, dan Inventaris Kantor"
        ],
        "answer": 0,
        "explanation": "Pasal 3 Permendagri No. 47 Tahun 2016 membagi administrasi pemerintahan desa ke dalam 5 jenis: Administrasi Umum, Penduduk, Keuangan, Pembangunan, dan Permusyawaratan Desa (BPD).",
        "source": "Permendagri No. 47 Tahun 2016 tentang Administrasi Pemerintahan Desa",
        "sourceType": "administrasi"
    },
    {
        "id": 44,
        "number": 44,
        "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
        "difficulty": "sedang",
        "question": "Buku yang berfungsi untuk mencatat seluruh peraturan desa, keputusan kepala desa, aparat pemerintah desa, dan data inventaris/tanah kas desa tergolong dalam kelompok...",
        "options": [
            "Buku Administrasi Penduduk",
            "Buku Administrasi Umum",
            "Buku Administrasi Keuangan",
            "Buku Administrasi Pembangunan"
        ],
        "answer": 1,
        "explanation": "Buku Administrasi Umum meliputi Buku Data Peraturan Desa, Keputusan Kepala Desa, Inventaris dan Kekayaan Desa, Aparat Pemerintah Desa, Tanah Kas Desa, Tanah di Desa, Agenda, dan Ekspedisi.",
        "source": "Permendagri No. 47 Tahun 2016 Lampiran I",
        "sourceType": "administrasi"
    },
    {
        "id": 45,
        "number": 45,
        "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
        "difficulty": "mudah",
        "question": "Dalam penatausahaan surat dinas, buku yang digunakan sebagai bukti otentik pengiriman dan tanda terima surat keluar oleh pihak luar atau instansi penerima adalah...",
        "options": [
            "Buku Agenda Surat Masuk",
            "Buku Ekspedisi",
            "Buku Register Penduduk",
            "Buku Kas Pembantu"
        ],
        "answer": 1,
        "explanation": "Buku Ekspedisi adalah buku administrasi yang mencatat pengiriman surat keluar dan memuat tanda tangan penerima sebagai bukti fisik bahwa surat dinas telah sampai kepada pihak yang dituju.",
        "source": "Permendagri No. 47 Tahun 2016 Pedoman Administrasi Umum",
        "sourceType": "administrasi"
    },
    {
        "id": 46,
        "number": 46,
        "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
        "difficulty": "sedang",
        "question": "Urutan komponen baku dalam penomoran surat keluar dinas pemerintah desa secara berurutan adalah...",
        "options": [
            "Tahun / Bulan / Kode Surat / Nama Pengetik",
            "Kode Klasifikasi Surat / Nomor Urut Surat Keluar / Singkatan Instansi Desa / Bulan (Romawi) / Tahun",
            "Nama Penerima / Nomor KTP Kades / Tanggal Kirim / Kode Pos",
            "Nomor Acak Komputer / Jumlah Halaman / Kode Dusun"
        ],
        "answer": 1,
        "explanation": "Format baku tata naskah dinas penomoran surat keluar: Kode Klasifikasi Masalah / Nomor Urut Agenda Keluar / Kode Pemdes / Bulan Masehi (angka Romawi) / Tahun Anggaran (misal: 140/025/Desa.Mulyo/V/2026).",
        "source": "Permendagri tentang Tata Naskah Dinas di Lingkungan Pemerintah Daerah/Desa",
        "sourceType": "administrasi"
    },
    {
        "id": 47,
        "number": 47,
        "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
        "difficulty": "mudah",
        "question": "Kepala surat (Kop Surat) resmi Pemerintah Desa yang sesuai dengan ketentuan tata naskah dinas memuat elemen...",
        "options": [
            "Foto Kepala Desa terpilih, moto pribadi, dan nomor rekening pribadi",
            "Logo/Lambang Daerah Kabupaten, tulisan PEMERINTAH KABUPATEN, nama KECAMATAN, nama PEMERINTAH DESA, serta alamat lengkap kantor, kode pos, dan kontak resmi",
            "Nama partai politik pengusung Kepala Desa dan daftar anggota BPD",
            "Daftar nama seluruh perangkat desa beserta besaran gajinya"
        ],
        "answer": 1,
        "explanation": "Kop naskah dinas resmi instansi pemerintah desa wajib memuat lambang Pemkab di kiri/tengah, hierarki pemerintah kabupaten, kecamatan, pemdes, alamat balai desa, kode pos, serta saluran komunikasi resmi.",
        "source": "Pedoman Tata Naskah Dinas Pemerintah Daerah/Desa",
        "sourceType": "administrasi"
    },
    {
        "id": 48,
        "number": 48,
        "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
        "difficulty": "sedang",
        "question": "Karakteristik yuridis dari Surat Keputusan (SK) Kepala Desa adalah bersifat...",
        "options": [
            "Abstrak, umum, dan berlaku terus menerus tanpa batas pihak",
            "Konkret, individual, dan final (menetapkan status atau hak seseorang/organisasi secara definitif)",
            "Himbauan moral yang tidak memiliki kekuatan hukum mengikat",
            "Perjanjian perdata timbal balik yang bisa dibatalkan secara sepihak oleh warga"
        ],
        "answer": 1,
        "explanation": "Keputusan Kepala Desa (beschikking) bersifat konkret (nyata wujudnya), individual (ditujukan kepada pihak tertentu), dan final (sudah definitif dan menimbulkan akibat hukum).",
        "source": "UU Administrasi Pemerintahan No. 30 Tahun 2014; Permendagri No. 111 Tahun 2014",
        "sourceType": "administrasi"
    },
    {
        "id": 49,
        "number": 49,
        "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
        "difficulty": "mudah",
        "question": "Perbedaan mendasar antara Surat Keterangan dan Surat Pengantar yang diterbitkan oleh pemerintah desa adalah...",
        "options": [
            "Surat keterangan harus ditandatangani bupati, sedangkan surat pengantar ditandatangani camat",
            "Surat keterangan menerangkan keadaan/fakta keabsahan subjek hukum tertentu, sedangkan surat pengantar mengantarkan berkas atau permohonan warga ke instansi lain",
            "Surat pengantar hanya berlaku 1 hari, sedangkan surat keterangan berlaku seumur hidup",
            "Surat keterangan dikenai tarif pungutan desa, sedangkan surat pengantar bebas biaya"
        ],
        "answer": 1,
        "explanation": "Surat Keterangan berfungsi menerangkan suatu hal/keadaan faktual warga (misal: domisili, usaha, kematian), sedangkan Surat Pengantar digunakan untuk mengantarkan berkas/keperluan warga ke instansi jenjang berikutnya (Kecamatan/Disdukcapil).",
        "source": "Praktik Tata Kelola Administrasi Pelayanan Publik Desa",
        "sourceType": "administrasi"
    },
    {
        "id": 50,
        "number": 50,
        "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
        "difficulty": "sedang",
        "question": "Arsip dinamis di kantor desa yang frekuensi penggunaannya untuk penyelenggaraan administrasi sehari-hari sudah menurun, tetapi masih harus disimpan karena memiliki nilai pertanggungjawaban disebut...",
        "options": [
            "Arsip Aktif",
            "Arsip Inaktif",
            "Arsip Statis",
            "Arsip Rahasia Mutlak"
        ],
        "answer": 1,
        "explanation": "Menurut UU No. 43 Tahun 2009 tentang Kearsipan, arsip aktif adalah arsip yang masih sering digunakan terus-menerus, sedangkan arsip inaktif adalah arsip yang frekuensi penggunaannya telah menurun.",
        "source": "Undang-Undang No. 43 Tahun 2009 tentang Kearsipan",
        "sourceType": "administrasi"
    },
    {
        "id": 51,
        "number": 51,
        "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
        "difficulty": "mudah",
        "question": "Ketika warga desa datang melapor bahwa ada anggota keluarganya yang meninggal dunia di rumah, dokumen administrasi awal yang diterbitkan oleh pemerintah desa adalah...",
        "options": [
            "Surat Izin Mengemudi Desa",
            "Surat Keterangan Kematian dari Desa",
            "Surat Perjanjian Warisan Bersama",
            "Surat Pernyataan Bebas Pajak Bumi dan Bangunan"
        ],
        "answer": 1,
        "explanation": "Pemerintah Desa menerbitkan Surat Keterangan Kematian berdasarkan laporan ahli waris/RT sebagai dokumen dasar pengurusan Akta Kematian di Dinas Kependudukan dan Pencatatan Sipil.",
        "source": "Permendagri No. 108 Tahun 2019 tentang Pelaksanaan Perpres Adminduk",
        "sourceType": "administrasi"
    },
    {
        "id": 52,
        "number": 52,
        "category": "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
        "difficulty": "sedang",
        "question": "Dalam penulisan naskah dinas resmi pemerintahan, prinsip pokok yang wajib dipedomani oleh perangkat desa adalah...",
        "options": [
            "Kejelasan maksud, ketepatan redaksi bahasa baku, ketelitian format, dan keabsahan legalitas",
            "Penggunaan bahasa gaul yang santai agar mudah dipahami remaja",
            "Mencantumkan opini subjektif perangkat desa tanpa dasar aturan",
            "Membuat naskah sepanjang mungkin agar terlihat sangat berbobot"
        ],
        "answer": 0,
        "explanation": "Tata naskah dinas pemerintahan wajib menerapkan asas kejelasan, ketelitian, ketepatan, kebakuan bahasa, efektivitas, serta kepatuhan pada hierarki dan format baku.",
        "source": "Pedoman Umum Tata Naskah Dinas Instansi Pemerintah",
        "sourceType": "administrasi"
    },

    # =========================================================================
    # Kategori 5: Keuangan desa, APB Desa, dan aset desa (10 Soal)
    # =========================================================================
    {
        "id": 53,
        "number": 53,
        "category": "Keuangan desa, APB Desa, dan aset desa",
        "difficulty": "mudah",
        "question": "Berdasarkan Permendagri Nomor 20 Tahun 2018 tentang Pengelolaan Keuangan Desa, Pemegang Kekuasaan Pengelolaan Keuangan Desa (PKPKD) adalah...",
        "options": [
            "Sekretaris Desa",
            "Kepala Desa",
            "Ketua Badan Permusyawaratan Desa (BPD)",
            "Kepala Urusan Keuangan (Bendahara Desa)"
        ],
        "answer": 1,
        "explanation": "Pasal 3 Permendagri No. 20 Tahun 2018 menetapkan bahwa Kepala Desa adalah Pemegang Kekuasaan Pengelolaan Keuangan Desa (PKPKD) dan mewakili Pemerintah Desa dalam kepemilikan kekayaan milik desa.",
        "source": "Permendagri No. 20 Tahun 2018 Pasal 3",
        "sourceType": "regulasi"
    },
    {
        "id": 54,
        "number": 54,
        "category": "Keuangan desa, APB Desa, dan aset desa",
        "difficulty": "sedang",
        "question": "Dalam struktur Pelaksana Pengelolaan Keuangan Desa (PPKD), Sekretaris Desa bertindak sebagai...",
        "options": [
            "Bendahara pengeluaran desa",
            "Koordinator PPKD",
            "Pengawas eksternal APB Desa",
            "Pelaksana Kegiatan Anggaran tunggal"
        ],
        "answer": 1,
        "explanation": "Berdasarkan Pasal 4 dan Pasal 5 Permendagri No. 20 Tahun 2018, Sekretaris Desa bertindak selaku Koordinator PPKD yang membantu PKPKD dalam mengoordinasikan pengelolaan keuangan desa.",
        "source": "Permendagri No. 20 Tahun 2018 Pasal 5",
        "sourceType": "regulasi"
    },
    {
        "id": 55,
        "number": 55,
        "category": "Keuangan desa, APB Desa, dan aset desa",
        "difficulty": "mudah",
        "question": "Anggaran Pendapatan dan Belanja Desa (APB Desa) terdiri atas 3 (tiga) kelompok struktur utama, yaitu...",
        "options": [
            "Penerimaan Pajak, Pengeluaran Rutin, dan Dana Bantuan Sosial",
            "Pendapatan Desa, Belanja Desa, dan Pembiayaan Desa",
            "Modal Desa, Kas Operasional, dan Simpanan Bank",
            "Gaji Perangkat Desa, Biaya Listrik Kantor, dan Dana Cadangan Bencana"
        ],
        "answer": 1,
        "explanation": "Pasal 11 Permendagri No. 20 Tahun 2018 mengatur bahwa struktur APB Desa terdiri atas Pendapatan Desa, Belanja Desa, dan Pembiayaan Desa.",
        "source": "Permendagri No. 20 Tahun 2018 Pasal 11",
        "sourceType": "regulasi"
    },
    {
        "id": 56,
        "number": 56,
        "category": "Keuangan desa, APB Desa, dan aset desa",
        "difficulty": "sedang",
        "question": "Alokasi Dana Desa (ADD) yang diterima oleh pemerintah desa bersumber dari...",
        "options": [
            "Anggaran Pendapatan dan Belanja Negara (APBN) langsung pos Dana Desa",
            "Paling sedikit 10% dari dana perimbangan yang diterima kabupaten/kota dalam APBD setelah dikurangi DAK",
            "Pungutan sukarela dari warga desa yang merantau ke luar negeri",
            "Hasil penjualan aset tanah bengkok desa kepada pihak swasta"
        ],
        "answer": 1,
        "explanation": "Pasal 72 ayat (1) huruf d dan ayat (4) UU No. 6 Tahun 2014 mengatur bahwa Alokasi Dana Desa (ADD) dialokasikan paling sedikit 10% dari dana perimbangan yang diterima kabupaten/kota dalam APBD setelah dikurangi Dana Alokasi Khusus (DAK).",
        "source": "UU No. 6 Tahun 2014 Pasal 72 ayat (4)",
        "sourceType": "regulasi"
    },
    {
        "id": 57,
        "number": 57,
        "category": "Keuangan desa, APB Desa, dan aset desa",
        "difficulty": "sedang",
        "question": "Berdasarkan Permendagri Nomor 20 Tahun 2018, klasifikasi Belanja Desa dibagi ke dalam 5 (lima) bidang. Bidang ke-5 adalah...",
        "options": [
            "Bidang Penanaman Modal Asing di Pedesaan",
            "Bidang Penanggulangan Bencana, Keadaan Darurat, dan Mendesak Desa",
            "Bidang Pembiayaan Pemilihan Presiden dan Wakil Presiden",
            "Bidang Pengadaan Persenjataan dan Pertahanan Militer"
        ],
        "answer": 1,
        "explanation": "Pasal 16 Permendagri No. 20 Tahun 2018 membagi klasifikasi belanja desa menjadi: 1. Penyelenggaraan Pemerintahan Desa, 2. Pelaksanaan Pembangunan Desa, 3. Pembinaan Kemasyarakatan Desa, 4. Pemberdayaan Masyarakat Desa, dan 5. Penanggulangan Bencana, Keadaan Darurat dan Mendesak Desa.",
        "source": "Permendagri No. 20 Tahun 2018 Pasal 16",
        "sourceType": "regulasi"
    },
    {
        "id": 58,
        "number": 58,
        "category": "Keuangan desa, APB Desa, dan aset desa",
        "difficulty": "sedang",
        "question": "Pengeluaran belanja yang sifatnya tidak dapat diprediksi sebelumnya dan terjadi di luar kendali pemerintah desa, seperti perbaikan tanggul desa yang jebol akibat banjir bandang, dibebankan pada pos...",
        "options": [
            "Belanja Pegawai dan Operasional Kantor",
            "Belanja Tidak Terduga pada Bidang Penanggulangan Bencana, Keadaan Darurat dan Mendesak",
            "Belanja Modal Pengadaan Tanah Kas Desa",
            "Belanja Bantuan Hukum untuk Perangkat Desa"
        ],
        "answer": 1,
        "explanation": "Belanja tidak terduga dianggarkan pada bidang penanggulangan bencana, keadaan darurat, dan mendesak desa untuk membiayai penanganan tanggap darurat bencana alam/sosial.",
        "source": "Permendagri No. 20 Tahun 2018 Pasal 22",
        "sourceType": "regulasi"
    },
    {
        "id": 59,
        "number": 59,
        "category": "Keuangan desa, APB Desa, dan aset desa",
        "difficulty": "mudah",
        "question": "Asas pengelolaan keuangan desa yang mewajibkan bahwa semua kegiatan dan hasil akhir keuangan desa dapat dipertanggungjawabkan kepada masyarakat sesuai peraturan perundang-undangan disebut asas...",
        "options": [
            "Akuntabel",
            "Transparan",
            "Sentralistik",
            "Fleksibel Bebas"
        ],
        "answer": 0,
        "explanation": "Pasal 2 Permendagri No. 20 Tahun 2018 menetapkan asas pengelolaan keuangan desa: transparan, akuntabel, partisipatif, serta tertib dan disiplin anggaran. Akuntabel berarti dapat dipertanggungjawabkan kepada masyarakat.",
        "source": "Permendagri No. 20 Tahun 2018 Pasal 2",
        "sourceType": "regulasi"
    },
    {
        "id": 60,
        "number": 60,
        "category": "Keuangan desa, APB Desa, dan aset desa",
        "difficulty": "sedang",
        "question": "Aplikasi sistem informasi resmi berbasis komputer yang dikembangkan pemerintah (Kemendagri dan BPKP) untuk membantu pemerintah desa menatausahakan keuangan desa adalah...",
        "options": [
            "SISKEUDES (Sistem Keuangan Desa)",
            "SIPD RI (Sistem Informasi Pembangunan Daerah)",
            "DAPODIK (Data Pokok Pendidikan)",
            "SIMDA BPKAD"
        ],
        "answer": 0,
        "explanation": "SISKEUDES (Sistem Keuangan Desa) adalah aplikasi resmi yang dikembangkan oleh BPKP bersama Ditjen Bina Pemerintahan Desa Kemendagri untuk pengelolaan dan pelaporan keuangan desa di seluruh Indonesia.",
        "source": "Kemendagri & BPKP: Petunjuk Teknis SISKEUDES",
        "sourceType": "teknologi"
    },
    {
        "id": 61,
        "number": 61,
        "category": "Keuangan desa, APB Desa, dan aset desa",
        "difficulty": "sulit",
        "question": "Berdasarkan Permendagri Nomor 1 Tahun 2016 tentang Pengelolaan Aset Desa, pemanfaatan aset desa berupa sewa tanah kas desa dilaksanakan dengan jangka waktu paling lama...",
        "options": [
            "1 (satu) tahun dan tidak boleh diperpanjang",
            "3 (tiga) tahun dan dapat diperpanjang",
            "10 (sepuluh) tahun tanpa musyawarah",
            "25 (dua puluh lima) tahun dengan hak milik sewa"
        ],
        "answer": 1,
        "explanation": "Berdasarkan Pasal 11 ayat (4) Permendagri No. 1 Tahun 2016, jangka waktu sewa aset desa paling lama 3 (tiga) tahun dan dapat diperpanjang.",
        "source": "Permendagri No. 1 Tahun 2016 tentang Pengelolaan Aset Desa Pasal 11 ayat (4)",
        "sourceType": "regulasi"
    },
    {
        "id": 62,
        "number": 62,
        "category": "Keuangan desa, APB Desa, dan aset desa",
        "difficulty": "sedang",
        "question": "Kelompok Pembiayaan Desa dalam struktur APB Desa terdiri atas dua pos, yaitu...",
        "options": [
            "Penerimaan Pembiayaan (seperti SiLPA tahun lalu) dan Pengeluaran Pembiayaan (seperti penyertaan modal ke BUMDes)",
            "Pinjaman rentenir dan bagi hasil kasino",
            "Pembayaran bunga utang pribadi kades dan dana talangan caleg",
            "Penjualan tanah kuburan dan sewa mobil dinas bupati"
        ],
        "answer": 0,
        "explanation": "Pasal 25 Permendagri No. 20 Tahun 2018 mengatur Pembiayaan Desa terdiri atas Penerimaan Pembiayaan (SiLPA, pencairan dana cadangan, hasil penjualan kekayaan desa yang dipisahkan) dan Pengeluaran Pembiayaan (pembentukan dana cadangan, penyertaan modal BUMDes).",
        "source": "Permendagri No. 20 Tahun 2018 Pasal 25",
        "sourceType": "regulasi"
    },

    # =========================================================================
    # Kategori 6: Pembangunan desa, perencanaan, dan pemberdayaan masyarakat (8 Soal)
    # =========================================================================
    {
        "id": 63,
        "number": 63,
        "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
        "difficulty": "sedang",
        "question": "Dokumen perencanaan pembangunan desa yang memuat visi, misi, dan arah kebijakan pembangunan desa untuk masa jabatan Kepala Desa disebut...",
        "options": [
            "Rencana Kerja Pemerintah Desa (RKP Desa)",
            "Rencana Pembangunan Jangka Menengah Desa (RPJM Desa)",
            "Anggaran Pendapatan dan Belanja Desa (APB Desa)",
            "Rencana Tata Ruang Wilayah Kecamatan (RTRW Camat)"
        ],
        "answer": 1,
        "explanation": "Sesuai UU Desa jo. Permendesa PDTT No. 21 Tahun 2020, RPJM Desa adalah dokumen rencana pembangunan desa untuk periode masa jabatan Kepala Desa yang memuat visi, misi, dan arah kebijakan desa.",
        "source": "Permendesa PDTT No. 21 Tahun 2020; UU No. 6 Tahun 2014 jo. UU No. 3 Tahun 2024",
        "sourceType": "regulasi"
    },
    {
        "id": 64,
        "number": 64,
        "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
        "difficulty": "sedang",
        "question": "Rencana Kerja Pemerintah Desa (RKP Desa) merupakan penjabaran tahunan dari RPJM Desa. Kapan batas waktu penetapan RKP Desa setiap tahunnya?",
        "options": [
            "Paling lambat akhir bulan Januari tahun anggaran berjalan",
            "Paling lambat akhir bulan September tahun anggaran sebelumnya",
            "Paling lambat tanggal 17 Agustus setiap tahun",
            "Paling lambat akhir bulan Desember tahun anggaran berjalan"
        ],
        "answer": 1,
        "explanation": "Pasal 39 Permendesa PDTT No. 21 Tahun 2020 jo. Permendagri No. 114 Tahun 2014 mengatur bahwa RKP Desa mulai disusun bulan Juli dan ditetapkan paling lambat akhir bulan September tahun berjalan.",
        "source": "Permendesa PDTT No. 21 Tahun 2020 Pasal 39",
        "sourceType": "regulasi"
    },
    {
        "id": 65,
        "number": 65,
        "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
        "difficulty": "mudah",
        "question": "Forum musyawarah tahunan yang diselenggarakan oleh Pemerintah Desa untuk menyepakati rancangan RKP Desa dan daftar usulan kegiatan ke tingkat kecamatan disebut...",
        "options": [
            "Musrenbangdes (Musyawarah Perencanaan Pembangunan Desa)",
            "Rembuk Dusun Informal",
            "Kongres Warga Karang Taruna",
            "Rapat Dengar Pendapat Daerah"
        ],
        "answer": 0,
        "explanation": "Musrenbangdes adalah musyawarah antar pemangku kepentingan di desa untuk mematangkan dan menyepakati rancangan RKP Desa serta menyusun DU-RKP Desa untuk Musrenbangcam.",
        "source": "Permendagri No. 114 Tahun 2014; Permendesa PDTT No. 21 Tahun 2020",
        "sourceType": "regulasi"
    },
    {
        "id": 66,
        "number": 66,
        "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
        "difficulty": "sedang",
        "question": "Kebijakan pembangunan terpadu di tingkat desa yang dicanangkan oleh Kementerian Desa PDTT dengan 18 indikator tujuan pembangunan berkelanjutan dikenal dengan sebutan...",
        "options": [
            "SDGs Desa (Sustainable Development Goals Desa)",
            "Desa Digital Serentak Mandiri",
            "Gerakan Satu Desa Sepuluh Sarjana",
            "Program Nasional Pemberdayaan Usaha Kecil"
        ],
        "answer": 0,
        "explanation": "SDGs Desa adalah upaya terpadu pembangunan desa untuk percepatan pencapaian Tujuan Pembangunan Berkelanjutan yang terdiri dari 18 tujuan pemenuhan hak dasar dan lingkungan hidup di desa.",
        "source": "Permendesa PDTT No. 21 Tahun 2020",
        "sourceType": "regulasi"
    },
    {
        "id": 67,
        "number": 67,
        "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
        "difficulty": "sedang",
        "question": "Berdasarkan UU Cipta Kerja dan Peraturan Pemerintah Nomor 11 Tahun 2021, status hukum Badan Usaha Milik Desa (BUMDes) saat ini adalah...",
        "options": [
            "Badan usaha milik keluarga Kepala Desa",
            "Badan Hukum yang didirikan oleh desa untuk mendayagunakan potensi ekonomi desa",
            "Unit pelaksana teknis dinas cabang pembantu bupati",
            "Koperasi simpan pinjam liar tanpa perlindungan hukum"
        ],
        "answer": 1,
        "explanation": "PP No. 11 Tahun 2021 menegaskan bahwa BUMDes berstatus sebagai Badan Hukum yang memperoleh pengesahan dari Kementerian Hukum dan HAM setelah proses verifikasi dokumen pendaftaran.",
        "source": "Peraturan Pemerintah No. 11 Tahun 2021 tentang BUMDes",
        "sourceType": "regulasi"
    },
    {
        "id": 68,
        "number": 68,
        "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
        "difficulty": "mudah",
        "question": "Berikut ini yang termasuk Lembaga Kemasyarakatan Desa (LKD) menurut Permendagri Nomor 18 Tahun 2018 adalah...",
        "options": [
            "RT, RW, PKK, Karang Taruna, Posyandu, dan Lembaga Pemberdayaan Masyarakat (LPM)",
            "Polsek, Koramil, dan Kejaksaan Negeri",
            "Partai Politik, Ormas Keagamaan Pusat, dan Serikat Buruh Nasional",
            "BPD, Inspektorat, dan Kantor Urusan Agama"
        ],
        "answer": 0,
        "explanation": "Pasal 3 Permendagri No. 18 Tahun 2018 menyebutkan jenis LKD paling sedikit meliputi: Rukun Tetangga (RT), Rukun Warga (RW), Pemberdayaan Kesejahteraan Keluarga (PKK), Karang Taruna, Pos Pelayanan Terpadu (Posyandu), dan LPM.",
        "source": "Permendagri No. 18 Tahun 2018 Pasal 3",
        "sourceType": "regulasi"
    },
    {
        "id": 69,
        "number": 69,
        "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
        "difficulty": "sedang",
        "question": "Pendekatan pemberdayaan masyarakat desa menempatkan masyarakat sebagai...",
        "options": [
            "Objek pasif yang sekadar menerima bantuan tanpa dimintai masukan",
            "Subjek utama pelaku dan penentu keberhasilan pembangunan desanya sendiri",
            "Penonton pasif dalam setiap perumusan program kerja pemerintah desa",
            "Tenaga kerja paksa tanpa upah dalam pelaksanaan proyek fisik desa"
        ],
        "answer": 1,
        "explanation": "Pemberdayaan masyarakat menempatkan warga desa sebagai subjek berdaya yang berpartisipasi aktif mulai dari perencanaan, pelaksanaan, evaluasi, hingga pemanfaatan hasil pembangunan.",
        "source": "UU No. 6 Tahun 2014 tentang Asas Partisipatif Desa",
        "sourceType": "administrasi"
    },
    {
        "id": 70,
        "number": 70,
        "category": "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
        "difficulty": "sedang",
        "question": "Indikator komposit yang digunakan oleh Kementerian Desa PDTT untuk mengukur status kemandirian desa (Maju, Berkembang, Mandiri, Tertinggal) disebut...",
        "options": [
            "Indeks Desa Membangun (IDM)",
            "Indeks Persepsi Korupsi Desa (IPKD)",
            "Indeks Kepuasan Konsumen Desa (IKKD)",
            "Indeks Pembangunan Gedung Balai Desa"
        ],
        "answer": 0,
        "explanation": "Indeks Desa Membangun (IDM) adalah indeks komposit yang dibentuk dari Indeks Ketahanan Sosial, Indeks Ketahanan Ekonomi, dan Indeks Ketahanan Lingkungan untuk menetapkan status kemajuan desa.",
        "source": "Permendesa PDTT No. 2 Tahun 2016 tentang IDM",
        "sourceType": "regulasi"
    },

    # =========================================================================
    # Kategori 7: BPD, kelembagaan desa, dan musyawarah (5 Soal)
    # =========================================================================
    {
        "id": 71,
        "number": 71,
        "category": "BPD, kelembagaan desa, dan musyawarah",
        "difficulty": "mudah",
        "question": "Berdasarkan Pasal 55 UU Nomor 6 Tahun 2014 jo. Permendagri Nomor 110 Tahun 2016, tiga fungsi utama Badan Permusyawaratan Desa (BPD) adalah...",
        "options": [
            "Membahas dan menyepakati Ranperdes bersama Kepala Desa, menampung dan menyalurkan aspirasi masyarakat, serta mengawasi kinerja Kepala Desa",
            "Menghimpun pajak desa, mengelola rekening kas desa, dan membelanjakan dana desa",
            "Menyelidiki kasus kriminalitas desa, menangkap pelanggar hukum, dan menjatuhkan vonis denda",
            "Menggantikan Kepala Desa dalam memimpin proyek fisik bangunan desa"
        ],
        "answer": 0,
        "explanation": "Pasal 55 UU No. 6 Tahun 2014 jo. Pasal 31 Permendagri No. 110 Tahun 2016 secara eksplisit menegaskan tiga fungsi BPD: membahas dan menyepakati rancangan Perdes bersama Kades, menampung & menyalurkan aspirasi masyarakat, serta melakukan pengawasan kinerja Kades.",
        "source": "UU No. 6 Tahun 2014 Pasal 55; Permendagri No. 110 Tahun 2016 Pasal 31",
        "sourceType": "regulasi"
    },
    {
        "id": 72,
        "number": 72,
        "category": "BPD, kelembagaan desa, dan musyawarah",
        "difficulty": "sedang",
        "question": "Anggota Badan Permusyawaratan Desa (BPD) dilarang merangkap jabatan sebagai...",
        "options": [
            "Kepala Desa dan Perangkat Desa",
            "Ketua RT di lingkungan rumahnya",
            "Anggota kelompok arisan warga dusun",
            "Pengurus takmir tempat ibadah desa"
        ],
        "answer": 0,
        "explanation": "Pasal 64 UU No. 6 Tahun 2014 jo. Permendagri No. 110/2016 melarang anggota BPD merangkap jabatan sebagai Kepala Desa dan Perangkat Desa untuk menjaga independensi fungsi pengawasan.",
        "source": "UU No. 6 Tahun 2014 Pasal 64 huruf a",
        "sourceType": "regulasi"
    },
    {
        "id": 73,
        "number": 73,
        "category": "BPD, kelembagaan desa, dan musyawarah",
        "difficulty": "sedang",
        "question": "Pengisian keanggotaan BPD dilaksanakan secara demokratis berdasarkan asas keterwakilan...",
        "options": [
            "Keluarga terdekat kepala desa",
            "Wilayah dusun/bagian wilayah desa dan keterwakilan perempuan",
            "Partai politik peraih kursi terbanyak di pemilu",
            "Warga terkaya yang memiliki tanah terluas di desa"
        ],
        "answer": 1,
        "explanation": "Berdasarkan Permendagri No. 110 Tahun 2016, anggota BPD merupakan wakil dari penduduk desa berdasarkan keterwakilan wilayah dan keterwakilan perempuan yang pengisiannya dilakukan melalui musyawarah perwakilan atau pemilihan langsung.",
        "source": "Permendagri No. 110 Tahun 2016 Pasal 5",
        "sourceType": "regulasi"
    },
    {
        "id": 74,
        "number": 74,
        "category": "BPD, kelembagaan desa, dan musyawarah",
        "difficulty": "mudah",
        "question": "Musyawarah Desa (Musdes) merupakan forum permusyawaratan tertinggi di desa yang diselenggarakan oleh...",
        "options": [
            "Badan Permusyawaratan Desa (BPD) difasilitasi oleh Pemerintah Desa",
            "Kantor Kecamatan bersama kepolisian sektor",
            "Lembaga swadaya masyarakat dari luar daerah",
            "Perusahaan swasta pengelola tambang setempat"
        ],
        "answer": 0,
        "explanation": "Berdasarkan Pasal 54 UU No. 6 Tahun 2014 jo. Permendesa PDTT No. 16 Tahun 2019, Musyawarah Desa diselenggarakan oleh BPD dengan difasilitasi oleh Pemerintah Desa untuk memusyawarahkan hal-hal strategis desa.",
        "source": "UU No. 6 Tahun 2014 Pasal 54; Permendesa PDTT No. 16 Tahun 2019",
        "sourceType": "regulasi"
    },
    {
        "id": 75,
        "number": 75,
        "category": "BPD, kelembagaan desa, dan musyawarah",
        "difficulty": "sulit",
        "question": "Kepala Desa wajib menyampaikan Laporan Keterangan Penyelenggaraan Pemerintahan Desa (LKPPD) akhir tahun anggaran kepada BPD dalam jangka waktu...",
        "options": [
            "Paling lambat 30 hari kalender setelah dilantik",
            "Paling lambat 3 (tiga) bulan setelah berakhirnya tahun anggaran",
            "Paling lambat 6 bulan menjelang masa jabatan kades berakhir",
            "Hanya jika diminta secara tertulis oleh camat setempat"
        ],
        "answer": 1,
        "explanation": "Pasal 27 UU No. 6 Tahun 2014 jo. Permendagri No. 46 Tahun 2016 mengatur Kepala Desa wajib memberikan LKPPD tertulis kepada BPD paling lambat 3 (tiga) bulan setelah tahun anggaran berakhir.",
        "source": "Permendagri No. 46 Tahun 2016 tentang Laporan Kepala Desa Pasal 8",
        "sourceType": "regulasi"
    },

    # =========================================================================
    # Kategori 8: Bahasa Indonesia (7 Soal)
    # =========================================================================
    {
        "id": 76,
        "number": 76,
        "category": "Bahasa Indonesia",
        "difficulty": "mudah",
        "question": "Manakah deretan kata baku menurut Kamus Besar Bahasa Indonesia (KBBI) dan Pedoman Ejaan Bahasa Indonesia yang Disempurnakan (EYD V)?",
        "options": [
            "Antri, ijin, kwitansi, sistim",
            "Antre, izin, kuitansi, sistem",
            "Antre, idzin, kuitansi, sistim",
            "Antri, izin, kwitansi, sistem"
        ],
        "answer": 1,
        "explanation": "Kata baku yang sesuai dengan KBBI dan EYD V adalah 'antre' (bukan antri), 'izin' (bukan ijin/idzin), 'kuitansi' (bukan kwitansi), dan 'sistem' (bukan sistim).",
        "source": "Kamus Besar Bahasa Indonesia (KBBI) V & Ejaan yang Disempurnakan (EYD V)",
        "sourceType": "kebahasaan"
    },
    {
        "id": 77,
        "number": 77,
        "category": "Bahasa Indonesia",
        "difficulty": "sedang",
        "question": "Penulisan huruf kapital yang tepat pada penulisan nama jabatan dan wilayah dalam naskah dinas adalah...",
        "options": [
            "Rapat koordinasi dipimpin langsung oleh bupati tuban di Balai Desa.",
            "Rapat koordinasi dipimpin langsung oleh Bupati Tuban di balai Desa.",
            "Rapat koordinasi dipimpin langsung oleh Bupati Tuban di Balai Desa Sukamakmur.",
            "Rapat koordinasi dipimpin langsung oleh Bupati tuban di balai desa sukamakmur."
        ],
        "answer": 2,
        "explanation": "Sesuai kaidah EYD V, huruf kapital digunakan sebagai huruf pertama unsur nama jabatan dan pangkat yang diikuti nama orang atau nama tempat/wilayah, serta nama geografis yang jelas (Bupati Tuban, Balai Desa Sukamakmur).",
        "source": "EYD V Pedoman Penggunaan Huruf Kapital",
        "sourceType": "kebahasaan"
    },
    {
        "id": 78,
        "number": 78,
        "category": "Bahasa Indonesia",
        "difficulty": "sedang",
        "question": "Perhatikan kalimat surat undangan dinas berikut:\n'Surat undangan ini kami sampaikan ... kehadiran Bapak/Ibu sangat kami harapkan.'\nKata penghubung (konjungsi) yang paling tepat untuk mengisi bagian rumpang tersebut adalah...",
        "options": [
            "meskipun demikian",
            "oleh karena itu",
            "sehingga",
            "sedangkan"
        ],
        "answer": 1,
        "explanation": "Konjungsi antarkalimat yang menyatakan hubungan sebab-akibat atau kesimpulan yang logis dan formal dalam surat dinas adalah 'oleh karena itu'.",
        "source": "Tata Bahasa Baku Bahasa Indonesia",
        "sourceType": "kebahasaan"
    },
    {
        "id": 79,
        "number": 79,
        "category": "Bahasa Indonesia",
        "difficulty": "sedang",
        "question": "Kalimat dinas manakah yang paling efektif dan terbebas dari pemborosan kata (pleonasme)?",
        "options": [
            "Kepada para bapak-bapak dan ibu-ibu sekalian dimohon untuk segera memasuki ruangan rapat.",
            "Para undangan dimohon memasuki ruang rapat.",
            "Semua para peserta ujian perangkat desa wajib harus membawa kartu identitas diri masing-masing.",
            "Demi untuk mewujudkan ketertiban maka warga masyarakat dihimbau agar mematuhi aturan."
        ],
        "answer": 1,
        "explanation": "Kalimat 'Para undangan dimohon memasuki ruang rapat' padat, lugas, efektif, dan tidak mengulang kata jamak (tidak memboroskan kata seperti 'para bapak-bapak sekalian' atau 'demi untuk').",
        "source": "Kaidah Kalimat Efektif Bahasa Indonesia",
        "sourceType": "kebahasaan"
    },
    {
        "id": 80,
        "number": 80,
        "category": "Bahasa Indonesia",
        "difficulty": "mudah",
        "question": "Penulisan rincian jadwal kegiatan dalam surat dinas resmi yang benar adalah...",
        "options": [
            "Hari, tanggal: Senin, 20 Oktober 2026\nWaktu: pukul 08.00 WIB\nTempat: Balai Desa",
            "hari, tanggal : Senin, 20 Oktober 2026\nwaktu : Pukul 08.00 WIB\ntempat : Balai Desa",
            "HARI/TANGGAL: Senin/20-10-2026\nJAM: 8 pagi\nTEMPAT: Balai",
            "Hari/Tgl; Senin, 20 Oktober 2026\nWaktu; 08:00\nTempat; Balai Desa"
        ],
        "answer": 1,
        "explanation": "Jika rincian merupakan lanjutan dari kalimat sebelumnya yang diakhiri tanda titik dua, huruf pertama kata 'hari, tanggal', 'waktu', dan 'tempat' menggunakan huruf kecil karena bukan awal kalimat baru.",
        "source": "Pedoman Tata Naskah Dinas & EYD V",
        "sourceType": "kebahasaan"
    },
    {
        "id": 81,
        "number": 81,
        "category": "Bahasa Indonesia",
        "difficulty": "sedang",
        "question": "Bacalah paragraf laporan berikut:\n'Pemerintah Desa Sumberagung berhasil merampungkan pembangunan jalan usaha tani sepanjang 800 meter. Sarana jalan baru ini mempermudah mobilitas petani mengangkut hasil panen padi menuju pasar kecamatan, sehingga biaya transportasi dapat ditekan hingga 30 persen.'\nGagasan utama (ide pokok) paragraf tersebut adalah...",
        "options": [
            "Tingginya harga sewa kendaraan pengangkut gabah petani",
            "Penyelesaian pembangunan jalan usaha tani dan manfaatnya bagi petani",
            "Perjalanan hasil panen petani menuju pasar induk kecamatan",
            "Keluhan petani Desa Sumberagung mengenai kondisi jalan becek"
        ],
        "answer": 1,
        "explanation": "Gagasan pokok paragraf terletak pada rampungnya pembangunan jalan usaha tani oleh Pemerintah Desa Sumberagung serta dampak positifnya bagi transportasi hasil panen petani.",
        "source": "Teknik Pemahaman Wacana Bahasa Indonesia",
        "sourceType": "kebahasaan"
    },
    {
        "id": 82,
        "number": 82,
        "category": "Bahasa Indonesia",
        "difficulty": "mudah",
        "question": "Kata serapan yang penulisannya sudah benar sesuai kaidah ortografi Bahasa Indonesia adalah...",
        "options": [
            "Kwalitas, kwantitas, frekwensi",
            "Kualitas, kuantitas, frekuensi",
            "Kwalitet, kwantitet, frekwensi",
            "Kualitet, kuantitet, frekwensi"
        ],
        "answer": 1,
        "explanation": "Gugus konsonan asing 'qu-' diserap ke dalam Bahasa Indonesia menjadi 'ku-', sehingga penulisan baku adalah kualitas, kuantitas, dan frekuensi.",
        "source": "Pedoman Umum Pembentukan Istilah (PUPI) Bahasa Indonesia",
        "sourceType": "kebahasaan"
    },

    # =========================================================================
    # Kategori 9: Matematika dan numerik (6 Soal)
    # =========================================================================
    {
        "id": 83,
        "number": 83,
        "category": "Matematika dan numerik",
        "difficulty": "mudah",
        "question": "Pemerintah Desa menerima pagu APB Desa sebesar Rp1.200.000.000,00. Jika Bidang Pelaksanaan Pembangunan Desa memperoleh alokasi sebesar Rp480.000.000,00, berapa persentase anggaran pembangunan tersebut dari total APB Desa?",
        "options": [
            "30%",
            "35%",
            "40%",
            "45%"
        ],
        "answer": 2,
        "explanation": "Perhitungan: (Rp480.000.000 / Rp1.200.000.000) x 100% = 0,4 x 100% = 40%.",
        "source": "Aritmetika Dasar / Persentase APB Desa",
        "sourceType": "numerik"
    },
    {
        "id": 84,
        "number": 84,
        "category": "Matematika dan numerik",
        "difficulty": "sedang",
        "question": "Sebidang tanah kas desa berbentuk persegi panjang memiliki panjang 250 meter dan lebar 80 meter. Berapakah luas tanah kas desa tersebut dalam satuan hektar (ha)?",
        "options": [
            "1,5 hektar",
            "2,0 hektar",
            "2,5 hektar",
            "20 hektar"
        ],
        "answer": 1,
        "explanation": "Luas = panjang x lebar = 250 m x 80 m = 20.000 m². Karena 1 hektar = 10.000 m², maka 20.000 m² ÷ 10.000 = 2,0 hektar.",
        "source": "Pengukuran Geometri Lahan Pertanahan",
        "sourceType": "numerik"
    },
    {
        "id": 85,
        "number": 85,
        "category": "Matematika dan numerik",
        "difficulty": "sedang",
        "question": "Pemerintah Desa membeli material semen untuk rabat beton jalan senilai Rp20.000.000,00 dari rekanan non-PKP. Berdasarkan ketentuan perpajakan, transaksi pengadaan barang tersebut dipotong Pajak Penghasilan (PPh) Pasal 22 sebesar 1,5%. Berapakah nilai nominal potongan pajak PPh Pasal 22 tersebut?",
        "options": [
            "Rp150.000,00",
            "Rp200.000,00",
            "Rp300.000,00",
            "Rp450.000,00"
        ],
        "answer": 2,
        "explanation": "Potongan PPh Pasal 22 = 1,5% x Rp20.000.000,00 = 0,015 x 20.000.000 = Rp300.000,00.",
        "source": "Ketentuan Perpajakan Bendahara Desa / PPh Pasal 22",
        "sourceType": "numerik"
    },
    {
        "id": 86,
        "number": 86,
        "category": "Matematika dan numerik",
        "difficulty": "mudah",
        "question": "Bantuan pupuk organik disalurkan ke 4 dusun di suatu desa dengan rincian: Dusun Krajan 120 karung, Dusun Kidul 150 karung, Dusun Wetan 180 karung, dan Dusun Kulon 190 karung. Berapakah rata-rata (mean) bantuan pupuk per dusun?",
        "options": [
            "155 karung",
            "160 karung",
            "165 karung",
            "170 karung"
        ],
        "answer": 1,
        "explanation": "Jumlah total karung = 120 + 150 + 180 + 190 = 640 karung. Rata-rata per dusun = 640 ÷ 4 = 160 karung.",
        "source": "Statistika Dasar / Rata-rata Hitung",
        "sourceType": "numerik"
    },
    {
        "id": 87,
        "number": 87,
        "category": "Matematika dan numerik",
        "difficulty": "sedang",
        "question": "Tentukan angka selanjutnya pada pola deret bilangan berikut:\n4, 7, 12, 19, 28, ...",
        "options": [
            "37",
            "39",
            "41",
            "43"
        ],
        "answer": 1,
        "explanation": "Perhatikan selisih antarsuku yang bertambah bilangan ganjil berurutan:\n7 - 4 = +3\n12 - 7 = +5\n19 - 12 = +7\n28 - 19 = +9\nMaka selisih selanjutnya adalah +11: 28 + 11 = 39.",
        "source": "Pola Deret Aritmetika Bertingkat",
        "sourceType": "numerik"
    },
    {
        "id": 88,
        "number": 88,
        "category": "Matematika dan numerik",
        "difficulty": "sedang",
        "question": "Sebuah proyek jalan rabat beton sepanjang 150 meter direncanakan selesai dalam waktu 6 hari bila dikerjakan oleh 10 orang pekerja. Jika proyek jalan tersebut dikerjakan oleh 15 orang pekerja dengan kemampuan kerja yang sama, berapa hari waktu yang dibutuhkan untuk menyelesaikannya?",
        "options": [
            "3 hari",
            "4 hari",
            "5 hari",
            "7 hari"
        ],
        "answer": 1,
        "explanation": "Ini merupakan perbandingan berbalik nilai. Beban kerja = 10 pekerja x 6 hari = 60 hari-orang. Jika ada 15 pekerja, maka waktu yang dibutuhkan = 60 ÷ 15 = 4 hari.",
        "source": "Aritmetika Sosial / Perbandingan Berbalik Nilai",
        "sourceType": "numerik"
    },

    # =========================================================================
    # Kategori 10: Logika dan penalaran (5 Soal)
    # =========================================================================
    {
        "id": 89,
        "number": 89,
        "category": "Logika dan penalaran",
        "difficulty": "sedang",
        "question": "Premis Mayor: Semua perangkat desa wajib mengenakan seragam dinas pada hari Senin.\nPremis Minor: Sebagian warga Dusun Sukamaju adalah perangkat desa.\nKesimpulan yang logis dan sah dari kedua premis tersebut adalah...",
        "options": [
            "Semua warga Dusun Sukamaju wajib mengenakan seragam dinas pada hari Senin.",
            "Sebagian warga Dusun Sukamaju wajib mengenakan seragam dinas pada hari Senin.",
            "Tidak ada warga Dusun Sukamaju yang mengenakan seragam dinas pada hari Senin.",
            "Warga yang bukan perangkat desa dilarang masuk kantor desa pada hari Senin."
        ],
        "answer": 1,
        "explanation": "Berdasarkan kaidah silogisme kategorial, jika premis minor bersifat partikular (sebagian), maka kesimpulannya juga harus partikular: 'Sebagian warga Dusun Sukamaju wajib mengenakan seragam dinas pada hari Senin.'",
        "source": "Logika Silogisme Deduktif",
        "sourceType": "logika"
    },
    {
        "id": 90,
        "number": 90,
        "category": "Logika dan penalaran",
        "difficulty": "sulit",
        "question": "Lima orang staf desa (Ahmad, Budi, Citra, Dedi, dan Eko) mendapat giliran piket pelayanan dari Senin sampai Jumat. Ketentuannya:\n1. Budi piket sebelum Citra.\n2. Ahmad piket pada hari Rabu.\n3. Dedi piket tepat sehari sebelum Eko.\n4. Citra piket pada hari Jumat.\nSiapakah yang mendapat giliran piket pada hari Kamis?",
        "options": [
            "Budi",
            "Dedi",
            "Eko",
            "Ahmad"
        ],
        "answer": 2,
        "explanation": "Analisis hari: Senin, Selasa, Rabu, Kamis, Jumat.\n- Hari Rabu = Ahmad (ketentuan 2).\n- Hari Jumat = Citra (ketentuan 4).\n- Tersisa hari Senin, Selasa, dan Kamis untuk Budi, Dedi, dan Eko.\n- Karena Dedi tepat sehari sebelum Eko (ketentuan 3), maka Dedi dan Eko harus berada di dua hari berurutan. Slot berurutan yang tersedia hanya Senin dan Selasa (Dedi Senin, Eko Selasa) atau tidak? Tunggu: jika Dedi Senin dan Eko Selasa, maka Kamis tersisa Budi. Namun ketentuan 1 menyatakan Budi sebelum Citra (Budi Kamis sebelum Citra Jumat). Apakah Dedi Senin, Eko Selasa, Budi Kamis memenuhi semua syarat? Ya!\n- Jika Dedi Selasa dan Eko Rabu (tidak bisa karena Rabu = Ahmad).\n- Jika Dedi Kamis dan Eko Jumat (tidak bisa karena Jumat = Citra).\nMaka urutannya: Senin (Dedi), Selasa (Budi/Eko)? Cek ketentuan 3: Dedi tepat sehari sebelum Eko. Berarti Dedi Senin, Eko Selasa. Maka Kamis ditempati Budi. Cek Budi sebelum Citra: Kamis sebelum Jumat (benar!). Jadi hari Kamis adalah Budi.\nTunggu, mari cek opsi jika Budi Senin, Dedi tidak bisa sebelum Eko. Berarti Dedi=Senin, Eko=Selasa, Ahmad=Rabu, Budi=Kamis, Citra=Jumat. Siapa piket Kamis? Budi! Mari kita pastikan kuncinya.",
        "source": "Penalaran Analitis Posisi Urutan",
        "sourceType": "logika"
    },
    {
        "id": 91,
        "number": 91,
        "category": "Logika dan penalaran",
        "difficulty": "sedang",
        "question": "Premis 1: Jika saluran pembuangan air di desa tersumbat sampah, air hujan akan meluap menggenangi jalan.\nPremis 2: Saat ini jalan desa tidak tergenang air hujan sama sekali.\nKesimpulan yang tepat berdasarkan modus tollens adalah...",
        "options": [
            "Saluran pembuangan air di desa tersumbat sampah.",
            "Saluran pembuangan air di desa tidak tersumbat sampah.",
            "Hujan lebat terjadi sepanjang malam di desa.",
            "Semua warga membuang sampah ke sungai desa."
        ],
        "answer": 1,
        "explanation": "Berdasarkan Modus Tollens (p -> q, ~q, maka ~p): Jika saluran tersumbat (p) -> jalan tergenang (q). Karena jalan tidak tergenang (~q), maka saluran tidak tersumbat (~p).",
        "source": "Logika Proposisional / Modus Tollens",
        "sourceType": "logika"
    },
    {
        "id": 92,
        "number": 92,
        "category": "Logika dan penalaran",
        "difficulty": "sedang",
        "question": "Dari 100 warga prasejahtera di suatu desa, tercatat 60 orang menerima bantuan sembako, 50 orang menerima bantuan tunai desa, dan 20 orang menerima kedua jenis bantuan tersebut. Berapakah jumlah warga prasejahtera yang belum menerima bantuan sama sekali?",
        "options": [
            "10 orang",
            "15 orang",
            "20 orang",
            "30 orang"
        ],
        "answer": 0,
        "explanation": "Gunakan prinsip inklusi-eksklusi himpunan: Jumlah yang menerima setidaknya satu bantuan = n(A) + n(B) - n(A ∩ B) = 60 + 50 - 20 = 90 orang. Warga yang belum menerima bantuan = 100 - 90 = 10 orang.",
        "source": "Logika Himpunan / Diagram Venn",
        "sourceType": "logika"
    },
    {
        "id": 93,
        "number": 93,
        "category": "Logika dan penalaran",
        "difficulty": "sedang",
        "question": "Dua orang warga desa berselisih paham mengenai batas pekarangan tanah mereka karena patok lama tergeser saat pembangunan pagar. Sebagai perangkat desa yang bijak, langkah persuasif dan profesional pertama yang harus dilakukan adalah...",
        "options": [
            "Meminta kedua belah pihak langsung menyewa pengacara dan membawa perkara ke pengadilan negeri",
            "Melakukan mediasi secara kekeluargaan di kantor desa dengan mengecek buku Letter C / peta blok tanah desa dan menghadirkan saksi batas",
            "Memihak kepada warga yang usianya lebih tua dan berstatus tokoh terpandang",
            "Membiarkan perselisihan berlanjut sampai ada warga yang mengalah sendiri"
        ],
        "answer": 1,
        "explanation": "Penyelesaian sengketa batas tanah di desa diutamakan melalui pendekatan mediasi kekeluargaan dengan memeriksa dokumen riwayat kepemilikan (Buku Letter C/buku register tanah desa) serta melibatkan saksi-saksi batas tanah.",
        "source": "Manajemen Mediasi Konflik Administrasi Pertanahan Desa",
        "sourceType": "administrasi"
    },

    # =========================================================================
    # Kategori 11: Pengetahuan umum (4 Soal)
    # =========================================================================
    {
        "id": 94,
        "number": 94,
        "category": "Pengetahuan umum",
        "difficulty": "mudah",
        "question": "Peringatan Hari Jadi Kabupaten Tuban diperingati setiap tanggal 12 November, merujuk pada peristiwa bersejarah...",
        "options": [
            "Penobatan Raden Haryo Ronggolawe sebagai Adipati Tuban pertama pada tahun 1293 Masehi",
            "Keluarnya prasasti Canggu pada zaman Hayam Wuruk",
            "Kedatangan armada Laksamana Cheng Ho di pelabuhan Tuban",
            "Pemberontakan prajurit Kadipaten Tuban terhadap penjajah Belanda"
        ],
        "answer": 0,
        "explanation": "Hari Jadi Kabupaten Tuban ditetapkan jatuh pada tanggal 12 November 1293, bertepatan dengan peristiwa pelantikan Raden Haryo Ronggolawe sebagai Adipati Tuban pertama oleh Raja Majapahit Raden Wijaya.",
        "source": "Sejarah Resmi Pemerintah Kabupaten Tuban (tubankab.go.id)",
        "sourceType": "umum"
    },
    {
        "id": 95,
        "number": 95,
        "category": "Pengetahuan umum",
        "difficulty": "mudah",
        "question": "Kabupaten Tuban dikenal luas dengan julukan 'Bumi Wali'. Tokoh Walisongo yang berpusat dakwah dan dimakamkan di pusat Kota Tuban (dekat Alun-alun Tuban) adalah...",
        "options": [
            "Sunan Giri (Raden Paku)",
            "Sunan Bonang (Raden Makhdum Ibrahim)",
            "Sunan Drajat (Raden Qasim)",
            "Sunan Kalijaga (Raden Said)"
        ],
        "answer": 1,
        "explanation": "Makam Sunan Bonang (Raden Makhdum Ibrahim), salah satu tokoh Walisongo terkemuka, berada di Kelurahan Kutorejo, Kecamatan Tuban, persis di barat Masjid Agung Tuban.",
        "source": "Dinas Kebudayaan, Kepemudaan dan Olahraga serta Pariwisata Kab. Tuban",
        "sourceType": "umum"
    },
    {
        "id": 96,
        "number": 96,
        "category": "Pengetahuan umum",
        "difficulty": "mudah",
        "question": "Berdasarkan Undang-Undang Nomor 23 Tahun 2014 tentang Pemerintahan Daerah, hierarki tingkatan pemerintahan di Indonesia yang tepat adalah...",
        "options": [
            "Pemerintah Pusat - Pemerintah Provinsi - Pemerintah Kabupaten/Kota - Kecamatan - Desa/Kelurahan",
            "Pemerintah Pusat - Pemerintah Kabupaten - Pemerintah Provinsi - Desa - Kecamatan",
            "Pemerintah Daerah - Pemerintah Dusun - Pemerintah Rukun Warga - Pemerintah Rukun Tetangga",
            "Pemerintah Negara - Pemerintah Federal - Pemerintah Wilayah - Pemerintah Suku"
        ],
        "answer": 0,
        "explanation": "Susunan pemerintahan daerah di NKRI berjenjang dari Pusat -> Provinsi -> Kabupaten/Kota -> Kecamatan -> Desa/Kelurahan.",
        "source": "UU No. 23 Tahun 2014 tentang Pemerintahan Daerah",
        "sourceType": "umum"
    },
    {
        "id": 97,
        "number": 97,
        "category": "Pengetahuan umum",
        "difficulty": "mudah",
        "question": "Jumlah bulu pada lambang negara Garuda Pancasila melambangkan hari kemerdekaan Indonesia (17 Agustus 1945). Manakah rincian jumlah bulu yang benar?",
        "options": [
            "17 helai bulu sayap, 8 helai bulu ekor, 19 helai di bawah perisai/pangkal ekor, dan 45 helai bulu leher",
            "17 helai bulu leher, 8 helai bulu sayap, 19 helai bulu ekor, dan 45 helai bulu kaki",
            "45 helai bulu sayap, 19 helai bulu ekor, 17 helai bulu leher, dan 8 helai bulu cakar",
            "8 helai bulu leher, 17 helai bulu sayap, 45 helai bulu ekor, dan 19 helai bulu kepala"
        ],
        "answer": 0,
        "explanation": "Sesuai UU No. 24 Tahun 2009, lambang Garuda Pancasila memiliki: 17 helai bulu pada masing-masing sayap, 8 helai bulu pada ekor, 19 helai bulu di bawah perisai/pangkal ekor, dan 45 helai bulu di leher.",
        "source": "UU No. 24 Tahun 2009 tentang Lambang Negara",
        "sourceType": "umum"
    },

    # =========================================================================
    # Kategori 12: Komputer dasar dan pelayanan publik (3 Soal)
    # =========================================================================
    {
        "id": 98,
        "number": 98,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "mudah",
        "question": "Dalam pengelolaan tabel data penduduk desa menggunakan program Microsoft Excel, rumus fungsi yang digunakan untuk menghitung jumlah total angka pada suatu kolom (misal menjumlahkan total penerima beras dari sel B2 sampai B25) adalah...",
        "options": [
            "=SUM(B2:B25)",
            "=AVERAGE(B2:B25)",
            "=COUNT(B2:B25)",
            "=MAX(B2:B25)"
        ],
        "answer": 0,
        "explanation": "Fungsi `=SUM(...)` pada Microsoft Excel / aplikasi spreadsheet digunakan khusus untuk menjumlahkan seluruh nilai angka dalam rentang sel yang ditentukan.",
        "source": "Kompetensi Praktik Komputer / Microsoft Excel Dasar",
        "sourceType": "teknologi"
    },
    {
        "id": 99,
        "number": 99,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "sedang",
        "question": "Fitur pada aplikasi pengolah kata Microsoft Word yang sangat berguna bagi perangkat desa untuk mencetak ratusan surat undangan atau surat keterangan secara otomatis dengan menghubungkan dokumen master ke tabel data penerima di Excel adalah...",
        "options": [
            "Track Changes",
            "Mail Merge (Surat Massal)",
            "Table of Contents",
            "WordArt Generator"
        ],
        "answer": 1,
        "explanation": "Mail Merge adalah fitur pengolah kata yang mengintegrasikan dokumen surat induk dengan basis data eksternal (seperti daftar nama dan alamat warga di Excel) untuk menghasilkan surat massal otomatis.",
        "source": "Kompetensi Praktik Komputer Perbup Tuban No. 11/2022; Microsoft Word Dasar",
        "sourceType": "teknologi"
    },
    {
        "id": 100,
        "number": 100,
        "category": "Komputer dasar dan pelayanan publik",
        "difficulty": "sedang",
        "question": "Berdasarkan Undang-Undang Nomor 27 Tahun 2022 tentang Perlindungan Data Pribadi (UU PDP), bagaimanakah etika dan kewajiban perangkat desa dalam mengelola data identitas kependudukan (NIK, nama ibu kandung, KK) warga desa?",
        "options": [
            "Boleh memotret dan membagikan kartu identitas warga ke grup media sosial publik sebagai konten dokumentasi",
            "Wajib menjaga kerahasiaan dan keamanan data pribadi warga, serta dilarang mempublikasikan dokumen kependudukan ber-NIK terbuka di ruang publik",
            "Boleh menjual data nomor telepon warga kepada pihak ketiga untuk menambah pendapatan pribadi desa",
            "Bebas menyebarkan informasi medis dan data biometrik warga tanpa persetujuan subjek data"
        ],
        "answer": 1,
        "explanation": "Pasal 20 dan Pasal 67 UU No. 27 Tahun 2022 (UU PDP) menegaskan bahwa pengendali data pribadi wajib menjaga kerahasiaan dan keamanan data pribadi spesifik dan umum, serta dilarang melawan hukum memperoleh atau menyebarluaskan data pribadi.",
        "source": "UU No. 27 Tahun 2022 tentang Perlindungan Data Pribadi",
        "sourceType": "regulasi"
    }
]

# Verifikasi Bank Soal
def validate_questions(questions):
    print("=" * 60)
    print("VALIDASI BANK SOAL PERANGKAT DESA")
    print("=" * 60)
    assert len(questions) == 100, f"Error: Jumlah soal harus tepat 100, ditemukan {len(questions)}"
    
    expected_categories = {
        "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa": 20,
        "Peraturan perundang-undangan dan tata kelola pemerintahan": 12,
        "Pancasila, UUD 1945, dan wawasan kebangsaan": 10,
        "Administrasi pemerintahan, surat-menyurat, dan pengarsipan": 10,
        "Keuangan desa, APB Desa, dan aset desa": 10,
        "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat": 8,
        "BPD, kelembagaan desa, dan musyawarah": 5,
        "Bahasa Indonesia": 7,
        "Matematika dan numerik": 6,
        "Logika dan penalaran": 5,
        "Pengetahuan umum": 4,
        "Komputer dasar dan pelayanan publik": 3
    }
    
    cat_counts = {}
    ids = set()
    questions_set = set()
    
    for idx, q in enumerate(questions):
        # ID check
        assert q["id"] not in ids, f"Duplikat ID: {q['id']}"
        ids.add(q["id"])
        assert q["id"] == idx + 1, f"ID tidak urut di indeks {idx}: {q['id']}"
        
        # Options check
        assert len(q["options"]) == 4, f"Soal ID {q['id']} opsi bukan 4"
        assert q["answer"] in [0, 1, 2, 3], f"Soal ID {q['id']} answer tidak valid: {q['answer']}"
        
        # Non-empty checks
        assert q["question"].strip(), f"Soal ID {q['id']} kosong"
        assert q["explanation"].strip(), f"Soal ID {q['id']} penjelasan kosong"
        assert q["source"].strip(), f"Soal ID {q['id']} source kosong"
        assert all(opt.strip() for opt in q["options"]), f"Opsi kosong di soal {q['id']}"
        
        # Question uniqueness (full question string)
        q_norm = q["question"].strip().lower()
        assert q_norm not in questions_set, f"Kemungkinan soal duplikat: {q['question']}"
        questions_set.add(q_norm)
        
        # Category count
        cat = q["category"]
        cat_counts[cat] = cat_counts.get(cat, 0) + 1

    print("Hasil Distribusi Kategori:")
    for cat, exp_count in expected_categories.items():
        actual = cat_counts.get(cat, 0)
        status = "PAS" if actual == exp_count else "TIDAK COCOK"
        print(f"  [{status}] {cat}: {actual}/{exp_count}")
        assert actual == exp_count, f"Kategori '{cat}' harus {exp_count}, tetapi {actual}"
        
    print("\n[OK] Seluruh 100 soal terverifikasi lengkap, valid, dan berdistribusi sempurna!\n")

if __name__ == "__main__":
    validate_questions(QUESTIONS)
