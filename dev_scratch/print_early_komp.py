# -*- coding: utf-8 -*-
from merge_and_validate import ALL_QUESTIONS

komp_ids = [98, 99, 100, 198, 199, 200, 298, 299, 300, 398, 399, 400, 498, 499, 500]
print("EARLY COMPUTER QUESTIONS:")
for qid in komp_ids:
    q = ALL_QUESTIONS[qid-1]
    print(f"ID {q['id']}: {q['question']}")
    for idx, opt in enumerate(q['options']):
        marker = " [*]" if idx == q['answer'] else ""
        print(f"   {chr(65+idx)}. {opt}{marker}")
