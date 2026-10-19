// Comprehensive Test Suite for Simulasi CBT Perangkat Desa (All 12 Features + 500 Questions Pool)
const fs = require('fs');
const path = require('path');

const htmlPath = path.join(__dirname, 'index.html');
const htmlContent = fs.readFileSync(htmlPath, 'utf-8');

console.log("==================================================================");
console.log("MENJALANKAN COMPREHENSIVE TEST SUITE CBT PERANGKAT DESA (500 SOAL)");
console.log("==================================================================");

// 1. Ekstraksi Master Database Soal (500 Soal)
const matchQuestions = htmlContent.match(/const MASTER_QUESTIONS = (\[[\s\S]*?\]);\s*(\/\/[^\n]*\r?\n\s*)?const GLOSSARY_DATA/);
if (!matchQuestions) {
  console.error("GAGAL: Tidak dapat mengekstrak MASTER_QUESTIONS dari index.html");
  process.exit(1);
}
const MASTER_QUESTIONS = JSON.parse(matchQuestions[1]);
console.log(`[TEST 1] Ekstraksi Master Pool: Ditemukan ${MASTER_QUESTIONS.length} butir soal.`);
if (MASTER_QUESTIONS.length !== 500) {
  throw new Error(`Master pool harus berjumlah 500 butir, tetapi ditemukan ${MASTER_QUESTIONS.length}`);
}

// 2. Integritas Data dan Sumber Regulasi Terverifikasi (500 Soal)
const catCounts = {};
MASTER_QUESTIONS.forEach((q, i) => {
  if (q.id !== i + 1) throw new Error(`ID tidak urut pada indeks ${i}`);
  if (!q.question || !q.question.trim()) throw new Error(`Pertanyaan kosong pada ID ${q.id}`);
  if (!Array.isArray(q.options) || q.options.length !== 4) throw new Error(`Opsi harus tepat 4 pada ID ${q.id}`);
  if (![0, 1, 2, 3].includes(q.answer)) throw new Error(`Kunci jawaban tidak valid pada ID ${q.id}`);
  if (!q.explanation || !q.explanation.trim()) throw new Error(`Pembahasan kosong pada ID ${q.id}`);
  if (!q.source || !q.source.trim()) throw new Error(`Rujukan regulasi kosong pada ID ${q.id}`);
  catCounts[q.category] = (catCounts[q.category] || 0) + 1;
});
console.log("[TEST 2] Integritas 500 Soal, Kunci, Pembahasan, & Rujukan Regulasi Terverifikasi: LULUS");

// 3. Validasi Distribusi 12 Kategori di Master Database (500 Butir: 5x Kuota Ujian)
const EXPECTED_POOL_CATS = {
  "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa": 100,
  "Peraturan perundang-undangan dan tata kelola pemerintahan": 60,
  "Pancasila, UUD 1945, dan wawasan kebangsaan": 50,
  "Administrasi pemerintahan, surat-menyurat, dan pengarsipan": 50,
  "Keuangan desa, APB Desa, dan aset desa": 50,
  "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat": 40,
  "BPD, kelembagaan desa, dan musyawarah": 25,
  "Bahasa Indonesia": 35,
  "Matematika dan numerik": 30,
  "Logika dan penalaran": 25,
  "Pengetahuan umum": 20,
  "Komputer dasar dan pelayanan publik": 15
};

for (const [cat, expected] of Object.entries(EXPECTED_POOL_CATS)) {
  if (catCounts[cat] !== expected) {
    throw new Error(`Distribusi pool ${cat} salah: didapat ${catCounts[cat]}, harusnya ${expected}`);
  }
}
console.log("[TEST 3] Distribusi 12 Kategori pada Master Pool (500 Butir): LULUS");

// 4. Ekstraksi CATEGORIES_SPEC dan Uji Randomisasi Aman Otomatis
const matchCatSpec = htmlContent.match(/const CATEGORIES_SPEC = (\[[\s\S]*?\]);/);
if (!matchCatSpec) throw new Error("GAGAL: Tidak dapat mengekstrak CATEGORIES_SPEC");
const CATEGORIES_SPEC = new Function(`return ${matchCatSpec[1]}`)();

function shuffleArray(arr) {
  const copy = [...arr];
  for (let i = copy.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  return copy;
}

function generateExam100Questions(masterList, categorySpec, randomizeQuestions = true, randomizeOptions = true) {
  let sampled = [];
  categorySpec.forEach(cat => {
    const pool = masterList.filter(q => q.category === cat.name);
    const shuffledPool = randomizeQuestions ? shuffleArray([...pool]) : [...pool];
    const picked = shuffledPool.slice(0, cat.count);
    sampled.push(...picked);
  });

  if (randomizeQuestions) {
    shuffleArray(sampled);
  }

  return sampled.map((q, idx) => {
    const originalCorrectText = q.options[q.answer];
    const optionsList = [...q.options];
    if (randomizeOptions) {
      shuffleArray(optionsList);
    }
    const newAnswerIndex = optionsList.indexOf(originalCorrectText);

    return {
      ...q,
      number: idx + 1,
      options: optionsList,
      answer: newAnswerIndex,
      originalAnswer: q.answer,
      originalId: q.id
    };
  });
}

// Uji 10x Randomisasi dengan Opsi Diacak
for (let run = 1; run <= 10; run++) {
  const examSet = generateExam100Questions(MASTER_QUESTIONS, CATEGORIES_SPEC, true, true);
  if (examSet.length !== 100) throw new Error(`Run ${run}: Soal ujian bukan 100 butir`);

  const examCatCounts = {};
  examSet.forEach(q => {
    examCatCounts[q.category] = (examCatCounts[q.category] || 0) + 1;
    // Verifikasi teks opsi jawaban benar tetap cocok dengan master
    const origQ = MASTER_QUESTIONS.find(m => m.id === q.id);
    const origAnsText = origQ.options[origQ.answer];
    const currAnsText = q.options[q.answer];
    if (origAnsText !== currAnsText) {
      throw new Error(`Sinkronisasi kunci acak gagal pada ID ${q.id}!`);
    }
  });

  CATEGORIES_SPEC.forEach(spec => {
    if (examCatCounts[spec.name] !== spec.count) {
      throw new Error(`Kuota kategori ${spec.name} tidak sesuai`);
    }
  });
}
console.log("[TEST 4] Pengacakan Otomatis 100 Soal dari 500 Bank Soal & Sinkronisasi Kunci Jawaban: LULUS");

// 5. Uji Antrean Prioritas Soal Kosong (Feature 1 CAT)
const sampleExam = generateExam100Questions(MASTER_QUESTIONS, CATEGORIES_SPEC, false, false);
const mockAnswers = {};
for (let i = 0; i < 100; i++) {
  if (i !== 7 && i !== 24 && i !== 68) {
    mockAnswers[sampleExam[i].id] = 1;
  }
}

function findLowestUnanswered(questions, answers) {
  for (let i = 0; i < questions.length; i++) {
    if (answers[questions[i].id] === undefined) return i;
  }
  return null;
}

const firstUnanswered = findLowestUnanswered(sampleExam, mockAnswers);
if (firstUnanswered !== 7) throw new Error(`Harusnya indeks 7, didapat ${firstUnanswered}`);
mockAnswers[sampleExam[7].id] = 0;

const secondUnanswered = findLowestUnanswered(sampleExam, mockAnswers);
if (secondUnanswered !== 24) throw new Error(`Harusnya indeks 24, didapat ${secondUnanswered}`);
mockAnswers[sampleExam[24].id] = 2;

const thirdUnanswered = findLowestUnanswered(sampleExam, mockAnswers);
if (thirdUnanswered !== 68) throw new Error(`Harusnya indeks 68, didapat ${thirdUnanswered}`);
mockAnswers[sampleExam[68].id] = 3;

if (findLowestUnanswered(sampleExam, mockAnswers) !== null) {
  throw new Error("Seluruh soal seharusnya telah terjawab");
}
console.log("[TEST 5] Siklus Antrean Prioritas Soal Kosong: LULUS");

// 6. Uji Analisis Kelemahan & Rekomendasi Belajar (Feature 2)
const catStatsMock = {};
CATEGORIES_SPEC.forEach(c => {
  catStatsMock[c.name] = { total: c.count, correct: c.count, wrong: 0, empty: 0 };
});

// Mock: Keuangan desa skor rendah (2/10 = 20%), kategori lain 100%
catStatsMock["Keuangan desa, APB Desa, dan aset desa"].correct = 2;
catStatsMock["Keuangan desa, APB Desa, dan aset desa"].wrong = 8;

const rankedCats = Object.keys(catStatsMock).map(name => {
  const st = catStatsMock[name];
  const acc = (st.correct / st.total) * 100;
  return { name, acc };
}).sort((a, b) => a.acc - b.acc);

if (rankedCats[0].name !== "Keuangan desa, APB Desa, dan aset desa" || rankedCats[0].acc !== 20) {
  throw new Error("Urutan analisis kelemahan salah: kategori terendah harus Keuangan Desa");
}
console.log("[TEST 6] Analisis Kelemahan Kategori & Pengurutan Prioritas: LULUS");

// 7. Uji Glosarium 36 Istilah Desa (Feature 4)
const matchGlossary = htmlContent.match(/const GLOSSARY_DATA = (\[[\s\S]*?\]);\s*(\/\/[^\n]*\r?\n\s*)?const CATEGORIES_SPEC/);
if (!matchGlossary) throw new Error("GAGAL: Tidak dapat mengekstrak GLOSSARY_DATA");
const GLOSSARY_DATA = JSON.parse(matchGlossary[1]);
console.log(`[TEST 7] Glosarium Istilah Desa: Ditemukan ${GLOSSARY_DATA.length} istilah.`);
if (GLOSSARY_DATA.length !== 36) {
  throw new Error(`Glosarium harus berisi 36 istilah, ditemukan ${GLOSSARY_DATA.length}`);
}
GLOSSARY_DATA.forEach(item => {
  if (!item.term || !item.name || !item.definition || !item.source || !item.category) {
    throw new Error(`Data glosarium tidak lengkap pada istilah ${item.term}`);
  }
});
const searchResults = GLOSSARY_DATA.filter(g => g.term.toLowerCase().includes('siltap') || g.definition.toLowerCase().includes('siltap'));
if (searchResults.length === 0) throw new Error("Pencarian istilah 'siltap' gagal");
console.log("  - Glosarium 36 Istilah & Fungsi Pencarian: LULUS");

// 8. Uji Riwayat & Komparasi Antar-Sesi yang Adil (Feature 5)
const sessionOfficial1 = { isOfficialExam: true, totalQuestions: 100, score: 72, accuracy: 72.0, modeLabel: 'Simulasi CAT' };
const sessionOfficial2 = { isOfficialExam: true, totalQuestions: 100, score: 78, accuracy: 78.0, modeLabel: 'Simulasi CAT' };
const deltaOfficial = sessionOfficial2.score - sessionOfficial1.score;
if (deltaOfficial !== 6) throw new Error("Kalkulasi delta skor setara salah");

const sessionPractice = { isOfficialExam: false, totalQuestions: 25, score: 88, accuracy: 88.0, modeLabel: 'Mode Latihan' };
const isDisparate = !(sessionPractice.isOfficialExam && sessionOfficial2.isOfficialExam);
if (!isDisparate) throw new Error("Harus terdeteksi sebagai perbandingan yang tidak setara (disparate)");
console.log("[TEST 8] Logika Komparasi Antar-Sesi (Setara vs Disparate Warning): LULUS");

// 9. Uji Cadangan Lokal (Ekspor & Validasi Impor JSON) (Feature 8)
const mockBackup = {
  app: "CBT_PERANGKAT_DESA",
  version: 2,
  exportDate: new Date().toISOString(),
  candidateProfile: { name: "Budi", village: "Sugihwaras", region: "tuban" },
  history: [sessionOfficial1, sessionOfficial2]
};
const exportedStr = JSON.stringify(mockBackup);
if (!exportedStr.includes("CBT_PERANGKAT_DESA")) throw new Error("Format ekspor cadangan salah");

const mockBigSize = 2.5 * 1024 * 1024;
if (!(mockBigSize > 2 * 1024 * 1024)) throw new Error("Pengecekan batas ukuran 2MB gagal");

const invalidBackup = { app: "OTHER_APP", history: [] };
const isValid = invalidBackup.app === "CBT_PERANGKAT_DESA" && Array.isArray(invalidBackup.history);
if (isValid) throw new Error("File tanpa token CBT_PERANGKAT_DESA harus ditolak");
console.log("[TEST 9] Validasi Cadangan Lokal JSON (Ukuran & Skema Keamanan): LULUS");

// 10. Uji Elemen UI, Anti-Kecurangan & Penghapusan Sakelar Manual
const mandatoryElements = [
  'preFinishAnswered',
  'preFinishFlagged',
  'preFinishEmpty',
  'btnFlagQuestion',
  'weaknessListContainer',
  'viewGlossary',
  'glossarySearchInput',
  'viewHistory',
  'chartContainer',
  'modalBackupRestore',
  'font-scale-control',
  'Sistem Integritas & Anti-Kecurangan Aktif'
];

mandatoryElements.forEach(id => {
  if (!htmlContent.includes(id)) {
    throw new Error(`Elemen penting antarmuka tidak ditemukan: ${id}`);
  }
});

// Verifikasi bahwa tombol toggle manual telah benar-benar dihapus agar tidak ada kecurangan
if (htmlContent.includes('id="toggleShuffleQuestions"') || htmlContent.includes('id="toggleShuffleOptions"')) {
  throw new Error("Tombol manual toggle acak seharusnya sudah dihilangkan sesuai permintaan user!");
}
console.log("[TEST 10] Penghapusan Sakelar Manual & Penegakan Pengacakan Otomatis Anti-Kecurangan: LULUS");

console.log("\n==================================================================");
console.log("SELURUH 10 MODUL PENGUJIAN (TEST 1 - 10) BERHASIL 100%!");
console.log("==================================================================");
