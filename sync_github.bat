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

:: 3. Hapus cache folder scratch dari index git (jika sebelumnya pernah terunggah)
echo [1/4] Menghapus tracking folder dev_scratch dari GitHub...
git rm -r --cached dev_scratch 2>nul
git rm --cached audit_deep.py audit_questions.py export_modular_assets.py find_duplicates.py find_js_lines.py inspect_analysis.py inspect_komputer.py print_early_komp.py print_komp.py verify_pool_integrity.py 2>nul

:: 4. Catat seluruh perubahan (pemindahan ke generator/, file baru .gitignore, dll.)
echo [2/4] Merekam seluruh pemindahan file dan perubahan struktur...
git add -A

:: 5. Buat commit
echo [3/4] Menyimpan commit lokal...
git commit -m "Refactor: Pindahkan seluruh file python ke folder generator dan rapikan repositori"

:: 6. Dorong perubahan ke GitHub
echo [4/4] Mengunggah (push) perubahan ke remote GitHub...
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
