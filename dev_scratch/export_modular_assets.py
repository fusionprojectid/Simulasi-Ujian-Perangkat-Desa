# -*- coding: utf-8 -*-
"""
Helper script to export modular assets:
- js/data/questions.js (585 questions)
- js/data/glossary.js (36 terms)
- js/data/practical.js (10 practical tasks)
- js/app.js (CBTApp application logic)
- css/style.css (Design System & CSS)
- index.html (Clean HTML referencing modular files)
"""

import json
import os
from merge_and_validate import ALL_QUESTIONS
from glossary_data import GLOSSARY_TERMS
from practical_tasks_data import PRACTICAL_TASKS
from styles_css import APP_CSS
from html_templates import get_html_body
from js_engine import get_js_engine

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JS_DIR = os.path.join(BASE_DIR, "js")
JS_DATA_DIR = os.path.join(JS_DIR, "data")
CSS_DIR = os.path.join(BASE_DIR, "css")

os.makedirs(JS_DATA_DIR, exist_ok=True)
os.makedirs(CSS_DIR, exist_ok=True)

# 1. Export js/data/questions.js
questions_path = os.path.join(JS_DATA_DIR, "questions.js")
with open(questions_path, "w", encoding="utf-8") as f:
    f.write("// Master Database 585 Soal CBT Perangkat Desa Kabupaten Tuban\n")
    f.write("window.__MASTER_QUESTIONS__ = ")
    json.dump(ALL_QUESTIONS, f, ensure_ascii=False)
    f.write(";\nwindow.MASTER_QUESTIONS = window.__MASTER_QUESTIONS__;\n")
print(f"[OK] Exported {questions_path} ({os.path.getsize(questions_path):,} bytes)")

# 2. Export js/data/glossary.js
glossary_path = os.path.join(JS_DATA_DIR, "glossary.js")
with open(glossary_path, "w", encoding="utf-8") as f:
    f.write("// Glosarium 36 Istilah Pemerintahan Desa\n")
    f.write("window.__GLOSSARY_DATA__ = ")
    json.dump(GLOSSARY_TERMS, f, ensure_ascii=False)
    f.write(";\nwindow.GLOSSARY_DATA = window.__GLOSSARY_DATA__;\n")
print(f"[OK] Exported {glossary_path} ({os.path.getsize(glossary_path):,} bytes)")

# 3. Export js/data/practical.js
practical_path = os.path.join(JS_DATA_DIR, "practical.js")
with open(practical_path, "w", encoding="utf-8") as f:
    f.write("// 10 Butir Praktik Komputer Interaktif\n")
    f.write("window.__PRACTICAL_TASKS__ = ")
    json.dump(PRACTICAL_TASKS, f, ensure_ascii=False)
    f.write(";\nwindow.PRACTICAL_TASKS = window.__PRACTICAL_TASKS__;\n")
print(f"[OK] Exported {practical_path} ({os.path.getsize(practical_path):,} bytes)")

# 4. Export js/app.js (clean JS code without <script> tags)
raw_js = get_js_engine().strip()
if raw_js.startswith("<script>"):
    raw_js = raw_js[len("<script>"):].strip()
if raw_js.endswith("</script>"):
    raw_js = raw_js[:-len("</script>")].strip()

app_js_path = os.path.join(JS_DIR, "app.js")
with open(app_js_path, "w", encoding="utf-8") as f:
    f.write("// ==========================================================================\n")
    f.write("// CBT APPLICATION ENGINE - KABUPATEN TUBAN\n")
    f.write("// 5 Bidang Tertulis (125 Soal) & Praktik Komputer (10 Butir)\n")
    f.write("// ==========================================================================\n\n")
    f.write(raw_js)
    f.write("\n")
print(f"[OK] Exported {app_js_path} ({os.path.getsize(app_js_path):,} bytes)")

# 5. Export css/style.css
css_path = os.path.join(CSS_DIR, "style.css")
with open(css_path, "w", encoding="utf-8") as f:
    f.write(APP_CSS.strip())
    f.write("\n")
print(f"[OK] Exported {css_path} ({os.path.getsize(css_path):,} bytes)")

# 6. Generate Clean Modular index.html
modular_html = f'''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Simulasi Ujian Perangkat Desa Kabupaten Tuban | 5 Bidang Tertulis & Praktik Komputer</title>
  <meta name="description" content="Aplikasi simulasi resmi ujian perangkat desa Kabupaten Tuban. 5 bidang materi tertulis berurutan @ 25 soal (30 menit/bidang, total 125 soal) dan praktik komputer 10 butir. Nilai akhir gabungan tertulis (87,5) dan praktik (12,5).">
  <meta name="author" content="Simulasi CBT Perangkat Desa Kabupaten Tuban">
  <!-- Modular Stylesheet -->
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
{get_html_body()}

  <!-- Modular Scripts & Data (100% Offline & Relative) -->
  <script src="js/data/questions.js"></script>
  <script src="js/data/glossary.js"></script>
  <script src="js/data/practical.js"></script>
  <script src="js/app.js"></script>
</body>
</html>
'''

index_path = os.path.join(BASE_DIR, "index.html")
with open(index_path, "w", encoding="utf-8") as f:
    f.write(modular_html)
print(f"[OK] Generated Clean Modular {index_path} ({os.path.getsize(index_path):,} bytes)")

# 7. Also create a self-contained bundle for single-file deployment if desired
bundle_html = f'''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Simulasi Ujian Perangkat Desa Kabupaten Tuban | 5 Bidang Tertulis & Praktik Komputer</title>
  <meta name="description" content="Aplikasi simulasi resmi ujian perangkat desa Kabupaten Tuban. 5 bidang materi tertulis berurutan @ 25 soal (30 menit/bidang, total 125 soal) dan praktik komputer 10 butir. Nilai akhir gabungan tertulis (87,5) dan praktik (12,5).">
  <meta name="author" content="Simulasi CBT Perangkat Desa Kabupaten Tuban">
  <style>
{APP_CSS}
  </style>
</head>
<body>
{get_html_body()}

  <script>
    window.__MASTER_QUESTIONS__ = {json.dumps(ALL_QUESTIONS, ensure_ascii=False)};
    const MASTER_QUESTIONS = window.__MASTER_QUESTIONS__;
    window.__GLOSSARY_DATA__ = {json.dumps(GLOSSARY_TERMS, ensure_ascii=False)};
    const GLOSSARY_DATA = window.__GLOSSARY_DATA__;
    window.__PRACTICAL_TASKS__ = {json.dumps(PRACTICAL_TASKS, ensure_ascii=False)};
    const PRACTICAL_TASKS = window.__PRACTICAL_TASKS__;
  </script>
{get_js_engine()}
</body>
</html>
'''

bundle_path = os.path.join(BASE_DIR, "index_standalone_bundle.html")
with open(bundle_path, "w", encoding="utf-8") as f:
    f.write(bundle_html)
print(f"[OK] Generated Standalone Bundle {bundle_path} ({os.path.getsize(bundle_path):,} bytes)")
