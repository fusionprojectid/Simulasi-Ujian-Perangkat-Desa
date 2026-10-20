@echo off
chcp 65001 >nul
title Sinkronisasi Perubahan ke GitHub
echo ==============================================================================
echo SINKRONISASI PERUBAHAN STRUKTUR KE GITHUB
echo CBT Simulasi Ujian Perangkat Desa Kabupaten Tuban
echo ==============================================================================
echo.

:: 1. Verifikasi ketersediaan perintah git
where git >nul 2>nul
if %errorlevel% neq 0 (
    echo [PERINGATAN] Perintah 'git' belum terdeteksi di sistem Anda.
    echo Jika Anda belum menginstal Git, unduh di: https://git-scm.com/download/win
    echo Jika Anda menggunakan Git Bash, Anda dapat menjalankan perintah git langsung dari Git Bash.
    echo.
    pause
    exit /b 1
)

:: 2. Periksa apakah repositori lokal sudah ada (.git)
if not exist ".git" (
    echo [INFO] Menginisialisasi repositori Git baru...
    git init
    git branch -M main
    echo.
)

:: 3. Jalankan Pembersihan Seluruh File Tidak Diperlukan & Optimasi Aset
echo [1/5] Menjalankan pembersihan file liar dan optimasi aset (CSS, JS, SVG, HTML)...
python generator\optimize_assets.py
if %errorlevel% neq 0 (
    echo [PERINGATAN] Python tidak ditemukan atau terjadi kendala saat optimasi, melanjutkan sinkronisasi...
)

:: 4. Hapus tracking folder/file usang dari index git jika sebelumnya pernah terlacak
echo [2/5] Menghapus tracking berkas usang dari index Git...
git rm -r --cached dev_scratch 2>nul
git rm --cached audit_deep.py audit_questions.py export_modular_assets.py find_duplicates.py find_js_lines.py inspect_analysis.py inspect_komputer.py print_early_komp.py print_komp.py verify_pool_integrity.py 2>nul
git rm --cached expand_bank.py expand_bank_300.py expand_bank_400.py expand_bank_500.py expand_bank_agama.py expand_bank_bahasa.py expand_bank_komputer.py validate_data.py 2>nul
git rm -r --cached generator/__pycache__ 2>nul
git rm -r --cached __pycache__ 2>nul

:: 5. Catat seluruh perubahan
echo [3/5] Merekam seluruh perubahan berkas (git add -A)...
git add -A

:: 6. Buat commit
echo [4/5] Menyimpan commit lokal...
git commit -m "Release v5.1.0: Pembersihan mendalam seluruh folder repositori, optimasi aset, dan perbaikan popup changelog"

:: 7. Dorong perubahan ke GitHub
echo [5/5] Mengunggah (push) perubahan ke remote GitHub...
git push origin main
if %errorlevel% neq 0 (
    echo.
    echo Mencoba push ke branch 'master'...
    git push origin master
)

echo.
echo ==============================================================================
echo SELESAI: Perubahan struktur repositori telah disinkronkan ke GitHub!
echo GitHub Actions (.github/workflows/deploy.yml) akan otomatis:
echo  1. Menjalankan pengujian otomatis (test suite).
echo  2. Men-deploy aplikasi web ke GitHub Pages secara online dan otomatis!
echo ==============================================================================
echo.
pause
