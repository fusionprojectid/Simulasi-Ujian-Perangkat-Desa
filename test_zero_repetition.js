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
console.log("PENGUJIAN SIKLUS TANPA PENGULANGAN (ZERO REPETITION ENGINE)");
console.log("=========================================================================");

const CBTApp = context.window.CBTApp;
const generateTubanExamSections = context.generateTubanExamSections;

// 1. Session 1 Generation
console.log("[1] Memulai Sesi Ujian 1 (125 Soal)...");
const sections1 = generateTubanExamSections(context.window.MASTER_QUESTIONS, true);
const qIds1 = [];
sections1.forEach(s => s.questions.forEach(q => qIds1.push(q.id)));

if (qIds1.length !== 125) {
  console.error(`FAIL: Expected 125 questions, got ${qIds1.length}`);
  process.exit(1);
}
const uniqueQIds1 = new Set(qIds1);
if (uniqueQIds1.size !== 125) {
  console.error(`FAIL: Intra-exam duplicates found in Session 1! ${uniqueQIds1.size} unique.`);
  process.exit(1);
}
console.log(`  -> Sesi 1 LULUS: 125 soal unik tanpa duplikasi intra-sesi.`);

// Check seen storage
const seenAfter1 = JSON.parse(mockLocalStorage['cbt_seen_question_ids_tuban_v2'] || '[]');
console.log(`  -> Jumlah soal tercatat di localStorage: ${seenAfter1.length} / 585.`);

// 2. Session 2 Generation
console.log("\n[2] Memulai Sesi Ujian 2 (125 Soal)...");
const sections2 = generateTubanExamSections(context.window.MASTER_QUESTIONS, true);
const qIds2 = [];
sections2.forEach(s => s.questions.forEach(q => qIds2.push(q.id)));

if (qIds2.length !== 125) {
  console.error(`FAIL: Expected 125 questions, got ${qIds2.length}`);
  process.exit(1);
}
const uniqueQIds2 = new Set(qIds2);
if (uniqueQIds2.size !== 125) {
  console.error(`FAIL: Intra-exam duplicates found in Session 2! ${uniqueQIds2.size} unique.`);
  process.exit(1);
}
console.log(`  -> Sesi 2 LULUS: 125 soal unik tanpa duplikasi intra-sesi.`);

// Verify zero-overlap in categories with >= 50 questions (Agama, Komputer)
const agama1 = sections1[0].questions.map(q => q.id);
const agama2 = sections2[0].questions.map(q => q.id);
const overlapAgama = agama1.filter(id => agama2.includes(id));
console.log(`  -> Overlap Soal Agama (Pool 50, Kuota 25): ${overlapAgama.length} soal mengulang`);
if (overlapAgama.length !== 0) {
  console.error(`FAIL: Agama questions repeated across Session 1 and 2! Overlap: ${overlapAgama}`);
  process.exit(1);
}

const komp1 = sections1[4].questions.map(q => q.id);
const komp2 = sections2[4].questions.map(q => q.id);
const overlapKomp = komp1.filter(id => komp2.includes(id));
console.log(`  -> Overlap Soal Komputer (Pool 50, Kuota 25): ${overlapKomp.length} soal mengulang`);
if (overlapKomp.length !== 0) {
  console.error(`FAIL: Komputer questions repeated across Session 1 and 2! Overlap: ${overlapKomp}`);
  process.exit(1);
}

const seenAfter2 = JSON.parse(mockLocalStorage['cbt_seen_question_ids_tuban_v2'] || '[]');
console.log(`  -> Jumlah total soal terpakai setelah 2 sesi: ${seenAfter2.length} / 585 (${(seenAfter2.length/585*100).toFixed(1)}%).`);

// 3. Test Reset
console.log("\n[3] Menguji Reset Riwayat Soal...");
CBTApp.resetQuestionHistory();
const seenAfterReset = JSON.parse(mockLocalStorage['cbt_seen_question_ids_tuban_v2'] || '[]');
if (seenAfterReset.length !== 0) {
  console.error(`FAIL: Reset failed, seen length is ${seenAfterReset.length}`);
  process.exit(1);
}
console.log("  -> LULUS: Riwayat bank soal berhasil di-reset menjadi 0.");

console.log("\n=========================================================================");
console.log("SEMUA PENGUJIAN SIKLUS TANPA PENGULANGAN LULUS 100%!");
console.log("=========================================================================");
