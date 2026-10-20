# -*- coding: utf-8 -*-
"""
Builder script to generate the complete, production-ready, standalone 'index.html'
for 'Simulasi Ujian Perangkat Desa Kabupaten Tuban, Jawa Timur'
Format Resmi:
- Ujian Tertulis: 5 Bidang Materi Berurutan (Masing-masing 25 Soal, Waktu 30 Menit/Bidang, Total 125 Soal)
- Praktik Komputer: 10 Butir Tugas Interaktif (Word, Excel, Berkas Digital, Sandi UU PDP)
- Sistem Penilaian: Tertulis (125 x 0,7 = 87,5) + Praktik Komputer (10 x 1,25 = 12,5) = Nilai Akhir 100,0 Maks
- Kunci jawaban & pembahasan baru dibuka setelah seluruh tahapan ujian selesai
- 100% Offline & Privat, Single File index.html
"""

import json
import os
from merge_and_validate import ALL_QUESTIONS
from glossary_data import GLOSSARY_TERMS
from practical_tasks_data import PRACTICAL_TASKS
from styles_css import APP_CSS
from html_templates import get_html_body
from js_engine import get_js_engine

def build_all_assets():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    css_dir = os.path.join(base_dir, "css")
    js_dir = os.path.join(base_dir, "js")
    js_data_dir = os.path.join(js_dir, "data")

    os.makedirs(css_dir, exist_ok=True)
    os.makedirs(js_data_dir, exist_ok=True)

    # 1. Export css/style.css
    css_path = os.path.join(css_dir, "style.css")
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(APP_CSS.strip() + "\n")

    # 2. Export js/data/questions.js
    q_path = os.path.join(js_data_dir, "questions.js")
    with open(q_path, "w", encoding="utf-8") as f:
        f.write("// Master Database 585 Soal CBT Perangkat Desa Kabupaten Tuban\n")
        f.write("window.__MASTER_QUESTIONS__ = ")
        json.dump(ALL_QUESTIONS, f, ensure_ascii=False)
        f.write(";\nwindow.MASTER_QUESTIONS = window.__MASTER_QUESTIONS__;\n")

    # 3. Export js/data/glossary.js
    g_path = os.path.join(js_data_dir, "glossary.js")
    with open(g_path, "w", encoding="utf-8") as f:
        f.write("// Glosarium 36 Istilah Pemerintahan Desa\n")
        f.write("window.__GLOSSARY_DATA__ = ")
        json.dump(GLOSSARY_TERMS, f, ensure_ascii=False)
        f.write(";\nwindow.GLOSSARY_DATA = window.__GLOSSARY_DATA__;\n")

    # 4. Export js/data/practical.js
    p_path = os.path.join(js_data_dir, "practical.js")
    with open(p_path, "w", encoding="utf-8") as f:
        f.write("// 10 Butir Praktik Komputer Interaktif\n")
        f.write("window.__PRACTICAL_TASKS__ = ")
        json.dump(PRACTICAL_TASKS, f, ensure_ascii=False)
        f.write(";\nwindow.PRACTICAL_TASKS = window.__PRACTICAL_TASKS__;\n")

    # 5. Export js/app.js
    raw_js = get_js_engine().strip()
    if raw_js.startswith("<script>"):
        raw_js = raw_js[len("<script>"):].strip()
    if raw_js.endswith("</script>"):
        raw_js = raw_js[:-len("</script>")].strip()

    app_path = os.path.join(js_dir, "app.js")
    with open(app_path, "w", encoding="utf-8") as f:
        f.write("// ==========================================================================\n")
        f.write("// CBT APPLICATION ENGINE - KABUPATEN TUBAN\n")
        f.write("// 5 Bidang Tertulis (125 Soal) & Praktik Komputer (10 Butir)\n")
        f.write("// ==========================================================================\n\n")
        f.write(raw_js + "\n")

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

  <!-- Modular Scripts & Master Data (100% Offline & Relative) -->
  <script src="js/data/questions.js"></script>
  <script src="js/data/glossary.js"></script>
  <script src="js/data/practical.js"></script>
  <script src="js/app.js"></script>
</body>
</html>
'''
    index_path = os.path.join(base_dir, "index.html")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(modular_html)

    # 7. Generate Standalone Bundle index_standalone_bundle.html
    questions_json = json.dumps(ALL_QUESTIONS, ensure_ascii=False)
    glossary_json = json.dumps(GLOSSARY_TERMS, ensure_ascii=False)
    practical_json = json.dumps(PRACTICAL_TASKS, ensure_ascii=False)

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
    window.__MASTER_QUESTIONS__ = {questions_json};
    const MASTER_QUESTIONS = window.__MASTER_QUESTIONS__;
    window.__GLOSSARY_DATA__ = {glossary_json};
    const GLOSSARY_DATA = window.__GLOSSARY_DATA__;
    window.__PRACTICAL_TASKS__ = {practical_json};
    const PRACTICAL_TASKS = window.__PRACTICAL_TASKS__;
  </script>
{get_js_engine()}
</body>
</html>
'''
    bundle_path = os.path.join(base_dir, "index_standalone_bundle.html")
    with open(bundle_path, "w", encoding="utf-8") as f:
        f.write(bundle_html)

    print("[OK] Seluruh aset modular dan bundle berhasil diperbarui:")
    print(f"     - index.html (Modular): {os.path.getsize(index_path):,} bytes")
    print(f"     - css/style.css: {os.path.getsize(css_path):,} bytes")
    print(f"     - js/data/questions.js (585 Soal): {os.path.getsize(q_path):,} bytes")
    print(f"     - js/data/glossary.js (36 Istilah): {os.path.getsize(g_path):,} bytes")
    print(f"     - js/data/practical.js (10 Praktik): {os.path.getsize(p_path):,} bytes")
    print(f"     - js/app.js (CBT Engine): {os.path.getsize(app_path):,} bytes")
    print(f"     - index_standalone_bundle.html: {os.path.getsize(bundle_path):,} bytes")

if __name__ == "__main__":
    build_all_assets()
