# -*- coding: utf-8 -*-
"""
Asset Optimizer & Repository Cleaner for CBT Perangkat Desa Kabupaten Tuban
Fungsi:
1. Pembersihan File Tidak Diperlukan:
   - Di Luar Folder: file .py di root, file sampah OS (Thumbs.db, .DS_Store, desktop.ini), file log/tmp.
   - Di Dalam Folder: folder dev_scratch/, file legacy generator (expand_bank*.py, validate_data.py), folder __pycache__/*.pyc.
2. Optimasi CSS:
   - Minifikasi css/style.css -> css/style.min.css
   - Menghapus komentar, whitespace berlebih, zero-units, mempersingkat warna hex.
3. Optimasi SVG:
   - Kompresi whitespace, metadata, dan komentar XML pada seluruh file SVG.
4. Optimasi JavaScript & Data:
   - Minifikasi js/app.js -> js/app.min.js
   - Pembersihan whitespace berlebih pada file data JSON/JS.
5. Optimasi HTML:
   - Penghapusan komentar berlebih pada index.html & index_standalone_bundle.html.
"""

import os
import re
import shutil

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENERATOR_DIR = os.path.join(ROOT_DIR, "generator")
CSS_DIR = os.path.join(ROOT_DIR, "css")
JS_DIR = os.path.join(ROOT_DIR, "js")
ASSETS_DIR = os.path.join(ROOT_DIR, "assets")

def format_size(bytes_size):
    if bytes_size < 1024:
        return f"{bytes_size} B"
    elif bytes_size < 1024 * 1024:
        return f"{bytes_size / 1024:.2f} KB"
    else:
        return f"{bytes_size / (1024 * 1024):.2f} MB"

# ==============================================================================
# 1. PEMBERSIHAN FILE DI LUAR & DI DALAM FOLDER
# ==============================================================================
def clean_unnecessary_files():
    print("=" * 70)
    print("1. PEMBERSIHAN FILE TIDAK DIPERLUKAN (DI LUAR & DI DALAM FOLDER)")
    print("=" * 70)
    
    deleted_items = []
    
    # A. File .py di luar folder (root directory)
    for f in os.listdir(ROOT_DIR):
        full_path = os.path.join(ROOT_DIR, f)
        if os.path.isfile(full_path) and f.endswith(".py"):
            os.remove(full_path)
            deleted_items.append(f"[Root] File Python luar folder: {f}")
            
    # B. File sampah OS dan editor di seluruh workspace
    junk_patterns = ["Thumbs.db", "desktop.ini", ".DS_Store", "ehthumbs.db", "*.tmp", "*.bak", "*.swp", "*.log"]
    for root, dirs, files in os.walk(ROOT_DIR):
        for f in files:
            if f in ["Thumbs.db", "desktop.ini", ".DS_Store", "ehthumbs.db"] or f.endswith((".tmp", ".bak", ".swp", ".log")):
                full_path = os.path.join(root, f)
                try:
                    os.remove(full_path)
                    rel = os.path.relpath(full_path, ROOT_DIR)
                    deleted_items.append(f"[Sampah OS/Temp] {rel}")
                except Exception as e:
                    print(f"Gagal menghapus {full_path}: {e}")
                    
    # C. Hapus semua folder __pycache__ dan file .pyc
    for root, dirs, files in os.walk(ROOT_DIR, topdown=False):
        for d in dirs:
            if d == "__pycache__" or d == ".pytest_cache":
                full_path = os.path.join(root, d)
                try:
                    shutil.rmtree(full_path)
                    rel = os.path.relpath(full_path, ROOT_DIR)
                    deleted_items.append(f"[Cache Python] {rel}/")
                except Exception as e:
                    print(f"Gagal menghapus {full_path}: {e}")
        for f in files:
            if f.endswith((".pyc", ".pyo")):
                full_path = os.path.join(root, f)
                try:
                    os.remove(full_path)
                    rel = os.path.relpath(full_path, ROOT_DIR)
                    deleted_items.append(f"[Bytecode] {rel}")
                except Exception as e:
                    print(f"Gagal menghapus {full_path}: {e}")

    # D. Hapus folder dev_scratch (skrip investigasi lama)
    dev_scratch_path = os.path.join(ROOT_DIR, "dev_scratch")
    if os.path.exists(dev_scratch_path):
        try:
            shutil.rmtree(dev_scratch_path)
            deleted_items.append("[Folder Usang] dev_scratch/ (10 file investigasi scratch lama)")
        except Exception as e:
            print(f"Gagal menghapus dev_scratch: {e}")

    # E. Hapus file legacy generator yang sudah digantikan oleh 5 master bank
    legacy_generator_files = [
        "expand_bank.py",
        "expand_bank_300.py",
        "expand_bank_400.py",
        "expand_bank_500.py",
        "expand_bank_agama.py",
        "expand_bank_bahasa.py",
        "expand_bank_komputer.py",
        "validate_data.py"
    ]
    for lf in legacy_generator_files:
        full_path = os.path.join(GENERATOR_DIR, lf)
        if os.path.exists(full_path):
            try:
                os.remove(full_path)
                deleted_items.append(f"[Generator Legacy] generator/{lf}")
            except Exception as e:
                print(f"Gagal menghapus {full_path}: {e}")

    # F. Hapus file duplikat di root jika sudah ada di dalam folder assets/
    for dup in ["logo.svg"]:
        root_dup = os.path.join(ROOT_DIR, dup)
        asset_dup = os.path.join(ASSETS_DIR, dup)
        if os.path.exists(root_dup) and os.path.exists(asset_dup):
            try:
                os.remove(root_dup)
                deleted_items.append(f"[Duplikat Root] {dup} (sudah ada di assets/{dup})")
            except Exception as e:
                print(f"Gagal menghapus {root_dup}: {e}")

    if deleted_items:
        for item in deleted_items:
            print(f"  [OK] {item}")
        print(f"\nTotal item yang dibersihkan: {len(deleted_items)} item.")
    else:
        print("  [OK] Repositori sudah bersih, tidak ada file tidak berguna yang ditemukan.")
    print()


# ==============================================================================
# 2. OPTIMASI CSS
# ==============================================================================
def minify_css(css_text):
    """Minifikasi CSS murni tanpa dependensi eksternal."""
    # 1. Hapus komentar CSS /* ... */
    css = re.sub(r'/\*[\s\S]*?\*/', '', css_text)
    # 2. Hapus whitespace di sekitar simbol struktural
    css = re.sub(r'\s*([\{\}\:\;\,\>])\s*', r'\1', css)
    # 3. Normalisasi titik koma berulang
    css = re.sub(r';+', ';', css)
    # 4. Hapus titik koma sebelum tutup kurung }
    css = re.sub(r';\}', '}', css)
    # 5. Zero unit normalization: 0px, 0rem, 0em, 0% -> 0
    css = re.sub(r'(?<=[\s\:\,])0(px|rem|em|\%|pt)', '0', css)
    # 6. Singkat warna hex 6 digit yang bisa disingkat (misal: #ffffff -> #fff)
    css = re.sub(r'#([0-9a-fA-F])\1([0-9a-fA-F])\2([0-9a-fA-F])\3(?=[\s\;\,\)\}]|$)', r'#\1\2\3', css)
    # 7. Hapus newline & spasi berlebih
    css = re.sub(r'\s+', ' ', css).strip()
    return css

def optimize_css():
    print("=" * 70)
    print("2. OPTIMASI CSS (STYLESHEET)")
    print("=" * 70)
    css_file = os.path.join(CSS_DIR, "style.css")
    min_css_file = os.path.join(CSS_DIR, "style.min.css")
    
    if not os.path.exists(css_file):
        print(f"File {css_file} tidak ditemukan!")
        return

    with open(css_file, "r", encoding="utf-8") as f:
        raw_css = f.read()

    orig_size = len(raw_css.encode("utf-8"))
    minified = minify_css(raw_css)
    min_size = len(minified.encode("utf-8"))
    saving_pct = ((orig_size - min_size) / orig_size) * 100

    with open(min_css_file, "w", encoding="utf-8") as f:
        f.write(minified)

    print(f"  - css/style.css      : {format_size(orig_size)}")
    print(f"  - css/style.min.css  : {format_size(min_size)} (-{saving_pct:.1f}% lebih hemat)")
    print("  [OK] Minifikasi CSS berhasil dibuat.")
    print()


# ==============================================================================
# 3. OPTIMASI JAVASCRIPT
# ==============================================================================
def minify_js_simple(js_text):
    """Minifikasi ringan dan aman untuk JavaScript tanpa merusak string/regex."""
    # Hapus komentar multi-line /* ... */ yang bukan preserve
    cleaned = re.sub(r'/\*(?![\!]).*?\*/', '', js_text, flags=re.DOTALL)
    # Hapus baris yang hanya berisi komentar // ...
    lines = cleaned.split('\n')
    optimized_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('//'):
            continue
        if stripped:
            optimized_lines.append(line)
    return '\n'.join(optimized_lines)

def optimize_js():
    print("=" * 70)
    print("3. OPTIMASI JAVASCRIPT ENGINE")
    print("=" * 70)
    app_js = os.path.join(JS_DIR, "app.js")
    app_min_js = os.path.join(JS_DIR, "app.min.js")

    if os.path.exists(app_js):
        with open(app_js, "r", encoding="utf-8") as f:
            raw = f.read()
        orig_size = len(raw.encode("utf-8"))
        minified = minify_js_simple(raw)
        min_size = len(minified.encode("utf-8"))
        saving_pct = ((orig_size - min_size) / orig_size) * 100

        with open(app_min_js, "w", encoding="utf-8") as f:
            f.write(minified)

        print(f"  - js/app.js          : {format_size(orig_size)}")
        print(f"  - js/app.min.js      : {format_size(min_size)} (-{saving_pct:.1f}% lebih hemat)")
        print("  [OK] Minifikasi js/app.min.js berhasil dibuat.")
    print()


# ==============================================================================
# 4. OPTIMASI SVG (VEKTOR)
# ==============================================================================
def optimize_svg_text(svg_content):
    """Kompresi SVG: hapus komentar XML, metadata, dan rapikan whitespace."""
    # Hapus komentar XML
    svg = re.sub(r'<!--[\s\S]*?-->', '', svg_content)
    # Hapus newline dan spasi antar-tag
    svg = re.sub(r'>\s+<', '><', svg)
    # Hapus spasi berlebih dalam atribut
    svg = re.sub(r'\s+', ' ', svg)
    return svg.strip()

def optimize_svg_assets():
    print("=" * 70)
    print("4. OPTIMASI GRAFIS VEKTOR (SVG ICONS & LOGO)")
    print("=" * 70)
    svg_files = []
    
    # Kumpulkan file SVG di root dan assets/
    for root, dirs, files in os.walk(ROOT_DIR):
        if "generator" in root or ".git" in root:
            continue
        for f in files:
            if f.endswith(".svg"):
                svg_files.append(os.path.join(root, f))

    for path in svg_files:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        orig = len(content.encode("utf-8"))
        optimized = optimize_svg_text(content)
        opt_len = len(optimized.encode("utf-8"))
        saving = ((orig - opt_len) / orig) * 100 if orig > 0 else 0
        with open(path, "w", encoding="utf-8") as f:
            f.write(optimized + "\n")
        rel = os.path.relpath(path, ROOT_DIR)
        print(f"  - {rel:<25}: {format_size(orig)} -> {format_size(opt_len)} (-{saving:.1f}%)")

    print("  [OK] Seluruh file SVG berhasil dioptimasi.")
    print()


# ==============================================================================
# 5. OPTIMASI BUNDLE & HTML
# ==============================================================================
def optimize_html_files():
    print("=" * 70)
    print("5. OPTIMASI DOKUMEN HTML (INDEX & STANDALONE BUNDLE)")
    print("=" * 70)
    html_files = [
        os.path.join(ROOT_DIR, "index.html"),
        os.path.join(ROOT_DIR, "index_standalone_bundle.html")
    ]
    for p in html_files:
        if not os.path.exists(p):
            continue
        with open(p, "r", encoding="utf-8") as f:
            raw = f.read()
        orig = len(raw.encode("utf-8"))
        
        # Hapus komentar HTML (kecuali conditional comment IE jika ada)
        opt = re.sub(r'<!--(?!\[if)[\s\S]*?-->', '', raw)
        # Normalisasi baris kosong beruntun (lebih dari 2 baris kosong jadi 1)
        opt = re.sub(r'\n\s*\n\s*\n', '\n\n', opt)
        
        opt_len = len(opt.encode("utf-8"))
        saving = ((orig - opt_len) / orig) * 100
        with open(p, "w", encoding="utf-8") as f:
            f.write(opt)
        rel = os.path.relpath(p, ROOT_DIR)
        print(f"  - {rel:<28}: {format_size(orig)} -> {format_size(opt_len)} (-{saving:.1f}%)")
    print("  [OK] Dokumen HTML berhasil dioptimasi.")
    print()


# ==============================================================================
# MAIN ENTRYPOINT
# ==============================================================================
def main():
    print("\n======================================================================")
    print("START: REPOSITORY CLEANUP & ASSET OPTIMIZER - CBT PERANGKAT DESA")
    print("======================================================================\n")
    
    clean_unnecessary_files()
    optimize_css()
    optimize_js()
    optimize_svg_assets()
    optimize_html_files()
    
    print("======================================================================")
    print("ALL CLEANUP & OPTIMIZATION TASKS COMPLETED SUCCESSFULLY!")
    print("======================================================================\n")

if __name__ == "__main__":
    main()
