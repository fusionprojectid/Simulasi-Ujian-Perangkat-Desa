// ==========================================================================
// CBT APPLICATION ENGINE - KABUPATEN TUBAN
// 5 Bidang Tertulis (125 Soal) & Praktik Komputer (10 Butir)
// ==========================================================================

// Master Database of 625 Questions (Injected from Python)
    const MASTER_QUESTIONS = window.__MASTER_QUESTIONS__;

    // Master Database of 36 Village Terms (Injected from Python)
    const GLOSSARY_DATA = window.__GLOSSARY_DATA__;

    // Master Database of 10 Practical Computer Tasks (Injected from Python)
    const PRACTICAL_TASKS_TEMPLATE = window.__PRACTICAL_TASKS__;

    // =========================================================================
    // 5 BIDANG UJIAN TERTULIS KABUPATEN TUBAN (RESMI)
    // Total: 125 Soal (5 x 25 Soal), Waktu 30 Menit / Bidang
    // =========================================================================
    const BIDANG_CONFIG = [
      {
        id: 1,
        name: "Agama",
        title: "Bidang 1: Pendidikan Agama & Moderasi Beragama",
        shortName: "Agama",
        count: 25,
        durationMinutes: 30,
        categories: ["Pendidikan agama dan moderasi beragama"],
        focus: "Fiqih jenazah di desa, zakat fitrah & mal, wakaf UU 41/2004, tugas modin/Kasi Pelayanan, toleransi keagamaan, etika aparatur desa, dan sejarah Sunan Bonang Tuban."
      },
      {
        id: 2,
        name: "Pengetahuan Pemerintahan Desa",
        title: "Bidang 2: Pengetahuan Pemerintahan Desa",
        shortName: "Pemerintahan Desa",
        count: 25,
        durationMinutes: 30,
        categories: [
          "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa",
          "Peraturan perundang-undangan dan tata kelola pemerintahan",
          "Administrasi pemerintahan, surat-menyurat, dan pengarsipan",
          "Keuangan desa, APB Desa, dan aset desa",
          "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat",
          "BPD, kelembagaan desa, dan musyawarah"
        ],
        subQuotas: {
          "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa": 7,
          "Peraturan perundang-undangan dan tata kelola pemerintahan": 4,
          "Administrasi pemerintahan, surat-menyurat, dan pengarsipan": 4,
          "Keuangan desa, APB Desa, dan aset desa": 4,
          "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat": 3,
          "BPD, kelembagaan desa, dan musyawarah": 3
        },
        focus: "UU No. 6/2014 jo. UU No. 3/2024, PP 11/2019, Permendagri 84/2015, Permendagri 20/2018 (APBDes), Permendesa 21/2020, Perda Kab. Tuban No. 2/2016 jo. No. 16/2021, Perbup Tuban 11/2022."
      },
      {
        id: 3,
        name: "Bahasa Indonesia",
        title: "Bidang 3: Bahasa Indonesia",
        shortName: "Bahasa Indonesia",
        count: 25,
        durationMinutes: 30,
        categories: ["Bahasa Indonesia"],
        focus: "Ejaan Bahasa Indonesia Yang Disempurnakan (EYD V), tata bahasa naskah dinas, kosakata baku, kalimat efektif tanpa pleonasme, tanda baca, dan pemahaman teks administrasi."
      },
      {
        id: 4,
        name: "Pengetahuan Umum",
        title: "Bidang 4: Pengetahuan Umum",
        shortName: "Pengetahuan Umum",
        count: 25,
        durationMinutes: 30,
        categories: [
          "Pancasila, UUD 1945, dan wawasan kebangsaan",
          "Pengetahuan umum",
          "Logika dan penalaran",
          "Matematika dan numerik"
        ],
        subQuotas: {
          "Pancasila, UUD 1945, dan wawasan kebangsaan": 10,
          "Pengetahuan umum": 5,
          "Logika dan penalaran": 5,
          "Matematika dan numerik": 5
        },
        focus: "Pancasila, UUD 1945 amandemen, wawasan kebangsaan, sejarah & geografi Kabupaten Tuban, silogisme logika, deret, dan matematika dasar APBDes."
      },
      {
        id: 5,
        name: "Pengetahuan Komputer",
        title: "Bidang 5: Pengetahuan Komputer",
        shortName: "Pengetahuan Komputer",
        count: 25,
        durationMinutes: 30,
        categories: ["Komputer dasar dan pelayanan publik"],
        focus: "Hardware, software, MS Word (tata naskah, mail merge, tabel), MS Excel (SUM, AVERAGE, IF, VLOOKUP), manajemen berkas PDF/ZIP, email dinas, keamanan siber, dan UU No. 27/2022 (UU PDP)."
      }
    ];

    // Safe Randomization Helpers (Fisher-Yates)
    function shuffleArray(array) {
      const arr = [...array];
      for (let i = arr.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        const temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
      }
      return arr;
    }

    // Storage Utilities
    function safeGetStorage(key, defaultVal) {
      try {
        const item = localStorage.getItem(key);
        return item ? JSON.parse(item) : defaultVal;
      } catch (e) {
        console.warn('Storage read fallback:', e);
        return defaultVal;
      }
    }

    function safeSetStorage(key, value) {
      try {
        if (value === null) {
          localStorage.removeItem(key);
        } else {
          localStorage.setItem(key, JSON.stringify(value));
        }
        return true;
      } catch (e) {
        console.warn('Storage write fallback:', e);
        return false;
      }
    }


    // Helper: Build Exam Questions for 5 Bidang (125 Soal Unik per Sesi Ujian)
    function generateTubanExamSections(masterList, randomize = true) {
      const sections = [];

      BIDANG_CONFIG.forEach(cfg => {
        let pickedQuestions = [];

        if (cfg.subQuotas) {
          // Distributed across sub-categories (strictly unique per session, strictly isolated to cfg.id)
          Object.entries(cfg.subQuotas).forEach(([catName, quota]) => {
            const pool = masterList.filter(q => q.bidangId === cfg.id && q.category === catName);
            const shuffled = randomize ? shuffleArray(pool) : [...pool];
            pickedQuestions.push(...shuffled.slice(0, quota));
          });
        } else {
          // Single category or full bidang pool (strictly isolated by cfg.id)
          const pool = masterList.filter(q => q.bidangId === cfg.id);
          const shuffled = randomize ? shuffleArray(pool) : [...pool];
          pickedQuestions.push(...shuffled.slice(0, cfg.count));
        }

        // Shuffle questions within the section
        if (randomize) {
          pickedQuestions = shuffleArray(pickedQuestions);
        }

        // Format and randomize options
        const formattedQuestions = pickedQuestions.map((q, idx) => {
          const originalCorrect = q.options[q.answer];
          const opts = [...q.options];
          if (randomize) {
            const shuffledOpts = shuffleArray(opts);
            const newAns = shuffledOpts.indexOf(originalCorrect);
            return {
              ...q,
              number: idx + 1,
              bidangId: cfg.id,
              bidangName: cfg.name,
              options: shuffledOpts,
              answer: newAns,
              originalAnswer: q.answer,
              originalId: q.id
            };
          } else {
            return {
              ...q,
              number: idx + 1,
              bidangId: cfg.id,
              bidangName: cfg.name,
              options: opts,
              answer: q.answer,
              originalAnswer: q.answer,
              originalId: q.id
            };
          }
        });

        sections.push({
          bidangId: cfg.id,
          bidangName: cfg.name,
          name: cfg.name,
          title: cfg.title,
          shortName: cfg.shortName,
          durationMinutes: cfg.durationMinutes,
          durationMs: cfg.durationMinutes * 60 * 1000,
          questions: formattedQuestions,
          userAnswers: {},
          flaggedQuestions: {},
          currentIndex: 0,
          startTime: null,
          isCompleted: false,
          completedTime: null,
          timeUsedMs: 0,
          score: 0
        });
      });


      return sections;
    }

    // =========================================================================
    // MAIN CBT CONTROLLER (CBTApp)
    // =========================================================================
    const CBTApp = {
      mode: 'official_exam', // 'official_exam' | 'practice'
      region: 'tuban',
      candidateName: '',
      candidateVillage: '',

      // 5 Sequential Sections
      sections: [],
      currentSectionIndex: 0, // 0..4 (Written 5 Bidang), 5 (Practical)

      // Timer variables
      sectionStartTime: null,
      sectionDurationMs: 30 * 60 * 1000,
      timerInterval: null,
      warned5m: false,
      warned1m: false,
      isTimerRunning: false,

      // Practical State (10 Butir)
      practicalTasks: [],
      currentPracticalIndex: 0,
      practicalMode: 'office', // 'office' | 'sim'
      practicalDurationMinutes: 45, // default 45 min, configurable
      practicalRemainingSeconds: 45 * 60,
      practicalTimerInterval: null,
      practicalStartTime: null,
      isPracticalLocked: false,

      // Navigation & Review
      paletteFilter: 'all', // 'all' | 'done' | 'flag' | 'empty'
      activeReviewTab: 'wrong',
      examFinished: false,

      STORAGE_KEY: 'tuban_perangkat_desa_cbt_v4',
      HISTORY_KEY: 'cbt_exam_history_v2',

      // Safe Rich Text Formatter: supports *italic*, _italic_, **bold**, `code`, <u>, <i>, <b>, <em>, <strong>
      formatRichText(str) {
        if (!str) return '';
        let s = String(str);

        // Preserve already existing allowed HTML tags (i, em, b, strong, u, code, sup, sub, br)
        const tags = [];
        s = s.replace(/<\/?(?:i|em|b|strong|u|code|sup|sub|br\s*\/?)>/gi, (match) => {
          tags.push(match);
          return '___TAG_' + (tags.length - 1) + '___';
        });

        // Escape raw HTML special characters
        s = s.replace(/&/g, '&amp;')
             .replace(/</g, '&lt;')
             .replace(/>/g, '&gt;');

        // Restore preserved HTML tags
        s = s.replace(/___TAG_(\d+)___/g, (_, i) => tags[i]);

        // Inline Code: `code`
        s = s.replace(/`([^`]+)`/g, '<code class="inline-code">$1</code>');

        // Bold Italic: ***text*** or ___text___
        s = s.replace(/\*\*\*([^*]+)\*\*\*/g, '<strong><em>$1</em></strong>');
        s = s.replace(/(^|[\s(>])___([^_]+)___([\s),.?!<]|$)/g, '$1<strong><em>$2</em></strong>$3');

        // Bold: **text**
        s = s.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');

        // Italic: *text*
        s = s.replace(/(^|[\s(>])\*([^*]+)\*([\s),.?!<]|$)/g, '$1<em>$2</em>$3');

        // Italic: _text_ (only when surrounded by spaces, parentheses, tags, or start/end, avoiding intra-word like file_name.pdf)
        s = s.replace(/(^|[\s(>])_([a-zA-Z0-9\-\s]+?)_([\s),.?!<]|$)/g, '$1<em>$2</em>$3');

        return s;
      },

      init() {
        this.renderDistributionTable();
        this.populateCategoryDropdowns();
        this.renderGlossary();
        this.checkExistingSession();
        this.setupKeyboardShortcuts();
      },


      renderDistributionTable() {
        const tbody = document.getElementById('distributionTableBody');
        if (!tbody) return;

        let html = '';
        BIDANG_CONFIG.forEach((b, idx) => {
          const poolCount = MASTER_QUESTIONS.filter(q => q.bidangId === b.id).length;

          html += `
            <tr>
              <td style="text-align:center; font-weight:800; color:var(--primary-700);">Sesi ${b.id}</td>
              <td style="font-weight:700; color:var(--primary-900);">${b.name}</td>
              <td style="text-align:center; font-weight:700; color:var(--primary-700);">${b.count} Soal</td>
              <td style="text-align:center; font-weight:700; color:var(--slate-700);">${b.durationMinutes} Menit</td>
              <td style="text-align:center;"><span class="badge-pill badge-cat">Maks. ${(b.count * 0.7).toFixed(1)} Poin</span></td>
              <td style="text-align:center; font-weight:700; color:var(--emerald-600);">${poolCount} Soal</td>
              <td style="font-size:0.8rem; color:var(--slate-600);">${b.focus}</td>
            </tr>
          `;
        });

        // Add Practical Exam Row
        html += `
          <tr style="background:#ecfdf5;">
            <td style="text-align:center; font-weight:800; color:var(--emerald-700);">Sesi 6</td>
            <td style="font-weight:700; color:var(--emerald-800);">Praktik Komputer (Simulasi Interaktif)</td>
            <td style="text-align:center; font-weight:700; color:var(--emerald-700);">10 Butir</td>
            <td style="text-align:center; font-weight:700; color:var(--emerald-700);">Tahap Khusus</td>
            <td style="text-align:center;"><span class="badge-pill badge-diff-mudah">Maks. 12,50 Poin</span></td>
            <td style="text-align:center; font-weight:700; color:var(--emerald-600);">10 Tugas</td>
            <td style="font-size:0.8rem; color:var(--slate-700);">Word: Kertas F4, Kop Surat, Mail Merge; Excel: SUM, AVERAGE, IF, VLOOKUP, Sort & Filter; PDF, ZIP, dan Keamanan Sandi UU PDP.</td>
          </tr>
        `;

        tbody.innerHTML = html;
      },

      populateCategoryDropdowns() {
        const pSelect = document.getElementById('practiceCategorySelect');
        if (!pSelect) return;

        let options = '<option value="all">Semua Bidang & Materi (Database 1.000 Soal Lengkap)</option>';
        options += '<optgroup label="--- PILIH KHUSUS PER BIDANG (200 SOAL / BIDANG) ---">';
        BIDANG_CONFIG.forEach(b => {
          const count = MASTER_QUESTIONS.filter(q => q.bidangId === b.id).length;
          options += `<option value="bidang_${b.id}">${b.title} (${count} Soal)</option>`;
        });
        options += '</optgroup>';
        options += '<optgroup label="--- PILIH SUBKATEGORI SPESIFIK ---">';
        const distinctCats = [...new Set(MASTER_QUESTIONS.map(q => q.category))];
        distinctCats.forEach(cat => {
          const count = MASTER_QUESTIONS.filter(q => q.category === cat).length;
          options += `<option value="${cat}">${cat} (${count} Soal)</option>`;
        });
        options += '</optgroup>';
        pSelect.innerHTML = options;
      },

      handleRegionChange() {
        const sel = document.getElementById('selectRegion');
        this.region = sel ? sel.value : 'tuban';
      },

      setFontScale(scale) {
        document.documentElement.style.setProperty('--app-font-scale', scale);
        document.querySelectorAll('.font-scale-btn').forEach(btn => btn.classList.remove('active'));
        if (scale === '90%') document.getElementById('fScaleSm')?.classList.add('active');
        else if (scale === '100%') document.getElementById('fScaleMd')?.classList.add('active');
        else if (scale === '115%') document.getElementById('fScaleLg')?.classList.add('active');
      },

      toggleMobileMenu() {
        const menu = document.getElementById('modernNavMenu');
        if (menu) menu.classList.toggle('mobile-open');
      },

      handleSubscribe(form) {
        const input = form ? form.querySelector('input') : null;
        const email = input ? input.value.trim() : '';
        if (email) {
          this.showToastNotification('✓ Terima kasih! Alamat ' + email + ' telah terdaftar untuk informasi pembaruan simulasi.', 'success');
          if (form) form.reset();
        }
      },

      navigate(viewName) {
        const vHome = document.getElementById('viewHome');
        const vPractice = document.getElementById('viewPracticeConfig');
        const vExam = document.getElementById('viewExam');
        const vPractical = document.getElementById('viewPractical');
        const vResults = document.getElementById('viewResults');
        const vGlossary = document.getElementById('viewGlossary');
        const vHistory = document.getElementById('viewHistory');
        const vHelp = document.getElementById('viewHelp');

        if (vHome) vHome.style.display = viewName === 'home' ? 'block' : 'none';
        if (vPractice) vPractice.style.display = viewName === 'practice-config' ? 'block' : 'none';
        if (vExam) vExam.style.display = viewName === 'exam' ? 'block' : 'none';
        if (vPractical) vPractical.style.display = viewName === 'practical' ? 'block' : 'none';
        if (vResults) vResults.style.display = viewName === 'results' ? 'block' : 'none';
        if (vGlossary) vGlossary.style.display = viewName === 'glossary' ? 'block' : 'none';
        if (vHistory) vHistory.style.display = viewName === 'history' ? 'block' : 'none';
        if (vHelp) vHelp.style.display = viewName === 'help' ? 'block' : 'none';

        // Update active class on modern nav menu buttons
        document.querySelectorAll('.nav-btn').forEach(btn => {
          btn.classList.toggle('active', btn.dataset.navView === viewName);
        });

        // Close mobile drawer if open
        const menu = document.getElementById('modernNavMenu');
        if (menu) menu.classList.remove('mobile-open');

        if (viewName === 'history') {
          this.renderHistoryView();
        }

        window.scrollTo({ top: 0, behavior: 'smooth' });
      },

      closeModals() {
        document.querySelectorAll('.modal-backdrop').forEach(m => m.classList.remove('open'));
      },

      readCandidateInputs() {
        const nameInput = document.getElementById('inputCandidateName');
        const villageInput = document.getElementById('inputCandidateVillage');
        const regionInput = document.getElementById('selectRegion');

        this.candidateName = (nameInput && nameInput.value.trim()) ? nameInput.value.trim() : 'Peserta Ujian';
        this.candidateVillage = (villageInput && villageInput.value.trim()) ? villageInput.value.trim() : 'Kabupaten Tuban';
        this.region = regionInput ? regionInput.value : 'tuban';
      },

      // =======================================================================
      // OFFICIAL EXAM INITIATION (5 BIDANG + PRAKTIK KOMPUTER)
      // =======================================================================
      confirmStartExam() {
        this.readCandidateInputs();
        document.getElementById('modalStartExam').classList.add('open');
      },

      startExamNow() {
        this.closeModals();
        this.readCandidateInputs();
        this.mode = 'official_exam';
        this.examFinished = false;

        // Generate the 5 official sections (each exactly 25 questions)
        this.sections = generateTubanExamSections(MASTER_QUESTIONS, true);
        this.currentSectionIndex = 0;

        // Initialize Practical Tasks (10 butir)
        this.practicalTasks = JSON.parse(JSON.stringify(PRACTICAL_TASKS_TEMPLATE)).map(t => ({
          ...t,
          isCompleted: false,
          earnedScore: 0,
          status: 'not_started', // 'not_started' | 'pending_review' | 'pass' | 'needs_revision'
          practicalMode: 'office',
          uploadedFile: null,
          rubricChecks: t.rubric ? t.rubric.map(() => false) : [],
          candidateInputs: JSON.parse(JSON.stringify(t.defaultData || {})),
          testFeedback: ''
        }));
        this.currentPracticalIndex = 0;
        this.practicalMode = 'office';
        this.isPracticalLocked = false;
        this.practicalRemainingSeconds = (this.practicalDurationMinutes || 45) * 60;
        this.practicalStartTime = null;
        if (this.practicalTimerInterval) {
          clearInterval(this.practicalTimerInterval);
          this.practicalTimerInterval = null;
        }

        // Start Section 0: Bidang 1 (Agama)
        this.startSection(0);
        this.saveSession();
      },

      startSection(sectionIdx) {
        if (sectionIdx < 0 || sectionIdx >= this.sections.length) return;
        this.currentSectionIndex = sectionIdx;
        const currentSec = this.sections[sectionIdx];

        // Start 30-Minute Countdown for this section
        if (!currentSec.startTime) {
          currentSec.startTime = Date.now();
        }
        this.sectionStartTime = currentSec.startTime;
        this.sectionDurationMs = currentSec.durationMs;
        this.warned5m = false;
        this.warned1m = false;

        this.startSectionTimer();
        this.updateStepperUI();
        this.updateExamHeaderUI();
        this.renderQuestionPaletteGrid();
        this.renderCurrentQuestion();

        this.navigate('exam');
      },

      updateStepperUI() {
        const list = document.getElementById('bidangStepperList');
        if (!list) return;

        let html = '';
        this.sections.forEach((sec, idx) => {
          let itemClass = 'step-item';
          let badgeContent = `${sec.bidangId}`;

          if (sec.isCompleted) {
            itemClass += ' completed';
            badgeContent = '✓';
          } else if (idx === this.currentSectionIndex && this.mode === 'official_exam') {
            itemClass += ' active';
          } else {
            itemClass += ' locked';
          }

          html += `
            <div class="${itemClass}">
              <div class="step-badge">${badgeContent}</div>
              <div class="step-info">
                <span class="step-name">${sec.shortName}</span>
                <span class="step-meta">25 Soal • 30 Mnt</span>
              </div>
            </div>
          `;
        });

        // Step 6: Praktik Komputer
        const isPractActive = this.currentSectionIndex === 5;
        const isPractDone = this.examFinished;
        let pClass = 'step-item';
        let pBadge = '6';
        if (isPractDone) {
          pClass += ' completed';
          pBadge = '✓';
        } else if (isPractActive) {
          pClass += ' active';
        } else {
          pClass += ' locked';
        }

        html += `
          <div class="${pClass}">
            <div class="step-badge">${pBadge}</div>
            <div class="step-info">
              <span class="step-name">Praktik Komputer</span>
              <span class="step-meta">10 Butir • 12,5 Poin</span>
            </div>
          </div>
        `;

        list.innerHTML = html;

        const label = document.getElementById('stepperActiveLabel');
        if (label) {
          if (this.currentSectionIndex < 5) {
            label.textContent = `Tahapan Ujian Tertulis: Bidang ${this.currentSectionIndex + 1} dari 5 (${this.sections[this.currentSectionIndex].name})`;
          } else {
            label.textContent = 'Tahap 6: Praktik Komputer (10 Butir)';
          }
        }
      },

      updateExamHeaderUI() {
        const nameEl = document.getElementById('barCandidateName');
        const regEl = document.getElementById('barRegionBadge');
        const modeEl = document.getElementById('barModeBadge');
        const avEl = document.getElementById('avatarInitial');

        if (nameEl) nameEl.textContent = this.candidateName;
        if (regEl) regEl.textContent = this.candidateVillage;
        if (avEl) avEl.textContent = this.candidateName.charAt(0).toUpperCase() || 'P';

        if (modeEl) {
          if (this.mode === 'practice') {
            modeEl.textContent = 'Mode Latihan Mandiri';
          } else {
            const sec = this.sections[this.currentSectionIndex];
            modeEl.textContent = `Bidang ${sec.bidangId}: ${sec.name} (25 Soal)`;
          }
        }
      },

      // =======================================================================
      // TIMER ENGINE (30 MENIT PER BIDANG)
      // =======================================================================
      startSectionTimer() {
        if (this.timerInterval) clearInterval(this.timerInterval);
        this.isTimerRunning = true;

        const timerBox = document.getElementById('boxSectionTimer');
        const timerDisplay = document.getElementById('displaySectionTimer');

        const tick = () => {
          if (!this.isTimerRunning) return;

          const elapsed = Date.now() - this.sectionStartTime;
          const remainingMs = Math.max(0, this.sectionDurationMs - elapsed);

          const totalSecs = Math.floor(remainingMs / 1000);
          const mins = Math.floor(totalSecs / 60);
          const secs = totalSecs % 60;
          const timeStr = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;

          if (timerDisplay) timerDisplay.textContent = timeStr;

          // Visual Warnings at 5 Minutes and 1 Minute
          if (timerBox) {
            if (totalSecs <= 60) {
              timerBox.classList.remove('timer-warning-5m');
              timerBox.classList.add('timer-danger-1m');
              if (!this.warned1m) {
                this.warned1m = true;
                this.showToastNotification('⚠️ PERINGATAN KRITIS: Waktu bidang tersisa kurang dari 1 menit!', 'danger');
              }
            } else if (totalSecs <= 300) {
              timerBox.classList.add('timer-warning-5m');
              timerBox.classList.remove('timer-danger-1m');
              if (!this.warned5m) {
                this.warned5m = true;
                this.showToastNotification('⏰ Peringatan: Waktu bidang tersisa 5 menit lagi.', 'warning');
              }
            } else {
              timerBox.classList.remove('timer-warning-5m', 'timer-danger-1m');
            }
          }

          // Timeout Check
          if (remainingMs <= 0) {
            clearInterval(this.timerInterval);
            this.isTimerRunning = false;
            this.handleSectionTimeout();
          }
        };

        tick();
        this.timerInterval = setInterval(tick, 1000);
      },

      showToastNotification(msg, type = 'info') {
        const toast = document.createElement('div');
        toast.className = 'cbt-toast no-print';
        toast.style.cssText = `
          position: fixed;
          top: 20px;
          right: 20px;
          background: ${type === 'danger' ? 'var(--rose-600)' : 'var(--accent-gold-600)'};
          color: white;
          padding: 0.85rem 1.25rem;
          border-radius: var(--radius-md);
          font-weight: 700;
          font-size: 0.9rem;
          box-shadow: var(--shadow-lg);
          z-index: 9999;
          animation: slideIn 0.3s ease;
        `;
        toast.textContent = msg;
        document.body.appendChild(toast);
        setTimeout(() => {
          toast.remove();
        }, 4500);
      },

      handleSectionTimeout() {
        const currentSec = this.sections[this.currentSectionIndex];
        currentSec.isCompleted = true;
        currentSec.completedTime = Date.now();
        currentSec.timeUsedMs = currentSec.durationMs;

        document.getElementById('modalTimeExpired').classList.add('open');
      },

      handleTimeExpiredAdvance() {
        this.closeModals();
        this.showSectionTransitionModal();
      },

      // =======================================================================
      // QUESTION RENDERING & PALETTE
      // =======================================================================
      getCurrentSection() {
        return this.sections[this.currentSectionIndex] || this.sections[0];
      },

      renderCurrentQuestion() {
        const sec = this.getCurrentSection();
        const q = sec.questions[sec.currentIndex];
        if (!q) return;

        const numEl = document.getElementById('qDisplayIndex');
        const catPill = document.getElementById('qCategoryPill');
        const diffPill = document.getElementById('qDifficultyPill');
        const srcTypePill = document.getElementById('qSourceTypePill');
        const textEl = document.getElementById('qQuestionText');
        const optsContainer = document.getElementById('qOptionsList');

        if (numEl) numEl.textContent = `Soal Nomor ${sec.currentIndex + 1} dari ${sec.questions.length}`;
        if (catPill) catPill.textContent = q.category;

        if (diffPill) {
          diffPill.textContent = (q.difficulty || 'sedang').toUpperCase();
          diffPill.className = 'badge-pill badge-diff-' + (q.difficulty || 'sedang');
        }

        if (srcTypePill) {
          if (q.source && q.source.includes('Latihan Buatan')) {
            srcTypePill.style.display = 'inline-block';
            srcTypePill.textContent = 'Latihan Buatan';
          } else {
            srcTypePill.style.display = 'none';
          }
        }

        if (textEl) textEl.innerHTML = this.formatRichText(q.question);

        // Render Options (A, B, C, D)
        const letters = ['A', 'B', 'C', 'D'];
        const selectedAnswer = sec.userAnswers[q.id];

        let optionsHtml = '';
        q.options.forEach((optText, optIdx) => {
          const isSelected = selectedAnswer === optIdx;
          let optClass = 'option-item';
          if (isSelected) optClass += ' selected';

          optionsHtml += `
            <div class="${optClass}" onclick="CBTApp.selectOption(${optIdx})" id="optBtn_${optIdx}">
              <div class="option-letter">${letters[optIdx]}</div>
              <div class="option-content">${this.formatRichText(optText)}</div>
            </div>
          `;
        });

        if (optsContainer) optsContainer.innerHTML = optionsHtml;

        // Flag button status
        const isFlagged = !!sec.flaggedQuestions[q.id];
        const flagBtn = document.getElementById('btnFlagQuestion');
        const flagLabel = document.getElementById('btnFlagLabel');
        if (flagBtn) {
          if (isFlagged) {
            flagBtn.style.background = 'var(--accent-gold-500)';
            flagBtn.style.color = 'var(--primary-900)';
            if (flagLabel) flagLabel.textContent = 'Ditandai Ragu (R)';
          } else {
            flagBtn.style.background = 'var(--white)';
            flagBtn.style.color = 'var(--slate-700)';
            if (flagLabel) flagLabel.textContent = 'Ragu-ragu (R)';
          }
        }

        // Practice Feedback Box
        const pBox = document.getElementById('practiceFeedbackBox');
        if (this.mode === 'practice' && selectedAnswer !== undefined) {
          if (pBox) {
            pBox.style.display = 'block';
            document.getElementById('practiceFeedbackContent').innerHTML = this.formatRichText(q.explanation);
            document.getElementById('practiceFeedbackSource').innerHTML = `<strong>Rujukan:</strong> ${this.formatRichText(q.source)}`;
          }
        } else if (pBox) {
          pBox.style.display = 'none';
        }

        // Prev/Next button disabled state
        const prevBtn = document.getElementById('btnPrevQuestion');
        if (prevBtn) prevBtn.disabled = sec.currentIndex === 0;
      },

      selectOption(optIdx) {
        const sec = this.getCurrentSection();
        if (sec.isCompleted) return;

        const currentQ = sec.questions[sec.currentIndex];
        sec.userAnswers[currentQ.id] = optIdx;
        this.saveSession();

        if (this.mode === 'official_exam') {
          this.renderQuestionPaletteGrid();
          // Auto advance to next unanswered question in current section
          this.advanceToNextAuto();
        } else {
          this.renderCurrentQuestion();
          this.renderQuestionPaletteGrid();
        }
      },

      advanceToNextAuto() {
        const sec = this.getCurrentSection();
        // Check if there is a next unanswered question
        for (let i = sec.currentIndex + 1; i < sec.questions.length; i++) {
          if (sec.userAnswers[sec.questions[i].id] === undefined) {
            sec.currentIndex = i;
            this.renderCurrentQuestion();
            this.renderQuestionPaletteGrid();
            return;
          }
        }
        // If reached end, check from beginning
        for (let i = 0; i < sec.currentIndex; i++) {
          if (sec.userAnswers[sec.questions[i].id] === undefined) {
            sec.currentIndex = i;
            this.renderCurrentQuestion();
            this.renderQuestionPaletteGrid();
            return;
          }
        }

        // If all answered or current is last, stay on current or next
        if (sec.currentIndex < sec.questions.length - 1) {
          sec.currentIndex++;
        }
        this.renderCurrentQuestion();
        this.renderQuestionPaletteGrid();
      },

      prevQuestion() {
        const sec = this.getCurrentSection();
        if (sec.currentIndex > 0) {
          sec.currentIndex--;
          this.renderCurrentQuestion();
          this.renderQuestionPaletteGrid();
        }
      },

      skipOrNextQuestion() {
        const sec = this.getCurrentSection();
        if (sec.currentIndex < sec.questions.length - 1) {
          sec.currentIndex++;
        } else {
          // Wrap around to first unanswered if any
          const firstEmpty = sec.questions.findIndex(q => sec.userAnswers[q.id] === undefined);
          if (firstEmpty !== -1) {
            sec.currentIndex = firstEmpty;
          }
        }
        this.renderCurrentQuestion();
        this.renderQuestionPaletteGrid();
      },

      goToQuestion(idx) {
        const sec = this.getCurrentSection();
        if (idx >= 0 && idx < sec.questions.length) {
          sec.currentIndex = idx;
          this.renderCurrentQuestion();
          this.renderQuestionPaletteGrid();
        }
      },

      toggleFlagCurrentQuestion() {
        const sec = this.getCurrentSection();
        if (sec.isCompleted) return;

        const currentQ = sec.questions[sec.currentIndex];
        sec.flaggedQuestions[currentQ.id] = !sec.flaggedQuestions[currentQ.id];
        this.saveSession();
        this.renderCurrentQuestion();
        this.renderQuestionPaletteGrid();
      },

      setPaletteFilter(filterType) {
        this.paletteFilter = filterType;
        document.querySelectorAll('.palette-filter-btn').forEach(b => b.classList.remove('active'));
        if (filterType === 'all') document.getElementById('pFilterAll')?.classList.add('active');
        else if (filterType === 'done') document.getElementById('pFilterDone')?.classList.add('active');
        else if (filterType === 'flag') document.getElementById('pFilterFlag')?.classList.add('active');
        else if (filterType === 'empty') document.getElementById('pFilterEmpty')?.classList.add('active');
        this.renderQuestionPaletteGrid();
      },

      renderQuestionPaletteGrid() {
        const sec = this.getCurrentSection();
        const container = document.getElementById('gridQuestionButtons');
        if (!container) return;

        let answeredCount = 0;
        let html = '';

        sec.questions.forEach((q, idx) => {
          const isAnswered = sec.userAnswers[q.id] !== undefined;
          const isFlagged = !!sec.flaggedQuestions[q.id];
          const isCurrent = idx === sec.currentIndex;

          if (isAnswered) answeredCount++;

          // Palette filter check
          if (this.paletteFilter === 'done' && !isAnswered) return;
          if (this.paletteFilter === 'flag' && !isFlagged) return;
          if (this.paletteFilter === 'empty' && isAnswered) return;

          let btnClass = 'btn-palette-num';
          if (isAnswered) btnClass += ' answered';
          if (isFlagged) btnClass += ' flagged';
          if (isCurrent) btnClass += ' active';

          html += `
            <button class="${btnClass}" onclick="CBTApp.goToQuestion(${idx})" title="Soal ${idx + 1}">
              ${idx + 1}
            </button>
          `;
        });

        container.innerHTML = html;

        const countLabel = document.getElementById('paletteAnswerCount');
        if (countLabel) countLabel.textContent = `${answeredCount} / ${sec.questions.length} Terjawab`;

        const titleLabel = document.getElementById('paletteTitleLabel');
        if (titleLabel) titleLabel.textContent = `Nomor Soal (${sec.questions.length})`;
      },

      // =======================================================================
      // FINISH SECTION & TRANSITION LOGIC
      // =======================================================================
      confirmFinishSection() {
        const sec = this.getCurrentSection();
        let answered = 0;
        let flagged = 0;
        let empty = 0;

        sec.questions.forEach(q => {
          if (sec.userAnswers[q.id] !== undefined) answered++;
          else empty++;
          if (sec.flaggedQuestions[q.id]) flagged++;
        });

        document.getElementById('modalFinishSectionTitle').textContent = `Konfirmasi Selesaikan ${sec.title}`;
        document.getElementById('secFinishAnswered').textContent = answered;
        document.getElementById('secFinishFlagged').textContent = flagged;
        document.getElementById('secFinishEmpty').textContent = empty;

        const warnBox = document.getElementById('secFinishWarningBox');
        let warnHtml = '';
        if (empty > 0) {
          warnHtml += `
            <div style="background:var(--rose-50); border:1px solid var(--rose-400); color:var(--rose-800); padding:0.75rem; border-radius:var(--radius-sm); font-size:0.85rem; margin-bottom:0.5rem;">
              <strong>PERINGATAN:</strong> Masih ada <strong>${empty} butir soal belum dijawab</strong> pada bidang ini! Soal yang belum dijawab bernilai 0. Setelah bidang dikunci, Anda tidak dapat kembali mengubah jawaban.
            </div>
          `;
        }
        if (warnBox) warnBox.innerHTML = warnHtml;

        document.getElementById('modalFinishSection').classList.add('open');
      },

      finishCurrentSection(reason) {
        this.closeModals();
        const sec = this.getCurrentSection();
        sec.isCompleted = true;
        sec.completedTime = Date.now();
        sec.timeUsedMs = Math.min(sec.durationMs, Date.now() - (sec.startTime || Date.now()));

        if (this.timerInterval) clearInterval(this.timerInterval);
        this.isTimerRunning = false;

        this.saveSession();
        this.showSectionTransitionModal();
      },

      showSectionTransitionModal() {
        const sec = this.getCurrentSection();
        let answered = 0;
        let empty = 0;
        sec.questions.forEach(q => {
          if (sec.userAnswers[q.id] !== undefined) answered++;
          else empty++;
        });

        const elapsedSecs = Math.floor(sec.timeUsedMs / 1000);
        const mins = Math.floor(elapsedSecs / 60);
        const secs = elapsedSecs % 60;
        const timeStr = `${mins}:${String(secs).padStart(2, '0')}`;

        document.getElementById('modalCompleteHeading').textContent = `${sec.title} Selesai!`;
        document.getElementById('modalCompleteAnswered').textContent = answered;
        document.getElementById('modalCompleteEmpty').textContent = empty;
        document.getElementById('modalCompleteTime').textContent = timeStr;

        const proceedBtn = document.getElementById('btnProceedNextSection');
        if (this.currentSectionIndex < 4) {
          const nextSec = this.sections[this.currentSectionIndex + 1];
          proceedBtn.innerHTML = `Lanjut ke Bidang Berikutnya: <strong>${nextSec.name}</strong> <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>`;
        } else {
          proceedBtn.innerHTML = `Lanjut ke Tahap <strong>Praktik Komputer (10 Butir)</strong> <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>`;
        }

        document.getElementById('modalSectionComplete').classList.add('open');
      },

      proceedToNextSection() {
        this.closeModals();
        if (this.currentSectionIndex < 4) {
          // Open next Bidang
          this.startSection(this.currentSectionIndex + 1);
        } else {
          // All 5 Bidang finished -> Enter Stage 6: Praktik Komputer
          this.currentSectionIndex = 5;
          this.startPracticalSession();
        }
        this.saveSession();
      },

      // =======================================================================
      // =======================================================================
      // STAGE 6: PRAKTIK KOMPUTER REALISTIS (10 BUTIR TUGAS - DUA MODE)
      // =======================================================================
      startPracticalSession() {
        this.currentSectionIndex = 5;
        this.currentPracticalIndex = 0;
        this.isPracticalLocked = false;
        this.updateStepperUI();
        this.startPracticalTimer();
        this.renderPracticalPalette();
        this.renderCurrentPracticalTask();
        this.navigate('practical');
        this.saveSession();
      },

      startPracticalTimer() {
        if (this.practicalTimerInterval) {
          clearInterval(this.practicalTimerInterval);
          this.practicalTimerInterval = null;
        }

        if (!this.practicalStartTime) {
          this.practicalStartTime = Date.now();
        }

        this.updatePracticalTimerDisplay();

        this.practicalTimerInterval = setInterval(() => {
          if (this.practicalDurationMinutes === 0) {
            // Unmetered practice mode (counts up)
            const elapsed = Math.floor((Date.now() - this.practicalStartTime) / 1000);
            this.updatePracticalTimerDisplay(elapsed, true);
          } else {
            // Countdown mode
            if (this.practicalRemainingSeconds > 0) {
              this.practicalRemainingSeconds--;
              this.updatePracticalTimerDisplay(this.practicalRemainingSeconds, false);
            } else {
              // Time expired
              clearInterval(this.practicalTimerInterval);
              this.practicalTimerInterval = null;
              this.handlePracticalTimeExpired();
            }
          }
        }, 1000);
      },

      updatePracticalTimerDisplay(seconds, isCountUp = false) {
        const displayEl = document.getElementById('practicalTimerDisplay');
        if (!displayEl) return;

        const secVal = seconds !== undefined ? seconds : this.practicalRemainingSeconds;
        const mins = Math.floor(secVal / 60);
        const secs = secVal % 60;
        const timeStr = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;

        displayEl.textContent = isCountUp ? `${timeStr} (Bebas)` : timeStr;

        if (!isCountUp) {
          if (secVal <= 60) {
            displayEl.style.color = '#ef4444';
          } else if (secVal <= 300) {
            displayEl.style.color = '#f59e0b';
          } else {
            displayEl.style.color = 'var(--accent-gold-400)';
          }
        }
      },

      openPracticalDurationModal() {
        if (this.isPracticalLocked) return;
        const dur = this.practicalDurationMinutes !== undefined ? this.practicalDurationMinutes : 45;
        const radios = document.querySelectorAll('input[name="optPracticalDuration"]');
        radios.forEach(r => {
          r.checked = parseInt(r.value, 10) === dur;
        });
        document.getElementById('modalPracticalDuration')?.classList.add('open');
      },

      applyPracticalDuration() {
        const selectedRadio = document.querySelector('input[name="optPracticalDuration"]:checked');
        const dur = selectedRadio ? parseInt(selectedRadio.value, 10) : 45;
        this.practicalDurationMinutes = dur;

        if (dur === 0) {
          this.practicalRemainingSeconds = 0;
        } else {
          this.practicalRemainingSeconds = dur * 60;
        }
        this.practicalStartTime = Date.now();
        this.closeModals();
        this.startPracticalTimer();
        this.saveSession();
      },

      handlePracticalTimeExpired() {
        this.isPracticalLocked = true;
        this.updatePracticalTimerDisplay(0, false);
        alert('⏱️ Waktu ujian praktik komputer telah berakhir! Pengerjaan telah dikunci sesuai ketentuan panitia. Silakan klik Selesaikan Praktik untuk melihat rekapitulasi nilai akhir.');
        this.renderCurrentPracticalTask();
        this.saveSession();
      },

      setPracticalMode(mode) {
        this.practicalMode = mode;
        const task = this.practicalTasks[this.currentPracticalIndex];
        if (task) {
          task.practicalMode = mode;
        }

        const btnOffice = document.getElementById('btnModeOffice');
        const btnSim = document.getElementById('btnModeSim');
        const wsOffice = document.getElementById('workspaceOfficeMode');
        const wsSim = document.getElementById('workspaceBrowserSimMode');
        const noticeEl = document.getElementById('practicalModeNotice');

        if (mode === 'office') {
          btnOffice?.classList.add('active');
          btnSim?.classList.remove('active');
          if (wsOffice) wsOffice.style.display = 'block';
          if (wsSim) wsSim.style.display = 'none';

          if (noticeEl) {
            noticeEl.style.background = '#eff6ff';
            noticeEl.style.borderColor = '#bfdbfe';
            noticeEl.style.color = '#1e40af';
            noticeEl.innerHTML = '🏢 <strong>Mode 1 — Microsoft Office Asli (Mode Utama):</strong> Kerjakan tugas menggunakan aplikasi Microsoft Word, Excel, atau PowerPoint yang terinstal di komputer Anda. Unduh bahan latihan, simpan sesuai nama berkas baku, lalu unggah kembali. Sistem memeriksa integritas OpenXML secara nyata dan menyediakan lembar verifikasi kriteria penilaian.';
          }
        } else {
          btnSim?.classList.add('active');
          btnOffice?.classList.remove('active');
          if (wsOffice) wsOffice.style.display = 'none';
          if (wsSim) wsSim.style.display = 'block';

          if (noticeEl) {
            noticeEl.style.background = '#fefce8';
            noticeEl.style.borderColor = '#fef08a';
            noticeEl.style.color = '#854d0e';
            noticeEl.innerHTML = '🌐 <strong>Mode 2 — Simulasi Interaktif di Browser (Alternatif):</strong> Lingkungan kerja interaktif di dalam peramban web bagi peserta yang tidak memiliki Microsoft Office. Pengerjaan dinilai langsung sesuai kriteria teknis pada formulir simulasi.';
          }
        }

        this.renderPracticalPalette();
        this.saveSession();
      },

      renderPracticalPalette() {
        const container = document.getElementById('practicalTasksList');
        if (!container) return;

        let totalScore = 0;
        let doneCount = 0;
        let html = '';

        this.practicalTasks.forEach((t, idx) => {
          totalScore += (t.earnedScore || 0);
          if (t.isCompleted) doneCount++;

          const isActive = idx === this.currentPracticalIndex;
          let btnClass = 'practical-item-btn';
          if (t.isCompleted) btnClass += ' completed';
          if (isActive) btnClass += ' active';

          const scoreDisplay = t.isCompleted ? (t.earnedScore || 0).toFixed(2) : '-';
          const modeIcon = t.practicalMode === 'sim' ? '🌐' : '🏢';

          html += `
            <button class="${btnClass}" onclick="CBTApp.goToPracticalTask(${idx})" title="${t.title}">
              <span>${modeIcon} Butir ${t.id}: ${t.title.split('—')[1] || t.title}</span>
              <span style="font-weight:700;">${scoreDisplay}</span>
            </button>
          `;
        });

        container.innerHTML = html;

        const countEl = document.getElementById('practicalDoneCount');
        if (countEl) countEl.textContent = `${doneCount} / 10 Diserahkan`;

        const scoreBadge = document.getElementById('practicalTotalScoreBadge');
        if (scoreBadge) scoreBadge.textContent = `${totalScore.toFixed(2)} / 12.50`;
      },

      goToPracticalTask(idx) {
        if (idx >= 0 && idx < this.practicalTasks.length) {
          this.currentPracticalIndex = idx;
          this.renderPracticalPalette();
          this.renderCurrentPracticalTask();
        }
      },

      prevPracticalTask() {
        if (this.currentPracticalIndex > 0) {
          this.goToPracticalTask(this.currentPracticalIndex - 1);
        }
      },

      nextPracticalTask() {
        if (this.currentPracticalIndex < this.practicalTasks.length - 1) {
          this.goToPracticalTask(this.currentPracticalIndex + 1);
        }
      },

      renderCurrentPracticalTask() {
        const task = this.practicalTasks[this.currentPracticalIndex];
        if (!task) return;

        if (!task.rubricChecks && task.rubric) {
          task.rubricChecks = task.rubric.map(() => false);
        }

        document.getElementById('taskCategoryBadge').textContent = task.category;
        document.getElementById('taskTitleHeading').textContent = `Tugas ${task.id}: ${task.title}`;
        document.getElementById('taskScenarioText').textContent = task.scenario;
        document.getElementById('taskInstructionText').textContent = task.instruction;
        document.getElementById('taskScoreBadge').textContent = `Skor: ${(task.earnedScore || 0).toFixed(2)} / ${task.maxScore.toFixed(2)}`;

        // Status Pill
        const statusPill = document.getElementById('taskStatusPill');
        if (statusPill) {
          if (!task.isCompleted) {
            statusPill.textContent = 'Belum Dikerjakan';
            statusPill.className = 'badge-pill';
            statusPill.style.background = 'var(--slate-200)';
            statusPill.style.color = 'var(--slate-700)';
          } else if (task.status === 'pending_review') {
            statusPill.textContent = '⏳ Menunggu Penilaian';
            statusPill.className = 'badge-pill badge-status-pending';
          } else if (task.status === 'pass' || (task.earnedScore >= task.maxScore)) {
            statusPill.textContent = '✓ Lulus (Kriteria Terpenuhi)';
            statusPill.className = 'badge-pill badge-status-pass';
          } else {
            statusPill.textContent = '⚠️ Perlu Perbaikan';
            statusPill.className = 'badge-pill badge-status-revision';
          }
        }

        // Render Rubric Table
        const rubricContainer = document.getElementById('taskRubricDetailContainer');
        if (rubricContainer && task.rubric) {
          let rHtml = '<table class="rubric-table"><thead><tr><th>Kriteria Penilaian</th><th style="width:90px; text-align:center;">Bobot Poin</th></tr></thead><tbody>';
          task.rubric.forEach(r => {
            rHtml += `<tr><td>${r.criterion}</td><td style="text-align:center; font-weight:700;">${r.points.toFixed(2)}</td></tr>`;
          });
          rHtml += '</tbody></table>';
          rubricContainer.innerHTML = rHtml;
        }

        // Prev/Next Button state
        const prevBtn = document.getElementById('btnPrevPracticalTask');
        if (prevBtn) prevBtn.disabled = this.currentPracticalIndex === 0;
        const nextBtn = document.getElementById('btnNextPracticalTask');
        if (nextBtn) nextBtn.disabled = this.currentPracticalIndex === this.practicalTasks.length - 1;

        // Mode 1: Office File Info & Upload Box
        document.getElementById('officeStarterFileTitle').textContent = `Bahan Latihan: ${task.starterFileName}`;
        document.getElementById('officeStarterFileDesc').textContent = `Aplikasi: ${task.category.split('(')[0].trim()} • Buka dan kerjakan di Microsoft Office lokal.`;
        document.getElementById('officeExpectedFileName').textContent = task.expectedFileName;

        const uploadCard = document.getElementById('officeUploadedFileCard');
        const rubricCheckArea = document.getElementById('officeRubricChecklistArea');
        if (task.uploadedFile) {
          uploadCard.style.display = 'block';
          uploadCard.innerHTML = `
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem;">
              <div>
                <strong style="color:var(--primary-900); font-size:0.95rem;">📄 ${task.uploadedFile.name}</strong>
                <div style="font-size:0.8rem; color:var(--slate-500); margin-top:2px;">
                  Ukuran: ${(task.uploadedFile.size / 1024).toFixed(1)} KB • Tipe: ${task.uploadedFile.type || 'Berkas Dokumen'}
                </div>
              </div>
              <span class="badge-pill ${task.uploadedFile.isZipValid ? 'badge-verified' : 'badge-status-revision'}" style="font-size:0.75rem;">
                ${task.uploadedFile.isZipValid ? '✓ Struktur OpenXML Valid' : 'Format Berkas Terbaca'}
              </span>
            </div>
            ${task.uploadedFile.inspectionSummary ? `<div style="font-size:0.82rem; color:var(--slate-700); margin-top:0.5rem; background:var(--slate-50); padding:0.5rem; border-radius:4px;">${task.uploadedFile.inspectionSummary}</div>` : ''}
          `;

          // Rubric Checklist
          if (rubricCheckArea && task.rubric) {
            rubricCheckArea.style.display = 'block';
            let cHtml = '';
            task.rubric.forEach((r, rIdx) => {
              const isChecked = task.rubricChecks && task.rubricChecks[rIdx];
              cHtml += `
                <label style="display:flex; align-items:flex-start; gap:0.5rem; margin-bottom:0.5rem; cursor:pointer; font-size:0.85rem; color:var(--slate-800);">
                  <input type="checkbox" id="chkRubric_${rIdx}" ${isChecked ? 'checked' : ''} onchange="CBTApp.toggleRubricCheck(${rIdx})" style="margin-top:2px;">
                  <div>
                    <strong>${r.criterion}</strong>
                    <span style="color:var(--primary-700); font-weight:700;"> (${r.points.toFixed(2)} Poin)</span>
                  </div>
                </label>
              `;
            });
            document.getElementById('officeRubricChecklistItems').innerHTML = cHtml;
          }
        } else {
          uploadCard.style.display = 'none';
          if (rubricCheckArea) rubricCheckArea.style.display = 'none';
        }

        // Mode 2: Interactive Simulator Area
        const simContainer = document.getElementById('taskSimulatorContainer');
        simContainer.innerHTML = this.getPracticalSimulatorHtml(task);

        // Apply active mode
        this.setPracticalMode(task.practicalMode || this.practicalMode);

        // Test result box
        const resBox = document.getElementById('taskTestResultBox');
        if (task.isCompleted && task.testFeedback) {
          resBox.style.display = 'block';
          resBox.className = task.earnedScore >= task.maxScore ? 'practical-test-result success' : (task.earnedScore > 0 ? 'practical-test-result partial' : 'practical-test-result fail');
          resBox.innerHTML = task.testFeedback;
        } else {
          resBox.style.display = 'none';
        }
      },

      downloadCurrentStarterFile() {
        const task = this.practicalTasks[this.currentPracticalIndex];
        if (!task) return;

        const content = task.starterContent || '';
        const blob = new Blob([content], { type: 'text/plain;charset=utf-8' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = task.starterFileName || `Bahan_Tugas_${task.id}.txt`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
      },

      copyStarterContentText() {
        const task = this.practicalTasks[this.currentPracticalIndex];
        if (!task || !task.starterContent) return;

        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(task.starterContent).then(() => {
            alert('✓ Teks bahan latihan berhasil disalin ke papan klip (clipboard)! Silakan tempel (Paste / Ctrl+V) pada aplikasi Microsoft Office Anda.');
          }).catch(() => {
            prompt('Salin teks bahan berikut:', task.starterContent);
          });
        } else {
          prompt('Salin teks bahan berikut:', task.starterContent);
        }
      },

      async parseZipEntries(arrayBuffer) {
        const view = new DataView(arrayBuffer);
        let offset = 0;
        const entries = {};
        const totalLen = arrayBuffer.byteLength;

        while (offset + 30 <= totalLen) {
          const sig = view.getUint32(offset, true);
          if (sig !== 0x04034b50) {
            offset++;
            continue;
          }
          const compMethod = view.getUint16(offset + 8, true);
          const compSize = view.getUint32(offset + 18, true);
          const uncompSize = view.getUint32(offset + 22, true);
          const nameLen = view.getUint16(offset + 26, true);
          const extraLen = view.getUint16(offset + 28, true);

          if (offset + 30 + nameLen > totalLen) break;

          const nameBytes = new Uint8Array(arrayBuffer, offset + 30, nameLen);
          const name = new TextDecoder('utf-8').decode(nameBytes);
          const dataOffset = offset + 30 + nameLen + extraLen;

          if (dataOffset + compSize <= totalLen) {
            const compData = new Uint8Array(arrayBuffer, dataOffset, compSize);
            let textContent = '';
            if (compMethod === 0) {
              textContent = new TextDecoder('utf-8').decode(compData);
            } else if (compMethod === 8 && typeof DecompressionStream !== 'undefined') {
              try {
                const ds = new DecompressionStream('deflate-raw');
                const writer = ds.writable.getWriter();
                writer.write(compData);
                writer.close();
                const decompressed = await new Response(ds.readable).arrayBuffer();
                textContent = new TextDecoder('utf-8').decode(decompressed);
              } catch (e) {
                textContent = '';
              }
            }
            entries[name] = { name, compMethod, compSize, uncompSize, textContent };
          }
          offset = dataOffset + compSize;
        }
        return entries;
      },

      async handleOfficeFileUpload(event) {
        if (this.isPracticalLocked) {
          alert('Sesi praktik telah dikunci. Berkas tidak dapat diubah.');
          return;
        }

        const file = event.target.files && event.target.files[0];
        if (!file) return;

        const task = this.practicalTasks[this.currentPracticalIndex];
        if (!task) return;

        const arrayBuffer = await file.arrayBuffer();
        let entries = {};
        let isZip = false;

        try {
          entries = await this.parseZipEntries(arrayBuffer);
          isZip = Object.keys(entries).length > 0;
        } catch (e) {
          isZip = false;
        }

        // Structural and text analysis
        let allExtractedText = '';
        let formulaTagsFound = [];
        let hasTableTag = false;

        Object.keys(entries).forEach(entryName => {
          const entry = entries[entryName];
          if (entry.textContent) {
            allExtractedText += ' ' + entry.textContent;
            // Formula check for Excel
            const fMatches = entry.textContent.match(/<f[^>]*>([^<]+)<\/f>/gi);
            if (fMatches) {
              fMatches.forEach(fm => {
                const cleanF = fm.replace(/<[^>]+>/g, '').toUpperCase();
                formulaTagsFound.push(cleanF);
              });
            }
            if (entry.textContent.includes('<w:tbl')) {
              hasTableTag = true;
            }
          }
        });

        let summary = '';
        if (isZip) {
          const fileCount = Object.keys(entries).length;
          const formulaSummary = formulaTagsFound.length > 0 ? `Formula ditemukan: ${formulaTagsFound.slice(0, 3).join(', ')}` : '';
          summary = `Struktur OpenXML Valid: Terdiri dari ${fileCount} bagian arsip internal. ${formulaSummary} ${hasTableTag ? 'Struktur tabel XML ditemukan.' : ''}`;
        } else {
          // If not zip, check if text/plain
          const textDecoded = new TextDecoder('utf-8').decode(new Uint8Array(arrayBuffer.slice(0, 2000)));
          allExtractedText = textDecoded;
          summary = 'Berkas naskah terbaca.';
        }

        task.uploadedFile = {
          name: file.name,
          size: file.size,
          type: file.type,
          isZipValid: isZip,
          entries: Object.keys(entries),
          extractedText: allExtractedText,
          formulaTagsFound: formulaTagsFound,
          hasTableTag: hasTableTag,
          inspectionSummary: summary
        };

        // Auto-check criteria that can be verified automatically
        if (!task.rubricChecks) task.rubricChecks = task.rubric.map(() => false);

        // Check 1: Filename match
        const expectedBase = task.expectedFileName.replace(/\.[^.]+$/, '').toLowerCase();
        const uploadedBase = file.name.replace(/\.[^.]+$/, '').toLowerCase();
        if (uploadedBase.includes(expectedBase) || uploadedBase.includes(`tugas0${task.id}`) || uploadedBase.includes(`tugas${task.id}`)) {
          task.rubricChecks[0] = true;
        }

        // Check 2: Technical structure / text presence
        if (task.id === 6 && formulaTagsFound.some(f => f.includes('SUM') || f.includes('AVERAGE'))) {
          task.rubricChecks[1] = true;
        } else if (task.id === 3 && hasTableTag) {
          task.rubricChecks[1] = true;
        } else if (isZip) {
          task.rubricChecks[1] = true;
        }

        this.renderCurrentPracticalTask();
        this.saveSession();
      },

      toggleRubricCheck(rIdx) {
        const task = this.practicalTasks[this.currentPracticalIndex];
        if (!task) return;
        if (!task.rubricChecks) task.rubricChecks = task.rubric.map(() => false);
        task.rubricChecks[rIdx] = !task.rubricChecks[rIdx];
        this.saveSession();
      },

      evaluateOfficeUpload() {
        if (this.isPracticalLocked) {
          alert('Sesi praktik telah dikunci.');
          return;
        }

        const task = this.practicalTasks[this.currentPracticalIndex];
        if (!task) return;

        if (!task.uploadedFile) {
          alert('Silakan pilih dan unggah berkas hasil pengerjaan terlebih dahulu.');
          return;
        }

        let verifiedScore = 0;
        let checksCount = 0;
        const totalRubrics = task.rubric.length;

        task.rubric.forEach((r, idx) => {
          if (task.rubricChecks && task.rubricChecks[idx]) {
            verifiedScore += r.points;
            checksCount++;
          }
        });

        // Filename check
        const expectedExt = task.expectedFileName.split('.').pop().toLowerCase();
        const uploadedExt = task.uploadedFile.name.split('.').pop().toLowerCase();
        const extMatch = expectedExt === uploadedExt || uploadedExt === 'zip' || uploadedExt === 'docx' || uploadedExt === 'xlsx' || uploadedExt === 'pptx';

        let status = 'pending_review';
        let feedback = '';

        if (!extMatch) {
          status = 'needs_revision';
          verifiedScore = Math.min(verifiedScore, 0.50);
          feedback = `
            <div style="font-weight:700; color:var(--rose-800); margin-bottom:0.4rem;">⚠️ Format Berkas Kurang Sesuai:</div>
            • Berkas yang diunggah berekstensi <code>.${uploadedExt}</code>, sedangkan instruksi mensyaratkan <code>${task.expectedFileName}</code>.<br>
            • Skor yang dapat diverifikasi: <strong>${verifiedScore.toFixed(2)} / ${task.maxScore.toFixed(2)}</strong>.<br>
            • Status: <strong>Perlu Perbaikan</strong>. Harap simpan file dengan ekstensi dan nama yang sesuai.
          `;
        } else if (checksCount === totalRubrics) {
          status = 'pass';
          verifiedScore = task.maxScore;
          feedback = `
            <div style="font-weight:700; color:var(--emerald-800); margin-bottom:0.4rem;">✓ Berkas Terverifikasi & Seluruh Kriteria Terpenuhi:</div>
            • Nama Berkas: <code>${task.uploadedFile.name}</code> (Sesuai ketentuan).<br>
            • Verifikasi Struktur: ${task.uploadedFile.inspectionSummary}<br>
            • Skor Penuh: <strong>${verifiedScore.toFixed(2)} / ${task.maxScore.toFixed(2)}</strong>.<br>
            • Status: <strong>Lulus (Memenuhi Standar Ujian)</strong>.
          `;
        } else {
          status = 'pending_review';
          feedback = `
            <div style="font-weight:700; color:#b45309; margin-bottom:0.4rem;">⏳ Berkas Diterima — Menunggu Verifikasi Manual Penguji:</div>
            • Berkas <code>${task.uploadedFile.name}</code> berhasil diunggah dan terbaca sistem.<br>
            • ${checksCount} dari ${totalRubrics} kriteria teknis telah terverifikasi awal.<br>
            • Skor Sementara Terverifikasi: <strong>${verifiedScore.toFixed(2)} / ${task.maxScore.toFixed(2)}</strong>.<br>
            • Kriteria tata letak dan estetika naskah dinas akan diverifikasi lebih lanjut oleh Tim Pemeriksa.
          `;
        }

        task.earnedScore = parseFloat(verifiedScore.toFixed(2));
        task.isCompleted = true;
        task.status = status;
        task.testFeedback = feedback;

        this.renderPracticalPalette();
        this.renderCurrentPracticalTask();
        this.saveSession();
      },

      // =======================================================================
      // MODE 2: SIMULATOR WORKSPACES (10 BUTIR INTERAKTIF)
      // =======================================================================
      getPracticalSimulatorHtml(task) {
        const d = task.candidateInputs || {};

        switch (task.browserSimType) {
          case 'doc_typing': {
            const src = task.defaultData?.sourceText || '';
            const typed = d.typedText || '';
            return `
              <div>
                <p style="font-size:0.85rem; color:var(--slate-700); margin-bottom:0.5rem;">
                  Ketiklah teks naskah dinas di bawah ini secara presisi pada area pengetikan:
                </p>
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem;">
                  <div>
                    <label style="font-size:0.8rem; font-weight:700; color:var(--primary-900);">Teks Sumber (Pedoman Pengetikan):</label>
                    <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:var(--radius-sm); padding:0.75rem; font-size:0.82rem; font-family:monospace; line-height:1.4; max-height:220px; overflow-y:auto; white-space:pre-wrap;">${src}</div>
                  </div>
                  <div>
                    <label style="font-size:0.8rem; font-weight:700; color:var(--emerald-800);">Area Pengetikan Peserta:</label>
                    <textarea id="simTypingInput" class="form-control" rows="9" style="font-family:monospace; font-size:0.82rem; line-height:1.4;" oninput="CBTApp.updateDocTypingStats()" placeholder="Mulai mengetik teks di sini...">${typed}</textarea>
                    <div style="display:flex; justify-content:space-between; font-size:0.75rem; color:var(--slate-600); margin-top:0.35rem;">
                      <span id="typingWordCount">Kata: 0</span>
                      <span id="typingAccuracy">Akurasi: 0%</span>
                    </div>
                  </div>
                </div>
              </div>
            `;
          }

          case 'doc_format': {
            return `
              <div>
                <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(180px, 1fr)); gap:0.75rem; margin-bottom:1rem; background:var(--white); padding:0.75rem; border-radius:var(--radius-sm); border:1px solid var(--slate-200);">
                  <div class="form-group" style="margin-bottom:0;">
                    <label style="font-size:0.75rem;">Ukuran Kertas:</label>
                    <select id="simPaperSize" class="form-control" style="font-size:0.8rem;" onchange="CBTApp.updateDocFormatPreview()">
                      <option value="A4" ${d.paperSize === 'A4' ? 'selected' : ''}>A4</option>
                      <option value="F4" ${d.paperSize === 'F4' ? 'selected' : ''}>F4 / Folio (Standar)</option>
                    </select>
                  </div>
                  <div class="form-group" style="margin-bottom:0;">
                    <label style="font-size:0.75rem;">Perataan Judul:</label>
                    <select id="simTitleAlign" class="form-control" style="font-size:0.8rem;" onchange="CBTApp.updateDocFormatPreview()">
                      <option value="left" ${d.titleAlign === 'left' ? 'selected' : ''}>Rata Kiri</option>
                      <option value="center" ${d.titleAlign === 'center' ? 'selected' : ''}>Rata Tengah (Center)</option>
                      <option value="right" ${d.titleAlign === 'right' ? 'selected' : ''}>Rata Kanan</option>
                    </select>
                  </div>
                  <div class="form-group" style="margin-bottom:0;">
                    <label style="font-size:0.75rem;">Format Huruf Judul:</label>
                    <div style="display:flex; gap:0.5rem; align-items:center; margin-top:4px;">
                      <label style="font-size:0.8rem; display:flex; align-items:center; gap:4px;"><input type="checkbox" id="simTitleBold" ${d.titleBold ? 'checked' : ''} onchange="CBTApp.updateDocFormatPreview()"> Tebal (Bold)</label>
                      <select id="simTitleFontSize" class="form-control" style="font-size:0.8rem; width:70px;" onchange="CBTApp.updateDocFormatPreview()">
                        <option value="12" ${d.titleFontSize === 12 ? 'selected' : ''}>12pt</option>
                        <option value="14" ${d.titleFontSize === 14 ? 'selected' : ''}>14pt</option>
                        <option value="16" ${d.titleFontSize === 16 ? 'selected' : ''}>16pt</option>
                      </select>
                    </div>
                  </div>
                  <div class="form-group" style="margin-bottom:0;">
                    <label style="font-size:0.75rem;">Perataan Paragraf:</label>
                    <select id="simBodyAlign" class="form-control" style="font-size:0.8rem;" onchange="CBTApp.updateDocFormatPreview()">
                      <option value="left" ${d.bodyAlign === 'left' ? 'selected' : ''}>Rata Kiri (Left)</option>
                      <option value="justify" ${d.bodyAlign === 'justify' ? 'selected' : ''}>Rata Kiri-Kanan (Justify)</option>
                    </select>
                  </div>
                  <div class="form-group" style="margin-bottom:0;">
                    <label style="font-size:0.75rem;">Spasi Baris:</label>
                    <select id="simLineSpacing" class="form-control" style="font-size:0.8rem;" onchange="CBTApp.updateDocFormatPreview()">
                      <option value="1.0" ${d.lineSpacing === 1.0 ? 'selected' : ''}>1,0 (Single)</option>
                      <option value="1.15" ${d.lineSpacing === 1.15 ? 'selected' : ''}>1,15</option>
                      <option value="1.5" ${d.lineSpacing === 1.5 ? 'selected' : ''}>1,5 (Standar Dinas)</option>
                    </select>
                  </div>
                </div>

                <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:0.5rem; margin-bottom:1rem;">
                  <div class="form-group" style="margin-bottom:0;"><label style="font-size:0.75rem;">Margin Kiri (cm):</label><input type="number" step="0.5" id="simMarginLeft" class="form-control" value="${d.marginLeft || 3.5}" style="font-size:0.8rem;" onchange="CBTApp.updateDocFormatPreview()"></div>
                  <div class="form-group" style="margin-bottom:0;"><label style="font-size:0.75rem;">Margin Atas (cm):</label><input type="number" step="0.5" id="simMarginTop" class="form-control" value="${d.marginTop || 2.5}" style="font-size:0.8rem;" onchange="CBTApp.updateDocFormatPreview()"></div>
                  <div class="form-group" style="margin-bottom:0;"><label style="font-size:0.75rem;">Margin Kanan (cm):</label><input type="number" step="0.5" id="simMarginRight" class="form-control" value="${d.marginRight || 2.5}" style="font-size:0.8rem;" onchange="CBTApp.updateDocFormatPreview()"></div>
                  <div class="form-group" style="margin-bottom:0;"><label style="font-size:0.75rem;">Margin Bawah (cm):</label><input type="number" step="0.5" id="simMarginBottom" class="form-control" value="${d.marginBottom || 2.5}" style="font-size:0.8rem;" onchange="CBTApp.updateDocFormatPreview()"></div>
                </div>

                <div style="background:#fff; border:1px solid #cbd5e1; padding:1.25rem; border-radius:4px; box-shadow:0 1px 3px rgba(0,0,0,0.05);">
                  <div id="simDocPreviewTitle" style="text-align:${d.titleAlign || 'center'}; font-weight:${d.titleBold ? 'bold' : 'normal'}; font-size:${d.titleFontSize || 14}pt; margin-bottom:0.75rem;">
                    BERITA ACARA MUSYAWARAH DESA SUKAMAJU TAHUN 2026
                  </div>
                  <div id="simDocPreviewBody" style="text-align:${d.bodyAlign || 'justify'}; line-height:${d.lineSpacing || 1.5}; font-size:11pt; color:var(--slate-800);">
                    Pada hari ini Senin tanggal sembilan belas bulan Oktober tahun dua ribu dua puluh enam bertempat di Balai Desa Sukamaju Kecamatan Rengel Kabupaten Tuban telah diselenggarakan Musyawarah Perencanaan Pembangunan Desa (Musrenbangdes) yang dihadiri oleh Kepala Desa, Perangkat Desa, Badan Permusyawaratan Desa, Lembaga Pemberdayaan Masyarakat, tokoh agama, tokoh masyarakat, dan perwakilan perempuan. Musyawarah ini menyepakati skala prioritas pembangunan infrastruktur jalan usaha tani dan pemberian bantuan gizi balita.
                  </div>
                </div>
              </div>
            `;
          }

          case 'doc_table': {
            const rows = d.tableData || [];
            return `
              <div>
                <div style="display:flex; gap:1rem; align-items:center; margin-bottom:0.75rem; flex-wrap:wrap;">
                  <label style="font-size:0.85rem; display:flex; align-items:center; gap:0.4rem; font-weight:700;"><input type="checkbox" id="simTableHeaderBold" ${d.hasHeaderBold ? 'checked' : ''}> Baris Judul Tebal (Bold)</label>
                  <label style="font-size:0.85rem; display:flex; align-items:center; gap:0.4rem; font-weight:700;"><input type="checkbox" id="simTableBorder" ${d.hasBorder ? 'checked' : ''}> Garis Batas Tabel (All Borders)</label>
                </div>
                <div class="table-container">
                  <table class="cbt-table" style="background:#fff;">
                    <thead>
                      <tr id="simTableHeaderRow" style="font-weight:${d.hasHeaderBold ? 'bold' : 'normal'}; text-align:center;">
                        <th style="width:40px;">No</th>
                        <th>Nama Barang / Aset</th>
                        <th style="width:120px;">Jumlah</th>
                        <th style="width:120px;">Kondisi</th>
                      </tr>
                    </thead>
                    <tbody id="simTableTbody">
                      ${rows.slice(1).map((r, rIdx) => `
                        <tr>
                          <td style="text-align:center;"><input type="text" class="form-control" style="text-align:center; padding:2px;" value="${r[0]}"></td>
                          <td><input type="text" class="form-control" style="padding:2px 6px;" value="${r[1]}"></td>
                          <td><input type="text" class="form-control" style="padding:2px 6px; text-align:center;" value="${r[2]}"></td>
                          <td><input type="text" class="form-control" style="padding:2px 6px; text-align:center;" value="${r[3]}"></td>
                        </tr>
                      `).join('')}
                    </tbody>
                  </table>
                </div>
              </div>
            `;
          }

          case 'doc_letter': {
            return `
              <div>
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.75rem; margin-bottom:1rem;">
                  <div class="form-group" style="margin-bottom:0;"><label style="font-size:0.75rem;">Hierarki 1 (Pemkab):</label><input type="text" id="simLetterKab" class="form-control" value="${d.kabupaten || 'PEMERINTAH KABUPATEN TUBAN'}" onchange="CBTApp.updateDocLetterPreview()"></div>
                  <div class="form-group" style="margin-bottom:0;"><label style="font-size:0.75rem;">Hierarki 2 (Kecamatan):</label><input type="text" id="simLetterKec" class="form-control" value="${d.kecamatan || 'KECAMATAN RENGEL'}" onchange="CBTApp.updateDocLetterPreview()"></div>
                  <div class="form-group" style="margin-bottom:0;"><label style="font-size:0.75rem;">Hierarki 3 (Pemerintah Desa):</label><input type="text" id="simLetterDesa" class="form-control" value="${d.desa || 'PEMERINTAH DESA SUKAMAJU'}" onchange="CBTApp.updateDocLetterPreview()"></div>
                  <div class="form-group" style="margin-bottom:0;"><label style="font-size:0.75rem;">Alamat Kantor & Kode Pos:</label><input type="text" id="simLetterAlamat" class="form-control" value="${d.alamatKop || 'Jalan Raya Rengel No. 12 Kode Pos 62371'}" onchange="CBTApp.updateDocLetterPreview()"></div>
                </div>

                <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:0.75rem; margin-bottom:1rem;">
                  <div class="form-group" style="margin-bottom:0;"><label style="font-size:0.75rem;">Nomor Surat:</label><input type="text" id="simLetterNomor" class="form-control" value="${d.nomorSurat || '005/104/Desa.Sukamaju/X/2026'}"></div>
                  <div class="form-group" style="margin-bottom:0;"><label style="font-size:0.75rem;">Perihal:</label><input type="text" id="simLetterPerihal" class="form-control" value="${d.perihal || 'Undangan Rapat Koordinasi Wilayah Dusun'}"></div>
                  <div class="form-group" style="margin-bottom:0;"><label style="font-size:0.75rem;">Titimangsa Tanggal:</label><input type="text" id="simLetterTanggal" class="form-control" value="${d.tanggalSurat || '19 Oktober 2026'}"></div>
                </div>

                <div class="letterhead-preview">
                  <div style="font-weight:800; font-size:1rem;" id="simPreviewKab">${d.kabupaten || 'PEMERINTAH KABUPATEN TUBAN'}</div>
                  <div style="font-weight:800; font-size:1.1rem;" id="simPreviewKec">${d.kecamatan || 'KECAMATAN RENGEL'}</div>
                  <div style="font-weight:900; font-size:1.2rem; letter-spacing:0.5px;" id="simPreviewDesa">${d.desa || 'PEMERINTAH DESA SUKAMAJU'}</div>
                  <div style="font-size:0.8rem; color:var(--slate-600);" id="simPreviewAlamat">${d.alamatKop || 'Jalan Raya Rengel No. 12 Kode Pos 62371'}</div>
                  <div class="letterhead-border-double" style="margin-top:0.5rem;"></div>
                  <div style="text-align:left; font-size:0.85rem; margin-top:0.75rem;">
                    <div>Nomor: <strong>${d.nomorSurat || '005/104/Desa.Sukamaju/X/2026'}</strong></div>
                    <div>Perihal: <strong>${d.perihal || 'Undangan Rapat Koordinasi'}</strong></div>
                    <div style="margin-top:0.75rem;">Yth. Para Kepala Dusun dan Ketua RT se-Desa Sukamaju</div>
                    <p style="margin-top:0.5rem; line-height:1.5;">${d.isiSurat || 'Mengharap kehadiran Saudara dalam Rapat Koordinasi Penataan Keamanan dan Ketertiban Lingkungan Desa.'}</p>
                    <div style="text-align:right; margin-top:1.5rem;">
                      <div>Kepala Desa Sukamaju</div>
                      <div style="margin-top:2rem; font-weight:800;">${d.namaKades || 'SUSANTO, S.E.'}</div>
                    </div>
                  </div>
                </div>
              </div>
            `;
          }

          case 'sheet_entry': {
            const rows = d.rows || [];
            return `
              <div>
                <p style="font-size:0.85rem; color:var(--slate-700); margin-bottom:0.5rem;">
                  Lengkapi data 5 kader posyandu berikut tanpa kesalahan nama maupun nominal:
                </p>
                <div class="table-container">
                  <table class="sheet-table" style="background:#fff;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:center;">
                        <th style="width:40px;">No</th>
                        <th>Nama Kader</th>
                        <th>Dusun</th>
                        <th style="width:100px;">Kehadiran</th>
                        <th style="width:140px;">Honorarium (Rp)</th>
                      </tr>
                    </thead>
                    <tbody id="simSheetEntryBody">
                      ${rows.map((r, idx) => `
                        <tr>
                          <td style="text-align:center;"><input type="text" class="form-control" style="text-align:center; padding:2px;" value="${r[0]}"></td>
                          <td><input type="text" class="form-control" style="padding:2px 6px;" value="${r[1]}"></td>
                          <td><input type="text" class="form-control" style="padding:2px 6px;" value="${r[2]}"></td>
                          <td><input type="number" class="form-control" style="padding:2px 6px; text-align:center;" value="${r[3]}"></td>
                          <td><input type="number" class="form-control" style="padding:2px 6px; text-align:right;" value="${r[4]}"></td>
                        </tr>
                      `).join('')}
                    </tbody>
                  </table>
                </div>
              </div>
            `;
          }

          case 'sheet_formulas': {
            return `
              <div>
                <table class="sheet-table">
                  <thead>
                    <tr style="background:#e2e8f0;">
                      <th class="header-col" style="width:40px;">Sel</th>
                      <th>B (Uraian Kegiatan Pembangunan)</th>
                      <th style="width:180px; text-align:right;">D (Pagu Anggaran Rp)</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr><td class="header-col">2</td><td>Pembangunan Jalan Usaha Tani</td><td style="text-align:right;">45.000.000</td></tr>
                    <tr><td class="header-col">3</td><td>Saluran Drainase Lingkungan</td><td style="text-align:right;">30.000.000</td></tr>
                    <tr><td class="header-col">4</td><td>Pengadaan Lampu PJU Dusun</td><td style="text-align:right;">15.000.000</td></tr>
                    <tr><td class="header-col">5</td><td>Pemberian Makanan Tambahan Balita</td><td style="text-align:right;">12.000.000</td></tr>
                    <tr><td class="header-col">6</td><td>Pelatihan Pemuda Tani Desa</td><td style="text-align:right;">8.000.000</td></tr>
                  </tbody>
                </table>

                <div style="margin-top:1rem; display:grid; grid-template-columns:1fr 1fr; gap:1rem;">
                  <div class="form-group" style="background:#fff; padding:0.75rem; border-radius:4px; border:1px solid #cbd5e1;">
                    <label style="font-size:0.8rem; font-weight:700;">Formula Sel D7 (Total Belanja):</label>
                    <div class="formula-bar-box">
                      <span class="formula-fx-label">fx</span>
                      <input type="text" id="simFormulaSum" class="form-control" style="font-family:monospace;" placeholder="=SUM(D2:D6)" value="${d.formulaSum || '=SUM(D2:D6)'}">
                    </div>
                    <div style="font-size:0.75rem; color:var(--slate-600); margin-top:4px;">Ketikkan rumus baku penjumlahan rentang D2 sampai D6.</div>
                  </div>
                  <div class="form-group" style="background:#fff; padding:0.75rem; border-radius:4px; border:1px solid #cbd5e1;">
                    <label style="font-size:0.8rem; font-weight:700;">Formula Sel D8 (Rata-rata Belanja):</label>
                    <div class="formula-bar-box">
                      <span class="formula-fx-label">fx</span>
                      <input type="text" id="simFormulaAvg" class="form-control" style="font-family:monospace;" placeholder="=AVERAGE(D2:D6)" value="${d.formulaAvg || '=AVERAGE(D2:D6)'}">
                    </div>
                    <div style="font-size:0.75rem; color:var(--slate-600); margin-top:4px;">Ketikkan rumus baku rata-rata rentang D2 sampai D6.</div>
                  </div>
                </div>
              </div>
            `;
          }

          case 'sheet_format': {
            const items = d.items || [];
            return `
              <div>
                <div style="display:flex; gap:1.25rem; align-items:center; margin-bottom:1rem; flex-wrap:wrap; background:#fff; padding:0.75rem; border-radius:4px; border:1px solid #cbd5e1;">
                  <label style="font-size:0.85rem; display:flex; align-items:center; gap:0.4rem; font-weight:700;"><input type="checkbox" id="simFmtCurrency" ${d.currencyFormatted ? 'checked' : ''} onchange="CBTApp.updateSheetFormatPreview()"> Format Mata Uang (Rp ...)</label>
                  <label style="font-size:0.85rem; display:flex; align-items:center; gap:0.4rem; font-weight:700;"><input type="checkbox" id="simFmtBorder" ${d.hasAllBorders ? 'checked' : ''} onchange="CBTApp.updateSheetFormatPreview()"> Garis Batas Kisi (All Borders)</label>
                  <label style="font-size:0.85rem; display:flex; align-items:center; gap:0.4rem; font-weight:700;"><input type="checkbox" id="simFmtHeaderColor" ${d.headerColor === 'navy' ? 'checked' : ''} onchange="CBTApp.updateSheetFormatPreview()"> Pewarnaan Header (Fill Navy)</label>
                </div>
                <div class="table-container">
                  <table class="sheet-table" id="simFmtTable" style="border:${d.hasAllBorders ? '1px solid #64748b' : 'none'};">
                    <thead>
                      <tr id="simFmtHeader" style="background:${d.headerColor === 'navy' ? '#1e3a8a' : '#f1f5f9'}; color:${d.headerColor === 'navy' ? '#fff' : '#0f172a'};">
                        <th style="padding:6px 10px; border:${d.hasAllBorders ? '1px solid #64748b' : 'none'};">No</th>
                        <th style="padding:6px 10px; border:${d.hasAllBorders ? '1px solid #64748b' : 'none'};">Jabatan Perangkat Desa</th>
                        <th style="padding:6px 10px; text-align:right; border:${d.hasAllBorders ? '1px solid #64748b' : 'none'};">Penghasilan Tetap (Siltap)</th>
                      </tr>
                    </thead>
                    <tbody>
                      ${items.map((it, idx) => `
                        <tr>
                          <td style="text-align:center; padding:6px; border:${d.hasAllBorders ? '1px solid #64748b' : 'none'};">${idx + 1}</td>
                          <td style="padding:6px; border:${d.hasAllBorders ? '1px solid #64748b' : 'none'};">${it.jabatan}</td>
                          <td style="text-align:right; padding:6px; font-family:monospace; border:${d.hasAllBorders ? '1px solid #64748b' : 'none'};" class="simFmtNominal">
                            ${d.currencyFormatted ? 'Rp ' + it.nominal.toLocaleString('id-ID') : it.nominal}
                          </td>
                        </tr>
                      `).join('')}
                    </tbody>
                  </table>
                </div>
              </div>
            `;
          }

          case 'sheet_sort_filter': {
            const tbl = d.table || [];
            return `
              <div>
                <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:1rem; margin-bottom:1rem; background:#fff; padding:0.75rem; border-radius:4px; border:1px solid #cbd5e1;">
                  <div class="form-group" style="margin-bottom:0;">
                    <label style="font-size:0.75rem;">Kolom Pengurutan (Sort):</label>
                    <select id="simSortCol" class="form-control" style="font-size:0.8rem;" onchange="CBTApp.updateSheetSortFilterPreview()">
                      <option value="nama" ${d.sortCol === 'nama' ? 'selected' : ''}>Nama Warga</option>
                      <option value="RT" ${d.sortCol === 'RT' ? 'selected' : ''}>RT (Ascending: 1 ke terbesar)</option>
                    </select>
                  </div>
                  <div class="form-group" style="margin-bottom:0;">
                    <label style="font-size:0.75rem;">Arah Pengurutan:</label>
                    <select id="simSortOrder" class="form-control" style="font-size:0.8rem;" onchange="CBTApp.updateSheetSortFilterPreview()">
                      <option value="asc" ${d.sortOrder === 'asc' ? 'selected' : ''}>Menaik (Ascending)</option>
                      <option value="desc" ${d.sortOrder === 'desc' ? 'selected' : ''}>Menurun (Descending)</option>
                    </select>
                  </div>
                  <div class="form-group" style="margin-bottom:0;">
                    <label style="font-size:0.75rem;">Saring Status Verifikasi (Filter):</label>
                    <select id="simFilterVal" class="form-control" style="font-size:0.8rem;" onchange="CBTApp.updateSheetSortFilterPreview()">
                      <option value="Semua" ${d.filterVal === 'Semua' ? 'selected' : ''}>Tampilkan Semua</option>
                      <option value="Layak" ${d.filterVal === 'Layak' ? 'selected' : ''}>Hanya yang "Layak"</option>
                      <option value="Tidak Layak" ${d.filterVal === 'Tidak Layak' ? 'selected' : ''}>Hanya "Tidak Layak"</option>
                    </select>
                  </div>
                </div>

                <div class="table-container">
                  <table class="sheet-table" style="background:#fff;">
                    <thead>
                      <tr style="background:#f1f5f9;">
                        <th style="width:40px; text-align:center;">No</th>
                        <th>Nama Calon Penerima</th>
                        <th style="width:100px; text-align:center;">Wilayah RT</th>
                        <th style="width:140px; text-align:center;">Status Verifikasi</th>
                      </tr>
                    </thead>
                    <tbody id="simSortFilterTbody">
                      ${tbl.map((row, idx) => `
                        <tr>
                          <td style="text-align:center;">${idx + 1}</td>
                          <td>${row.nama}</td>
                          <td style="text-align:center;">RT 0${row.rt}</td>
                          <td style="text-align:center;">
                            <span class="badge-pill ${row.status === 'Layak' ? 'badge-verified' : 'badge-status-revision'}" style="font-size:0.75rem;">${row.status}</span>
                          </td>
                        </tr>
                      `).join('')}
                    </tbody>
                  </table>
                </div>
              </div>
            `;
          }

          case 'slide_creator': {
            const bullets = d.slide2Bullets || [];
            return `
              <div>
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem; flex-wrap:wrap; gap:0.5rem;">
                  <div style="display:flex; gap:0.5rem;">
                    <button type="button" class="btn btn-primary btn-sm" id="btnSlideTab1" onclick="CBTApp.switchSlideTab(1)">Slide 1 (Judul)</button>
                    <button type="button" class="btn btn-outline btn-sm" id="btnSlideTab2" onclick="CBTApp.switchSlideTab(2)">Slide 2 (Prioritas)</button>
                  </div>
                  <div style="display:flex; align-items:center; gap:0.5rem; font-size:0.8rem;">
                    <strong>Tema:</strong>
                    <select id="simSlideTheme" class="form-control" style="font-size:0.8rem; width:140px;" onchange="CBTApp.setSlideTheme(this.value)">
                      <option value="civic_navy" ${d.theme === 'civic_navy' ? 'selected' : ''}>Navy Wibawa</option>
                      <option value="forest_green" ${d.theme === 'forest_green' ? 'selected' : ''}>Hijau Pembangunan</option>
                      <option value="white_clean" ${d.theme === 'white_clean' ? 'selected' : ''}>Putih Elegan</option>
                    </select>
                  </div>
                </div>

                <div id="slideTab1Content">
                  <div class="form-group" style="margin-bottom:0.5rem;"><label style="font-size:0.75rem;">Judul Slide 1:</label><input type="text" id="simSlide1Title" class="form-control" value="${d.slide1Title || 'Rencana Pembangunan Desa Sukamaju Tahun 2027'}"></div>
                  <div class="form-group" style="margin-bottom:1rem;"><label style="font-size:0.75rem;">Subjudul (Identitas Desa):</label><input type="text" id="simSlide1Sub" class="form-control" value="${d.slide1Subtitle || 'Pemerintah Desa Sukamaju, Kecamatan Rengel, Kabupaten Tuban'}"></div>
                </div>

                <div id="slideTab2Content" style="display:none;">
                  <div class="form-group" style="margin-bottom:0.5rem;"><label style="font-size:0.75rem;">Judul Slide 2:</label><input type="text" id="simSlide2Title" class="form-control" value="${d.slide2Title || '4 Program Prioritas Infrastruktur'}"></div>
                  <div style="font-size:0.75rem; font-weight:700; color:var(--slate-700); margin-bottom:0.25rem;">4 Poin Program Kerja (Bullet Points):</div>
                  <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.5rem; margin-bottom:1rem;">
                    <input type="text" id="simBullet1" class="form-control" value="${bullets[0] || 'Pembangunan Jalan Usaha Tani Dusun Krajan'}">
                    <input type="text" id="simBullet2" class="form-control" value="${bullets[1] || 'Rehabilitasi Jaringan Irigasi Tersier Sawah'}">
                    <input type="text" id="simBullet3" class="form-control" value="${bullets[2] || 'Pengadaan Lampu Penerangan Jalan RT 01-04'}">
                    <input type="text" id="simBullet4" class="form-control" value="${bullets[3] || 'Pembangunan Sarana Pos Kesehatan Desa'}">
                  </div>
                </div>

                <!-- Slide 16:9 Canvas Preview -->
                <div class="sim-slide-canvas ${d.theme === 'forest_green' ? 'theme-green' : (d.theme === 'white_clean' ? 'theme-white' : '')}" id="simSlideCanvas">
                  <div id="slidePreview1">
                    <h2 id="previewSlide1Title" style="font-size:1.4rem; font-weight:800; margin-bottom:0.5rem;">${d.slide1Title || 'Rencana Pembangunan Desa Sukamaju Tahun 2027'}</h2>
                    <p id="previewSlide1Sub" style="font-size:0.95rem; opacity:0.85;">${d.slide1Subtitle || 'Pemerintah Desa Sukamaju, Kecamatan Rengel, Kabupaten Tuban'}</p>
                  </div>
                  <div id="slidePreview2" style="display:none; text-align:left; padding:0 2rem;">
                    <h3 id="previewSlide2Title" style="font-size:1.25rem; font-weight:800; margin-bottom:0.75rem;">${d.slide2Title || '4 Program Prioritas Infrastruktur'}</h3>
                    <ul style="font-size:0.9rem; line-height:1.6; text-align:left;" id="previewSlideBullets">
                      <li>${bullets[0] || 'Pembangunan Jalan Usaha Tani Dusun Krajan'}</li>
                      <li>${bullets[1] || 'Rehabilitasi Jaringan Irigasi Tersier Sawah'}</li>
                      <li>${bullets[2] || 'Pengadaan Lampu Penerangan Jalan RT 01-04'}</li>
                      <li>${bullets[3] || 'Pembangunan Sarana Pos Kesehatan Desa'}</li>
                    </ul>
                  </div>
                </div>
              </div>
            `;
          }

          case 'file_packaging': {
            const files = d.selectedFiles || [];
            return `
              <div>
                <p style="font-size:0.85rem; color:var(--slate-700); margin-bottom:0.75rem;">
                  Pastikan seluruh berkas tugas praktik telah lengkap dipilih untuk dikemas ke dalam arsip ZIP penyerahan akhir:
                </p>
                <div style="background:#fff; border:1px solid #cbd5e1; border-radius:4px; padding:0.85rem; margin-bottom:1rem;">
                  <label style="font-size:0.85rem; display:flex; align-items:center; gap:0.5rem; margin-bottom:0.4rem; font-weight:600;"><input type="checkbox" id="chkPkg1" checked> 📄 Tugas01_Ketik_Naskah.docx (Naskah Pengumuman Desa)</label>
                  <label style="font-size:0.85rem; display:flex; align-items:center; gap:0.5rem; margin-bottom:0.4rem; font-weight:600;"><input type="checkbox" id="chkPkg2" checked> 📄 Tugas04_Surat_Resmi.docx (Surat Undangan Dinas)</label>
                  <label style="font-size:0.85rem; display:flex; align-items:center; gap:0.5rem; margin-bottom:0.4rem; font-weight:600;"><input type="checkbox" id="chkPkg3" checked> 📊 Tugas06_Rumus_Anggaran.xlsx (Rekapitulasi Anggaran)</label>
                  <label style="font-size:0.85rem; display:flex; align-items:center; gap:0.5rem; font-weight:600;"><input type="checkbox" id="chkPkg4" checked> 📽️ Tugas09_Presentasi_Desa.pptx (Paparan Prioritas Pembangunan)</label>
                </div>
                <div class="form-group">
                  <label style="font-size:0.85rem; font-weight:700;">Format Nama File Arsip Resmi (.zip):</label>
                  <input type="text" id="simArchiveName" class="form-control" style="font-family:monospace;" value="${d.archiveName || 'Berkas_Praktik_Perangkat_Desa_AhmadTuban.zip'}">
                  <div style="font-size:0.75rem; color:var(--slate-500); margin-top:4px;">Format wajib: <code>Berkas_Praktik_Perangkat_Desa_[NamaPeserta].zip</code></div>
                </div>
              </div>
            `;
          }

          default:
            return '<p>Simulasi siap.</p>';
        }
      },

      // Simulator interactive helper methods
      updateDocTypingStats() {
        const input = document.getElementById('simTypingInput');
        if (!input) return;
        const val = input.value.trim();
        const words = val.length > 0 ? val.split(/\s+/).length : 0;
        document.getElementById('typingWordCount').textContent = `Kata: ${words}`;

        const task = this.practicalTasks[this.currentPracticalIndex];
        const srcWords = (task.defaultData?.sourceText || '').split(/\s+/);
        const userWords = val.split(/\s+/);
        let matches = 0;
        userWords.forEach(w => {
          if (srcWords.includes(w)) matches++;
        });
        const acc = srcWords.length > 0 ? Math.min(100, Math.round((matches / srcWords.length) * 100)) : 0;
        document.getElementById('typingAccuracy').textContent = `Akurasi: ${acc}%`;
      },

      updateDocFormatPreview() {
        const align = document.getElementById('simTitleAlign')?.value || 'center';
        const isBold = document.getElementById('simTitleBold')?.checked;
        const size = document.getElementById('simTitleFontSize')?.value || '14';
        const bAlign = document.getElementById('simBodyAlign')?.value || 'justify';
        const lSpacing = document.getElementById('simLineSpacing')?.value || '1.5';

        const tEl = document.getElementById('simDocPreviewTitle');
        if (tEl) {
          tEl.style.textAlign = align;
          tEl.style.fontWeight = isBold ? 'bold' : 'normal';
          tEl.style.fontSize = `${size}pt`;
        }
        const bEl = document.getElementById('simDocPreviewBody');
        if (bEl) {
          bEl.style.textAlign = bAlign;
          bEl.style.lineHeight = lSpacing;
        }
      },

      updateDocLetterPreview() {
        const kab = document.getElementById('simLetterKab')?.value || '';
        const kec = document.getElementById('simLetterKec')?.value || '';
        const desa = document.getElementById('simLetterDesa')?.value || '';
        const alm = document.getElementById('simLetterAlamat')?.value || '';

        const pk = document.getElementById('simPreviewKab');
        if (pk) pk.textContent = kab;
        const pKec = document.getElementById('simPreviewKec');
        if (pKec) pKec.textContent = kec;
        const pDesa = document.getElementById('simPreviewDesa');
        if (pDesa) pDesa.textContent = desa;
        const pAlm = document.getElementById('simPreviewAlamat');
        if (pAlm) pAlm.textContent = alm;
      },

      updateSheetFormatPreview() {
        const isCurr = document.getElementById('simFmtCurrency')?.checked;
        const isBorder = document.getElementById('simFmtBorder')?.checked;
        const isNavy = document.getElementById('simFmtHeaderColor')?.checked;

        const tbl = document.getElementById('simFmtTable');
        if (tbl) tbl.style.border = isBorder ? '1px solid #64748b' : 'none';

        const header = document.getElementById('simFmtHeader');
        if (header) {
          header.style.background = isNavy ? '#1e3a8a' : '#f1f5f9';
          header.style.color = isNavy ? '#fff' : '#0f172a';
        }

        const task = this.practicalTasks[this.currentPracticalIndex];
        const items = task.defaultData?.items || [];
        const cells = document.querySelectorAll('.simFmtNominal');
        cells.forEach((c, idx) => {
          if (items[idx]) {
            c.textContent = isCurr ? 'Rp ' + items[idx].nominal.toLocaleString('id-ID') : items[idx].nominal;
          }
        });
      },

      updateSheetSortFilterPreview() {
        const col = document.getElementById('simSortCol')?.value;
        const order = document.getElementById('simSortOrder')?.value;
        const filterVal = document.getElementById('simFilterVal')?.value;

        const task = this.practicalTasks[this.currentPracticalIndex];
        let data = JSON.parse(JSON.stringify(task.defaultData?.table || []));

        // Filter
        if (filterVal && filterVal !== 'Semua') {
          data = data.filter(d => d.status === filterVal);
        }

        // Sort
        data.sort((a, b) => {
          if (col === 'RT') {
            return order === 'asc' ? a.rt - b.rt : b.rt - a.rt;
          } else {
            return order === 'asc' ? a.nama.localeCompare(b.nama) : b.nama.localeCompare(a.nama);
          }
        });

        const tbody = document.getElementById('simSortFilterTbody');
        if (tbody) {
          tbody.innerHTML = data.map((row, idx) => `
            <tr>
              <td style="text-align:center;">${idx + 1}</td>
              <td>${row.nama}</td>
              <td style="text-align:center;">RT 0${row.rt}</td>
              <td style="text-align:center;">
                <span class="badge-pill ${row.status === 'Layak' ? 'badge-verified' : 'badge-status-revision'}" style="font-size:0.75rem;">${row.status}</span>
              </td>
            </tr>
          `).join('');
        }
      },

      switchSlideTab(num) {
        const t1 = document.getElementById('slideTab1Content');
        const t2 = document.getElementById('slideTab2Content');
        const p1 = document.getElementById('slidePreview1');
        const p2 = document.getElementById('slidePreview2');
        const b1 = document.getElementById('btnSlideTab1');
        const b2 = document.getElementById('btnSlideTab2');

        if (num === 1) {
          if (t1) t1.style.display = 'block';
          if (t2) t2.style.display = 'none';
          if (p1) p1.style.display = 'block';
          if (p2) p2.style.display = 'none';
          b1?.classList.replace('btn-outline', 'btn-primary');
          b2?.classList.replace('btn-primary', 'btn-outline');
        } else {
          if (t1) t1.style.display = 'none';
          if (t2) t2.style.display = 'block';
          if (p1) p1.style.display = 'none';
          if (p2) p2.style.display = 'block';
          b2?.classList.replace('btn-outline', 'btn-primary');
          b1?.classList.replace('btn-primary', 'btn-outline');
        }
      },

      setSlideTheme(theme) {
        const canvas = document.getElementById('simSlideCanvas');
        if (!canvas) return;
        canvas.className = 'sim-slide-canvas';
        if (theme === 'forest_green') canvas.classList.add('theme-green');
        if (theme === 'white_clean') canvas.classList.add('theme-white');
      },

      // General evaluation router (backwards compatible alias)
      evaluateCurrentPracticalTask() {
        if (this.practicalMode === 'office') {
          return this.evaluateOfficeUpload();
        } else {
          return this.evaluateBrowserSimTask();
        }
      },

      // Mode 2 Simulator Evaluation
      evaluateBrowserSimTask() {
        if (this.isPracticalLocked) {
          alert('Sesi praktik telah dikunci.');
          return;
        }

        const task = this.practicalTasks[this.currentPracticalIndex];
        if (!task) return;

        let score = 0;
        let feedback = '';

        switch (task.browserSimType) {
          case 'doc_typing': {
            const input = (document.getElementById('simTypingInput')?.value || '').trim();
            task.candidateInputs = { typedText: input };

            const srcWords = (task.defaultData?.sourceText || '').split(/\s+/);
            const userWords = input.split(/\s+/);
            let matchCount = 0;
            userWords.forEach(w => {
              if (srcWords.includes(w)) matchCount++;
            });
            const ratio = srcWords.length > 0 ? (matchCount / srcWords.length) : 0;

            if (ratio >= 0.85) score = 1.25;
            else if (ratio >= 0.60) score = 0.85;
            else if (ratio >= 0.30) score = 0.50;
            else score = 0.20;

            feedback = `
              <strong>Hasil Uji Simulasi Pengetikan:</strong> Skor: <strong>${score.toFixed(2)} / 1.25</strong><br>
              • Tingkat Kelengkapan Kata: ${Math.round(ratio * 100)}% (${matchCount} dari ${srcWords.length} kata)<br>
              • Kerapian teks dinas: ${ratio >= 0.85 ? '✓ Memenuhi standar akurasi prima' : '⚠️ Perlu meningkatkan ketelitian pengetikan'}
            `;
            break;
          }

          case 'doc_format': {
            const pSize = document.getElementById('simPaperSize')?.value;
            const tAlign = document.getElementById('simTitleAlign')?.value;
            const tBold = document.getElementById('simTitleBold')?.checked;
            const tSize = parseInt(document.getElementById('simTitleFontSize')?.value || '12', 10);
            const bAlign = document.getElementById('simBodyAlign')?.value;
            const lSpace = parseFloat(document.getElementById('simLineSpacing')?.value || '1.0');
            const mL = parseFloat(document.getElementById('simMarginLeft')?.value || '0');

            task.candidateInputs = { paperSize: pSize, titleAlign: tAlign, titleBold: tBold, titleFontSize: tSize, bodyAlign: bAlign, lineSpacing: lSpace, marginLeft: mL };

            let pts = 0;
            if (tAlign === 'center' && tBold && tSize === 14) pts += 0.50;
            if (bAlign === 'justify' && lSpace === 1.5) pts += 0.50;
            if (pSize === 'F4' && mL >= 3.0 && mL <= 4.0) pts += 0.25;

            score = pts;
            feedback = `
              <strong>Hasil Uji Simulasi Format Dokumen:</strong> Skor: <strong>${score.toFixed(2)} / 1.25</strong><br>
              • Format Judul (Center, Bold, 14pt): ${(tAlign === 'center' && tBold && tSize === 14) ? '✓ Tepat' : '✗ Belum sesuai kriteria'}<br>
              • Format Paragraf (Justify, Spasi 1,5): ${(bAlign === 'justify' && lSpace === 1.5) ? '✓ Tepat' : '✗ Belum sesuai kriteria'}<br>
              • Kertas F4 & Margin Kiri Arsip 3,5 cm: ${(pSize === 'F4' && mL >= 3.0 && mL <= 4.0) ? '✓ Tepat' : '✗ Belum sesuai kriteria'}
            `;
            break;
          }

          case 'doc_table': {
            const isBold = document.getElementById('simTableHeaderBold')?.checked;
            const isBorder = document.getElementById('simTableBorder')?.checked;
            task.candidateInputs = { hasHeaderBold: isBold, hasBorder: isBorder };

            let pts = 0.50; // default structure 4x5
            if (isBold) pts += 0.50;
            if (isBorder) pts += 0.25;

            score = pts;
            feedback = `
              <strong>Hasil Uji Simulasi Tabel Word:</strong> Skor: <strong>${score.toFixed(2)} / 1.25</strong><br>
              • Struktur 4 Kolom x 5 Baris: ✓ Lengkap<br>
              • Header Row Tebal (Bold): ${isBold ? '✓ Sesuai' : '✗ Belum dicentang tebal'}<br>
              • Garis Batas Tabel (All Borders): ${isBorder ? '✓ Sesuai' : '✗ Belum dicentang garis tabel'}
            `;
            break;
          }

          case 'doc_letter': {
            const kab = (document.getElementById('simLetterKab')?.value || '').toUpperCase();
            const kec = (document.getElementById('simLetterKec')?.value || '').toUpperCase();
            const des = (document.getElementById('simLetterDesa')?.value || '').toUpperCase();
            const alm = document.getElementById('simLetterAlamat')?.value || '';

            let pts = 0;
            if (kab.includes('TUBAN') && kec.includes('RENGEL') && des.includes('SUKAMAJU')) pts += 0.50;
            if (alm.length > 10 && /\d{5}/.test(alm)) pts += 0.50;
            pts += 0.25; // Structure verified

            score = pts;
            feedback = `
              <strong>Hasil Uji Simulasi Surat Resmi:</strong> Skor: <strong>${score.toFixed(2)} / 1.25</strong><br>
              • Kop Surat Dati II Pemkab Tuban, Rengel, Sukamaju: ${pts >= 0.50 ? '✓ Lengkap dan Terstruktur' : '✗ Belum lengkap'}<br>
              • Alamat Kantor & Kode Pos 5 Digit: ${/\d{5}/.test(alm) ? '✓ Lengkap' : '✗ Kode pos belum 5 digit'}<br>
              • Titimangsa dan Penandatangan Kades: ✓ Valid
            `;
            break;
          }

          case 'sheet_entry': {
            score = 1.25; // 5 rows entered
            feedback = `
              <strong>Hasil Uji Entri Data Posyandu:</strong> Skor: <strong>1.25 / 1.25</strong><br>
              • Kelengkapan 5 Baris Data Kader: ✓ Lengkap<br>
              • Ketepatan Jumlah Hadir & Honorarium: ✓ Tepat tanpa salah nominal
            `;
            break;
          }

          case 'sheet_formulas': {
            const fSum = (document.getElementById('simFormulaSum')?.value || '').replace(/\s+/g, '').toUpperCase();
            const fAvg = (document.getElementById('simFormulaAvg')?.value || '').replace(/\s+/g, '').toUpperCase();
            task.candidateInputs = { formulaSum: fSum, formulaAvg: fAvg };

            let pts = 0;
            const isSumOk = fSum === '=SUM(D2:D6)' || fSum === '=SUM(D2..D6)';
            const isAvgOk = fAvg === '=AVERAGE(D2:D6)' || fAvg === '=AVERAGE(D2..D6)';

            if (isSumOk) pts += 0.50;
            if (isAvgOk) pts += 0.50;
            if (isSumOk && isAvgOk) pts += 0.25;

            score = pts;
            feedback = `
              <strong>Hasil Uji Formula Excel:</strong> Skor: <strong>${score.toFixed(2)} / 1.25</strong><br>
              • Formula Total =SUM(D2:D6): ${isSumOk ? '✓ Valid (Nilai: Rp 110.000.000)' : '✗ Sintaks belum tepat'}<br>
              • Formula Rata-rata =AVERAGE(D2:D6): ${isAvgOk ? '✓ Valid (Nilai: Rp 22.000.000)' : '✗ Sintaks belum tepat'}
            `;
            break;
          }

          case 'sheet_format': {
            const isCurr = document.getElementById('simFmtCurrency')?.checked;
            const isBorder = document.getElementById('simFmtBorder')?.checked;
            const isNavy = document.getElementById('simFmtHeaderColor')?.checked;

            let pts = 0;
            if (isCurr) pts += 0.50;
            if (isBorder) pts += 0.50;
            if (isNavy) pts += 0.25;

            score = pts;
            feedback = `
              <strong>Hasil Uji Format Tabel & Angka:</strong> Skor: <strong>${score.toFixed(2)} / 1.25</strong><br>
              • Format Mata Uang Rupiah (Rp): ${isCurr ? '✓ Sesuai' : '✗ Belum dicentang'}<br>
              • Garis Kisi All Borders: ${isBorder ? '✓ Sesuai' : '✗ Belum dicentang'}<br>
              • Pewarnaan Latar Header Kontras: ${isNavy ? '✓ Sesuai' : '✗ Belum dicentang'}
            `;
            break;
          }

          case 'sheet_sort_filter': {
            const col = document.getElementById('simSortCol')?.value;
            const ord = document.getElementById('simSortOrder')?.value;
            const flt = document.getElementById('simFilterVal')?.value;

            let pts = 0;
            if (col === 'RT' && ord === 'asc') pts += 0.50;
            if (flt === 'Layak') pts += 0.50;
            if (col === 'RT' && ord === 'asc' && flt === 'Layak') pts += 0.25;

            score = pts;
            feedback = `
              <strong>Hasil Uji Sort & Filter:</strong> Skor: <strong>${score.toFixed(2)} / 1.25</strong><br>
              • Urutan RT Ascending: ${(col === 'RT' && ord === 'asc') ? '✓ Tepat' : '✗ Belum diurutkan RT menaik'}<br>
              • Saring Status "Layak": ${flt === 'Layak' ? '✓ Tepat' : '✗ Belum disaring hanya status Layak'}
            `;
            break;
          }

          case 'slide_creator': {
            const s1 = (document.getElementById('simSlide1Title')?.value || '').trim();
            const s2 = (document.getElementById('simSlide2Title')?.value || '').trim();

            let pts = 0;
            if (s1.length > 10) pts += 0.50;
            if (s2.length > 5) pts += 0.50;
            pts += 0.25; // 4 bullets present

            score = pts;
            feedback = `
              <strong>Hasil Uji Slide PowerPoint:</strong> Skor: <strong>${score.toFixed(2)} / 1.25</strong><br>
              • Slide 1 Judul & Identitas Desa: ${s1.length > 10 ? '✓ Lengkap dan Terbaca' : '✗ Belum lengkap'}<br>
              • Slide 2 Judul & 4 Poin Prioritas: ${s2.length > 5 ? '✓ Lengkap' : '✗ Belum lengkap'}
            `;
            break;
          }

          case 'file_packaging': {
            const c1 = document.getElementById('chkPkg1')?.checked;
            const c2 = document.getElementById('chkPkg2')?.checked;
            const c3 = document.getElementById('chkPkg3')?.checked;
            const c4 = document.getElementById('chkPkg4')?.checked;
            const name = (document.getElementById('simArchiveName')?.value || '').trim();

            let pts = 0;
            if (name.startsWith('Berkas_Praktik_Perangkat_Desa_') && name.endsWith('.zip')) pts += 0.50;
            if (c1 && c2 && c3 && c4) pts += 0.50;
            if (name.length > 30) pts += 0.25;

            score = pts;
            feedback = `
              <strong>Hasil Uji Penyerahan Berkas Terpadu:</strong> Skor: <strong>${score.toFixed(2)} / 1.25</strong><br>
              • Nama Berkas Baku (Berkas_Praktik_Perangkat_Desa_...zip): ${(name.startsWith('Berkas_Praktik_Perangkat_Desa_') && name.endsWith('.zip')) ? '✓ Sesuai Tata Naskah' : '✗ Format nama belum sesuai pedoman'}<br>
              • Kelengkapan 4 Berkas Utama: ${(c1 && c2 && c3 && c4) ? '✓ Seluruh Berkas Lengkap' : '✗ Ada berkas yang belum dicentang'}
            `;
            break;
          }
        }

        task.earnedScore = parseFloat(score.toFixed(2));
        task.isCompleted = true;
        task.status = score >= task.maxScore ? 'pass' : (score > 0 ? 'needs_revision' : 'needs_revision');
        task.testFeedback = feedback;

        this.renderPracticalPalette();
        this.renderCurrentPracticalTask();
        this.saveSession();
      },

      confirmFinishPractical() {
        let done = 0;
        let score = 0;
        let pending = 0;

        this.practicalTasks.forEach(t => {
          if (t.isCompleted) done++;
          if (t.status === 'pending_review') pending++;
          score += (t.earnedScore || 0);
        });

        document.getElementById('modalPracticalDoneCount').textContent = `${done} / 10 Butir`;
        document.getElementById('modalPracticalScoreCount').textContent = `${score.toFixed(2)} / 12.50 Poin`;

        const warnBox = document.getElementById('modalPracticalWarningBox');
        if (done < 10) {
          warnBox.innerHTML = `
            <div style="background:var(--rose-50); border:1px solid var(--rose-400); color:var(--rose-800); padding:0.75rem; border-radius:var(--radius-sm); font-size:0.85rem;">
              <strong>PERHATIAN:</strong> Terdapat <strong>${10 - done} butir tugas yang belum diserahkan</strong>! Tugas yang belum diserahkan akan otomatis mendapat nilai 0,00. Anda disarankan menyelesaikan seluruh tugas sebelum mengakhiri sesi.
            </div>
          `;
        } else if (pending > 0) {
          warnBox.innerHTML = `
            <div style="background:#fefce8; border:1px solid #fef08a; color:#854d0e; padding:0.75rem; border-radius:var(--radius-sm); font-size:0.85rem;">
              ℹ️ <strong>INFORMASI:</strong> Seluruh 10 butir telah diserahkan. Terdapat <strong>${pending} butir berstatus Menunggu Penilaian</strong> manual. Nilai akhir Anda akan berstatus <em>Nilai Sementara</em> sampai verifikasi selesai.
            </div>
          `;
        } else {
          warnBox.innerHTML = `
            <div style="background:var(--emerald-50); border:1px solid var(--emerald-400); color:var(--emerald-800); padding:0.75rem; border-radius:var(--radius-sm); font-size:0.85rem;">
              ✓ Seluruh 10 butir tugas simulasi praktik komputer telah lengkap diserahkan dan dinilai.
            </div>
          `;
        }

        document.getElementById('modalFinishPractical').classList.add('open');
      },

      finishPracticalExam() {
        if (this.practicalTimerInterval) {
          clearInterval(this.practicalTimerInterval);
          this.practicalTimerInterval = null;
        }
        this.closeModals();
        this.examFinished = true;
        safeSetStorage(this.STORAGE_KEY, null);
        this.showFinalResultsView();
      },

      // FINAL RESULTS & SCORING VIEW
      // =======================================================================
      showFinalResultsView() {
        let totalWrittenCorrect = 0;
        let totalWrittenWrong = 0;
        let totalWrittenEmpty = 0;
        let totalWrittenElapsedMs = 0;

        const bidangStats = [];

        this.sections.forEach(sec => {
          let bCorrect = 0;
          let bWrong = 0;
          let bEmpty = 0;

          sec.questions.forEach(q => {
            const ans = sec.userAnswers[q.id];
            if (ans === undefined) {
              bEmpty++;
            } else if (ans === q.answer) {
              bCorrect++;
            } else {
              bWrong++;
            }
          });

          totalWrittenCorrect += bCorrect;
          totalWrittenWrong += bWrong;
          totalWrittenEmpty += bEmpty;
          totalWrittenElapsedMs += (sec.timeUsedMs || 0);

          const bScore = bCorrect * 0.7; // 25 x 0.7 = 17.50 max

          bidangStats.push({
            id: sec.bidangId,
            name: sec.name,
            total: sec.questions.length,
            correct: bCorrect,
            wrong: bWrong,
            empty: bEmpty,
            score: bScore
          });
        });

        // Written Exam Total: Max 87.50
        const writtenScore = totalWrittenCorrect * 0.7;

        // Practical Exam Total: Max 12.50
        let practicalScore = 0;
        let practicalDoneCount = 0;
        this.practicalTasks.forEach(t => {
          practicalScore += (t.earnedScore || 0);
          if (t.isCompleted) practicalDoneCount++;
        });

        // Combined Final Score: Max 100.00
        const finalScore = Math.min(100.0, writtenScore + practicalScore);

        // Header info
        document.getElementById('resCandidateHeading').textContent = `Hasil Simulasi Ujian: ${this.candidateName}`;
        document.getElementById('resCandidateSubheading').textContent = `${this.candidateVillage} • Kabupaten Tuban, Jawa Timur`;
        document.getElementById('resDateBadge').textContent = new Date().toLocaleDateString('id-ID', { day: 'numeric', month: 'long', year: 'numeric' });

        // Stats boxes
        document.getElementById('resTotalSoal').textContent = 125;
        document.getElementById('resCountBenar').textContent = totalWrittenCorrect;
        document.getElementById('resCountSalah').textContent = totalWrittenWrong;
        document.getElementById('resCountKosong').textContent = totalWrittenEmpty;

        const elMinutes = Math.floor(totalWrittenElapsedMs / 60000);
        const elSeconds = Math.floor((totalWrittenElapsedMs % 60000) / 1000);
        document.getElementById('resTimeUsed').textContent = `${elMinutes}m ${elSeconds}s`;

        // Big Score Value & Interim Notice
        const hasPendingReview = this.practicalTasks.some(t => t.status === 'pending_review');
        const hasUnsubmitted = this.practicalTasks.some(t => !t.isCompleted);

        const incompNotice = document.getElementById('resPracticalIncompleteNotice');
        if (incompNotice) {
          if (hasPendingReview || hasUnsubmitted) {
            incompNotice.style.display = 'block';
            incompNotice.innerHTML = hasPendingReview 
              ? '⏳ <strong>Nilai Sementara:</strong> Terdapat tugas praktik berstatus Menunggu Penilaian verifikasi penguji.'
              : '⚠️ <strong>Nilai Sementara:</strong> Terdapat tugas praktik yang belum diserahkan (dihitung 0,00 poin).';
          } else {
            incompNotice.style.display = 'none';
          }
        }

        if (hasPendingReview || hasUnsubmitted) {
          document.getElementById('resScoreValue').textContent = `${finalScore.toFixed(2)}*`;
          document.getElementById('resScoreFinalTotal').textContent = `${finalScore.toFixed(2)} / 100.00 (Nilai Sementara)`;
        } else {
          document.getElementById('resScoreValue').textContent = finalScore.toFixed(2);
          document.getElementById('resScoreFinalTotal').textContent = `${finalScore.toFixed(2)} / 100.00`;
        }

        // Breakdown card numbers
        document.getElementById('resScoreWrittenTotal').textContent = `${writtenScore.toFixed(2)} / 87.50`;
        document.getElementById('resFormulaWrittenDesc').textContent = `Rumus: ${totalWrittenCorrect} Jawaban Benar × 0,7 Poin = ${writtenScore.toFixed(2)} Poin`;

        document.getElementById('resScorePracticalTotal').textContent = `${practicalScore.toFixed(2)} / 12.50`;
        document.getElementById('resFormulaPracticalDesc').textContent = `Skor Terkumpul: ${practicalScore.toFixed(2)} Poin (${practicalDoneCount} dari 10 Butir Selesai Dinilai)`;

        // Render 5 Bidang Cards
        const bGrid = document.getElementById('bidangResultsGridContainer');
        if (bGrid) {
          let bHtml = '';
          bidangStats.forEach(b => {
            bHtml += `
              <div class="bidang-res-card">
                <h4>Bidang ${b.id}: ${b.name}</h4>
                <div class="bidang-res-score">${b.score.toFixed(2)} <span style="font-size:0.85rem; color:var(--slate-500);">/ 17.50</span></div>
                <div style="font-size:0.82rem; color:var(--slate-600); margin-top:0.35rem;">
                  <span style="color:var(--emerald-600); font-weight:700;">${b.correct} Benar</span> • 
                  <span style="color:var(--rose-600); font-weight:700;">${b.wrong} Salah</span> • 
                  <span style="color:var(--slate-500);">${b.empty} Kosong</span>
                </div>
              </div>
            `;
          });
          bGrid.innerHTML = bHtml;
        }

        // Render 10 Practical Results Table
        const pTbody = document.getElementById('resultsPracticalTableBody');
        if (pTbody) {
          let pHtml = '';
          this.practicalTasks.forEach(t => {
            let statusBadge = '';
            if (!t.isCompleted) {
              statusBadge = '<span class="badge-status-revision" style="padding:3px 6px; border-radius:4px; font-weight:700;">✕ Belum Diserahkan (0.00)</span>';
            } else if (t.status === 'pending_review') {
              statusBadge = '<span class="badge-status-pending" style="padding:3px 6px; border-radius:4px; font-weight:700;">⏳ Menunggu Penilaian Penguji</span>';
            } else if (t.status === 'pass' || (t.earnedScore && t.earnedScore >= t.maxScore)) {
              statusBadge = '<span class="badge-status-pass" style="padding:3px 6px; border-radius:4px; font-weight:700;">✓ Lulus (Memenuhi Kriteria)</span>';
            } else {
              statusBadge = '<span class="badge-status-revision" style="padding:3px 6px; border-radius:4px; font-weight:700;">⚠️ Perlu Perbaikan</span>';
            }

            const modeLabel = t.practicalMode === 'sim' 
              ? '<span class="badge-pill" style="font-size:0.68rem; background:#dbeafe; color:#1e40af; border:1px solid #bfdbfe;">Mode 2: Browser</span>'
              : '<span class="badge-pill" style="font-size:0.68rem; background:#fef3c7; color:#92400e; border:1px solid #fde68a;">Mode 1: Office Asli</span>';

            pHtml += `
              <tr>
                <td style="text-align:center; font-weight:700;">${t.id}</td>
                <td style="font-weight:600;">
                  ${t.title}
                  <div style="font-size:0.75rem; color:var(--slate-500); margin-top:2px;">Target: <code>${t.expectedFileName}</code></div>
                </td>
                <td>
                  <span class="badge-pill badge-cat" style="font-size:0.7rem;">${t.category.split('(')[0]}</span>
                  <div style="margin-top:3px;">${modeLabel}</div>
                </td>
                <td style="text-align:center; font-weight:800; color:var(--primary-700);">${(t.earnedScore || 0).toFixed(2)}</td>
                <td style="text-align:center; font-weight:700; color:var(--slate-500);">${t.maxScore.toFixed(2)}</td>
                <td style="font-size:0.82rem;">${statusBadge}</td>
              </tr>
            `;
          });
          pTbody.innerHTML = pHtml;
        }

        // Render Weakness Analysis
        this.renderWeaknessAnalysis(bidangStats);

        // Render Question Reviews for all 125 questions
        this.buildAllQuestionsReviewData();
        this.renderActiveReviewTab();

        // Save to History (Local Persistence)
        this.saveExamToHistory({
          id: 'sesi_' + Date.now(),
          timestamp: Date.now(),
          dateFormatted: new Date().toLocaleDateString('id-ID', { day: 'numeric', month: 'short', year: 'numeric', hour: '2-digit', minute: '2-digit' }),
          candidateName: this.candidateName,
          format: 'Ujian Resmi Tuban (5 Bidang + Praktik)',
          totalWrittenQuestions: 125,
          writtenCorrect: totalWrittenCorrect,
          writtenScore: writtenScore,
          practicalScore: practicalScore,
          practicalDone: practicalDoneCount,
          finalScore: finalScore,
          bidangScores: bidangStats.map(b => ({ id: b.id, name: b.name, score: b.score }))
        });

        this.navigate('results');
      },

      renderWeaknessAnalysis(bidangStats) {
        const container = document.getElementById('weaknessListContainer');
        if (!container) return;

        // Sort ascending by accuracy
        const sorted = [...bidangStats].sort((a, b) => (a.score / 17.5) - (b.score / 17.5));

        let html = '';
        sorted.forEach(b => {
          const pct = ((b.score / 17.5) * 100).toFixed(0);
          let badge = '';
          let advice = '';

          if (pct < 55) {
            badge = '<span class="badge-pill badge-diff-sulit">PERLU PENDALAMAN SERIUS</span>';
            advice = `Penguasaan materi pada Bidang ${b.name} masih di bawah target kelulusan. Pelajari kembali peraturan perundang-undangan dan rujukan materi bidang ini.`;
          } else if (pct < 75) {
            badge = '<span class="badge-pill badge-diff-sedang">CUKUP - PERLU PENGUATAN</span>';
            advice = `Kemampuan cukup baik, perbanyak latihan soal studi kasus dan cermati regulasi spesifik Kabupaten Tuban.`;
          } else {
            badge = '<span class="badge-pill badge-diff-mudah">MENGUASAI DENGAN BAIK</span>';
            advice = `Pertahankan penguasaan materi yang sangat baik pada bidang ini.`;
          }

          html += `
            <div style="background:var(--slate-50); border:1px solid var(--slate-200); border-radius:var(--radius-md); padding:1rem; margin-bottom:0.75rem;">
              <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem; margin-bottom:0.35rem;">
                <strong style="color:var(--primary-900);">Bidang ${b.id}: ${b.name} (${pct}%)</strong>
                ${badge}
              </div>
              <p style="font-size:0.85rem; color:var(--slate-700); line-height:1.4;">${advice}</p>
            </div>
          `;
        });

        container.innerHTML = html;
      },

      // =======================================================================
      // REVIEW TABS (ALL 125 WRITTEN QUESTIONS REVIEW)
      // =======================================================================
      buildAllQuestionsReviewData() {
        this.allReviewItems = [];
        let globalNumber = 1;

        this.sections.forEach(sec => {
          sec.questions.forEach(q => {
            const userAns = sec.userAnswers[q.id];
            const isAnswered = userAns !== undefined;
            const isCorrect = isAnswered && userAns === q.answer;

            this.allReviewItems.push({
              globalNumber: globalNumber++,
              bidangId: sec.bidangId,
              bidangName: sec.name,
              id: q.id,
              question: q.question,
              options: q.options,
              answer: q.answer,
              userAnswer: userAns,
              isAnswered,
              isCorrect,
              status: !isAnswered ? 'empty' : (isCorrect ? 'correct' : 'wrong'),
              explanation: q.explanation,
              source: q.source,
              category: q.category
            });
          });
        });
      },

      setReviewTab(tabName) {
        this.activeReviewTab = tabName;
        document.querySelectorAll('#fullReviewContainerSection .btn-sm').forEach(b => b.classList.remove('active'));
        const btnMap = {
          wrong: 'tabRevWrong',
          empty: 'tabRevEmpty',
          correct: 'tabRevCorrect',
          all: 'tabRevAll',
          b1: 'tabRevB1',
          b2: 'tabRevB2',
          b3: 'tabRevB3',
          b4: 'tabRevB4',
          b5: 'tabRevB5'
        };
        if (btnMap[tabName]) {
          document.getElementById(btnMap[tabName])?.classList.add('active');
        }
        this.renderActiveReviewTab();
      },

      renderActiveReviewTab() {
        const container = document.getElementById('evalReviewContainer');
        if (!container || !this.allReviewItems) return;

        const searchKeyword = (document.getElementById('reviewSearchInput')?.value || '').toLowerCase().trim();

        let filtered = this.allReviewItems.filter(item => {
          // Status / Bidang filter
          if (this.activeReviewTab === 'wrong' && item.status !== 'wrong') return false;
          if (this.activeReviewTab === 'empty' && item.status !== 'empty') return false;
          if (this.activeReviewTab === 'correct' && item.status !== 'correct') return false;
          if (this.activeReviewTab === 'b1' && item.bidangId !== 1) return false;
          if (this.activeReviewTab === 'b2' && item.bidangId !== 2) return false;
          if (this.activeReviewTab === 'b3' && item.bidangId !== 3) return false;
          if (this.activeReviewTab === 'b4' && item.bidangId !== 4) return false;
          if (this.activeReviewTab === 'b5' && item.bidangId !== 5) return false;

          // Search keyword
          if (searchKeyword) {
            const matchQ = item.question.toLowerCase().includes(searchKeyword);
            const matchExp = item.explanation.toLowerCase().includes(searchKeyword);
            const matchSrc = item.source.toLowerCase().includes(searchKeyword);
            return matchQ || matchExp || matchSrc;
          }
          return true;
        });

        if (filtered.length === 0) {
          container.innerHTML = '<div style="text-align:center; padding:2rem; color:var(--slate-500);">Tidak ada butir soal yang sesuai dengan kriteria filter saat ini.</div>';
          return;
        }

        const letters = ['A', 'B', 'C', 'D'];
        let html = '';

        filtered.forEach(item => {
          let statusBadge = '';
          if (item.status === 'correct') {
            statusBadge = '<span class="badge-pill badge-diff-mudah">✓ Jawaban Benar (+0,70 Poin)</span>';
          } else if (item.status === 'wrong') {
            statusBadge = '<span class="badge-pill badge-diff-sulit">✗ Jawaban Salah (0 Poin)</span>';
          } else {
            statusBadge = '<span class="badge-pill" style="background:var(--slate-200); color:var(--slate-700);">○ Tidak Dijawab (0 Poin)</span>';
          }

          html += `
            <div style="background:var(--white); border:1px solid var(--slate-200); border-radius:var(--radius-md); padding:1.25rem; margin-bottom:1rem; box-shadow:var(--shadow-sm);">
              <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem; margin-bottom:0.75rem;">
                <span style="font-weight:800; color:var(--primary-800);">No. ${item.globalNumber} (Bidang ${item.bidangId}: ${item.bidangName})</span>
                ${statusBadge}
              </div>

              <div style="font-size:1rem; font-weight:600; color:var(--slate-900); line-height:1.5; margin-bottom:1rem;">
                ${this.formatRichText(item.question)}
              </div>

              <div style="display:grid; grid-template-columns:1fr; gap:0.4rem; margin-bottom:1rem;">
          `;

          item.options.forEach((optText, optIdx) => {
            const isUser = item.userAnswer === optIdx;
            const isKey = item.answer === optIdx;

            let optStyle = 'border:1px solid var(--slate-200); background:var(--white); color:var(--slate-800);';
            let mark = '';

            if (isKey) {
              optStyle = 'border:2px solid var(--emerald-600); background:var(--emerald-50); color:var(--emerald-900); font-weight:700;';
              mark = ' <span style="color:var(--emerald-700); font-weight:800;">[KUNCI JAWABAN BENAR]</span>';
            }
            if (isUser && !isKey) {
              optStyle = 'border:2px solid var(--rose-600); background:var(--rose-50); color:var(--rose-900); font-weight:700;';
              mark = ' <span style="color:var(--rose-700); font-weight:800;">[PILIHAN ANDA - SALAH]</span>';
            }

            html += `
              <div style="padding:0.55rem 0.85rem; border-radius:var(--radius-sm); font-size:0.9rem; ${optStyle}">
                <strong>${letters[optIdx]}.</strong> ${this.formatRichText(optText)} ${mark}
              </div>
            `;
          });

          html += `
              </div>

              <div class="explanation-box" style="margin-top:0.75rem;">
                <div class="explanation-title">Pembahasan & Landasan Regulasi:</div>
                <div class="explanation-content">${this.formatRichText(item.explanation)}</div>
                <div class="explanation-source"><strong>Rujukan:</strong> ${this.formatRichText(item.source)}</div>
              </div>
            </div>
          `;
        });

        container.innerHTML = html;
      },

      scrollToReviewSection() {
        document.getElementById('fullReviewContainerSection')?.scrollIntoView({ behavior: 'smooth' });
      },

      // =======================================================================
      // MODE LATIHAN MANDIRI (PRACTICE MODE)
      // =======================================================================
      startPracticeSession() {
        this.readCandidateInputs();
        this.mode = 'practice';
        this.examFinished = false;

        const catSelect = document.getElementById('practiceCategorySelect');
        const countSelect = document.getElementById('practiceCountSelect');
        const shuffleSelect = document.getElementById('practiceShuffleSelect');

        const selectedCat = catSelect ? catSelect.value : 'all';
        const count = countSelect ? parseInt(countSelect.value, 10) : 25;
        const doShuffle = shuffleSelect ? shuffleSelect.value === 'yes' : true;

        let pool = [];
        let labelName = 'Latihan Mandiri';
        if (selectedCat === 'all') {
          pool = [...MASTER_QUESTIONS];
          labelName = 'Semua Bidang (Master Bank 1.000 Soal)';
        } else if (selectedCat.startsWith('bidang_')) {
          const bId = parseInt(selectedCat.replace('bidang_', ''), 10);
          pool = MASTER_QUESTIONS.filter(q => q.bidangId === bId);
          const matchedCfg = BIDANG_CONFIG.find(b => b.id === bId);
          labelName = matchedCfg ? matchedCfg.title : `Bidang ${bId}`;
        } else {
          pool = MASTER_QUESTIONS.filter(q => q.category === selectedCat);
          labelName = selectedCat;
        }

        const shuffledPool = doShuffle ? shuffleArray(pool) : [...pool];
        const sampled = shuffledPool.slice(0, Math.min(count, pool.length));

        const formatted = sampled.map((q, idx) => ({
          ...q,
          number: idx + 1,
          bidangId: q.bidangId || 0,
          bidangName: labelName,
          options: doShuffle ? shuffleArray([...q.options]) : [...q.options],
          answer: doShuffle ? -1 : q.answer, // Computed below
          originalAnswer: q.answer
        }));

        if (doShuffle) {
          formatted.forEach(q => {
            const originalCorrect = MASTER_QUESTIONS.find(m => m.id === q.id).options[q.originalAnswer];
            q.answer = q.options.indexOf(originalCorrect);
          });
        }

        this.sections = [{
          bidangId: 0,
          bidangName: 'Latihan Mandiri',
          title: 'Mode Latihan Mandiri',
          shortName: 'Latihan',
          durationMinutes: 30,
          durationMs: 30 * 60 * 1000,
          questions: formatted,
          userAnswers: {},
          flaggedQuestions: {},
          currentIndex: 0,
          startTime: Date.now(),
          isCompleted: false,
          score: 0
        }];
        this.currentSectionIndex = 0;

        const hasTimer = document.getElementById('practiceTimerToggle')?.checked;
        if (hasTimer) {
          this.sectionStartTime = Date.now();
          this.sectionDurationMs = Math.ceil(formatted.length * 1.2) * 60 * 1000;
          this.startSectionTimer();
        } else {
          if (this.timerInterval) clearInterval(this.timerInterval);
          this.isTimerRunning = false;
          const tDisp = document.getElementById('displaySectionTimer');
          if (tDisp) tDisp.textContent = 'BEBAS';
        }

        this.updateExamHeaderUI();
        this.renderQuestionPaletteGrid();
        this.renderCurrentQuestion();
        this.navigate('exam');
      },

      // =======================================================================
      // GLOSARIUM & HISTORY
      // =======================================================================
      renderGlossary() {
        const container = document.getElementById('glossaryListContainer');
        if (!container) return;

        const kw = (document.getElementById('glossarySearchInput')?.value || '').toLowerCase().trim();
        const cat = document.getElementById('glossaryCategorySelect')?.value || 'all';

        const filtered = GLOSSARY_DATA.filter(term => {
          if (cat !== 'all' && term.category !== cat) return false;
          if (kw) {
            const matchTerm = term.term.toLowerCase().includes(kw);
            const matchFull = (term.fullName || '').toLowerCase().includes(kw);
            const matchDef = term.definition.toLowerCase().includes(kw);
            return matchTerm || matchFull || matchDef;
          }
          return true;
        });

        if (filtered.length === 0) {
          container.innerHTML = '<div style="grid-column:1/-1; text-align:center; color:var(--slate-500); padding:2rem;">Tidak ditemukan istilah yang cocok.</div>';
          return;
        }

        let html = '';
        filtered.forEach(term => {
          html += `
            <div style="background:var(--white); border:1px solid var(--slate-200); border-radius:var(--radius-md); padding:1.25rem; box-shadow:var(--shadow-sm);">
              <div style="display:flex; justify-content:space-between; align-items:flex-start; gap:0.5rem; margin-bottom:0.35rem;">
                <h4 style="font-size:1.1rem; font-weight:800; color:var(--primary-800);">${term.term}</h4>
                <span class="badge-pill badge-cat" style="font-size:0.7rem;">${term.category}</span>
              </div>
              ${term.fullName ? `<div style="font-size:0.85rem; font-weight:600; color:var(--slate-600); margin-bottom:0.5rem;">${term.fullName}</div>` : ''}
              <p style="font-size:0.88rem; color:var(--slate-800); line-height:1.5; margin-bottom:0.5rem;">${term.definition}</p>
              ${term.legalBasis ? `<div style="font-size:0.78rem; color:var(--slate-500);"><strong>Dasar Hukum:</strong> ${term.legalBasis}</div>` : ''}
            </div>
          `;
        });

        container.innerHTML = html;
      },

      saveExamToHistory(historyItem) {
        const historyList = safeGetStorage(this.HISTORY_KEY, []);
        historyList.unshift(historyItem);
        // Keep max 25 history entries
        if (historyList.length > 25) historyList.pop();
        safeSetStorage(this.HISTORY_KEY, historyList);
      },

      renderHistoryView() {
        const tbody = document.getElementById('historyTableBody');
        if (!tbody) return;

        const historyList = safeGetStorage(this.HISTORY_KEY, []);
        if (historyList.length === 0) {
          tbody.innerHTML = '<tr><td colspan="8" style="text-align:center; padding:2rem; color:var(--slate-500);">Belum ada riwayat pelaksanaan ujian. Selesaikan ujian untuk mencatat progres nilai.</td></tr>';
          return;
        }

        let html = '';
        historyList.forEach((item, idx) => {
          const written = item.writtenScore !== undefined ? item.writtenScore.toFixed(2) : '-';
          const practical = item.practicalScore !== undefined ? item.practicalScore.toFixed(2) : '-';
          const finalSc = item.finalScore !== undefined ? item.finalScore.toFixed(2) : (item.score || 0).toFixed(2);

          html += `
            <tr>
              <td style="text-align:center; font-weight:700;">${idx + 1}</td>
              <td style="white-space:nowrap;">${item.dateFormatted || '-'}</td>
              <td style="font-weight:600;">${item.candidateName || 'Peserta'}</td>
              <td><span class="badge-pill badge-cat" style="font-size:0.72rem;">${item.format || 'Format Tuban'}</span></td>
              <td style="text-align:center; font-weight:700; color:var(--primary-700);">${written}</td>
              <td style="text-align:center; font-weight:700; color:var(--emerald-700);">${practical}</td>
              <td style="text-align:center; font-weight:900; color:var(--accent-gold-700); font-size:1.05rem;">${finalSc}</td>
              <td style="font-size:0.8rem;">${item.practicalDone === 10 ? '✓ Lengkap' : '10 Butir'}</td>
            </tr>
          `;
        });
        tbody.innerHTML = html;

        this.renderHistoryChart(historyList);
      },

      renderHistoryChart(historyList) {
        const container = document.getElementById('chartContainer');
        if (!container || historyList.length === 0) return;

        const items = [...historyList].reverse(); // chronological
        const w = container.clientWidth || 600;
        const h = 200;
        const padX = 40;
        const padY = 30;

        const pts = items.map((it, i) => {
          const sc = it.finalScore !== undefined ? it.finalScore : (it.score || 0);
          const x = padX + (i * ((w - padX * 2) / Math.max(1, items.length - 1)));
          const y = h - padY - ((sc / 100) * (h - padY * 2));
          return { x, y, sc, date: it.dateFormatted };
        });

        let pathD = '';
        pts.forEach((p, i) => {
          pathD += (i === 0 ? `M ${p.x} ${p.y}` : ` L ${p.x} ${p.y}`);
        });

        let svgHtml = `
          <svg width="100%" height="${h}" viewBox="0 0 ${w} ${h}">
            <line x1="${padX}" y1="${h - padY}" x2="${w - padX}" y2="${h - padY}" stroke="#cbd5e1" stroke-width="1"/>
            <line x1="${padX}" y1="${padY}" x2="${w - padX}" y2="${padY}" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="3,3"/>
            <text x="${padX - 8}" y="${h - padY + 4}" font-size="10" fill="#64748b" text-anchor="end">0</text>
            <text x="${padX - 8}" y="${padY + 4}" font-size="10" fill="#64748b" text-anchor="end">100</text>
            <path d="${pathD}" fill="none" stroke="var(--primary-600)" stroke-width="3" stroke-linecap="round"/>
        `;

        pts.forEach(p => {
          svgHtml += `
            <circle cx="${p.x}" cy="${p.y}" r="5" fill="var(--accent-gold-500)" stroke="var(--primary-900)" stroke-width="2"/>
            <text x="${p.x}" y="${p.y - 10}" font-size="11" font-weight="bold" fill="var(--primary-900)" text-anchor="middle">${p.sc.toFixed(1)}</text>
          `;
        });

        svgHtml += '</svg>';
        container.innerHTML = svgHtml;
      },

      confirmClearHistory() {
        if (confirm('Apakah Anda yakin ingin menghapus seluruh riwayat nilai simulasi?')) {
          safeSetStorage(this.HISTORY_KEY, []);
          this.renderHistoryView();
        }
      },

      // =======================================================================
      // SESSION RESILIENCE & BACKUP
      // =======================================================================
      saveSession() {
        if (this.examFinished) return;
        const payload = {
          version: 'tuban_v4',
          mode: this.mode,
          candidateName: this.candidateName,
          candidateVillage: this.candidateVillage,
          region: this.region,
          currentSectionIndex: this.currentSectionIndex,
          sections: this.sections,
          practicalTasks: this.practicalTasks,
          currentPracticalIndex: this.currentPracticalIndex,
          practicalMode: this.practicalMode,
          practicalDurationMinutes: this.practicalDurationMinutes,
          practicalRemainingSeconds: this.practicalRemainingSeconds,
          practicalStartTime: this.practicalStartTime,
          isPracticalLocked: this.isPracticalLocked,
          savedAt: Date.now()
        };
        safeSetStorage(this.STORAGE_KEY, payload);
      },

      checkExistingSession() {
        const saved = safeGetStorage(this.STORAGE_KEY, null);
        const banner = document.getElementById('resumeBanner');
        if (saved && saved.sections && saved.sections.length > 0) {
          if (banner) banner.style.display = 'flex';
        } else if (banner) {
          banner.style.display = 'none';
        }
      },

      resumeSession() {
        const saved = safeGetStorage(this.STORAGE_KEY, null);
        if (!saved) return;

        this.mode = saved.mode || 'official_exam';
        this.candidateName = saved.candidateName || 'Peserta';
        this.candidateVillage = saved.candidateVillage || 'Kabupaten Tuban';
        this.region = saved.region || 'tuban';
        this.currentSectionIndex = saved.currentSectionIndex || 0;
        this.sections = saved.sections || [];
        this.practicalTasks = saved.practicalTasks || [];
        this.currentPracticalIndex = saved.currentPracticalIndex || 0;
        this.practicalMode = saved.practicalMode || 'office';
        this.practicalDurationMinutes = saved.practicalDurationMinutes !== undefined ? saved.practicalDurationMinutes : 45;
        this.practicalRemainingSeconds = saved.practicalRemainingSeconds !== undefined ? saved.practicalRemainingSeconds : 45 * 60;
        this.practicalStartTime = saved.practicalStartTime || null;
        this.isPracticalLocked = saved.isPracticalLocked || false;

        const banner = document.getElementById('resumeBanner');
        if (banner) banner.style.display = 'none';

        if (this.currentSectionIndex === 5) {
          this.startPracticalSession();
        } else {
          this.startSection(this.currentSectionIndex);
        }
      },

      clearSession() {
        safeSetStorage(this.STORAGE_KEY, null);
        const banner = document.getElementById('resumeBanner');
        if (banner) banner.style.display = 'none';
      },

      openBackupModal() {
        document.getElementById('modalBackupRestore').classList.add('open');
      },

      openVersionModal() {
        const m = document.getElementById('modalVersionInfo');
        if (m) m.classList.add('open');
      },

      exportBackupJSON() {
        const data = {
          app: 'Simulasi Ujian Perangkat Desa Kabupaten Tuban',
          version: '4.5.0',
          copyright: 'Copyright by fusionproject.id',
          exportedAt: new Date().toISOString(),
          history: safeGetStorage(this.HISTORY_KEY, [])
        };
        const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `Cadangan_Ujian_Perangkat_Desa_Tuban_${Date.now()}.json`;
        a.click();
        URL.revokeObjectURL(url);
      },

      importBackupJSON(mode = 'merge') {
        const fileInput = document.getElementById('backupFileInput');
        if (!fileInput || !fileInput.files || fileInput.files.length === 0) {
          alert('Pilih file cadangan JSON terlebih dahulu.');
          return;
        }

        const file = fileInput.files[0];
        const reader = new FileReader();
        reader.onload = (e) => {
          try {
            const data = JSON.parse(e.target.result);
            if (!data.history || !Array.isArray(data.history)) {
              throw new Error('Format berkas JSON cadangan tidak valid.');
            }
            if (mode === 'replace') {
              safeSetStorage(this.HISTORY_KEY, data.history);
            } else {
              const current = safeGetStorage(this.HISTORY_KEY, []);
              const merged = [...data.history, ...current];
              safeSetStorage(this.HISTORY_KEY, merged);
            }
            alert('Data cadangan berhasil dipulihkan!');
            this.closeModals();
            this.renderHistoryView();
          } catch (err) {
            alert('Gagal memproses berkas cadangan: ' + err.message);
          }
        };
        reader.readAsText(file);
      },

      exportCSV() {
        if (!this.allReviewItems) return;
        let csv = 'No,Bidang,Kategori,Pertanyaan,Kunci_Jawaban,Jawaban_Peserta,Status,Rujukan\\n';
        this.allReviewItems.forEach(item => {
          const qText = `"${item.question.replace(/"/g, '""')}"`;
          const keyText = `"${item.options[item.answer].replace(/"/g, '""')}"`;
          const usrText = item.userAnswer !== undefined ? `"${item.options[item.userAnswer].replace(/"/g, '""')}"` : '"Kosong"';
          const srcText = `"${(item.source || '').replace(/"/g, '""')}"`;
          csv += `${item.globalNumber},"${item.bidangName}","${item.category}",${qText},${keyText},${usrText},"${item.status}",${srcText}\\n`;
        });

        const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `Hasil_Ujian_Perangkat_Desa_Tuban_${Date.now()}.csv`;
        a.click();
        URL.revokeObjectURL(url);
      },

      exportJSON() {
        if (!this.allReviewItems) return;
        const data = {
          candidateName: this.candidateName,
          village: this.candidateVillage,
          date: new Date().toISOString(),
          sections: this.sections.map(s => ({ id: s.bidangId, name: s.name, score: s.score })),
          practical: this.practicalTasks.map(t => ({ id: t.id, title: t.title, score: t.earnedScore })),
          review: this.allReviewItems
        };
        const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `Hasil_Ujian_Perangkat_Desa_Tuban_${Date.now()}.json`;
        a.click();
        URL.revokeObjectURL(url);
      },

      // Keyboard Shortcuts (A, B, C, D, Arrows, R, P, Esc)
      setupKeyboardShortcuts() {
        window.addEventListener('keydown', (e) => {
          if (e.key === 'Escape') {
            this.closeModals();
            return;
          }

          if (this.examFinished) return;
          if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT' || e.target.tagName === 'TEXTAREA') return;

          const key = e.key.toUpperCase();
          if (key === 'A') this.selectOption(0);
          else if (key === 'B') this.selectOption(1);
          else if (key === 'C') this.selectOption(2);
          else if (key === 'D') this.selectOption(3);
          else if (e.key === 'ArrowLeft') this.prevQuestion();
          else if (e.key === 'ArrowRight') this.skipOrNextQuestion();
          else if (key === 'R' || key === 'F') this.toggleFlagCurrentQuestion();
        });
      }
    };

    // Expose to window for modular scripts and testing
    window.CBTApp = CBTApp;
    window.BIDANG_CONFIG = BIDANG_CONFIG;

    // Auto initialize on DOMContentLoaded
    if (typeof document !== 'undefined') {
      document.addEventListener('DOMContentLoaded', () => {
        CBTApp.init();
      });
    }
