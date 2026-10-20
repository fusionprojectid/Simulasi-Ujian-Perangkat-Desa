# -*- coding: utf-8 -*-
from merge_and_validate import ALL_QUESTIONS

komp = [q for q in ALL_QUESTIONS if q['category'] == 'Komputer dasar dan pelayanan publik']
print(f"Total Soal Komputer: {len(komp)}")
for i, q in enumerate(komp, 1):
    print(f"\nNo {i} (ID {q['id']}): {q['question']}")
    for idx, opt in enumerate(q['options']):
        marker = " [BENAR]" if idx == q['answer'] else ""
        print(f"   {chr(65+idx)}. {opt}{marker}")
    print(f"   Sumber: {q.get('source')}")
