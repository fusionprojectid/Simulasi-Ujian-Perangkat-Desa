# -*- coding: utf-8 -*-
import json
import re
from difflib import SequenceMatcher
from merge_and_validate import ALL_QUESTIONS

def clean(text):
    return re.sub(r'[^a-zA-Z0-9\s]', '', text.lower()).strip()

duplicates_to_fix = []

for i in range(len(ALL_QUESTIONS)):
    q1 = ALL_QUESTIONS[i]
    t1 = clean(q1['question'])
    w1 = set(t1.split())
    for j in range(i + 1, len(ALL_QUESTIONS)):
        q2 = ALL_QUESTIONS[j]
        t2 = clean(q2['question'])
        w2 = set(t2.split())
        
        ratio = SequenceMatcher(None, t1, t2).ratio()
        ans1 = clean(q1['options'][q1['answer']])
        ans2 = clean(q2['options'][q2['answer']])
        ans_ratio = SequenceMatcher(None, ans1, ans2).ratio()
        
        # High question similarity OR identical answer with same topic
        if ratio >= 0.70 or (ratio >= 0.50 and ans_ratio >= 0.85 and len(w1 & w2) >= 4):
            duplicates_to_fix.append({
                "q_ratio": ratio,
                "ans_ratio": ans_ratio,
                "id1": q1['id'],
                "cat1": q1['category'],
                "text1": q1['question'],
                "ans1": q1['options'][q1['answer']],
                "id2": q2['id'],
                "cat2": q2['category'],
                "text2": q2['question'],
                "ans2": q2['options'][q2['answer']],
            })

print(f"Total duplicates / near duplicates flagged: {len(duplicates_to_fix)}")
for d in duplicates_to_fix:
    print(f"\n[ID {d['id1']} vs ID {d['id2']}] Q-Sim: {d['q_ratio']:.2f} | Ans-Sim: {d['ans_ratio']:.2f}")
    print(f"  Q1 ({d['id1']} - {d['cat1']}): {d['text1']}")
    print(f"     Ans1: {d['ans1']}")
    print(f"  Q2 ({d['id2']} - {d['cat2']}): {d['text2']}")
    print(f"     Ans2: {d['ans2']}")
