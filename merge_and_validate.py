# -*- coding: utf-8 -*-
"""
Script Validasi dan Penggabungan Master Pool 550 Soal CBT Perangkat Desa
Menggabungkan:
- Q1_100: Soal 1 s.d. 100 dari validate_data.py
- Q101_200: Soal 101 s.d. 200 dari expand_bank.py
- Q201_300: Soal 201 s.d. 300 dari expand_bank_300.py
- Q301_400: Soal 301 s.d. 400 dari expand_bank_400.py
- Q401_500: Soal 401 s.d. 500 dari expand_bank_500.py
- Q501_550: Soal 501 s.d. 550 dari expand_bank_agama.py
Total: 550 Butir Soal Seimbang (13 Kategori Materi Lengkap).
"""
from validate_data import QUESTIONS as Q1_100
from expand_bank import NEW_QUESTIONS as Q101_200
from expand_bank_300 import QUESTIONS_201_300 as Q201_300
from expand_bank_400 import QUESTIONS_301_400 as Q301_400
from expand_bank_500 import QUESTIONS_401_500 as Q401_500
from expand_bank_agama import QUESTIONS_501_550 as Q501_550

ALL_QUESTIONS = Q1_100 + Q101_200 + Q201_300 + Q301_400 + Q401_500 + Q501_550

print(f"Total pertanyaan terkumpul dalam master pool: {len(ALL_QUESTIONS)} butir soal.")

expected_distribution = {
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
    "Komputer dasar dan pelayanan publik": 15,
    "Pendidikan agama dan moderasi beragama": 50
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

print("\nVerifikasi Distribusi 550 Soal Master Pool:")
for cat, exp in expected_distribution.items():
    act = cat_counts.get(cat, 0)
    status = "OK" if act == exp else "MISMATCH"
    print(f"  [{status}] {cat}: {act}/{exp}")
    assert act == exp, f"Category '{cat}' mismatch: {act} != {exp}"

print("\n[SUKSES] Seluruh 550 butir soal terverifikasi 100% valid, seimbang, lengkap, dan siap digunakan!")
