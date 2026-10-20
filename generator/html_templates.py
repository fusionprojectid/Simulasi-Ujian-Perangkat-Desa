# -*- coding: utf-8 -*-
"""
HTML Templates Module for CBT Perangkat Desa Kabupaten Tuban
Clean, Semantic HTML5 with Unique Descriptive IDs
"""

def get_html_body():
    return '''
  <!-- Civic Top Header (Modern & Minimalist) -->
  <header class="civic-header no-print">
    <div class="civic-header-inner">
      <div class="brand-block" onclick="CBTApp.navigate('home')" title="Simulasi Ujian Perangkat Desa Kab. Tuban">
        <div class="brand-emblem-wrap">
          <img src="assets/favicon.svg" alt="Logo CBT Tuban" class="brand-logo-img" width="40" height="40">
        </div>
        <div class="brand-text">
          <div class="brand-title-row">
            <h1>Simulasi CBT Perangkat Desa</h1>
            <span class="version-badge" onclick="event.stopPropagation(); CBTApp.openVersionModal();" title="Versi v5.1.0 • Klik untuk Changelog">v5.1.0</span>
          </div>
          <p id="topRegionLabel">Kabupaten Tuban • <span class="brand-copyright">Copyright by fusionproject.id</span></p>
        </div>
      </div>

      <!-- Mobile Hamburger Button -->
      <button class="nav-toggle-btn" id="btnNavToggle" onclick="CBTApp.toggleMobileMenu()" aria-label="Toggle Navigasi">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
      </button>

      <!-- Modern Navigation Bar -->
      <nav class="modern-nav-menu" id="modernNavMenu">
        <button class="nav-btn active" data-nav-view="home" onclick="CBTApp.navigate('home')" title="Halaman Utama">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path></svg>
          <span>Beranda</span>
        </button>
        <button class="nav-btn" data-nav-view="practice-config" onclick="CBTApp.navigate('practice-config')" title="Mode Latihan Bebas">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>
          <span>Mode Latihan</span>
        </button>
        <button class="nav-btn" data-nav-view="glossary" onclick="CBTApp.navigate('glossary')" title="Glosarium 36 Istilah Desa">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
          <span>Glosarium</span>
        </button>
        <button class="nav-btn" data-nav-view="history" onclick="CBTApp.navigate('history')" title="Riwayat &amp; Statistik Nilai">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>
          <span>Riwayat</span>
        </button>
        <button class="nav-btn" data-nav-view="help" onclick="CBTApp.navigate('help')" title="Pusat Bantuan &amp; Panduan Lengkap">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
          <span>Bantuan</span>
        </button>
        <button class="nav-btn" onclick="CBTApp.openBackupModal()" title="Cadangan Data (Ekspor / Impor JSON)">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
          <span>Cadangan</span>
        </button>

        <!-- Font Scale Controls (Minimalist & Compact) -->
        <div class="font-scale-controls" title="Pengaturan Skala Ukuran Teks">
          <button class="font-scale-btn" id="fScaleSm" onclick="CBTApp.setFontScale('90%')">A-</button>
          <button class="font-scale-btn active" id="fScaleMd" onclick="CBTApp.setFontScale('100%')">A</button>
          <button class="font-scale-btn" id="fScaleLg" onclick="CBTApp.setFontScale('115%')">A+</button>
        </div>
      </nav>
    </div>
  </header>

  <main class="app-main">

    <!-- Active Resume Session Alert -->
    <div id="resumeBanner" class="resume-card no-print" style="display:none; background:var(--white); border-left:4px solid var(--emerald-600); border-radius:var(--radius-md); padding:1rem 1.25rem; margin-bottom:1.25rem; box-shadow:var(--shadow-sm); display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.75rem;">
      <div>
        <strong style="color:var(--slate-900);">Sesi Ujian Aktif Ditemukan!</strong>
        <p style="font-size:0.85rem; color:var(--slate-700); margin-top:2px;">Anda memiliki sesi simulasi ujian Kabupaten Tuban yang sedang berlangsung dengan progres dan timer tersimpan aman.</p>
      </div>
      <div style="display:flex; gap:0.5rem;">
        <button class="btn btn-emerald btn-sm" onclick="CBTApp.resumeSession()">Lanjutkan Ujian</button>
        <button class="btn btn-outline btn-sm" onclick="CBTApp.clearSession()">Hapus & Mulai Baru</button>
      </div>
    </div>

    <!-- Official Notice Banner -->
    <div class="disclaimer-banner no-print" style="background:#eff6ff; border:1px solid #bfdbfe; border-radius:var(--radius-md); padding:0.85rem 1.25rem; margin-bottom:1.25rem; display:flex; gap:0.75rem; align-items:flex-start; font-size:0.85rem; color:#1e3a8a; line-height:1.5;">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color:var(--primary-600); flex-shrink:0; margin-top:2px;">
        <circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line>
      </svg>
      <div>
        <strong>FORMAT UJIAN KABUPATEN TUBAN (JAWA TIMUR):</strong>
        Simulasi ini mengadopsi struktur resmi seleksi perangkat desa Kabupaten Tuban: Ujian Tertulis terdiri atas <strong>5 Bidang Materi berurutan (masing-masing 25 soal, 30 menit per bidang, total 125 soal)</strong> dan <strong>Praktik Komputer sebanyak 10 butir</strong>. Penilaian akhir menggabungkan Ujian Tertulis (maksimal 87,5 poin) dan Praktik Komputer (maksimal 12,5 poin) dengan skor maksimal 100 poin. <em>Aplikasi berjalan 100% lokal & privat di browser tanpa jaringan internet.</em>
      </div>
    </div>

    <!-- ======================================================================
         VIEW 1: BERANDA / LANDING PAGE SEDERHANA (SIMPLE LANDING VIEW)
         ====================================================================== -->
    <section id="viewHome">
      <div class="landing-hero-card">
        <!-- Top Badges / Chips -->
        <div class="landing-chip-row">
          <span class="landing-chip landing-chip-gold">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
            Format Resmi Kab. Tuban
          </span>
          <span class="landing-chip">5 Bidang Tertulis (125 Soal)</span>
          <span class="landing-chip">10 Butir Praktik Office</span>
          <span class="landing-chip">Skor Maks. 100,0</span>
          <span class="landing-chip landing-chip-green">100% Offline &amp; Privat</span>
        </div>

        <h2 class="landing-headline">Simulasi Ujian Seleksi Perangkat Desa</h2>
        <p class="landing-desc">
          Computer Assisted Test (CAT) terstandar untuk persiapan seleksi calon Sekretaris Desa, Kaur, Kasi, dan Kepala Dusun di Kabupaten Tuban. Evaluasi otomatis 5 bidang materi berurutan dan 10 butir praktik komputer perkantoran desa.
        </p>

        <!-- Formulir Peserta Sesuai Gambar 2 -->
        <div class="candidate-spec-card">
          <div class="candidate-form-row">
            <div class="candidate-form-col">
              <label for="inputCandidateName" class="spec-label">Nama Lengkap Peserta (Opsional):</label>
              <input type="text" id="inputCandidateName" class="spec-input" placeholder="Contoh: Muhammad Ilham">
            </div>
            <div class="candidate-form-col">
              <label for="inputCandidateVillage" class="spec-label">Desa &amp; Kecamatan (Opsional):</label>
              <input type="text" id="inputCandidateVillage" class="spec-input" placeholder="Contoh: Desa Sukamaju, Kec. Rengel">
            </div>
            <div class="candidate-form-col">
              <label for="selectRegion" class="spec-label">Fokus Regulasi &amp; Acuan Daerah:</label>
              <select id="selectRegion" class="spec-select" onchange="CBTApp.handleRegionChange()">
                <option value="tuban" selected>Kabupaten Tuban (Perda 2/2016 jo 16/2021 &amp; Perbup 11/2022)</option>
                <option value="nasional">Standar Nasional (UU 6/2014 jo. UU 3/2024)</option>
              </select>
            </div>
          </div>
        </div>

        <!-- Tombol Aksi Utama Sesuai Permintaan Pengguna -->
        <div class="landing-cta-row">
          <button class="btn btn-landing-exam" onclick="CBTApp.confirmStartExam()" id="btnStartExamMain">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
            <span>Mulai Ujian</span>
          </button>
          <button class="btn btn-landing-practice" onclick="CBTApp.navigate('practice-config')" id="btnStartPracticeMain">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>
            <span>Mulai Mode Latihan</span>
          </button>
        </div>

        <!-- Hint Menuju Halaman Bantuan -->
        <div class="landing-footer-hint">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color:var(--accent-gold-400); flex-shrink:0;"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
          <span>Memerlukan panduan teknis, rincian materi 5 bidang, atau format penilaian? <a href="javascript:void(0)" onclick="CBTApp.navigate('help')">Pelajari di Halaman Bantuan (Help) →</a></span>
        </div>
      </div>
    </section>


    <!-- ======================================================================
         VIEW 2: KONFIGURASI LATIHAN MANDIRI (PRACTICE CONFIG VIEW)
         ====================================================================== -->
    <section id="viewPracticeConfig" style="display:none;">
      <div class="cbt-card" style="max-width:700px; margin:0 auto;">
        <h2 style="font-size:1.35rem; font-weight:800; color:var(--primary-900); margin-bottom:0.5rem;">Pengaturan Mode Latihan Belajar</h2>
        <p style="font-size:0.88rem; color:var(--slate-600); margin-bottom:1.5rem;">Pada mode latihan mandiri, Anda dapat memilih materi spesifik dan kunci jawaban serta pembahasan mendalam akan langsung tampil setelah Anda memilih jawaban.</p>

        <div class="form-group" style="margin-bottom:1.25rem;">
          <label for="practiceCategorySelect" style="color:var(--slate-800);">Pilih Kategori Materi:</label>
          <select id="practiceCategorySelect" class="form-control">
            <option value="all">Semua Materi (Database 1.000 Soal Lengkap)</option>
            <!-- Populated via JS -->
          </select>
        </div>

        <div class="form-group" style="margin-bottom:1.25rem;">
          <label for="practiceCountSelect" style="color:var(--slate-800);">Jumlah Soal Latihan:</label>
          <select id="practiceCountSelect" class="form-control">
            <option value="10">10 Soal (Latihan Kilat)</option>
            <option value="25" selected>25 Soal (Standar 1 Bidang)</option>
            <option value="50">50 Soal (Pendalaman)</option>
            <option value="100">100 Soal (Simulasi Campuran)</option>
            <option value="125">125 Soal (Simulasi Lengkap)</option>
          </select>
        </div>

        <div class="form-group" style="margin-bottom:1.25rem;">
          <label for="practiceShuffleSelect" style="color:var(--slate-800);">Pengacakan Soal & Pilihan:</label>
          <select id="practiceShuffleSelect" class="form-control">
            <option value="yes" selected>Acak Soal dan Acak Opsi Jawaban</option>
            <option value="no">Urut Sesuai Database</option>
          </select>
        </div>

        <div class="form-group" style="margin-bottom:1.75rem;">
          <label style="color:var(--slate-800);">Timer Simulasi:</label>
          <div style="display:flex; align-items:center; gap:0.75rem; margin-top:0.35rem;">
            <input type="checkbox" id="practiceTimerToggle" style="width:18px; height:18px;">
            <span style="font-size:0.88rem; color:var(--slate-700);">Aktifkan batas waktu simulasi (30 menit per 25 soal)</span>
          </div>
        </div>

        <div style="display:flex; justify-content:space-between; gap:1rem;">
          <button class="btn btn-outline" onclick="CBTApp.navigate('home')">Kembali ke Beranda</button>
          <button class="btn btn-primary" onclick="CBTApp.startPracticeSession()">Mulai Latihan Mandiri</button>
        </div>
      </div>
    </section>

    <!-- ======================================================================
         VIEW 3: UJIAN TERTULIS 5 BIDANG (EXAM VIEW)
         ====================================================================== -->
    <section id="viewExam" style="display:none;">
      <!-- Bidang Stepper Progression -->
      <div class="bidang-stepper-wrap no-print">
        <div class="bidang-stepper-title">
          <h3>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 11l3 3L22 4"></path><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"></path></svg>
            <span id="stepperActiveLabel">Tahapan Ujian Tertulis: Bidang 1 dari 5</span>
          </h3>
          <span id="stepperStatusSummary">Ujian Tertulis Format Kabupaten Tuban</span>
        </div>
        <div class="bidang-stepper" id="bidangStepperList">
          <!-- Populated via JS -->
        </div>
      </div>

      <!-- Top Status Bar: Candidate Info & Section Timer -->
      <div class="exam-top-bar">
        <div class="candidate-info-chip">
          <div class="candidate-avatar" id="avatarInitial">P</div>
          <div class="candidate-text">
            <h4 id="barCandidateName">Nama Peserta</h4>
            <p><span id="barRegionBadge">Kabupaten Tuban</span> • <span id="barModeBadge" style="font-weight:700; color:var(--primary-700);">Bidang 1: Agama (25 Soal)</span></p>
          </div>
        </div>

        <div class="timers-wrapper">
          <div class="timer-badge section-timer" id="boxSectionTimer" title="Waktu tersisa untuk bidang ini">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
            <span id="labelTimerType">WAKTU BIDANG:</span>
            <span id="displaySectionTimer" style="font-size:1.15rem; font-weight:900;">30:00</span>
          </div>
        </div>
      </div>

      <!-- Main CBT Layout -->
      <div class="cbt-exam-layout">
        <div class="question-card">
          <div>
            <div class="question-meta-row">
              <div class="question-number-badge" id="qDisplayIndex">
                Soal Nomor 1 dari 25
              </div>
              <div class="badges-group">
                <span class="badge-pill badge-cat" id="qCategoryPill">Agama</span>
                <span class="badge-pill badge-diff-sedang" id="qDifficultyPill">SEDANG</span>
                <span class="badge-pill" id="qSourceTypePill" style="display:none; background:var(--slate-200); color:var(--slate-700);">Latihan Buatan</span>
              </div>
            </div>

            <!-- Question Body -->
            <div class="question-text" id="qQuestionText">
              Memuat pertanyaan...
            </div>

            <!-- Options List (A, B, C, D) -->
            <div class="options-list" id="qOptionsList">
              <!-- Rendered via JS -->
            </div>

            <!-- Instant Feedback (Practice Mode Only) -->
            <div id="practiceFeedbackBox" class="explanation-box" style="display:none;">
              <div class="explanation-title" id="practiceFeedbackTitle">
                Pembahasan & Kunci Jawaban
              </div>
              <div class="explanation-content" id="practiceFeedbackContent"></div>
              <div class="explanation-source" id="practiceFeedbackSource"></div>
            </div>
          </div>

          <!-- CBT Navigation Action Bar -->
          <div class="cbt-action-bar">
            <div class="cbt-action-left">
              <button class="btn btn-outline" id="btnPrevQuestion" onclick="CBTApp.prevQuestion()">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"></polyline></svg>
                Sebelumnya
              </button>
              <button class="btn btn-outline" id="btnNextQuestion" onclick="CBTApp.skipOrNextQuestion()">
                Berikutnya / Lewati
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
              </button>
              <button class="btn btn-outline btn-sm" id="btnFlagQuestion" onclick="CBTApp.toggleFlagCurrentQuestion()" title="Tandai ragu-ragu (Shortcut: R)">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"></path><line x1="4" y1="22" x2="4" y2="15"></line></svg>
                <span id="btnFlagLabel">Ragu-ragu (R)</span>
              </button>
            </div>

            <div class="cbt-action-right">
              <button class="btn btn-danger" onclick="CBTApp.confirmFinishSection()">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                <span id="btnFinishSectionLabel">Selesaikan Bidang Ini</span>
              </button>
            </div>
          </div>
        </div>

        <!-- 25-Question Palette Sidebar -->
        <aside class="palette-card" id="paletteDrawer">
          <div class="palette-header">
            <h3 id="paletteTitleLabel">Nomor Soal (25)</h3>
            <div id="paletteAnswerCount" style="font-size:0.8rem; font-weight:700; color:var(--primary-700);">0 / 25 Terjawab</div>
          </div>

          <div class="palette-filter-bar">
            <button class="palette-filter-btn active" id="pFilterAll" onclick="CBTApp.setPaletteFilter('all')">Semua</button>
            <button class="palette-filter-btn" id="pFilterDone" onclick="CBTApp.setPaletteFilter('done')">Dijawab</button>
            <button class="palette-filter-btn" id="pFilterFlag" onclick="CBTApp.setPaletteFilter('flag')">Ragu</button>
            <button class="palette-filter-btn" id="pFilterEmpty" onclick="CBTApp.setPaletteFilter('empty')">Belum</button>
          </div>

          <div class="palette-legend">
            <div class="legend-item"><span class="legend-dot" style="background:var(--emerald-600);"></span> Terjawab</div>
            <div class="legend-item"><span class="legend-dot" style="background:var(--accent-gold-500);"></span> Ragu-ragu</div>
            <div class="legend-item"><span class="legend-dot" style="background:var(--white); border:2px solid var(--primary-600);"></span> Aktif</div>
            <div class="legend-item"><span class="legend-dot" style="background:var(--white); border:1px solid var(--slate-300);"></span> Belum</div>
          </div>

          <div class="grid-palette" id="gridQuestionButtons">
            <!-- 25 Buttons rendered via JS -->
          </div>
        </aside>
      </div>
    </section>

    <!-- ======================================================================
         VIEW 4: PRAKTIK KOMPUTER 10 BUTIR (PRACTICAL VIEW - DUA MODE)
         ====================================================================== -->
    <section id="viewPractical" style="display:none;">
      <!-- Stepper / Status Bar -->
      <div class="bidang-stepper-wrap no-print">
        <div class="bidang-stepper-title">
          <h3 style="color:var(--emerald-400);">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>
            Tahap 6: Ujian Praktik Komputer (10 Butir Tugas Nyata)
          </h3>
          <div style="display:flex; align-items:center; gap:0.75rem; flex-wrap:wrap;">
            <div style="background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.2); padding:0.35rem 0.75rem; border-radius:var(--radius-sm); font-size:0.85rem; color:#fff;">
              ⏱️ Waktu Praktik: <strong id="practicalTimerDisplay" style="color:var(--accent-gold-400); font-variant-numeric:tabular-nums;">45:00</strong>
            </div>
            <button class="btn btn-outline btn-sm" onclick="CBTApp.openPracticalDurationModal()" style="border-color:rgba(255,255,255,0.4); color:#fff; font-size:0.78rem;">
              ⚙️ Atur Durasi
            </button>
            <span style="color:var(--white); font-weight:700;">Maksimal: 12,50 Poin (1,25 / Butir)</span>
          </div>
        </div>
        <p style="font-size:0.82rem; color:var(--slate-200); margin-top:0.35rem;">
          Ujian tertulis telah selesai terkunci. Selesaikan 10 butir tugas praktik komputer di bawah ini. Anda dapat menggunakan <strong>Microsoft Office asli di komputer Anda</strong> (unduh bahan & unggah berkas) atau <strong>Simulasi Browser interaktif</strong>.
        </p>
      </div>

      <!-- Mode Switcher Tabs -->
      <div class="mode-switch-bar no-print">
        <button class="mode-switch-btn active office" id="btnModeOffice" onclick="CBTApp.setPracticalMode('office')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
          Mode 1 — Microsoft Office Asli (Unduh & Unggah Berkas)
        </button>
        <button class="mode-switch-btn sim" id="btnModeSim" onclick="CBTApp.setPracticalMode('sim')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>
          Mode 2 — Simulasi Interaktif di Browser (Tanpa MS Office)
        </button>
      </div>

      <!-- Mode Notice Banner -->
      <div id="practicalModeNotice" style="background:#eff6ff; border:1px solid #bfdbfe; color:#1e40af; padding:0.75rem 1rem; border-radius:var(--radius-sm); font-size:0.85rem; margin-bottom:1.25rem;">
        <!-- Injected via JS -->
      </div>

      <div class="practical-workspace">
        <div class="task-card">
          <div class="task-header">
            <div>
              <span class="badge-pill badge-cat" id="taskCategoryBadge">Pengolah Kata</span>
              <h3 id="taskTitleHeading" style="margin-top:0.4rem;">Tugas 1: Word — Mengetik Dokumen Sesuai Teks Sumber</h3>
            </div>
            <div style="text-align:right;">
              <span class="badge-pill badge-verified" id="taskScoreBadge">Skor: 0.00 / 1.25</span>
              <div id="taskStatusBadgeWrap" style="margin-top:4px;">
                <span class="badge-pill" id="taskStatusPill" style="background:var(--slate-200); color:var(--slate-700); font-size:0.75rem;">Belum Dikerjakan</span>
              </div>
            </div>
          </div>

          <!-- Scenario & Instructions -->
          <div class="task-scenario-box">
            <strong>Skenario Administrasi Desa:</strong>
            <p id="taskScenarioText" style="margin-top:0.25rem;">Memuat skenario tugas...</p>
          </div>

          <div class="task-rubric-box">
            <strong>Instruksi & Kriteria Penilaian:</strong>
            <p id="taskInstructionText" style="margin-top:0.25rem;">Memuat instruksi pengerjaan...</p>
            <div id="taskRubricDetailContainer" style="margin-top:0.5rem;">
              <!-- Rubric breakdown rendered via JS -->
            </div>
          </div>

          <!-- =================================================================
               WORKSPACE MODE 1: MICROSOFT OFFICE ASLI (UNDUH & UNGGAH BERKAS)
               ================================================================= -->
          <div id="workspaceOfficeMode" style="display:block;">
            <div class="office-flow-card">
              <div class="office-flow-steps">
                <div class="office-flow-step">
                  <strong>Langkah 1: Unduh</strong>
                  Unduh berkas bahan latihan yang telah disiapkan sistem.
                </div>
                <div class="office-flow-step">
                  <strong>Langkah 2: Buka & Kerjakan</strong>
                  Buka di Microsoft Word / Excel / PowerPoint di komputer Anda.
                </div>
                <div class="office-flow-step">
                  <strong>Langkah 3: Simpan Sesuai Nama</strong>
                  Simpan file dengan format nama berkas yang telah ditentukan.
                </div>
                <div class="office-flow-step">
                  <strong>Langkah 4: Unggah & Nilai</strong>
                  Unggah berkas untuk verifikasi otomatis dan penilaian rubrik.
                </div>
              </div>

              <!-- Download Box -->
              <div class="office-download-box">
                <div>
                  <div style="font-weight:700; color:var(--primary-900);" id="officeStarterFileTitle">Bahan Latihan: Dokumen Template</div>
                  <div style="font-size:0.8rem; color:var(--slate-600);" id="officeStarterFileDesc">Unduh file bahan untuk dikerjakan di Microsoft Office lokal.</div>
                </div>
                <div style="display:flex; gap:0.5rem; flex-wrap:wrap;">
                  <button class="btn btn-primary btn-sm" onclick="CBTApp.downloadCurrentStarterFile()">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                    Unduh Berkas Latihan
                  </button>
                  <button class="btn btn-outline btn-sm" onclick="CBTApp.copyStarterContentText()">
                    Salin Teks Sumber
                  </button>
                </div>
              </div>

              <!-- Expected File Name Notice -->
              <div style="font-size:0.85rem; color:var(--slate-700); margin-bottom:0.75rem;">
                📌 <strong>Nama Berkas yang Diharapkan:</strong> <code class="inline-code" id="officeExpectedFileName">Tugas01_Ketik_Naskah.docx</code>
              </div>

              <!-- Upload Dropzone -->
              <div class="office-upload-box" onclick="document.getElementById('officeFileInput').click()">
                <input type="file" id="officeFileInput" style="display:none;" onchange="CBTApp.handleOfficeFileUpload(event)">
                <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="var(--primary-600)" stroke-width="2" style="margin-bottom:0.5rem;"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="17 8 12 3 7 8"></polyline><line x1="12" y1="3" x2="12" y2="15"></line></svg>
                <div style="font-weight:700; color:var(--primary-900);">Klik untuk Memilih File atau Seret File ke Sini</div>
                <div style="font-size:0.8rem; color:var(--slate-500); margin-top:0.25rem;">Mendukung format .docx, .xlsx, .pptx, .pdf, .zip, .txt</div>
              </div>

              <!-- Uploaded File Info Card -->
              <div id="officeUploadedFileCard" style="display:none; background:var(--white); border:1px solid #cbd5e1; border-radius:var(--radius-sm); padding:0.85rem; margin-bottom:1rem;">
                <!-- Injected via JS -->
              </div>

              <!-- Rubric Checklist for Examiner / Candidate Verification -->
              <div id="officeRubricChecklistArea" style="display:none; background:var(--white); border:1px solid var(--slate-200); border-radius:var(--radius-sm); padding:1rem; margin-bottom:1rem;">
                <div style="font-weight:800; color:var(--primary-900); margin-bottom:0.5rem; font-size:0.9rem;">Lembar Verifikasi Kriteria Penilaian:</div>
                <div id="officeRubricChecklistItems"></div>
              </div>

              <div style="display:flex; justify-content:flex-end;">
                <button class="btn btn-emerald" onclick="CBTApp.evaluateOfficeUpload()">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                  Simpan & Periksa Berkas Unggahan
                </button>
              </div>
            </div>
          </div>

          <!-- =================================================================
               WORKSPACE MODE 2: SIMULASI INTERAKTIF DI BROWSER
               ================================================================= -->
          <div id="workspaceBrowserSimMode" style="display:none;">
            <div class="browser-sim-badge">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
              Simulasi Browser Interaktif (Bukan Microsoft Office Asli)
            </div>

            <!-- Interactive Simulator Area -->
            <div class="interactive-simulator-area" id="taskSimulatorContainer">
              <!-- Dynamically injected per task -->
            </div>

            <div style="display:flex; justify-content:flex-end; margin-bottom:1.25rem;">
              <button class="btn btn-emerald" onclick="CBTApp.evaluateBrowserSimTask()">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                Uji & Simpan Hasil Simulasi Browser (Maks 1,25)
              </button>
            </div>
          </div>

          <!-- Test & Evaluation Result Feedback Box -->
          <div id="taskTestResultBox" style="display:none; padding:1rem; border-radius:var(--radius-md); margin-bottom:1.25rem;">
            <!-- Injected via JS -->
          </div>

          <!-- Task Action Buttons -->
          <div class="cbt-action-bar">
            <div class="cbt-action-left">
              <button class="btn btn-outline" id="btnPrevPracticalTask" onclick="CBTApp.prevPracticalTask()">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"></polyline></svg>
                Tugas Sebelumnya
              </button>
              <button class="btn btn-outline" id="btnNextPracticalTask" onclick="CBTApp.nextPracticalTask()">
                Tugas Berikutnya
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
              </button>
            </div>

            <div class="cbt-action-right">
              <span id="taskAutoSaveIndicator" style="font-size:0.8rem; color:var(--slate-500); margin-right:0.5rem;">Progres tersimpan otomatis</span>
            </div>
          </div>
        </div>

        <!-- 10-Task Palette Sidebar -->
        <aside class="practical-palette-card">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem; padding-bottom:0.5rem; border-bottom:1px solid var(--slate-100);">
            <h3 style="font-size:0.95rem; font-weight:800; color:var(--primary-900);">Daftar 10 Tugas Praktik</h3>
            <span id="practicalDoneCount" style="font-size:0.8rem; font-weight:700; color:var(--emerald-600);">0 / 10 Diserahkan</span>
          </div>

          <div style="margin-bottom:1rem;">
            <div style="font-size:0.8rem; color:var(--slate-600); margin-bottom:0.4rem;">Total Skor Praktik Terkumpul:</div>
            <div id="practicalTotalScoreBadge" style="font-size:1.4rem; font-weight:900; color:var(--primary-700);">0.00 / 12.50</div>
          </div>

          <div id="practicalTasksList">
            <!-- 10 Task buttons rendered via JS -->
          </div>

          <div style="margin-top:1.25rem; padding-top:1rem; border-top:1px solid var(--slate-200);">
            <button class="btn btn-danger" style="width:100%; justify-content:center;" onclick="CBTApp.confirmFinishPractical()">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
              Selesaikan Praktik & Lihat Hasil
            </button>
          </div>
        </aside>
      </div>
    </section>

    <!-- ======================================================================
         VIEW 5: HASIL AKHIR & PEMBAHASAN LENGKAP (RESULTS VIEW)
         ====================================================================== -->
    <section id="viewResults" style="display:none;">
      <!-- Results Hero Card -->
      <div class="results-hero">
        <div class="results-hero-grid">
          <div>
            <div class="hero-badge-row" style="justify-content:flex-start;">
              <span class="badge-pill badge-cat" id="resBadgeMode">Format Ujian Kabupaten Tuban</span>
              <span class="badge-pill badge-diff-mudah" id="resBadgeRegion">Kabupaten Tuban</span>
              <span class="badge-pill" style="background:rgba(255,255,255,0.2); color:#fff;" id="resDateBadge">19 Oktober 2026</span>
            </div>
            <h2 style="font-size:1.8rem; font-weight:800; margin-bottom:0.25rem;" id="resCandidateHeading">Hasil Simulasi Ujian: Peserta</h2>
            <p style="font-size:0.92rem; opacity:0.9;" id="resCandidateSubheading">Desa Sukamaju, Kec. Rengel • Pelaksanaan Lengkap</p>

            <div class="results-stats-row">
              <div class="stat-box">
                <div style="font-size:0.75rem; color:var(--slate-300);">Soal Tertulis</div>
                <div class="stat-box-num" id="resTotalSoal">125</div>
              </div>
              <div class="stat-box">
                <div style="font-size:0.75rem; color:var(--slate-300);">Tertulis Benar</div>
                <div class="stat-box-num benar" id="resCountBenar">0</div>
              </div>
              <div class="stat-box">
                <div style="font-size:0.75rem; color:var(--slate-300);">Tertulis Salah</div>
                <div class="stat-box-num salah" id="resCountSalah">0</div>
              </div>
              <div class="stat-box">
                <div style="font-size:0.75rem; color:var(--slate-300);">Tertulis Kosong</div>
                <div class="stat-box-num kosong" id="resCountKosong">0</div>
              </div>
              <div class="stat-box">
                <div style="font-size:0.75rem; color:var(--slate-300);">Waktu Tertulis</div>
                <div class="stat-box-num" id="resTimeUsed" style="font-size:1.05rem; padding-top:4px;">00:00</div>
              </div>
            </div>
          </div>

          <div class="results-score-badge">
            <div style="font-size:0.75rem; font-weight:700; letter-spacing:0.5px; color:var(--slate-300);">NILAI AKHIR SIMULASI</div>
            <div class="score-value" id="resScoreValue">0.00</div>
            <div style="font-size:0.85rem; color:var(--slate-200); font-weight:600;">Skala Maksimal 100,00 Poin</div>
            <div id="resPracticalIncompleteNotice" style="display:none; font-size:0.75rem; background:rgba(239,68,68,0.25); border:1px solid #ef4444; color:#fca5a5; padding:4px 6px; border-radius:4px; margin-top:8px;">
              ⚠️ Penilaian Praktik Belum Lengkap
            </div>
          </div>
        </div>
      </div>

      <!-- Action Toolbar -->
      <div style="display:flex; justify-content:space-between; align-items:center; gap:0.75rem; margin-bottom:1.5rem; flex-wrap:wrap;" class="no-print">
        <div style="display:flex; gap:0.5rem; flex-wrap:wrap;">
          <button class="btn btn-emerald btn-sm" id="btnUnlockReview" onclick="CBTApp.scrollToReviewSection()">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>
            Buka Pembahasan Lengkap Seluruh Soal
          </button>
          <button class="btn btn-outline btn-sm" onclick="CBTApp.navigate('glossary')">
            Glosarium Terkait
          </button>
        </div>
        <div style="display:flex; gap:0.5rem; flex-wrap:wrap;">
          <button class="btn btn-outline btn-sm" onclick="CBTApp.exportCSV()">Ekspor CSV</button>
          <button class="btn btn-outline btn-sm" onclick="CBTApp.exportJSON()">Ekspor JSON</button>
          <button class="btn btn-primary btn-sm" onclick="window.print()">Cetak Laporan</button>
          <button class="btn btn-outline btn-sm" onclick="CBTApp.navigate('home')">Kembali ke Beranda</button>
        </div>
      </div>

      <!-- Official Score Breakdown: Written (87.5) + Practical (12.5) = Final (100.0) -->
      <div class="cbt-card">
        <h3 style="font-size:1.25rem; font-weight:800; color:var(--primary-900); margin-bottom:0.5rem;">Rekapitulasi Penilaian Resmi (Format Kabupaten Tuban)</h3>
        <p style="font-size:0.88rem; color:var(--slate-600); margin-bottom:1.25rem;">Nilai akhir dihitung murni dari: <code>Nilai Akhir = Nilai Ujian Tertulis (Benar × 0,7) + Nilai Praktik Komputer (10 Butir)</code> tanpa bobot persentase tambahan.</p>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:1rem; margin-bottom:1.25rem;">
          <div style="background:var(--slate-50); border:1px solid var(--slate-300); border-radius:var(--radius-md); padding:1.25rem;">
            <div style="font-size:0.8rem; font-weight:700; color:var(--primary-700);">KOMPONEN 1: UJIAN TERTULIS (125 SOAL)</div>
            <div style="font-size:1.8rem; font-weight:900; color:var(--primary-900); margin:0.35rem 0;" id="resScoreWrittenTotal">0.00 / 87.50</div>
            <p style="font-size:0.82rem; color:var(--slate-600);" id="resFormulaWrittenDesc">Rumus: 0 Jawaban Benar × 0,7 Poin = 0,00 Poin</p>
          </div>

          <div style="background:var(--slate-50); border:1px solid var(--slate-300); border-radius:var(--radius-md); padding:1.25rem;">
            <div style="font-size:0.8rem; font-weight:700; color:var(--emerald-700);">KOMPONEN 2: PRAKTIK KOMPUTER (10 BUTIR)</div>
            <div style="font-size:1.8rem; font-weight:900; color:var(--emerald-800); margin:0.35rem 0;" id="resScorePracticalTotal">0.00 / 12.50</div>
            <p style="font-size:0.82rem; color:var(--slate-600);" id="resFormulaPracticalDesc">Total skor dari 10 butir tugas simulasi komputer (maks. 1,25 / butir)</p>
          </div>

          <div style="background:linear-gradient(135deg, var(--primary-900), var(--primary-800)); color:white; border-radius:var(--radius-md); padding:1.25rem;">
            <div style="font-size:0.8rem; font-weight:700; color:var(--accent-gold-400);">NILAI AKHIR GABUNGAN</div>
            <div style="font-size:2rem; font-weight:900; color:var(--accent-gold-400); margin:0.25rem 0;" id="resScoreFinalTotal">0.00 / 100.00</div>
            <p style="font-size:0.82rem; color:var(--slate-200);">Skor Tertulis + Skor Praktik Komputer</p>
          </div>
        </div>
      </div>

      <!-- Breakdown 5 Bidang Tertulis -->
      <div class="cbt-card">
        <h3 style="font-size:1.15rem; font-weight:800; color:var(--primary-900); margin-bottom:1rem;">Rincian Nilai 5 Bidang Ujian Tertulis (@ 25 Soal, Maks. 17,50 Poin / Bidang)</h3>
        <div class="bidang-results-grid" id="bidangResultsGridContainer">
          <!-- 5 Bidang Cards Rendered via JS -->
        </div>
      </div>

      <!-- Breakdown 10 Butir Praktik Komputer -->
      <div class="cbt-card">
        <h3 style="font-size:1.15rem; font-weight:800; color:var(--primary-900); margin-bottom:0.75rem;">Rincian Hasil 10 Butir Praktik Komputer (@ Maks. 1,25 Poin)</h3>
        <div class="table-container">
          <table class="cbt-table">
            <thead>
              <tr>
                <th style="width:40px; text-align:center;">No</th>
                <th>Tugas Praktik</th>
                <th style="width:180px;">Kategori & Mode</th>
                <th style="text-align:center;">Skor Diperoleh</th>
                <th style="text-align:center;">Skor Maksimal</th>
                <th>Status Penilaian & Catatan</th>
              </tr>
            </thead>
            <tbody id="resultsPracticalTableBody">
              <!-- Rendered via JS -->
            </tbody>
          </table>
        </div>
      </div>

      <!-- Section: Analisis Kelemahan & Rekomendasi Belajar -->
      <div class="cbt-card">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem; margin-bottom:1rem;">
          <div>
            <h3 style="font-size:1.2rem; font-weight:800; color:var(--primary-900);">Analisis Kelemahan & Rekomendasi Pembelajaran</h3>
            <p style="font-size:0.85rem; color:var(--slate-600);">Diurutkan berdasarkan materi yang memerlukan pendalaman lebih lanjut.</p>
          </div>
          <span class="badge-pill badge-cat">Berdasarkan Hasil Ujian</span>
        </div>

        <div id="weaknessListContainer">
          <!-- Injected via JS -->
        </div>
      </div>

      <!-- Review Section for all 125 Written Questions (Unlocked After Exam Selesai) -->
      <div class="cbt-card" id="fullReviewContainerSection">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.75rem; margin-bottom:1.25rem;">
          <div>
            <h3 style="font-size:1.2rem; font-weight:800; color:var(--primary-900);">Pembahasan & Kunci Jawaban Resmi 125 Soal Tertulis</h3>
            <p style="font-size:0.85rem; color:var(--slate-600);">Pelajari rujukan pasal perundang-undangan dan penjelasan komprehensif setiap butir soal.</p>
          </div>

          <div style="display:flex; gap:0.5rem; align-items:center;">
            <input type="text" id="reviewSearchInput" class="form-control" placeholder="Cari pembahasan / pasal..." oninput="CBTApp.renderActiveReviewTab()" style="max-width:240px; padding:0.4rem 0.65rem; font-size:0.85rem;">
          </div>
        </div>

        <!-- Filter tabs for 125 questions -->
        <div style="display:flex; gap:0.35rem; flex-wrap:wrap; margin-bottom:1.25rem;">
          <button class="btn btn-outline btn-sm active" id="tabRevWrong" onclick="CBTApp.setReviewTab('wrong')">Jawaban Salah</button>
          <button class="btn btn-outline btn-sm" id="tabRevEmpty" onclick="CBTApp.setReviewTab('empty')">Soal Kosong</button>
          <button class="btn btn-outline btn-sm" id="tabRevCorrect" onclick="CBTApp.setReviewTab('correct')">Jawaban Benar</button>
          <button class="btn btn-outline btn-sm" id="tabRevAll" onclick="CBTApp.setReviewTab('all')">Semua 125 Soal</button>
          <button class="btn btn-outline btn-sm" id="tabRevB1" onclick="CBTApp.setReviewTab('b1')">Bidang 1 (Agama)</button>
          <button class="btn btn-outline btn-sm" id="tabRevB2" onclick="CBTApp.setReviewTab('b2')">Bidang 2 (Pemdes)</button>
          <button class="btn btn-outline btn-sm" id="tabRevB3" onclick="CBTApp.setReviewTab('b3')">Bidang 3 (B. Indo)</button>
          <button class="btn btn-outline btn-sm" id="tabRevB4" onclick="CBTApp.setReviewTab('b4')">Bidang 4 (P. Umum)</button>
          <button class="btn btn-outline btn-sm" id="tabRevB5" onclick="CBTApp.setReviewTab('b5')">Bidang 5 (Komputer)</button>
        </div>

        <div id="evalReviewContainer">
          <!-- Rendered via JS -->
        </div>
      </div>

      <!-- Print-Only Certificate & Copyright Footer -->
      <div class="print-only-footer">
        <div>
          <strong>Simulasi CBT Seleksi Perangkat Desa Kabupaten Tuban</strong><br>
          <span style="font-size:0.7rem; color:#64748b;">Standar Resmi 125 Soal Tertulis (87,5 Poin) + 10 Praktik Komputer (12,5 Poin) = 100,00 Poin</span>
        </div>
        <div style="text-align:right;">
          <span>Versi Aplikasi: <strong>v5.1.0</strong></span><br>
          <span style="color:#0f172a; font-weight:700;">Copyright by fusionproject.id</span>
        </div>
      </div>
    </section>

    <!-- ======================================================================
         VIEW 6: GLOSARIUM ISTILAH DESA (GLOSSARY VIEW)
         ====================================================================== -->
    <section id="viewGlossary" style="display:none;">
      <div class="cbt-card">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem; margin-bottom:1.25rem;">
          <div>
            <h2 style="font-size:1.35rem; font-weight:800; color:var(--primary-900);">Glosarium Istilah & Regulasi Pemerintahan Desa</h2>
            <p style="font-size:0.88rem; color:var(--slate-600);">Kumpulan 36 istilah, singkatan, dan landasan hukum resmi yang sering keluar dalam seleksi perangkat desa.</p>
          </div>
          <button class="btn btn-outline btn-sm" onclick="CBTApp.navigate('home')">Kembali ke Beranda</button>
        </div>

        <div class="glossary-search-box" style="display:flex; gap:0.75rem; flex-wrap:wrap; margin-bottom:1.25rem;">
          <input type="text" id="glossarySearchInput" class="form-control" placeholder="Cari istilah, nama kepanjangan, atau kata kunci (misal: Siltap, APB Desa, BPD, Silpa)..." oninput="CBTApp.renderGlossary()" style="flex:1; min-width:240px;">
          <select id="glossaryCategorySelect" class="form-control" onchange="CBTApp.renderGlossary()" style="max-width:240px;">
            <option value="all">Semua Kategori</option>
            <option value="Keuangan & APB Desa">Keuangan & APB Desa</option>
            <option value="Perencanaan & Pembangunan">Perencanaan & Pembangunan</option>
            <option value="Kelembagaan & Musyawarah">Kelembagaan & Musyawarah</option>
            <option value="Pemerintahan & Organisasi">Pemerintahan & Organisasi</option>
            <option value="Regulasi & Tata Kelola">Regulasi & Tata Kelola</option>
            <option value="Perekonomian & BUMDes">Perekonomian & BUMDes</option>
          </select>
        </div>

        <div class="glossary-grid" id="glossaryListContainer" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(300px, 1fr)); gap:1rem;">
          <!-- Populated via JS -->
        </div>
      </div>
    </section>

    <!-- ======================================================================
         VIEW 7: RIWAYAT NILAI & GRAFIK TREN (HISTORY VIEW)
         ====================================================================== -->
    <section id="viewHistory" style="display:none;">
      <div class="cbt-card">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem; margin-bottom:1rem;">
          <div>
            <h2 style="font-size:1.35rem; font-weight:800; color:var(--primary-900);">Riwayat & Perkembangan Nilai Simulasi</h2>
            <p style="font-size:0.88rem; color:var(--slate-600);">Pantau tren skor latihan resmi Kabupaten Tuban dan komparasi hasil antar-sesi secara adil.</p>
          </div>
          <div style="display:flex; gap:0.5rem;">
            <button class="btn btn-outline btn-sm" onclick="CBTApp.confirmClearHistory()">Hapus Riwayat</button>
            <button class="btn btn-outline btn-sm" onclick="CBTApp.navigate('home')">Kembali ke Beranda</button>
          </div>
        </div>

        <!-- Disparity / Valid Comparison Banner -->
        <div id="historyComparisonBox">
          <!-- Injected via JS -->
        </div>

        <!-- SVG Line/Bar Chart -->
        <div style="background:var(--slate-50); border:1px solid var(--slate-200); border-radius:var(--radius-md); padding:1rem;">
          <h4 style="font-size:0.95rem; font-weight:800; color:var(--primary-900); margin-bottom:0.5rem;">Grafik Perkembangan Skor Akhir (0 - 100)</h4>
          <div class="chart-container" id="chartContainer" style="width:100%; height:240px;">
            <!-- SVG rendered via JS -->
          </div>
        </div>

        <!-- History Table -->
        <div class="table-container" style="margin-top:1.5rem;">
          <table class="cbt-table">
            <thead>
              <tr>
                <th style="text-align:center;">No</th>
                <th>Tanggal & Waktu</th>
                <th>Peserta</th>
                <th>Format Ujian</th>
                <th style="text-align:center;">Skor Tertulis (87.5)</th>
                <th style="text-align:center;">Skor Praktik (12.5)</th>
                <th style="text-align:center;">Nilai Akhir (100)</th>
                <th>Status Praktik</th>
              </tr>
            </thead>
            <tbody id="historyTableBody">
              <!-- Rendered via JS -->
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- ======================================================================
         VIEW 7: PUSAT BANTUAN & PANDUAN RESMI (HELP VIEW)
         ====================================================================== -->
    <section id="viewHelp" style="display:none;">
      <div class="help-hero-panel">
        <div class="help-header-content">
          <span class="badge-pill badge-cat">Pusat Informasi &amp; Regulasi</span>
          <h2 style="font-size:1.6rem; font-weight:900; color:var(--white); margin:0.4rem 0 0.5rem 0;">Bantuan &amp; Panduan Seleksi Perangkat Desa</h2>
          <p class="lead" style="color:var(--slate-200); font-size:0.95rem; max-width:850px; line-height:1.6;">Panduan lengkap format ujian resmi Kabupaten Tuban, ketentuan 5 bidang materi tertulis berurutan, ujian praktik komputer office, rubrik penilaian, dan rujukan hukum terkini.</p>
        </div>
        <div class="help-quick-nav">
          <a href="#helpSec1" class="help-nav-pill">1. Format 5 Bidang</a>
          <a href="#helpSec2" class="help-nav-pill">2. Tabel Distribusi Soal</a>
          <a href="#helpSec3" class="help-nav-pill">3. Praktik Komputer</a>
          <a href="#helpSec4" class="help-nav-pill">4. Formula Penilaian</a>
          <a href="#helpSec5" class="help-nav-pill">5. FAQ &amp; Tips CBT</a>
          <a href="#helpSec6" class="help-nav-pill">6. Rujukan Hukum</a>
        </div>
      </div>

      <!-- Section 1: Alur & Mekanisme Ujian Tertulis 5 Bidang -->
      <div class="cbt-card" id="helpSec1" style="margin-bottom:1.5rem;">
        <h3 style="font-size:1.15rem; font-weight:800; color:var(--primary-900); margin-bottom:0.75rem;">1. Ketentuan Ujian Tertulis Resmi (5 Bidang Berurutan)</h3>
        <p style="font-size:0.9rem; color:var(--slate-700); line-height:1.6; margin-bottom:1rem;">
          Berdasarkan standar seleksi perangkat desa Kabupaten Tuban (Perbup Tuban No. 11/2022), ujian tertulis diselenggarakan secara terpisah ke dalam 5 seksi bidang materi yang harus diselesaikan bertahap:
        </p>
        <div class="help-step-grid">
          <div class="help-step-card">
            <div class="help-step-num">Bidang 1</div>
            <h4>Agama &amp; Moderasi Beragama</h4>
            <p>25 Soal • 30 Menit. Fiqih jenazah desa, zakat, wakaf, batas usia nikah, moderasi beragama, aparatur bebas risywah, dan sejarah Sunan Bonang Tuban.</p>
          </div>
          <div class="help-step-card">
            <div class="help-step-num">Bidang 2</div>
            <h4>Pemerintahan Desa</h4>
            <p>25 Soal • 30 Menit. UU No. 6/2014 jo. UU No. 3/2024, PP 11/2019 (Siltap), Permendagri 84/2015 (SOTK), Permendagri 20/2018 (APBDes), Perda Tuban No. 2/2016 jo. No. 16/2021.</p>
          </div>
          <div class="help-step-card">
            <div class="help-step-num">Bidang 3</div>
            <h4>Bahasa Indonesia</h4>
            <p>25 Soal • 30 Menit. EYD Edisi V, penulisan naskah dinas resmi surat edaran, undangan, berita acara musdes, dan tata kalimat efektif kedinasan.</p>
          </div>
          <div class="help-step-card">
            <div class="help-step-num">Bidang 4</div>
            <h4>Pengetahuan Umum</h4>
            <p>25 Soal • 30 Menit. Pancasila &amp; Pembukaan UUD 1945, wawasan kebangsaan, matematika numerik anggaran/lahan, logika penalaran, dan sejarah Tuban.</p>
          </div>
          <div class="help-step-card">
            <div class="help-step-num">Bidang 5</div>
            <h4>Pengetahuan Komputer</h4>
            <p>25 Soal • 30 Menit. Aplikasi perkantoran desa (Word, Excel), surat elektronik dinas, pengarsipan digital, dan keamanan data kependudukan (UU PDP No. 27/2022).</p>
          </div>
        </div>
        <div style="background:var(--slate-50); border:1px solid var(--slate-200); border-radius:var(--radius-md); padding:1rem; margin-top:1rem; font-size:0.86rem; color:var(--slate-700);">
          <strong>Aturan Penguncian Sekuensial (Sequential Lock):</strong> Peserta harus menyelesaikan bidang satu per satu. Bidang yang sudah dikunci secara permanen tidak dapat dibuka kembali demi mencegah manipulasi waktu. Jika browser ditutup atau dimuat ulang secara tidak sengaja, sistem akan memulihkan sisa waktu dan jawaban terakhir Anda secara otomatis.
        </div>
      </div>

      <!-- Section 2: Tabel Distribusi Materi (distributionTableBody) -->
      <div class="cbt-card" id="helpSec2" style="margin-bottom:1.5rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem; margin-bottom:1rem;">
          <div>
            <h3 style="font-size:1.15rem; font-weight:800; color:var(--primary-900);">2. Tabel Distribusi Soal &amp; Alokasi Waktu Ujian</h3>
            <p style="font-size:0.85rem; color:var(--slate-600);">Rincian lengkap 125 butir soal ujian tertulis yang diundi secara acak dan bebas duplikasi dari master database 1.000 butir soal (5 bidang terisolasi masing-masing 200 soal).</p>
          </div>
          <span class="badge-pill badge-cat">Total Bank Soal: 1.000 Butir</span>
        </div>

        <div class="table-container">
          <table class="cbt-table">
            <thead>
              <tr>
                <th style="width:40px; text-align:center;">Sesi</th>
                <th>Bidang Materi Ujian</th>
                <th style="text-align:center;">Jumlah Soal</th>
                <th style="text-align:center;">Alokasi Waktu</th>
                <th style="text-align:center;">Bobot Nilai</th>
                <th style="text-align:center;">Tersedia di Bank</th>
                <th>Cakupan &amp; Fokus Kompetensi</th>
              </tr>
            </thead>
            <tbody id="distributionTableBody">
              <!-- Rendered via JS -->
            </tbody>
          </table>
        </div>
      </div>

      <!-- Section 3: Panduan Praktik Komputer (10 Butir Tugas) -->
      <div class="cbt-card" id="helpSec3" style="margin-bottom:1.5rem;">
        <h3 style="font-size:1.15rem; font-weight:800; color:var(--primary-900); margin-bottom:0.75rem;">3. Panduan Ujian Praktik Komputer (10 Butir Tugas Nyata)</h3>
        <p style="font-size:0.9rem; color:var(--slate-700); line-height:1.6; margin-bottom:1rem;">
          Setelah peserta menuntaskan seluruh 5 seksi bidang tertulis, tahapan ujian langsung berlanjut ke Ujian Praktik Komputer. Ujian ini menguji kecakapan menghasilkan naskah dinas desa secara konkret.
        </p>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:1rem; margin-bottom:1rem;">
          <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:var(--radius-md); padding:1rem;">
            <h4 style="font-size:0.95rem; font-weight:800; color:var(--primary-800); margin-bottom:0.5rem;">Mode 1: Microsoft Office Asli (Rekomendasi)</h4>
            <p style="font-size:0.85rem; color:var(--slate-600); line-height:1.5;">Peserta mengunduh naskah sumber, mengerjakan di aplikasi Word, Excel, PowerPoint asli di komputernya, dan mengunggah kembali berkas hasil. Sistem memeriksa struktur OpenXML secara nyata tanpa bantuan server eksternal.</p>
          </div>
          <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:var(--radius-md); padding:1rem;">
            <h4 style="font-size:0.95rem; font-weight:800; color:var(--primary-800); margin-bottom:0.5rem;">Mode 2: Simulasi Browser Interaktif</h4>
            <p style="font-size:0.85rem; color:var(--slate-600); line-height:1.5;">Alternatif bagi peserta yang tidak memiliki MS Office. Disediakan simulasi pengolah kata, spreadsheet live formula (SUM/AVERAGE), dan pembuat slide presentasi langsung di dalam halaman web.</p>
          </div>
        </div>
        <div style="font-size:0.85rem; color:var(--slate-700); line-height:1.6;">
          <strong>Alokasi Skor Praktik:</strong> 10 butir tugas dinilai secara objektif dengan bobot masing-masing <strong>1,25 poin</strong> (total maksimal 12,50 poin). Durasi timer praktik dapat diatur sesuai kebijakan panitia desa (30 menit, 45 menit standar, 60 menit, 90 menit, atau tanpa batas waktu).
        </div>
      </div>

      <!-- Section 4: Formula & Sistem Penilaian Resmi -->
      <div class="cbt-card" id="helpSec4" style="margin-bottom:1.5rem;">
        <h3 style="font-size:1.15rem; font-weight:800; color:var(--primary-900); margin-bottom:0.75rem;">4. Formula &amp; Perhitungan Nilai Akhir</h3>
        <p style="font-size:0.9rem; color:var(--slate-700); line-height:1.6; margin-bottom:1rem;">
          Sesuai regulasi Perda No. 2/2016 jo. No. 16/2021 dan Perbup Tuban No. 11/2022, nilai akhir seleksi perangkat desa menggabungkan dua instrumen ujian dengan total nilai maksimal 100,00 poin:
        </p>
        <div style="background:#eff6ff; border:1px solid #bfdbfe; border-radius:var(--radius-md); padding:1.25rem; margin-bottom:1rem; font-size:0.95rem; color:#1e3a8a;">
          <div style="margin-bottom:0.6rem;"><strong>• Nilai Ujian Tertulis:</strong> <code>Jumlah Jawaban Benar (dari 125 Soal) × 0,7 = Maksimal 87,50 Poin</code></div>
          <div style="margin-bottom:0.6rem;"><strong>• Nilai Praktik Komputer:</strong> <code>Total Skor 10 Butir Tugas Nyata = Maksimal 12,50 Poin</code></div>
          <div style="border-top:1px dashed #93c5fd; padding-top:0.6rem; font-weight:800; color:#1e40af; font-size:1.05rem;">
            <strong>• Nilai Akhir Total:</strong> <code>Nilai Tertulis + Nilai Praktik Komputer = Maksimal 100,00 Poin</code>
          </div>
        </div>
      </div>

      <!-- Section 5: FAQ & Tips Teknis CBT -->
      <div class="cbt-card" id="helpSec5" style="margin-bottom:1.5rem;">
        <h3 style="font-size:1.15rem; font-weight:800; color:var(--primary-900); margin-bottom:0.75rem;">5. Tanya Jawab (FAQ) &amp; Pintasan Keyboard</h3>
        <div style="display:flex; flex-direction:column; gap:0.75rem; font-size:0.88rem;">
          <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:var(--radius-sm); padding:0.85rem;">
            <strong style="color:var(--slate-900);">Apakah simulasi ini memerlukan koneksi internet?</strong>
            <p style="color:var(--slate-600); margin-top:0.25rem;">Tidak. Seluruh aplikasi dirancang 100% mandiri, offline, dan privat. Bank soal, aset icon, modul praktik, dan mesin penilaian tertanam sepenuhnya di dalam file tanpa mengirimkan data apa pun ke server luar.</p>
          </div>
          <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:var(--radius-sm); padding:0.85rem;">
            <strong style="color:var(--slate-900);">Pintasan Keyboard (Keyboard Shortcuts) saat Ujian:</strong>
            <p style="color:var(--slate-600); margin-top:0.25rem;">Tekan angka <strong>1 - 4</strong> atau huruf <strong>A - D</strong> untuk memilih opsi jawaban, tekan <strong>R</strong> atau <strong>F</strong> untuk menandai ragu-ragu (*flag*), dan tekan panah <strong>Kiri / Kanan</strong> untuk berpindah nomor soal secara cepat.</p>
          </div>
          <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:var(--radius-sm); padding:0.85rem;">
            <strong style="color:var(--slate-900);">Bagaimana jika laptop mati atau browser ter-refresh saat ujian?</strong>
            <p style="color:var(--slate-600); margin-top:0.25rem;">Sistem memiliki fitur <em>Crash Resilience</em> otomatis. Saat membuka kembali aplikasi, kotak dialog hijau akan muncul menawarkan opsi melanjutkan sesi terakhir dengan timer dan jawaban yang tersimpan utuh.</p>
          </div>
        </div>
      </div>

      <!-- Section 6: Rujukan Regulasi Resmi -->
      <div class="cbt-card" id="helpSec6" style="margin-bottom:1.5rem;">
        <h3 style="font-size:1.15rem; font-weight:800; color:var(--primary-900); margin-bottom:0.75rem;">6. Landasan Regulasi &amp; Dasar Hukum Resmi</h3>
        <ul style="margin-left:1.5rem; font-size:0.86rem; color:var(--slate-700); line-height:1.7;">
          <li><strong>Undang-Undang No. 6 Tahun 2014</strong> jo. <strong>Undang-Undang No. 3 Tahun 2024</strong> tentang Desa.</li>
          <li><strong>Peraturan Pemerintah No. 11 Tahun 2019</strong> tentang Penghasilan Tetap Kepala Desa dan Perangkat Desa.</li>
          <li><strong>Permendagri No. 84 Tahun 2015</strong> tentang Susunan Organisasi dan Tata Kerja Pemerintah Desa.</li>
          <li><strong>Permendagri No. 67 Tahun 2017</strong> tentang Pengangkatan dan Pemberhentian Perangkat Desa.</li>
          <li><strong>Permendagri No. 20 Tahun 2018</strong> tentang Pengelolaan Keuangan Desa.</li>
          <li><strong>Peraturan Daerah Kabupaten Tuban No. 2 Tahun 2016</strong> jo. <strong>Perda No. 16 Tahun 2021</strong> tentang Perangkat Desa.</li>
          <li><strong>Peraturan Bupati Tuban No. 11 Tahun 2022</strong> tentang Petunjuk Pelaksanaan Pengangkatan Perangkat Desa.</li>
          <li><strong>Peraturan Bupati Tuban No. 30 Tahun 2023</strong> tentang Pengelolaan Keuangan Desa di Kabupaten Tuban.</li>
          <li><strong>Undang-Undang No. 27 Tahun 2022</strong> tentang Perlindungan Data Pribadi (UU PDP).</li>
        </ul>
      </div>

      <div style="text-align:center; margin:2rem 0;">
        <button class="btn btn-outline" onclick="CBTApp.navigate('home')" style="margin-right:0.5rem;">← Kembali ke Beranda</button>
        <button class="btn btn-primary" onclick="CBTApp.confirmStartExam()">Mulai Ujian Sekarang →</button>
      </div>
    </section>

  </main>

  <!-- ======================================================================
       CIVIC FOOTER (ADOPTING COLORLIB DARK MINIMALIST FOOTER LAYOUT)
       ====================================================================== -->
  <footer class="civic-footer no-print">
    <div class="footer-main-container">
      <div class="footer-main-grid">
        <div class="footer-intro">
          <a class="footer-brand" href="javascript:void(0)" onclick="CBTApp.navigate('home')">FUSIONPROJECT.ID</a>
          <p>Aplikasi simulasi seleksi perangkat desa Kabupaten Tuban. Dilengkapi ujian tertulis 5 bidang dan praktik komputer 100% mandiri secara offline.</p>
          <a href="javascript:void(0)" onclick="CBTApp.navigate('help')" class="footer-read-more">read more <span aria-hidden="true">→</span></a>
        </div>

        <nav class="footer-nav-group" aria-label="Menu Discover">
          <h3>Discover</h3>
          <a href="javascript:void(0)" onclick="CBTApp.navigate('home')">Ujian Tertulis 5 Bidang</a>
          <a href="javascript:void(0)" onclick="CBTApp.navigate('practice-config')">Mode Latihan Bebas</a>
          <a href="javascript:void(0)" onclick="CBTApp.navigate('help')">Praktik Naskah Dinas</a>
          <a href="javascript:void(0)" onclick="CBTApp.navigate('glossary')">Glosarium Istilah Desa</a>
          <a href="javascript:void(0)" onclick="CBTApp.navigate('help')">Bank Soal 625 Butir</a>
        </nav>

        <nav class="footer-nav-group" aria-label="Menu About">
          <h3>About</h3>
          <a href="javascript:void(0)" onclick="CBTApp.navigate('help')">Profil CBT Desa</a>
          <a href="javascript:void(0)" onclick="CBTApp.navigate('help')">Format Resmi Tuban</a>
          <a href="javascript:void(0)" onclick="CBTApp.navigate('help')">Formula Skor 87,5 + 12,5</a>
          <a href="javascript:void(0)" onclick="CBTApp.navigate('help')">Tim Pengembang</a>
          <a href="javascript:void(0)" onclick="CBTApp.openVersionModal()">Changelog v5.1.0</a>
        </nav>

        <nav class="footer-nav-group" aria-label="Menu Resources">
          <h3>Resources</h3>
          <a href="javascript:void(0)" onclick="CBTApp.navigate('help')">Perda No. 2/2016</a>
          <a href="javascript:void(0)" onclick="CBTApp.navigate('help')">Perda No. 16/2021</a>
          <a href="javascript:void(0)" onclick="CBTApp.navigate('help')">Perbup No. 11/2022</a>
          <a href="javascript:void(0)" onclick="CBTApp.navigate('help')">Panduan &amp; Pintasan</a>
          <a href="javascript:void(0)" onclick="CBTApp.navigate('help')">Privasi &amp; Data</a>
        </nav>

        <nav class="footer-nav-group" aria-label="Menu Social">
          <h3>Social</h3>
          <a href="javascript:void(0)" onclick="alert('Media Sosial: Facebook Resmi')">Facebook</a>
          <a href="javascript:void(0)" onclick="alert('Media Sosial: Twitter / X')">Twitter</a>
          <a href="javascript:void(0)" onclick="alert('Media Sosial: Instagram')">Instagram</a>
          <a href="javascript:void(0)" onclick="alert('Media Sosial: YouTube Pembahasan')">YouTube</a>
          <a href="javascript:void(0)" onclick="alert('Kontak Pengembang: WhatsApp Support')">WhatsApp</a>
        </nav>
      </div>

      <div class="footer-partner-row">
        <span class="footer-partner-label">Our Partner:</span>
        <div class="footer-feature-list" aria-label="Mitra acuan regulasi">
          <span class="partner-item"><svg class="partner-bullet" width="12" height="12" viewBox="0 0 16 16" fill="none" aria-hidden="true"><circle cx="8" cy="8" r="6.5" stroke="currentColor" stroke-width="1.6"/><circle cx="8" cy="8" r="2.5" fill="currentColor"/></svg>PEMKAB TUBAN</span>
          <span class="partner-item"><svg class="partner-bullet" width="12" height="12" viewBox="0 0 16 16" fill="none" aria-hidden="true"><circle cx="8" cy="8" r="6.5" stroke="currentColor" stroke-width="1.6"/><circle cx="8" cy="8" r="2.5" fill="currentColor"/></svg>DISPERMAS BPD</span>
          <span class="partner-item"><svg class="partner-bullet" width="12" height="12" viewBox="0 0 16 16" fill="none" aria-hidden="true"><circle cx="8" cy="8" r="6.5" stroke="currentColor" stroke-width="1.6"/><circle cx="8" cy="8" r="2.5" fill="currentColor"/></svg>BKN RI</span>
          <span class="partner-item"><svg class="partner-bullet" width="12" height="12" viewBox="0 0 16 16" fill="none" aria-hidden="true"><circle cx="8" cy="8" r="6.5" stroke="currentColor" stroke-width="1.6"/><circle cx="8" cy="8" r="2.5" fill="currentColor"/></svg>KEMENDAGRI</span>
          <span class="partner-item"><svg class="partner-bullet" width="12" height="12" viewBox="0 0 16 16" fill="none" aria-hidden="true"><circle cx="8" cy="8" r="6.5" stroke="currentColor" stroke-width="1.6"/><circle cx="8" cy="8" r="2.5" fill="currentColor"/></svg>PERDA 2/2016</span>
          <span class="partner-item"><svg class="partner-bullet" width="12" height="12" viewBox="0 0 16 16" fill="none" aria-hidden="true"><circle cx="8" cy="8" r="6.5" stroke="currentColor" stroke-width="1.6"/><circle cx="8" cy="8" r="2.5" fill="currentColor"/></svg>PERBUP 11/2022</span>
        </div>
        <a href="javascript:void(0)" onclick="CBTApp.navigate('help')" class="footer-see-all">See All <span aria-hidden="true">→</span></a>
      </div>
    </div>

    <div class="civic-footer-bottom">
      <div class="footer-bottom-inner">
        <p class="footer-copy">Copyright ©2026 All rights reserved | This application is made with <span class="footer-heart">❤</span> by <strong>fusionproject.id</strong></p>
        <div class="footer-bottom-links">
          <a href="javascript:void(0)" onclick="CBTApp.navigate('help')">Terms</a>
          <a href="javascript:void(0)" onclick="CBTApp.navigate('help')">Privacy</a>
          <a href="javascript:void(0)" onclick="CBTApp.navigate('help')">Compliances</a>
        </div>
      </div>
    </div>
  </footer>


  <!-- ======================================================================
       MODAL DIALOGS
       ====================================================================== -->
  
  <!-- Modal 1: Mulai Ujian Confirmation -->
  <div class="modal-backdrop" id="modalStartExam">
    <div class="modal-dialog">
      <h3 style="font-size:1.25rem; font-weight:800; color:var(--primary-900); margin-bottom:0.75rem;">Konfirmasi Mulai Ujian Seleksi Kabupaten Tuban</h3>
      <div style="font-size:0.92rem; color:var(--slate-700); line-height:1.6; margin-bottom:1rem;">
        <p>Anda akan memulai <strong>Sesi Ujian Tertulis Resmi</strong> dengan ketentuan sebagai berikut:</p>
        <ul style="margin:0.75rem 0 0.75rem 1.5rem; font-size:0.88rem;">
          <li>Terdiri atas <strong>5 Bidang Materi berurutan</strong>, masing-masing tepat <strong>25 butir soal pilihan ganda</strong>.</li>
          <li>Setiap bidang memiliki batas waktu mandiri <strong>30 menit</strong>.</li>
          <li>Peserta memulai dari <strong>Bidang 1: Agama</strong>.</li>
          <li>Setelah menyelesaikan satu bidang, bidang tersebut dikunci permanen dan sistem beralih ke bidang berikutnya.</li>
          <li>Setelah Bidang 5 selesai, peserta wajib menyelesaikan <strong>10 Butir Praktik Komputer</strong>.</li>
          <li>Nilai Akhir = <code>(Jawaban Benar × 0,7) + Skor Praktik Komputer</code> (Maks. 100 poin).</li>
        </ul>
        <div style="background:var(--rose-50); border-left:4px solid var(--rose-600); padding:0.65rem 0.85rem; font-size:0.85rem; color:var(--rose-800);">
          <strong>Perhatian:</strong> Timer 30 menit untuk Bidang 1 (Agama) akan langsung berjalan saat tombol ditekan.
        </div>
      </div>
      <div class="modal-actions">
        <button class="btn btn-outline" onclick="CBTApp.closeModals()">Batal</button>
        <button class="btn btn-primary" onclick="CBTApp.startExamNow()">Mulai Bidang 1 (Agama)</button>
      </div>
    </div>
  </div>

  <!-- Modal 2: Konfirmasi Selesaikan Bidang Aktif -->
  <div class="modal-backdrop" id="modalFinishSection">
    <div class="modal-dialog">
      <h3 style="font-size:1.25rem; font-weight:800; color:var(--primary-900); margin-bottom:0.5rem;" id="modalFinishSectionTitle">Konfirmasi Selesaikan Bidang Ini</h3>
      <p style="font-size:0.88rem; color:var(--slate-600); margin-bottom:1rem;">Periksa rekapitulasi pengerjaan Anda pada bidang ini sebelum menguncinya:</p>

      <div class="status-summary-grid">
        <div class="status-pill-box answered">
          <div class="status-pill-num" id="secFinishAnswered">0</div>
          <div class="status-pill-label">Sudah Dijawab</div>
        </div>
        <div class="status-pill-box flagged">
          <div class="status-pill-num" id="secFinishFlagged">0</div>
          <div class="status-pill-label">Ragu-Ragu</div>
        </div>
        <div class="status-pill-box empty">
          <div class="status-pill-num" id="secFinishEmpty">0</div>
          <div class="status-pill-label">Belum Dijawab</div>
        </div>
      </div>

      <div id="secFinishWarningBox" style="margin:1rem 0;"></div>

      <div class="modal-actions">
        <button class="btn btn-outline" onclick="CBTApp.closeModals()">Kembali Periksa Soal</button>
        <button class="btn btn-danger" onclick="CBTApp.finishCurrentSection('USER_SUBMIT')">Kunci & Selesaikan Bidang Ini</button>
      </div>
    </div>
  </div>

  <!-- Modal 3: Ringkasan Sementara Bidang Selesai & Lanjut ke Bidang Berikutnya -->
  <div class="modal-backdrop" id="modalSectionComplete">
    <div class="modal-dialog">
      <div style="text-align:center; margin-bottom:1rem;">
        <div style="width:52px; height:52px; background:var(--emerald-100); color:var(--emerald-700); border-radius:50%; display:inline-flex; align-items:center; justify-content:center; margin-bottom:0.5rem;">
          <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>
        </div>
        <h3 style="font-size:1.35rem; font-weight:900; color:var(--primary-900);" id="modalCompleteHeading">Bidang 1: Agama Selesai!</h3>
        <p style="font-size:0.88rem; color:var(--slate-600);" id="modalCompleteSubheading">Jawaban pada bidang ini telah berhasil disimpan dan dikunci.</p>
      </div>

      <div style="background:var(--slate-50); border:1px solid var(--slate-200); border-radius:var(--radius-md); padding:1rem; margin-bottom:1rem;">
        <div style="font-size:0.85rem; font-weight:700; color:var(--primary-800); margin-bottom:0.5rem;">Ringkasan Sementara Bidang Ini:</div>
        <div style="display:flex; justify-content:space-around; text-align:center;">
          <div>
            <div style="font-size:1.4rem; font-weight:900; color:var(--emerald-600);" id="modalCompleteAnswered">25</div>
            <div style="font-size:0.75rem; color:var(--slate-500);">Terjawab</div>
          </div>
          <div>
            <div style="font-size:1.4rem; font-weight:900; color:var(--rose-600);" id="modalCompleteEmpty">0</div>
            <div style="font-size:0.75rem; color:var(--slate-500);">Kosong</div>
          </div>
          <div>
            <div style="font-size:1.4rem; font-weight:900; color:var(--slate-700);" id="modalCompleteTime">18:24</div>
            <div style="font-size:0.75rem; color:var(--slate-500);">Waktu Digunakan</div>
          </div>
        </div>
      </div>

      <div style="background:var(--primary-50); border:1px solid var(--primary-300); border-radius:var(--radius-sm); padding:0.75rem; font-size:0.82rem; color:var(--primary-900); margin-bottom:1.25rem;">
        <strong>Perhatian Ketentuan Ujian:</strong> Bidang ini sekarang telah dikunci dan tidak dapat diubah kembali. Kunci jawaban dan pembahasan belum ditampilkan pada tahap ini demi menjaga integritas simulasi ujian.
      </div>

      <div class="modal-actions" style="justify-content:center;">
        <button class="btn btn-gold btn-lg" id="btnProceedNextSection" onclick="CBTApp.proceedToNextSection()">
          Lanjut ke Bidang Berikutnya: Pemerintahan Desa
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
        </button>
      </div>
    </div>
  </div>

  <!-- Modal 4: Konfirmasi Selesaikan Praktik Komputer -->
  <div class="modal-backdrop" id="modalFinishPractical">
    <div class="modal-dialog">
      <h3 style="font-size:1.25rem; font-weight:800; color:var(--primary-900); margin-bottom:0.5rem;">Konfirmasi Pengakhiran Praktik Komputer</h3>
      <p style="font-size:0.88rem; color:var(--slate-600); margin-bottom:1rem;">Pastikan seluruh 10 butir tugas simulasi praktik telah Anda uji dan simpan hasilnya.</p>

      <div style="background:var(--slate-50); border:1px solid var(--slate-200); border-radius:var(--radius-md); padding:1rem; margin-bottom:1rem;">
        <div style="display:flex; justify-content:space-between; margin-bottom:0.5rem;">
          <span style="font-size:0.85rem; color:var(--slate-700);">Tugas Praktik Selesai Diuji:</span>
          <strong id="modalPracticalDoneCount" style="color:var(--emerald-700);">0 / 10 Butir</strong>
        </div>
        <div style="display:flex; justify-content:space-between;">
          <span style="font-size:0.85rem; color:var(--slate-700);">Total Skor Praktik Diperoleh:</span>
          <strong id="modalPracticalScoreCount" style="color:var(--primary-800);">0.00 / 12.50 Poin</strong>
        </div>
      </div>

      <div id="modalPracticalWarningBox" style="margin-bottom:1rem;"></div>

      <div class="modal-actions">
        <button class="btn btn-outline" onclick="CBTApp.closeModals()">Kembali Kerjakan Tugas</button>
        <button class="btn btn-danger" onclick="CBTApp.finishPracticalExam()">Selesaikan Seluruh Ujian & Hitung Nilai Akhir</button>
      </div>
    </div>
  </div>

  <!-- Modal 5: Waktu 30 Menit Habis Alert -->
  <div class="modal-backdrop" id="modalTimeExpired">
    <div class="modal-dialog">
      <h3 style="font-size:1.25rem; font-weight:800; color:var(--rose-700); margin-bottom:0.5rem;">Waktu 30 Menit Telah Habis!</h3>
      <p style="font-size:0.92rem; color:var(--slate-700); line-height:1.5; margin-bottom:1rem;">
        Alokasi waktu 30 menit untuk bidang ini telah berakhir. Seluruh jawaban yang telah Anda pilih telah otomatis disimpan dan dikunci oleh sistem.
      </p>
      <div class="modal-actions">
        <button class="btn btn-primary" onclick="CBTApp.closeModals(); CBTApp.handleTimeExpiredAdvance();">Lanjut</button>
      </div>
    </div>
  </div>

  <!-- Modal 6: Cadangan Lokal (Ekspor & Impor JSON) -->
  <div class="modal-backdrop" id="modalBackupRestore">
    <div class="modal-dialog">
      <h3 style="font-size:1.25rem; font-weight:800; color:var(--primary-900); margin-bottom:0.5rem;">Cadangan Data Lokal (Ekspor & Impor JSON)</h3>
      <p style="font-size:0.88rem; color:var(--slate-600); margin-bottom:1.25rem;">Cadangkan riwayat ujian dan pengaturan ke file JSON lokal, atau pulihkan data dari file cadangan sebelumnya. File diproses 100% offline di perangkat Anda.</p>

      <div style="background:var(--slate-50); border:1px solid var(--slate-200); border-radius:var(--radius-md); padding:1rem; margin-bottom:1.25rem;">
        <h4 style="font-size:0.95rem; font-weight:800; color:var(--primary-900); margin-bottom:0.25rem;">Ekspor Cadangan</h4>
        <p style="font-size:0.82rem; color:var(--slate-600); margin-bottom:0.75rem;">Unduh data riwayat latihan dan nilai ujian Anda dalam format JSON.</p>
        <button class="btn btn-primary btn-sm" onclick="CBTApp.exportBackupJSON()">
          Unduh File Cadangan JSON
        </button>
      </div>

      <div style="background:var(--slate-50); border:1px solid var(--slate-200); border-radius:var(--radius-md); padding:1rem;">
        <h4 style="font-size:0.95rem; font-weight:800; color:var(--primary-900); margin-bottom:0.25rem;">Impor & Pulihkan Data</h4>
        <p style="font-size:0.82rem; color:var(--slate-600); margin-bottom:0.75rem;">Pilih file cadangan JSON yang valid (maksimal ukuran 2 MB).</p>
        <input type="file" id="backupFileInput" accept=".json" class="form-control" style="font-size:0.85rem; margin-bottom:0.75rem;">
        <div style="display:flex; gap:0.5rem;">
          <button class="btn btn-emerald btn-sm" onclick="CBTApp.importBackupJSON('merge')">Gabungkan Riwayat</button>
          <button class="btn btn-outline btn-sm" onclick="CBTApp.importBackupJSON('replace')">Ganti Penuh</button>
        </div>
      </div>

      <div class="modal-actions">
        <button class="btn btn-outline" onclick="CBTApp.closeModals()">Tutup</button>
      </div>
    </div>
  </div>

  <!-- Modal 7: Konfigurasi Durasi Waktu Praktik Komputer -->
  <div class="modal-backdrop" id="modalPracticalDuration">
    <div class="modal-dialog">
      <h3 style="font-size:1.25rem; font-weight:800; color:var(--primary-900); margin-bottom:0.5rem;">⏱️ Konfigurasi Alokasi Waktu Praktik Komputer</h3>
      <p style="font-size:0.88rem; color:var(--slate-600); margin-bottom:1rem;">
        Alokasi waktu ujian praktik komputer ditentukan oleh Tim Penyusun Naskah Ujian / Panitia Pengawas Desa Tuban. Durasi di bawah ini merupakan opsi konfigurasi simulasi fleksibel:
      </p>

      <div style="display:flex; flex-direction:column; gap:0.5rem; margin-bottom:1.25rem;">
        <label style="display:flex; align-items:center; gap:0.75rem; padding:0.6rem 0.85rem; border:1px solid var(--slate-300); border-radius:var(--radius-sm); cursor:pointer;">
          <input type="radio" name="optPracticalDuration" value="30">
          <div>
            <strong>30 Menit</strong> — Simulasi Waktu Cepat (3 menit per butir tugas)
          </div>
        </label>
        <label style="display:flex; align-items:center; gap:0.75rem; padding:0.6rem 0.85rem; border:2px solid var(--primary-600); background:var(--primary-50); border-radius:var(--radius-sm); cursor:pointer;">
          <input type="radio" name="optPracticalDuration" value="45" checked>
          <div>
            <strong>45 Menit (Rekomendasi Standar)</strong> — Rata-rata 4,5 menit per butir tugas
          </div>
        </label>
        <label style="display:flex; align-items:center; gap:0.75rem; padding:0.6rem 0.85rem; border:1px solid var(--slate-300); border-radius:var(--radius-sm); cursor:pointer;">
          <input type="radio" name="optPracticalDuration" value="60">
          <div>
            <strong>60 Menit (1 Jam Penuh)</strong> — Alokasi pembuatan dokumen dan formula lengkap
          </div>
        </label>
        <label style="display:flex; align-items:center; gap:0.75rem; padding:0.6rem 0.85rem; border:1px solid var(--slate-300); border-radius:var(--radius-sm); cursor:pointer;">
          <input type="radio" name="optPracticalDuration" value="90">
          <div>
            <strong>90 Menit (1,5 Jam)</strong> — Alokasi simulasi bertahap dan menyeluruh
          </div>
        </label>
        <label style="display:flex; align-items:center; gap:0.75rem; padding:0.6rem 0.85rem; border:1px solid var(--slate-300); border-radius:var(--radius-sm); cursor:pointer;">
          <input type="radio" name="optPracticalDuration" value="0">
          <div>
            <strong>Tanpa Batas Waktu (Mode Latihan Bebas)</strong> — Timer hanya menghitung waktu berjalan tanpa batas mundur
          </div>
        </label>
      </div>

      <div class="modal-actions">
        <button class="btn btn-outline" onclick="CBTApp.closeModals()">Batal</button>
        <button class="btn btn-primary" onclick="CBTApp.applyPracticalDuration()">Terapkan Durasi</button>
      </div>
    </div>
  </div>

  <!-- Modal Catatan Rilis & Riwayat Fitur (Changelog) -->
  <div id="modalVersionInfo" class="modal-backdrop no-print">
    <div class="modal-dialog" style="max-width:680px;">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1.25rem; padding-bottom:0.85rem; border-bottom:1px solid var(--slate-200);">
        <div style="display:flex; align-items:center; gap:0.85rem;">
          <div style="width:42px; height:42px; border-radius:var(--radius-md); background:var(--primary-900); display:flex; align-items:center; justify-content:center; padding:3px; box-shadow:0 2px 6px rgba(0,0,0,0.15); flex-shrink:0;">
            <img src="assets/favicon.svg" alt="Logo" width="34" height="34" style="display:block;">
          </div>
          <div>
            <h3 style="font-size:1.22rem; font-weight:800; color:var(--primary-900); margin:0; line-height:1.2;">Catatan Rilis &amp; Riwayat Fitur</h3>
            <p style="font-size:0.8rem; color:var(--slate-500); margin:3px 0 0 0;">CBT Simulasi Ujian Perangkat Desa Kab. Tuban</p>
          </div>
        </div>
        <button class="btn-close-modal" onclick="CBTApp.closeModals()" title="Tutup" aria-label="Tutup">&times;</button>
      </div>

      <div style="background:var(--slate-50); border:1px solid var(--slate-200); border-radius:var(--radius-md); padding:0.85rem 1.15rem; margin-bottom:1.25rem; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem;">
        <div>
          <span style="font-size:1.05rem; font-weight:900; color:var(--primary-900);">Versi Aplikasi: <span style="color:var(--accent-gold-600); font-family:monospace; background:var(--accent-gold-50); padding:2px 8px; border-radius:4px; border:1px solid var(--accent-gold-200);">v5.1.0</span></span>
          <div style="font-size:0.78rem; color:var(--slate-600); margin-top:3px;">Hak Cipta: <strong>Copyright by fusionproject.id</strong></div>
        </div>
        <span class="badge-pill badge-verified" style="font-size:0.75rem; font-weight:700;">Production Ready</span>
      </div>

      <h4 style="font-size:0.92rem; font-weight:800; color:var(--primary-900); margin-bottom:0.75rem;">Daftar Fitur &amp; Pembaruan Aplikasi:</h4>
      <div class="modal-changelog-list">
        
        <!-- v5.1.0 -->
        <div style="padding:0.75rem 0.9rem; background:#eff6ff; border-left:3px solid #2563eb; border-radius:var(--radius-sm);">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.35rem;">
            <strong style="color:#1d4ed8; font-size:0.88rem;">Versi v5.1.0 (Pembersihan Menyeluruh Seluruh Folder &amp; Peningkatan UI)</strong>
            <span style="font-size:0.7rem; color:#64748b; font-weight:600;">Terbaru</span>
          </div>
          <ul style="margin:0; padding-left:1.15rem; color:var(--slate-700); line-height:1.5;">
            <li><strong>Pembersihan Seluruh Folder &amp; Subfolder (Deep Cleanup):</strong> Otomasi workflow GitHub Actions (<code>cleanup-repo.yml</code>) dan modul Python (<code>optimize_assets.py</code>) untuk memindai serta menghapus seluruh file tidak berguna lintas seluruh ekstensi di seluruh direktori (file <code>.py</code> di luar folder generator, file temporary <code>.tmp</code>/<code>.bak</code>/<code>.swp</code>, cache python <code>__pycache__</code>/<code>.pyc</code>, log sampah, OS metadata <code>Thumbs.db</code>/<code>.DS_Store</code>, dan folder scratch).</li>
            <li><strong>Perbaikan &amp; Redesain Popup Changelog:</strong> Rekonstruksi total dialog modal Catatan Rilis dengan background putih solid, backdrop blur, animasi halus <code>modalFadeIn</code>, custom scrollbar ramping, tombol tutup melingkar modern, dan dukungan penutupan fleksibel via tombol keyboard Escape maupun klik backdrop luar.</li>
            <li><strong>Optimasi Aset Maksimal:</strong> Minifikasi CSS (penghematan 32%), kompresi JavaScript engine CBT, optimasi grafis SVG (penghematan s.d. 29.5%), dan kompresi bundle HTML.</li>
          </ul>
        </div>

        <!-- v5.0.0 -->
        <div style="padding:0.75rem 0.9rem; background:#f8fafc; border-left:3px solid #64748b; border-radius:var(--radius-sm);">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.35rem;">
            <strong style="color:#334155; font-size:0.88rem;">Versi v5.0.0 (Pembaruan Arsitektur Besar)</strong>
            <span style="font-size:0.7rem; color:#64748b;">Rilis Sebelumnya</span>
          </div>
          <ul style="margin:0; padding-left:1.15rem; color:var(--slate-700); line-height:1.5;">
            <li><strong>Bank Soal Seimbang 1.000 Butir:</strong> Penyeimbangan master database bank soal menjadi tepat 200 butir soal per bidang untuk seluruh 5 bidang ujian (Total 1.000 butir: 200 Agama, 200 Pemdes, 200 Bahasa Indonesia, 200 Pengetahuan Umum, 200 Pengetahuan Komputer).</li>
            <li><strong>Isolasi Ketat Antarbidang (Zero Mixing):</strong> Pemisahan fisik bank soal setiap bidang ke dalam modul mandiri ber-<code>bidangId</code> dan rentang ID berurutan rapi (1–200, 201–400, 401–600, 601–800, 801–1000) sehingga soal satu bidang tidak akan pernah keluar atau tercampur di bidang lain.</li>
            <li><strong>Fitur Mode Latihan Khusus per Bidang:</strong> Menu latihan mandiri kini dilengkapi dropdown filter khusus per bidang (Bidang 1 s.d. Bidang 5) selain per subkategori dan database lengkap.</li>
            <li><strong>Pembaruan Pusat Bantuan &amp; Regulasi:</strong> Tabel distribusi materi di Halaman Bantuan kini menyajikan proporsi seimbang 1.000 butir soal resmi Perda Kab. Tuban.</li>
          </ul>
        </div>

        <!-- v4.5.1 -->
        <div style="padding:0.75rem 0.9rem; background:#f8fafc; border-left:3px solid #64748b; border-radius:var(--radius-sm);">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.35rem;">
            <strong style="color:#334155; font-size:0.88rem;">Versi v4.5.1</strong>
            <span style="font-size:0.7rem; color:#64748b;">Rilis Sebelumnya</span>
          </div>
          <ul style="margin:0; padding-left:1.15rem; color:var(--slate-700); line-height:1.5;">
            <li><strong>Ekspansi Bank Soal Bahasa Indonesia:</strong> Penambahan 40 butir soal baru (EYD V, tata naskah dinas desa, konjungsi antarkalimat, peluluhan fonem KTSP, nominal kas desa, dan kalimat efektif).</li>
            <li><strong>Eliminasi Kemiripan Soal:</strong> Refaktorisasi butir soal bernuansa serupa sehingga seluruh 25 soal Bahasa Indonesia per sesi ujian memiliki konsep dan opsi 100% unik tanpa pengulangan.</li>
          </ul>
        </div>

        <!-- v4.5.0 -->
        <div style="padding:0.75rem 0.9rem; background:#f8fafc; border-left:3px solid #64748b; border-radius:var(--radius-sm);">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.35rem;">
            <strong style="color:#334155; font-size:0.88rem;">Versi v4.5.0</strong>
            <span style="font-size:0.7rem; color:#64748b;">Rilis Sebelumnya</span>
          </div>
          <ul style="margin:0; padding-left:1.15rem; color:var(--slate-700); line-height:1.5;">
            <li><strong>Landing Page Sederhana:</strong> Tampilan depan minimalis dengan kartu identitas peserta dan tombol "Mulai Ujian" &amp; "Mulai Mode Latihan".</li>
            <li><strong>Halaman Pusat Bantuan (Help):</strong> Rujukan regulasi, alur 5 bidang, tabel distribusi soal, dan panduan praktik komputer dipindahkan ke halaman tersendiri.</li>
            <li><strong>Menu Navigasi Modern:</strong> Navigasi pill elegan, backdrop-blur, responsif mobile, dan pemilih skala font.</li>
            <li><strong>Footer direktori responsif:</strong> Menyediakan navigasi latihan, materi, bantuan, fitur aplikasi, dan tautan privasi.</li>
            <li>Penambahan <strong>Favicon SVG</strong> dan <strong>Logo Resmi Emblem</strong> Kabupaten Tuban yang tajam di semua layar.</li>
            <li>Optimasi pemilihan 125 soal unik tanpa duplikasi intra-sesi ujian.</li>
          </ul>
        </div>

        <!-- v4.4.0 -->
        <div style="padding:0.75rem 0.9rem; background:#f8fafc; border-left:3px solid #64748b; border-radius:var(--radius-sm);">
          <strong style="color:var(--slate-800); font-size:0.88rem;">Versi v4.4.0</strong>
          <ul style="margin:0.35rem 0 0; padding-left:1.15rem; color:var(--slate-700); line-height:1.5;">
            <li>Penataan direktori proyek dan isolasi modul generator ke folder <code>generator/</code>.</li>
            <li>Otomatisasi pengujian dan deployment CI/CD ke <strong>GitHub Pages</strong> via GitHub Actions.</li>
            <li>Penyediaan script sinkronisasi otomatis satu klik untuk Windows (<code>sync_github.bat</code>).</li>
          </ul>
        </div>

        <!-- v4.0.0 - v4.3.0 -->
        <div style="padding:0.75rem 0.9rem; background:#f8fafc; border-left:3px solid #059669; border-radius:var(--radius-sm);">
          <strong style="color:#047857; font-size:0.88rem;">Versi v4.0.0 – v4.3.0</strong>
          <ul style="margin:0.35rem 0 0; padding-left:1.15rem; color:var(--slate-700); line-height:1.5;">
            <li>Rilis Arsitektur Modular 100% Offline (HTML5, CSS, dan JS Engine terpisah).</li>
            <li>Modul Ujian Praktik Komputer 10 Butir Tugas Nyata (Word, Excel, PowerPoint, ZIP).</li>
            <li>Dual Mode Praktik Komputer: Mode 1 (Office Asli + Verifikasi OpenXML) &amp; Mode 2 (Simulasi Browser).</li>
            <li>Formula Penilaian Resmi Tuban: 87,5 (Tertulis) + 12,5 (Praktik) = 100,00 Poin Maksimal.</li>
            <li>Glosarium interaktif 36 istilah desa dan grafik histori tren nilai berbasis SVG native.</li>
          </ul>
        </div>

        <!-- v1.0.0 - v3.0.0 -->
        <div style="padding:0.75rem 0.9rem; background:#f8fafc; border-left:3px solid #d97706; border-radius:var(--radius-sm);">
          <strong style="color:#b45309; font-size:0.88rem;">Versi v1.0.0 – v3.0.0</strong>
          <ul style="margin:0.35rem 0 0; padding-left:1.15rem; color:var(--slate-700); line-height:1.5;">
            <li>Penyusunan Master Pool bank soal berdasar regulasi perundang-undangan.</li>
            <li>Format 5 bidang materi ujian tertulis berurutan (sequential locking) dengan timer mandiri 30 menit per bidang.</li>
            <li>Ketahanan sesi ujian dari refresh atau peramban tertutup tanpa kehilangan progres.</li>
          </ul>
        </div>

      </div>

      <div class="modal-actions" style="justify-content:space-between; align-items:center; margin-top:1.25rem; padding-top:0.85rem; border-top:1px solid var(--slate-200);">
        <span style="font-size:0.78rem; color:var(--slate-500);">© 2026 <strong>fusionproject.id</strong> • Seluruh hak cipta dilindungi</span>
        <button class="btn btn-primary btn-sm" onclick="CBTApp.closeModals()">Tutup</button>
      </div>
    </div>
  </div>
'''
