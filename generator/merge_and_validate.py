# -*- coding: utf-8 -*-
"""
Script Validasi dan Penggabungan Master Bank 1.000 Soal CBT Perangkat Desa Kabupaten Tuban
Menggabungkan 5 Bidang Ujian Terisolasi Masing-Masing 200 Soal:
- Bidang 1: Pendidikan Agama & Moderasi Beragama (200 Butir: ID 1 - 200)
- Bidang 2: Pengetahuan Pemerintahan Desa (200 Butir: ID 201 - 400)
- Bidang 3: Bahasa Indonesia (200 Butir: ID 401 - 600)
- Bidang 4: Pengetahuan Umum (200 Butir: ID 601 - 800)
- Bidang 5: Pengetahuan Komputer (200 Butir: ID 801 - 1000)
Total: Tepat 1.000 Butir Soal Seimbang, Terisolasi Bebas Campuran Antarbidang.
"""
from bank_bidang1_agama import QUESTIONS_BIDANG_1
from bank_bidang2_pemdes import QUESTIONS_BIDANG_2
from bank_bidang3_bahasa import QUESTIONS_BIDANG_3
from bank_bidang4_umum import QUESTIONS_BIDANG_4
from bank_bidang5_komputer import QUESTIONS_BIDANG_5

ALL_QUESTIONS = (
    QUESTIONS_BIDANG_1 +
    QUESTIONS_BIDANG_2 +
    QUESTIONS_BIDANG_3 +
    QUESTIONS_BIDANG_4 +
    QUESTIONS_BIDANG_5
)

print(f"Total pertanyaan terkumpul dalam master bank: {len(ALL_QUESTIONS)} butir soal.")

expected_bidang_counts = {
    1: 200,
    2: 200,
    3: 200,
    4: 200,
    5: 200
}

ids = set()
bidang_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

for idx, q in enumerate(ALL_QUESTIONS):
    expected_id = idx + 1
    assert q["id"] == expected_id, f"ID mismatch at {idx}: expected {expected_id}, got {q['id']}"
    assert q["id"] not in ids, f"Duplicate ID {q['id']}"
    ids.add(q["id"])
    
    bidang_id = q.get("bidangId")
    assert bidang_id in expected_bidang_counts, f"Invalid bidangId {bidang_id} at ID {q['id']}"
    bidang_counts[bidang_id] += 1
    
    # Strict range verification
    if expected_id <= 200:
        assert bidang_id == 1, f"Question ID {expected_id} should belong to Bidang 1, got {bidang_id}"
    elif expected_id <= 400:
        assert bidang_id == 2, f"Question ID {expected_id} should belong to Bidang 2, got {bidang_id}"
    elif expected_id <= 600:
        assert bidang_id == 3, f"Question ID {expected_id} should belong to Bidang 3, got {bidang_id}"
    elif expected_id <= 800:
        assert bidang_id == 4, f"Question ID {expected_id} should belong to Bidang 4, got {bidang_id}"
    else:
        assert bidang_id == 5, f"Question ID {expected_id} should belong to Bidang 5, got {bidang_id}"
    
    assert len(q["options"]) == 4, f"Options not 4 for ID {q['id']}"
    assert q["answer"] in [0, 1, 2, 3], f"Invalid answer for ID {q['id']}: {q['answer']}"
    
    assert q["question"].strip(), f"Empty question for ID {q['id']}"
    assert q["explanation"].strip(), f"Empty explanation for ID {q['id']}"
    assert q["source"].strip(), f"Empty source for ID {q['id']}"

print("\nVerifikasi Distribusi 1.000 Soal Master Bank (5 Bidang @ 200 Soal):")
for b_id, count in sorted(bidang_counts.items()):
    status = "OK" if count == 200 else "MISMATCH"
    print(f"  [{status}] Bidang {b_id}: {count}/200 butir")

assert len(ALL_QUESTIONS) == 1000, f"Expected 1000 questions, got {len(ALL_QUESTIONS)}"
print("\n[SUKSES] Seluruh 1.000 butir soal terverifikasi 100% valid, seimbang, terisolasi ketat, dan siap digunakan!")
