# -*- coding: utf-8 -*-
with open("js_engine.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Total lines in js_engine.py: {len(lines)}")
for idx, line in enumerate(lines):
    if any(k in line for k in ["generateTubanExamSections", "startExam", "resetExam", "newExam", "shuffled", "localStorage", "seenQuestions", "usedQuestions", "history"]):
        print(f"Line {idx+1}: {line.strip()[:100]}")
