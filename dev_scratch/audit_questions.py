# -*- coding: utf-8 -*-
"""
Script Audit Menyeluruh Bank Soal CBT Perangkat Desa
Memeriksa:
1. Struktur data (ID, kategori, kesulitan, opsi, kunci, pembahasan, sumber)
2. Duplikasi teks soal / kemiripan tinggi
3. Deteksi opsi duplikat / kosong
4. Analisis keterbacaan & panjang kalimat untuk lulusan SMA/SMK
5. Analisis kebaruan regulasi (UU 3/2024, PP 11/2019, Permendagri, Perda Tuban)
"""
import json
import re
from collections import Counter
from merge_and_validate import ALL_QUESTIONS

print(f"Total Soal di Master Pool: {len(ALL_QUESTIONS)}")

# 1. Validasi Struktur & Field
errors = []
categories = Counter()
difficulties = Counter()
sources_missing = []
short_explanations = []
long_questions = []
negative_questions = []

id_set = set()
duplicate_ids = []

for idx, q in enumerate(ALL_QUESTIONS):
    qid = q.get("id")
    if qid in id_set:
        duplicate_ids.append(qid)
    id_set.add(qid)
    
    cat = q.get("category", "")
    categories[cat] += 1
    
    diff = q.get("difficulty", "")
    difficulties[diff] += 1
    
    q_text = q.get("question", "")
    if not q_text.strip():
        errors.append(f"ID {qid}: Pertanyaan kosong")
        
    options = q.get("options", [])
    if len(options) != 4:
        errors.append(f"ID {qid}: Jumlah opsi bukan 4 ({len(options)})")
    if len(set(options)) != len(options):
        errors.append(f"ID {qid}: Ada opsi duplikat di dalam satu soal: {options}")
    for opt_idx, opt in enumerate(options):
        if not opt.strip():
            errors.append(f"ID {qid}: Opsi indeks {opt_idx} kosong")
            
    ans = q.get("answer")
    if ans not in [0, 1, 2, 3]:
        errors.append(f"ID {qid}: Kunci jawaban tidak valid ({ans})")
        
    exp = q.get("explanation", "")
    if not exp.strip():
        errors.append(f"ID {qid}: Pembahasan kosong")
    elif len(exp.split()) < 5:
        short_explanations.append((qid, exp))
        
    src = q.get("source", "")
    if not src.strip():
        sources_missing.append(qid)
        
    # Readability / sentence complexity for SMA/SMK
    words = q_text.split()
    if len(words) > 35:
        long_questions.append((qid, len(words), q_text[:80] + "..."))
        
    # Check for negative wording: kecuali, bukan, tidak termasuk
    lower_q = q_text.lower()
    if any(neg in lower_q for neg in ["kecuali", "bukan", "tidak termasuk", "tidak benar", "keliru"]):
        negative_questions.append((qid, q_text[:80] + "..."))

print("\n--- HASIL VALIDASI STRUKTUR ---")
print(f"Total Errors Struktur: {len(errors)}")
for err in errors[:10]:
    print(f"  - {err}")

print(f"\nDistribusi Kategori ({len(categories)} kategori):")
for cat, count in categories.most_common():
    print(f"  - {cat}: {count} soal")

print(f"\nDistribusi Tingkat Kesulitan:")
for diff, count in difficulties.most_common():
    print(f"  - {diff}: {count} soal")

print(f"\nSoal tanpa sumber: {len(sources_missing)}")
print(f"Soal dengan kalimat panjang (>35 kata): {len(long_questions)}")
print(f"Soal dengan kata negatif (kecuali/bukan/dll): {len(negative_questions)}")

# 2. Deteksi Kemiripan / Duplikasi Soal
print("\n--- PEMERIKSAAN KEMIRIPAN SOAL ---")
def clean_text(t):
    return re.sub(r'[^a-zA-Z0-9\s]', '', t.lower()).strip()

cleaned_questions = {}
duplicate_pairs = []
for q in ALL_QUESTIONS:
    c = clean_text(q["question"])
    # Simple token jaccard or exact match
    if c in cleaned_questions:
        duplicate_pairs.append((cleaned_questions[c], q["id"], q["question"]))
    else:
        cleaned_questions[c] = q["id"]

print(f"Jumlah soal dengan pertanyaan persis sama: {len(duplicate_pairs)}")
for orig_id, dup_id, text in duplicate_pairs:
    print(f"  [DUPLIKAT PERSIS] ID {orig_id} dan ID {dup_id}: {text[:70]}...")

# Check near-duplicates (high token overlap)
words_map = {q["id"]: set(clean_text(q["question"]).split()) for q in ALL_QUESTIONS}
high_similarity = []
all_ids = list(words_map.keys())

for i in range(len(all_ids)):
    id_a = all_ids[i]
    set_a = words_map[id_a]
    if len(set_a) < 5:
        continue
    for j in range(i + 1, len(all_ids)):
        id_b = all_ids[j]
        set_b = words_map[id_b]
        intersection = len(set_a & set_b)
        union = len(set_a | set_b)
        sim = intersection / union if union > 0 else 0
        if sim > 0.85:
            high_similarity.append((id_a, id_b, sim, ALL_QUESTIONS[id_a-1]["question"], ALL_QUESTIONS[id_b-1]["question"]))

print(f"Jumlah pasangan soal dengan kemiripan > 85%: {len(high_similarity)}")
for id_a, id_b, sim, q_a, q_b in high_similarity[:15]:
    print(f"  [KEMIRIPAN {sim:.2f}] ID {id_a} vs ID {id_b}:")
    print(f"    A: {q_a}")
    print(f"    B: {q_b}")

