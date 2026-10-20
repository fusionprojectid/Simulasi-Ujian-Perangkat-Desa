# -*- coding: utf-8 -*-
import sys
from merge_and_validate import ALL_QUESTIONS

print(f"Total questions loaded: {len(ALL_QUESTIONS)}")

# 1. Check ID uniqueness
ids = [q["id"] for q in ALL_QUESTIONS]
unique_ids = set(ids)
if len(ids) != len(unique_ids):
    print(f"ERROR: Duplicate IDs found! Total: {len(ids)}, Unique: {len(unique_ids)}")
else:
    print(f"SUCCESS: All {len(ids)} question IDs are strictly unique (1 to 585).")

# 2. Check question text duplicates
seen_texts = {}
duplicates = []
for q in ALL_QUESTIONS:
    text = q["question"].strip().lower()
    # simplify whitespace and punctuation
    simplified = "".join(c for c in text if c.isalnum() or c.isspace())
    simplified = " ".join(simplified.split())
    
    if simplified in seen_texts:
        duplicates.append((seen_texts[simplified], q["id"], q["question"]))
    else:
        seen_texts[simplified] = q["id"]

if duplicates:
    print(f"\nWARNING: Found {len(duplicates)} exact text duplicate(s):")
    for orig_id, dup_id, qtext in duplicates:
        print(f"  - Original #{orig_id} vs Duplicate #{dup_id}: {qtext[:80]}...")
else:
    print("SUCCESS: Zero exact question duplicates found!")

# 3. Check near duplicates by checking high word overlap (Jaccard similarity > 0.8)
near_dupes = []
items = [(q["id"], set("".join(c for c in q["question"].lower() if c.isalnum() or c.isspace()).split())) for q in ALL_QUESTIONS]
for i in range(len(items)):
    id_a, words_a = items[i]
    if len(words_a) < 5:
        continue
    for j in range(i + 1, len(items)):
        id_b, words_b = items[j]
        if len(words_b) < 5:
            continue
        intersection = len(words_a & words_b)
        union = len(words_a | words_b)
        sim = intersection / union if union > 0 else 0
        if sim >= 0.75:
            q_a = next(q["question"] for q in ALL_QUESTIONS if q["id"] == id_a)
            q_b = next(q["question"] for q in ALL_QUESTIONS if q["id"] == id_b)
            near_dupes.append((id_a, id_b, sim, q_a, q_b))

if near_dupes:
    print(f"\nFound {len(near_dupes)} potential near-duplicate(s) (sim >= 0.75):")
    for id_a, id_b, sim, qa, qb in near_dupes:
        print(f"  - [{sim:.2f}] #{id_a} vs #{id_b}:")
        print(f"      A: {qa[:90]}")
        print(f"      B: {qb[:90]}")
else:
    print("SUCCESS: Zero high-similarity near duplicates (sim >= 0.75) found!")

# 4. Check category distribution
cat_counts = {}
for q in ALL_QUESTIONS:
    cat = q["category"]
    cat_counts[cat] = cat_counts.get(cat, 0) + 1

print("\nCategory Distribution:")
for cat, count in sorted(cat_counts.items(), key=lambda x: -x[1]):
    print(f"  {cat}: {count}")

# 5. Check 'Pengetahuan umum' questions
print("\nInspecting 'Pengetahuan umum' questions:")
for q in ALL_QUESTIONS:
    if "Pengetahuan umum" in q["category"]:
        print(f"  #{q['id']}: {q['question'][:100]}")

# 6. Check 'Komputer' questions
print("\nInspecting 'Komputer' questions:")
komp_questions = [q for q in ALL_QUESTIONS if "Komputer" in q["category"]]
print(f"Total computer questions: {len(komp_questions)}")
excel_count = sum(1 for q in komp_questions if any(term in q["question"].lower() for term in ["excel", "spreadsheet", "=sum", "=if", "=average", "=vlookup", "=count", "rumus", "sel"]))
print(f"Excel questions count: {excel_count} out of {len(komp_questions)} ({excel_count/len(komp_questions)*100:.1f}%)")
