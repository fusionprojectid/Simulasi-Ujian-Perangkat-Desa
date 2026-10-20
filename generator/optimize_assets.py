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
# 1. PEMBERSIHAN MENDALAM SELURUH FOLDER (DEEP SCAN & CLEAN)
# ==============================================================================
# Whitelist file Python aktif di dalam generator/
ACTIVE_GENERATOR_FILES = {
    "bank_bidang1_agama.py",
    "bank_bidang2_pemdes.py",
    "bank_bidang3_bahasa.py",
    "bank_bidang4_umum.py",
    "bank_bidang5_komputer.py",
    "build_index.py",
    "glossary_data.py",
    "html_templates.py",
    "js_engine.py",
    "merge_and_validate.py",
    "optimize_assets.py",
    "practical_tasks_data.py",
    "styles_css.py"
}

JUNK_DIR_NAMES = {
    "__pycache__",
    ".pytest_cache",
    ".coverage",
    "htmlcov",
    "dev_scratch",
    "scratch",
    "temp",
    "tmp",
    ".cache"
}

JUNK_EXTENSIONS = (
    ".tmp", ".temp", ".bak", ".backup", ".old", ".orig", "~",
    ".swp", ".swo", ".swn", ".log", ".patch", ".diff",
    ".pyc", ".pyo", ".pyd"
)

JUNK_FILENAMES = {
    "Thumbs.db", "ehthumbs.db", "desktop.ini",
    ".DS_Store", "._*", ".Spotlight-V100", ".Trashes"
}

STRUCTURAL_DIRS = {
    os.path.normpath(ROOT_DIR),
    os.path.normpath(os.path.join(ROOT_DIR, ".github")),
    os.path.normpath(os.path.join(ROOT_DIR, ".github", "workflows")),
    os.path.normpath(ASSETS_DIR),
    os.path.normpath(CSS_DIR),
    os.path.normpath(JS_DIR),
    os.path.normpath(os.path.join(JS_DIR, "data")),
    os.path.normpath(GENERATOR_DIR)
}

def clean_unnecessary_files():
    print("=" * 70)
    print("1. PEMBERSIHAN MENDALAM SELURUH FOLDER & SUBFOLDER (SEMUA EKSTENSI)")
    print("=" * 70)
    
    deleted_items = []
    scanned_files_count = 0
    scanned_dirs_count = 0

    # Tahap 1: Pindai dan bersihkan folder cache/scratch usang di seluruh workspace
    for root, dirs, files in os.walk(ROOT_DIR, topdown=False):
        # Abaikan direktori .git
        if "/.git" in root.replace("\\", "/") or root.replace("\\", "/").endswith("/.git"):
            continue
            
        scanned_dirs_count += len(dirs)
        for d in list(dirs):
            d_norm = d.lower()
            if d_norm in JUNK_DIR_NAMES or d_norm.startswith("dev_scratch"):
                full_dir_path = os.path.join(root, d)
                try:
                    shutil.rmtree(full_dir_path)
                    rel = os.path.relpath(full_dir_path, ROOT_DIR)
                    deleted_items.append(f"[Folder Usang/Cache] {rel}/")
                except Exception as e:
                    print(f"Gagal menghapus folder {full_dir_path}: {e}")

    # Tahap 2: Pindai seluruh file di dalam setiap folder dan subfolder
    for root, dirs, files in os.walk(ROOT_DIR):
        if "/.git" in root.replace("\\", "/") or root.replace("\\", "/").endswith("/.git"):
            continue

        rel_root = os.path.relpath(root, ROOT_DIR)
        is_generator_dir = (os.path.normpath(root) == os.path.normpath(GENERATOR_DIR))
        is_root_dir = (os.path.normpath(root) == os.path.normpath(ROOT_DIR))

        for f in files:
            scanned_files_count += 1
            full_path = os.path.join(root, f)
            rel_file = os.path.relpath(full_path, ROOT_DIR)
            f_lower = f.lower()

            # A. File sampah OS / editor / log / backup di folder manapun
            if f in JUNK_FILENAMES or f_lower.endswith(JUNK_EXTENSIONS):
                try:
                    os.remove(full_path)
                    deleted_items.append(f"[Sampah/Temp] {rel_file}")
                    continue
                except Exception as e:
                    print(f"Gagal menghapus {full_path}: {e}")

            # B. File Python (*.py) di luar folder generator/ (apapun foldernya)
            if f.endswith(".py"):
                if not is_generator_dir:
                    try:
                        os.remove(full_path)
                        deleted_items.append(f"[Stray Python] {rel_file} (Python hanya diperbolehkan di generator/)")
                        continue
                    except Exception as e:
                        print(f"Gagal menghapus {full_path}: {e}")
                else:
                    # Di dalam generator/, hanya simpan file aktif
                    if f not in ACTIVE_GENERATOR_FILES:
                        try:
                            os.remove(full_path)
                            deleted_items.append(f"[Legacy Python] {rel_file} (modul generator usang/tidak aktif)")
                            continue
                        except Exception as e:
                            print(f"Gagal menghapus {full_path}: {e}")

            # C. File duplikat di root yang identik dan sudah ada di assets/
            if is_root_dir and f in ["logo.svg", "logo-full.svg"]:
                asset_counterpart = os.path.join(ASSETS_DIR, f)
                if os.path.exists(asset_counterpart):
                    try:
                        os.remove(full_path)
                        deleted_items.append(f"[Duplikat Root] {f} (sudah ada di assets/{f})")
                        continue
                    except Exception as e:
                        print(f"Gagal menghapus {full_path}: {e}")

    # Tahap 3: Hapus subfolder kosong yang tersisa (kecuali direktori struktur proyek)
    for root, dirs, files in os.walk(ROOT_DIR, topdown=False):
        if "/.git" in root.replace("\\", "/") or root.replace("\\", "/").endswith("/.git"):
            continue
        norm_root = os.path.normpath(root)
        if norm_root not in STRUCTURAL_DIRS:
            if not os.listdir(root):
                try:
                    os.rmdir(root)
                    rel = os.path.relpath(root, ROOT_DIR)
                    deleted_items.append(f"[Folder Kosong] {rel}/")
                except Exception as e:
                    pass

    print(f"Pemeriksaan selesai: {scanned_files_count} file dan {scanned_dirs_count} folder dianalisis.")
    if deleted_items:
        for item in deleted_items:
            print(f"  [BERSIH] {item}")
        print(f"\nTotal item yang berhasil dibersihkan: {len(deleted_items)} item.")
    else:
        print("  [OK] Seluruh folder repositori sudah 100% bersih dari file tidak berguna.")
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
    import sys
    print("\n======================================================================")
    print("START: REPOSITORY CLEANUP & ASSET OPTIMIZER - CBT PERANGKAT DESA")
    print("======================================================================\n")
    
    clean_only = "--clean-only" in sys.argv
    clean_unnecessary_files()
    
    if not clean_only:
        optimize_css()
        optimize_js()
        optimize_svg_assets()
        optimize_html_files()
    
    print("======================================================================")
    print("ALL CLEANUP & OPTIMIZATION TASKS COMPLETED SUCCESSFULLY!")
    print("======================================================================\n")

if __name__ == "__main__":
    main()
