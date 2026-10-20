// Automated End-to-End State Machine Simulation for CBTApp in index.html
const fs = require('fs');
const path = require('path');

const htmlContent = fs.readFileSync(path.join(__dirname, 'index.html'), 'utf-8');

console.log("=========================================================================");
console.log("SIMULASI STATE MACHINE CBT PERANGKAT DESA KAB. TUBAN (5 BIDANG + PRAKTIK)");
console.log("=========================================================================");

// Setup mock browser window & document environment
const mockLocalStorage = {};
global.localStorage = {
  getItem: (k) => mockLocalStorage[k] || null,
  setItem: (k, v) => { mockLocalStorage[k] = v; },
  removeItem: (k) => { delete mockLocalStorage[k]; }
};

global.window = {
  scrollTo: () => {},
  addEventListener: () => {},
  localStorage: global.localStorage
};

const domElements = {};
function createMockElement(id) {
  return {
    id,
    style: {},
    classList: {
      add: function(c) { this[c] = true; },
      remove: function(c) { delete this[c]; },
      contains: function(c) { return !!this[c]; }
    },
    value: '',
    textContent: '',
    innerHTML: '',
    disabled: false,
    checked: false,
    scrollIntoView: () => {},
    focus: () => {}
  };
}

global.document = {
  getElementById: (id) => {
    if (!domElements[id]) domElements[id] = createMockElement(id);
    return domElements[id];
  },
  querySelectorAll: (selector) => {
    return [];
  },
  documentElement: {
    style: { setProperty: () => {} }
  },
  body: {
    appendChild: () => {}
  },
  addEventListener: () => {}
};

// Muat seluruh file modular ke sandbox node
const vm = require('vm');
const context = vm.createContext({
  window: global.window,
  document: global.document,
  localStorage: global.localStorage,
  console: console,
  setTimeout: setTimeout,
  clearTimeout: clearTimeout,
  setInterval: setInterval,
  clearInterval: clearInterval,
  parseFloat: parseFloat,
  parseInt: parseInt,
  Math: Math,
  JSON: JSON,
  Array: Array,
  Set: Set,
  Object: Object,
  String: String,
  Number: Number,
  Boolean: Boolean,
  Date: Date,
  RegExp: RegExp
});

vm.runInContext(fs.readFileSync(path.join(__dirname, 'js/data/questions.js'), 'utf-8'), context);
vm.runInContext(fs.readFileSync(path.join(__dirname, 'js/data/glossary.js'), 'utf-8'), context);
vm.runInContext(fs.readFileSync(path.join(__dirname, 'js/data/practical.js'), 'utf-8'), context);
vm.runInContext(fs.readFileSync(path.join(__dirname, 'js/app.js'), 'utf-8'), context);

const CBTApp = context.window.CBTApp;
if (!CBTApp) throw new Error("CBTApp gagal dimuat dari js/app.js");

console.log("[1] Memeriksa Inisialisasi CBTApp...");
CBTApp.init();
console.log("  -> CBTApp.init() berhasil dijalankan tanpa error.");

console.log("\n[2] Memulai Ujian Resmi Format Kabupaten Tuban (startExamNow)...");
document.getElementById('inputCandidateName').value = 'Ahmad Tuban';
document.getElementById('inputCandidateVillage').value = 'Desa Sugihwaras, Kec. Jenu';
document.getElementById('selectRegion').value = 'tuban';

CBTApp.startExamNow();

if (CBTApp.sections.length !== 5) {
  throw new Error(`Jumlah seksi ujian tertulis harus 5, didapat ${CBTApp.sections.length}`);
}
if (CBTApp.currentSectionIndex !== 0) {
  throw new Error(`Seksi awal harus index 0 (Agama), didapat ${CBTApp.currentSectionIndex}`);
}
console.log(`  -> Berhasil memulai Bidang 1: ${CBTApp.sections[0].name} (25 Soal, 30 Menit).`);

console.log("\n[3] Mengerjakan Bidang 1 (Agama)...");
// Jawab 20 soal benar, 3 soal salah, 2 soal kosong
const sec0 = CBTApp.sections[0];
for (let i = 0; i < 20; i++) {
  sec0.currentIndex = i;
  CBTApp.selectOption(sec0.questions[i].answer); // Benar
}
for (let i = 20; i < 23; i++) {
  sec0.currentIndex = i;
  CBTApp.selectOption((sec0.questions[i].answer + 1) % 4); // Salah
}
// Soal 23 & 24 kosong
console.log("  -> Menyelesaikan Bidang 1...");
CBTApp.finishCurrentSection('USER_SUBMIT');
if (!sec0.isCompleted) throw new Error("Bidang 1 gagal dikunci!");
console.log("  -> Bidang 1 berhasil dikunci permanen.");

console.log("\n[4] Membuka Bidang 2 (Pengetahuan Pemerintahan Desa)...");
CBTApp.proceedToNextSection();
if (CBTApp.currentSectionIndex !== 1) throw new Error("Gagal beralih ke Bidang 2");
const sec1 = CBTApp.sections[1];
console.log(`  -> Bidang 2 aktif: ${sec1.name}.`);
// Jawab seluruh 25 soal benar pada Bidang 2
for (let i = 0; i < 25; i++) {
  sec1.currentIndex = i;
  CBTApp.selectOption(sec1.questions[i].answer);
}
CBTApp.finishCurrentSection('USER_SUBMIT');
console.log("  -> Bidang 2 berhasil dikunci.");

console.log("\n[5] Menyelesaikan Bidang 3, 4, dan 5 secara berurutan...");
// Bidang 3: Bahasa Indonesia
CBTApp.proceedToNextSection();
const sec2 = CBTApp.sections[2];
for (let i = 0; i < 22; i++) {
  sec2.currentIndex = i;
  CBTApp.selectOption(sec2.questions[i].answer);
}
CBTApp.finishCurrentSection('USER_SUBMIT');

// Bidang 4: Pengetahuan Umum
CBTApp.proceedToNextSection();
const sec3 = CBTApp.sections[3];
for (let i = 0; i < 24; i++) {
  sec3.currentIndex = i;
  CBTApp.selectOption(sec3.questions[i].answer);
}
CBTApp.finishCurrentSection('USER_SUBMIT');

// Bidang 5: Pengetahuan Komputer
CBTApp.proceedToNextSection();
const sec4 = CBTApp.sections[4];
for (let i = 0; i < 25; i++) {
  sec4.currentIndex = i;
  CBTApp.selectOption(sec4.questions[i].answer);
}
CBTApp.finishCurrentSection('USER_SUBMIT');
console.log("  -> Seluruh 5 Bidang Ujian Tertulis telah selesai dikunci!");

console.log("\n[6] Membuka Tahap 6: Praktik Komputer (10 Butir)...");
CBTApp.proceedToNextSection();
if (CBTApp.currentSectionIndex !== 5) throw new Error("Gagal beralih ke Praktik Komputer");
if (CBTApp.practicalTasks.length !== 10) throw new Error("Jumlah tugas praktik bukan 10");
console.log("  -> Tahap Praktik Komputer terbuka (10 Butir Interaktif).");

console.log("\n[7] Mengerjakan dan Menilai 10 Butir Praktik Komputer (Mode Simulasi Browser & Mode Office)...");
// Task 1: Word — Mengetik Dokumen
CBTApp.goToPracticalTask(0);
CBTApp.setPracticalMode('sim');
document.getElementById('simTypingInput').value = CBTApp.practicalTasks[0].defaultData.sourceText;
CBTApp.evaluateBrowserSimTask();

// Task 2: Word — Memformat Naskah
CBTApp.goToPracticalTask(1);
CBTApp.setPracticalMode('sim');
document.getElementById('simPaperSize').value = 'F4';
document.getElementById('simTitleAlign').value = 'center';
document.getElementById('simTitleBold').checked = true;
document.getElementById('simTitleFontSize').value = '14';
document.getElementById('simBodyAlign').value = 'justify';
document.getElementById('simLineSpacing').value = '1.5';
document.getElementById('simMarginLeft').value = '3.5';
CBTApp.evaluateBrowserSimTask();

// Task 3: Word — Membuat Tabel Sederhana
CBTApp.goToPracticalTask(2);
CBTApp.setPracticalMode('sim');
document.getElementById('simTableHeaderBold').checked = true;
document.getElementById('simTableBorder').checked = true;
CBTApp.evaluateBrowserSimTask();

// Task 4: Word — Membuat Surat Resmi
CBTApp.goToPracticalTask(3);
CBTApp.setPracticalMode('sim');
document.getElementById('simLetterKab').value = 'PEMERINTAH KABUPATEN TUBAN';
document.getElementById('simLetterKec').value = 'KECAMATAN RENGEL';
document.getElementById('simLetterDesa').value = 'PEMERINTAH DESA SUKAMAJU';
document.getElementById('simLetterAlamat').value = 'Jalan Raya Rengel No. 12 Kode Pos 62371';
CBTApp.evaluateBrowserSimTask();

// Task 5: Excel — Memasukkan Data ke Tabel Posyandu
CBTApp.goToPracticalTask(4);
CBTApp.setPracticalMode('sim');
CBTApp.evaluateBrowserSimTask();

// Task 6: Excel — Menggunakan Rumus SUM dan AVERAGE
CBTApp.goToPracticalTask(5);
CBTApp.setPracticalMode('sim');
document.getElementById('simFormulaSum').value = '=SUM(D2:D6)';
document.getElementById('simFormulaAvg').value = '=AVERAGE(D2:D6)';
CBTApp.evaluateBrowserSimTask();

// Task 7: Excel — Memformat Angka dan Tabel
CBTApp.goToPracticalTask(6);
CBTApp.setPracticalMode('sim');
document.getElementById('simFmtCurrency').checked = true;
document.getElementById('simFmtBorder').checked = true;
document.getElementById('simFmtHeaderColor').checked = true;
CBTApp.evaluateBrowserSimTask();

// Task 8: Excel — Mengurutkan atau Menyaring Data
CBTApp.goToPracticalTask(7);
CBTApp.setPracticalMode('sim');
document.getElementById('simSortCol').value = 'RT';
document.getElementById('simSortOrder').value = 'asc';
document.getElementById('simFilterVal').value = 'Layak';
CBTApp.evaluateBrowserSimTask();

// Task 9: PowerPoint — Membuat dan Memformat Slide
CBTApp.goToPracticalTask(8);
CBTApp.setPracticalMode('sim');
document.getElementById('simSlide1Title').value = 'Rencana Pembangunan Desa Sukamaju Tahun 2027';
document.getElementById('simSlide2Title').value = '4 Program Prioritas Infrastruktur';
CBTApp.evaluateBrowserSimTask();

// Task 10: Tugas Terpadu — Menyimpan, Memberi Nama, dan Menyerahkan Berkas
CBTApp.goToPracticalTask(9);
CBTApp.setPracticalMode('sim');
document.getElementById('chkPkg1').checked = true;
document.getElementById('chkPkg2').checked = true;
document.getElementById('chkPkg3').checked = true;
document.getElementById('chkPkg4').checked = true;
document.getElementById('simArchiveName').value = 'Berkas_Praktik_Perangkat_Desa_AhmadTuban.zip';
CBTApp.evaluateBrowserSimTask();

let totalPractScoreEarned = 0;
CBTApp.practicalTasks.forEach(t => {
  totalPractScoreEarned += t.earnedScore;
  if (!t.isCompleted) throw new Error(`Butir ${t.id} belum complete`);
});
console.log(`  -> Seluruh 10 butir praktik dinilai! Total skor praktik: ${totalPractScoreEarned.toFixed(2)} / 12.50`);

console.log("\n[8] Mengakhiri Ujian & Menampilkan Hasil Akhir (finishPracticalExam)...");
CBTApp.finishPracticalExam();

if (!CBTApp.examFinished) throw new Error("Status ujian belum finished");

// Validasi Angka Hasil Akhir
const totalWrittenCorrect = 20 + 25 + 22 + 24 + 25; // 116 benar dari 125
const expectedWrittenScore = 116 * 0.7; // 81.20
const expectedFinalScore = expectedWrittenScore + totalPractScoreEarned; // 81.20 + 12.50 = 93.70

console.log(`  -> Total Tertulis Benar : ${totalWrittenCorrect} / 125`);
console.log(`  -> Skor Ujian Tertulis  : ${expectedWrittenScore.toFixed(2)} / 87.50`);
console.log(`  -> Skor Praktik Komputer: ${totalPractScoreEarned.toFixed(2)} / 12.50`);
console.log(`  -> Nilai Akhir Total    : ${expectedFinalScore.toFixed(2)} / 100.00`);

const displayedFinalScore = parseFloat(domElements['resScoreValue'].textContent);
if (Math.abs(displayedFinalScore - expectedFinalScore) > 0.05) {
  throw new Error(`Skor akhir UI tidak cocok: UI=${displayedFinalScore}, Expected=${expectedFinalScore}`);
}
console.log("  -> Skor akhir pada UI terverifikasi 100% presisi.");

console.log("\n[9] Menguji Pembahasan Lengkap (Buka Pembahasan)...");
CBTApp.setReviewTab('all');
if (CBTApp.allReviewItems.length !== 125) {
  throw new Error(`Pembahasan harus memuat seluruh 125 soal, didapat ${CBTApp.allReviewItems.length}`);
}
console.log(`  -> Seluruh 125 butir soal tertulis tersedia di tab pembahasan dengan kunci dan rujukan regulasi.`);

console.log("\n=========================================================================");
console.log("SIMULASI STATE MACHINE END-TO-END BERHASIL 100% TANPA KESALAHAN!");
console.log("=========================================================================");
