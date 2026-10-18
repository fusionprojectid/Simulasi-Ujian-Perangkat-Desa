# -*- coding: utf-8 -*-
"""
Script Validasi dan Penggabungan Master Pool 300 Soal CBT Perangkat Desa
Menggabungkan:
- Q1_100: Soal 1 s.d. 100 dari validate_data.py
- Q101_200: Soal 101 s.d. 200 dari expand_bank.py
- Q201_300: Soal 201 s.d. 300 dari expand_bank_300.py
Total: 300 Butir Soal.
"""
from validate_data import QUESTIONS as Q1_100
from expand_bank import NEW_QUESTIONS as Q101_200
from expand_bank_300 import QUESTIONS_201_300 as Q201_300

ALL_QUESTIONS = Q1_100 + Q101_200 + Q201_300

print(f"Total pertanyaan terkumpul dalam master pool: {len(ALL_QUESTIONS)} butir soal.")

expected_distribution = {
    "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa": 60,
    "Peraturan perundang-undangan dan tata kelola pemerintahan": 36,
    "Pancasila, UUD 1945, dan wawasan kebangsaan": 30,
    "Administrasi pemerintahan, surat-menyurat, dan pengarsipan": 30,
    "Keuangan desa, APB Desa, dan aset desa": 30,
    "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat": 24,
    "BPD, kelembagaan desa, dan musyawarah": 15,
    "Bahasa Indonesia": 21,
    "Matematika dan numerik": 18,
    "Logika dan penalaran": 15,
    "Pengetahuan umum": 12,
    "Komputer dasar dan pelayanan publik": 9
}

ids = set()
cat_counts = {}

for idx, q in enumerate(ALL_QUESTIONS):
    expected_id = idx + 1
    assert q["id"] == expected_id, f"ID mismatch at {idx}: expected {expected_id}, got {q['id']}"
    assert q["id"] not in ids, f"Duplicate ID {q['id']}"
    ids.add(q["id"])
    
    assert len(q["options"]) == 4, f"Options not 4 for ID {q['id']}"
    assert q["answer"] in [0, 1, 2, 3], f"Invalid answer for ID {q['id']}: {q['answer']}"
    
    assert q["question"].strip(), f"Empty question for ID {q['id']}"
    assert q["explanation"].strip(), f"Empty explanation for ID {q['id']}"
    assert q["source"].strip(), f"Empty source for ID {q['id']}"
    
    cat = q["category"]
    cat_counts[cat] = cat_counts.get(cat, 0) + 1

print("\nVerifikasi Distribusi 300 Soal Master Pool:")
for cat, exp in expected_distribution.items():
    act = cat_counts.get(cat, 0)
    status = "OK" if act == exp else "MISMATCH"
    print(f"  [{status}] {cat}: {act}/{exp}")
    assert act == exp, f"Category '{cat}' mismatch: {act} != {exp}"

print("\n[SUKSES] Seluruh 300 butir soal terverifikasi 100% valid, lengkap, dan siap digunakan!")
