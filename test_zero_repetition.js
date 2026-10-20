// test_zero_repetition.js
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const mockLocalStorage = {};
const localStorage = {
  getItem: (k) => mockLocalStorage[k] || null,
  setItem: (k, v) => { mockLocalStorage[k] = String(v); },
  removeItem: (k) => { delete mockLocalStorage[k]; },
  clear: () => { Object.keys(mockLocalStorage).forEach(k => delete mockLocalStorage[k]); }
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
    focus: () => {},
    remove: () => {}
  };
}

const document = {
  getElementById: (id) => {
    if (!domElements[id]) domElements[id] = createMockElement(id);
    return domElements[id];
  },
  createElement: (tag) => createMockElement(tag),
  querySelectorAll: () => [],
  documentElement: { style: { setProperty: () => {} } },
  body: { appendChild: () => {} },
  addEventListener: () => {}
};

const window = {
  scrollTo: () => {},
  addEventListener: () => {},
  localStorage: localStorage
};

const context = vm.createContext({
  window: window,
  document: document,
  localStorage: localStorage,
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
  RegExp: RegExp,
  confirm: () => true
});

vm.runInContext(fs.readFileSync(path.join(__dirname, 'js/data/questions.js'), 'utf-8'), context);
vm.runInContext(fs.readFileSync(path.join(__dirname, 'js/data/glossary.js'), 'utf-8'), context);
vm.runInContext(fs.readFileSync(path.join(__dirname, 'js/data/practical.js'), 'utf-8'), context);
vm.runInContext(fs.readFileSync(path.join(__dirname, 'js/app.js'), 'utf-8'), context);

console.log("=========================================================================");
console.log("PENGUJIAN VALIDASI INTEGRITAS BANK SOAL & KEUNIKAN SESI UJIAN");
console.log("=========================================================================");

const CBTApp = context.window.CBTApp;
const MASTER_QUESTIONS = context.window.MASTER_QUESTIONS;
const generateTubanExamSections = context.generateTubanExamSections;

// 1. Bank Soal Integrity: Zero duplicate questions in database
console.log("[1] Memeriksa Duplikasi di Bank Soal Master (1.000 Butir)...");
const allIds = MASTER_QUESTIONS.map(q => q.id);
const uniqueIds = new Set(allIds);
if (uniqueIds.size !== MASTER_QUESTIONS.length || MASTER_QUESTIONS.length !== 1000) {
  console.error(`FAIL: Ditemukan masalah kuota/duplikasi ID di bank soal! (${uniqueIds.size} unik vs ${MASTER_QUESTIONS.length} total, target 1000)`);
  process.exit(1);
}
console.log(`  -> LULUS: Seluruh ${MASTER_QUESTIONS.length} butir soal di Bank Soal memiliki ID unik tanpa duplikasi.`);

// 2. Session 1 Generation: 125 questions, strictly 1 question per exam session
console.log("\n[2] Memulai Sesi Ujian 1 (125 Soal)...");
const sections1 = generateTubanExamSections(MASTER_QUESTIONS, true);
const qIds1 = [];
sections1.forEach(s => s.questions.forEach(q => qIds1.push(q.id)));

if (qIds1.length !== 125) {
  console.error(`FAIL: Expected 125 questions, got ${qIds1.length}`);
  process.exit(1);
}
const uniqueQIds1 = new Set(qIds1);
if (uniqueQIds1.size !== 125) {
  console.error(`FAIL: Duplikasi intra-sesi ditemukan pada Sesi 1! ${uniqueQIds1.size} unik.`);
  process.exit(1);
}
console.log(`  -> Sesi 1 LULUS: Tepat 125 butir soal keluar dengan 100% keunikan (1 soal keluar di satu ujian).`);

// 3. Session 2 Generation: Independent generation, 125 questions, strictly unique per session
console.log("\n[3] Memulai Sesi Ujian 2 (125 Soal)...");
const sections2 = generateTubanExamSections(MASTER_QUESTIONS, true);
const qIds2 = [];
sections2.forEach(s => s.questions.forEach(q => qIds2.push(q.id)));

if (qIds2.length !== 125) {
  console.error(`FAIL: Expected 125 questions, got ${qIds2.length}`);
  process.exit(1);
}
const uniqueQIds2 = new Set(qIds2);
if (uniqueQIds2.size !== 125) {
  console.error(`FAIL: Duplikasi intra-sesi ditemukan pada Sesi 2! ${uniqueQIds2.size} unik.`);
  process.exit(1);
}
console.log(`  -> Sesi 2 LULUS: Tepat 125 butir soal keluar dengan 100% keunikan per sesi.`);

// 4. Distribution verification across 5 bidang
console.log("\n[4] Verifikasi Distribusi 5 Bidang Ujian:");
const expectedCounts = [25, 25, 25, 25, 25];
sections1.forEach((sec, idx) => {
  console.log(`  -> Bidang ${sec.bidangId} (${sec.shortName}): ${sec.questions.length} Soal [OK]`);
  if (sec.questions.length !== expectedCounts[idx]) {
    console.error(`FAIL: Kuota bidang ${sec.bidangId} tidak sesuai.`);
    process.exit(1);
  }
});

// 5. Verifikasi Isolasi Ketat Antarbidang (Zero Mixing):
console.log("\n[5] Verifikasi Isolasi Ketat Antarbidang (Zero Mixing):");
sections1.forEach(sec => {
  sec.questions.forEach(q => {
    if (q.bidangId !== sec.bidangId) {
      console.error(`FAIL: Terjadi pencampuran soal! Soal ID ${q.originalId} (Bidang ${q.bidangId}) masuk ke Sesi ${sec.bidangId}`);
      process.exit(1);
    }
  });
  console.log(`  -> Sesi Bidang ${sec.bidangId} (${sec.shortName}): 100% Terisolasi (Semua 25 soal murni milik Bidang ${sec.bidangId})`);
});

console.log("\n=========================================================================");
console.log("SELURUH PENGUJIAN KEUNIKAN BANK SOAL & ISOLASI BIDANG LULUS 100%!");
console.log("Format Sesuai Ketentuan: 1.000 Soal Seimbang, Terisolasi Antarbidang & Bebas Duplikasi!");
console.log("=========================================================================");

