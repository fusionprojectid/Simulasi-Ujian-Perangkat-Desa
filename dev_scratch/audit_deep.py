# -*- coding: utf-8 -*-
import json
import re
from difflib import SequenceMatcher
from collections import defaultdict
from merge_and_validate import ALL_QUESTIONS

print(f"Total Soal di Master Pool: {len(ALL_QUESTIONS)}")

# 1. Check all text duplicates & high similarity (> 0.65)
def clean(text):
    return re.sub(r'[^a-zA-Z0-9\s]', '', text.lower()).strip()

duplicates = []
high_sim = []

for i in range(len(ALL_QUESTIONS)):
    q1 = ALL_QUESTIONS[i]
    t1 = clean(q1['question'])
    w1 = set(t1.split())
    for j in range(i + 1, len(ALL_QUESTIONS)):
        q2 = ALL_QUESTIONS[j]
        t2 = clean(q2['question'])
        w2 = set(t2.split())
        
        # Exact match
        if t1 == t2:
            duplicates.append((q1['id'], q2['id'], q1['question']))
            continue
            
        # Jaccard / SequenceMatcher
        overlap = len(w1 & w2) / max(len(w1 | w2), 1)
        if overlap > 0.50:
            ratio = SequenceMatcher(None, t1, t2).ratio()
            if ratio >= 0.65:
                # Check option overlap
                opt1 = set(clean(o) for o in q1['options'])
                opt2 = set(clean(o) for o in q2['options'])
                opt_overlap = len(opt1 & opt2)
                high_sim.append({
                    "ratio": ratio,
                    "opt_overlap": opt_overlap,
                    "id1": q1['id'],
                    "cat1": q1['category'],
                    "text1": q1['question'],
                    "ans1": q1['options'][q1['answer']],
                    "id2": q2['id'],
                    "cat2": q2['category'],
                    "text2": q2['question'],
                    "ans2": q2['options'][q2['answer']],
                })

print(f"\nExact Duplicates: {len(duplicates)}")
for id1, id2, txt in duplicates:
    print(f"  ID {id1} == ID {id2}: {txt}")

print(f"\nHigh Similarity Pairs (count: {len(high_sim)}):")
high_sim.sort(key=lambda x: (x['ratio'] + x['opt_overlap'] * 0.2), reverse=True)
for item in high_sim:
    print(f"\n[Score {item['ratio']:.2f} | Opts overlap: {item['opt_overlap']}/4]")
    print(f"  Q1 (ID {item['id1']} - {item['cat1']}): {item['text1']}")
    print(f"     Ans: {item['ans1']}")
    print(f"  Q2 (ID {item['id2']} - {item['cat2']}): {item['text2']}")
    print(f"     Ans: {item['ans2']}")
