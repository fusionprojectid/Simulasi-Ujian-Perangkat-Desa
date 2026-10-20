# -*- coding: utf-8 -*-
import json
import re
from collections import Counter
from merge_and_validate import ALL_QUESTIONS

print(f"Total questions: {len(ALL_QUESTIONS)}")

# 1. Analyze "Komputer dasar dan pelayanan publik"
komp = [q for q in ALL_QUESTIONS if q['category'] == 'Komputer dasar dan pelayanan publik']
print(f"\n--- KOMPUTER ({len(komp)} soal) ---")
excel_count = 0
word_count = 0
general_count = 0
for q in komp:
    text = q['question'] + " " + " ".join(q['options']) + " " + q['explanation']
    t_lower = text.lower()
    is_excel = any(k in t_lower for k in ['excel', 'spreadsheet', 'vlookup', 'hlookup', 'rumus =', 'formula =', 'sum(', 'average(', 'if(', 'countif', 'cell', 'kolom dan baris', 'worksheet'])
    is_word = any(k in t_lower for k in ['word', 'mail merge', 'surat massal', 'margin', 'font', 'spacing', 'paragraph'])
    tag = "EXCEL" if is_excel else ("WORD" if is_word else "LAINNYA/DASAR")
    if is_excel:
        excel_count += 1
    elif is_word:
        word_count += 1
    else:
        general_count += 1
    print(f"[{tag}] ID {q['id']}: {q['question']}")

print(f"\nKomputer summary: Excel={excel_count}, Word={word_count}, Lainnya/Dasar={general_count}")

# 2. Analyze "Pengetahuan umum"
print(f"\n--- PENGETAHUAN UMUM ---")
pu = [q for q in ALL_QUESTIONS if q['category'] == 'Pengetahuan umum']
print(f"Total Pengetahuan Umum: {len(pu)}")
for q in pu:
    print(f"ID {q['id']}: {q['question']}")

# 3. Check for duplicates across ALL questions (by question text, options, answer similarity)
print(f"\n--- DUPLIKAT CEK ---")
questions_by_text = {}
for q in ALL_QUESTIONS:
    clean = re.sub(r'[^a-zA-Z0-9]', '', q['question'].lower())
    if clean in questions_by_text:
        orig = questions_by_text[clean]
        print(f"[DUPLIKAT TEKS] ID {orig['id']} ({orig['category']}) vs ID {q['id']} ({q['category']}): {q['question']}")
    else:
        questions_by_text[clean] = q

# Check overlap / similarity
from difflib import SequenceMatcher
sim_pairs = []
for i in range(len(ALL_QUESTIONS)):
    for j in range(i + 1, len(ALL_QUESTIONS)):
        q1 = ALL_QUESTIONS[i]
        q2 = ALL_QUESTIONS[j]
        # Quick filter: word set overlap
        w1 = set(re.findall(r'\w+', q1['question'].lower()))
        w2 = set(re.findall(r'\w+', q2['question'].lower()))
        if len(w1 & w2) / max(len(w1 | w2), 1) > 0.65:
            ratio = SequenceMatcher(None, q1['question'].lower(), q2['question'].lower()).ratio()
            if ratio > 0.70:
                sim_pairs.append((ratio, q1, q2))

print(f"\nPasangan dengan kemiripan > 70%: {len(sim_pairs)}")
for r, q1, q2 in sorted(sim_pairs, key=lambda x: x[0], reverse=True)[:30]:
    print(f"[{r:.2f}] ID {q1['id']} ({q1['category']}) vs ID {q2['id']} ({q2['category']})")
    print(f"   Q1: {q1['question']}")
    print(f"   Q2: {q2['question']}")
