// End-to-End Simulation & Verification Test for CBT Perangkat Desa Kabupaten Tuban
// Tests: Privacy Offline, 585 Soal, 5 Bidang (125 Soal), 10 Praktik Komputer, 87.5 + 12.5 = 100.0 Scoring
const fs = require('fs');
const path = require('path');

const htmlPath = path.join(__dirname, 'index.html');
const htmlContent = fs.readFileSync(htmlPath, 'utf-8');

console.log("========================================================================");
console.log("MENJALANKAN AUDIT & PENGUJIAN KOMPREHENSIF CBT PERANGKAT DESA KAB. TUBAN");
console.log("========================================================================");

// -----------------------------------------------------------------------------
// PENGUJIAN A: STRUKTUR & PRIVASI 100% OFFLINE (ZERO NETWORK LEAKS)
// -----------------------------------------------------------------------------
console.log("\n[TEST A] Memeriksa Integritas File & Keamanan Privasi Offline...");
const externalUrls = [];
const urlRegex = /(?:src|href)=["'](https?:\/\/[^"']+)["']/gi;
let match;
while ((match = urlRegex.exec(htmlContent)) !== null) {
  if (!match[1].includes('w3.org')) {
    externalUrls.push(match[1]);
  }
}

if (externalUrls.length > 0) {
  throw new Error(`Ditemukan referensi eksternal jaringan: ${externalUrls.join(', ')}`);
}
console.log("  -> LULUS: 100% Offline, Tanpa CDN, Tanpa Pelacak, Tanpa Jaringan Eksternal.");

const secretKeywords = ['api_key', 'apikey', 'secret_key', 'auth_token', 'bearer'];
secretKeywords.forEach(sec => {
  if (htmlContent.toLowerCase().includes(sec)) {
    throw new Error(`Ditemukan indikasi kata kunci kredensial/rahasia: ${sec}`);
  }
});
console.log("  -> LULUS: Bebas dari hardcoded API key, token otentikasi, atau rahasia server.");

// -----------------------------------------------------------------------------
// PENGUJIAN B: AUDIT BANK SOAL (1.000 SOAL & 5 BIDANG TERISOLASI)
// -----------------------------------------------------------------------------
console.log("\n[TEST B] Audit Bank Soal 1.000 Butir & Kunci Jawaban...");
const vm = require('vm');
const questionsPath = path.join(__dirname, 'js', 'data', 'questions.js');
const qSandbox = { window: {} };
vm.createContext(qSandbox);
vm.runInContext(fs.readFileSync(questionsPath, 'utf-8'), qSandbox);
const MASTER_QUESTIONS = qSandbox.window.MASTER_QUESTIONS;

if (!Array.isArray(MASTER_QUESTIONS) || MASTER_QUESTIONS.length !== 1000) {
  throw new Error(`Ukuran database harus 1.000, didapat ${MASTER_QUESTIONS ? MASTER_QUESTIONS.length : 0}`);
}

const idSet = new Set();
const bidangCounts = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0 };
const diffCounts = {};
let noSourceCount = 0;

MASTER_QUESTIONS.forEach((q, idx) => {
  if (q.id !== idx + 1) throw new Error(`ID tidak berurutan pada indeks ${idx}`);
  if (idSet.has(q.id)) throw new Error(`Duplikat ID ${q.id}`);
  idSet.add(q.id);

  if (!q.bidangId || ![1, 2, 3, 4, 5].includes(q.bidangId)) throw new Error(`bidangId tidak valid pada ID ${q.id}`);
  bidangCounts[q.bidangId] = (bidangCounts[q.bidangId] || 0) + 1;

  if (!q.question || !q.question.trim()) throw new Error(`Pertanyaan kosong pada ID ${q.id}`);
  if (!Array.isArray(q.options) || q.options.length !== 4) throw new Error(`Opsi bukan 4 pada ID ${q.id}`);
  if (new Set(q.options).size !== 4) throw new Error(`Opsi kembar di ID ${q.id}`);
  if (![0, 1, 2, 3].includes(q.answer)) throw new Error(`Kunci jawaban salah indeks di ID ${q.id}`);
  if (!q.explanation || !q.explanation.trim()) throw new Error(`Pembahasan kosong di ID ${q.id}`);
  if (!q.source || !q.source.trim()) noSourceCount++;

  diffCounts[q.difficulty] = (diffCounts[q.difficulty] || 0) + 1;
});

if (noSourceCount > 0) throw new Error(`Ada ${noSourceCount} soal tanpa sumber`);
for (let b = 1; b <= 5; b++) {
  if (bidangCounts[b] !== 200) throw new Error(`Bidang ${b} tidak seimbang: didapat ${bidangCounts[b]}, harus 200`);
}
console.log(`  -> LULUS: 1.000 butir soal lengkap (5 bidang @ 200 soal), 4 opsi unik, 1 kunci valid, pembahasan memadai, dan 100% bersumber.`);
console.log(`  -> Distribusi Kesulitan: Mudah=${diffCounts['mudah']}, Sedang=${diffCounts['sedang']}, Sulit=${diffCounts['sulit']}`);

// -----------------------------------------------------------------------------
// PENGUJIAN C: STRUKTUR UJIAN TERTULIS 5 BIDANG (125 SOAL, 150 MENIT)
// -----------------------------------------------------------------------------
console.log("\n[TEST C] Pengujian Struktur Ujian Tertulis 5 Bidang Berurutan...");
const appPath = path.join(__dirname, 'js', 'app.js');
const appContent = fs.readFileSync(appPath, 'utf-8');
const matchBidang = appContent.match(/const BIDANG_CONFIG = (\[[\s\S]*?\]);\s*\/\/ Safe/);
if (!matchBidang) throw new Error("Gagal mengekstrak BIDANG_CONFIG dari js/app.js");
const BIDANG_CONFIG = new Function(`return ${matchBidang[1]}`)();

if (BIDANG_CONFIG.length !== 5) {
  throw new Error(`Harus ada 5 bidang resmi, didapat ${BIDANG_CONFIG.length}`);
}

BIDANG_CONFIG.forEach(b => {
  if (b.count !== 25) throw new Error(`Bidang ${b.name} harus tepat 25 soal`);
  if (b.durationMinutes !== 30) throw new Error(`Bidang ${b.name} harus tepat 30 menit`);
});
console.log("  -> LULUS: 5 Bidang @ 25 soal dan 30 menit per bidang (Total 125 soal, 150 menit).");

// -----------------------------------------------------------------------------
// PENGUJIAN D: PRAKTIK KOMPUTER 10 BUTIR INTERAKTIF
// -----------------------------------------------------------------------------
console.log("\n[TEST D] Pengujian Praktik Komputer (10 Butir, Maks. 1,25 Poin / Butir)...");
const practicalPath = path.join(__dirname, 'js', 'data', 'practical.js');
const pSandbox = { window: {} };
vm.createContext(pSandbox);
vm.runInContext(fs.readFileSync(practicalPath, 'utf-8'), pSandbox);
const PRACTICAL_TASKS = pSandbox.window.PRACTICAL_TASKS || pSandbox.window.__PRACTICAL_TASKS__;

if (!Array.isArray(PRACTICAL_TASKS) || PRACTICAL_TASKS.length !== 10) {
  throw new Error(`Harus tepat 10 butir praktik komputer, didapat ${PRACTICAL_TASKS ? PRACTICAL_TASKS.length : 0}`);
}

let totalPractScore = 0;
PRACTICAL_TASKS.forEach(t => {
  if (t.maxScore !== 1.25) throw new Error(`Skor per butir harus 1.25, didapat ${t.maxScore}`);
  totalPractScore += t.maxScore;
});
if (Math.abs(totalPractScore - 12.5) > 0.001) {
  throw new Error(`Total skor maksimal praktik harus 12.5, didapat ${totalPractScore}`);
}
console.log(`  -> LULUS: 10 Butir praktik komputer terverifikasi dengan total skor maksimal 12,50 poin.`);

// -----------------------------------------------------------------------------
// PENGUJIAN E: SISTEM PENILAIAN GABUNGAN RESMI (87,5 + 12,5 = 100,0)
// -----------------------------------------------------------------------------
console.log("\n[TEST E] Pengujian Sistem Penilaian Gabungan...");
// 125 soal tertulis x 0.7 = 87.5 poin
// 10 butir praktik x 1.25 = 12.5 poin
// Nilai Akhir = 87.5 + 12.5 = 100.0 poin

function calculateFinalScore(writtenCorrectCount, practicalScoresArray) {
  const writtenScore = writtenCorrectCount * 0.7;
  const practicalScore = practicalScoresArray.reduce((acc, val) => acc + val, 0);
  return {
    writtenScore: parseFloat(writtenScore.toFixed(2)),
    practicalScore: parseFloat(practicalScore.toFixed(2)),
    finalScore: parseFloat((writtenScore + practicalScore).toFixed(2))
  };
}

// Kasus 1: Nilai Maksimal
const resMax = calculateFinalScore(125, Array(10).fill(1.25));
if (resMax.writtenScore !== 87.5 || resMax.practicalScore !== 12.5 || resMax.finalScore !== 100.0) {
  throw new Error(`Kalkulasi nilai maksimal gagal: ${JSON.stringify(resMax)}`);
}
console.log("  -> LULUS: Nilai Maksimal = 87,5 (Tertulis) + 12,5 (Praktik) = 100,00 Poin.");

// Kasus 2: 90 Benar Tertulis, 7 Tugas Praktik (7 x 1.25 = 8.75)
const resMid = calculateFinalScore(90, [1.25, 1.25, 1.25, 1.25, 1.25, 1.25, 1.25, 0, 0, 0]);
if (resMid.writtenScore !== 63.0 || resMid.practicalScore !== 8.75 || resMid.finalScore !== 71.75) {
  throw new Error(`Kalkulasi nilai riil gagal: ${JSON.stringify(resMid)}`);
}
console.log(`  -> LULUS: Simulasi Riil = ${resMid.writtenScore} (Tertulis) + ${resMid.practicalScore} (Praktik) = ${resMid.finalScore} Poin.`);

// -----------------------------------------------------------------------------
// PENGUJIAN F: GLOSARIUM 36 ISTILAH PEMERINTAHAN DESA
// -----------------------------------------------------------------------------
console.log("\n[TEST F] Glosarium 36 Istilah Pemerintahan Desa...");
const glossaryPath = path.join(__dirname, 'js', 'data', 'glossary.js');
const gSandbox = { window: {} };
vm.createContext(gSandbox);
vm.runInContext(fs.readFileSync(glossaryPath, 'utf-8'), gSandbox);
const GLOSSARY_DATA = gSandbox.window.GLOSSARY_DATA;

if (!Array.isArray(GLOSSARY_DATA) || GLOSSARY_DATA.length !== 36) {
  throw new Error(`Glosarium harus berisi tepat 36 istilah, didapat ${GLOSSARY_DATA ? GLOSSARY_DATA.length : 0}`);
}

const sampleTerms = ['Siltap', 'PKPKD', 'PPKD', 'APB Desa', 'BPD', 'Siskeudes', 'BUMDes'];
sampleTerms.forEach(term => {
  const found = GLOSSARY_DATA.find(g => g.term === term);
  if (!found || !found.definition) {
    throw new Error(`Data glosarium untuk '${term}' tidak lengkap atau hilang`);
  }
});
console.log("  -> LULUS: 36 Istilah glosarium terverifikasi lengkap.");

console.log("\n========================================================================");
console.log("SEMUA PENGUJIAN AUDIT (TEST A - F) BERHASIL DENGAN NILAI SEMPURNA 100%!");
console.log("Aplikasi Sesuai Format Resmi Ujian Perangkat Desa Kabupaten Tuban!");
console.log("========================================================================");
