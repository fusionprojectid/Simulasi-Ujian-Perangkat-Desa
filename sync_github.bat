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

:: 3. Bersihkan file .py atau duplikat yang berada di luar folder (root)
echo [1/5] Memeriksa dan membersihkan file liar di luar folder...
for %%f in (*.py) do (
    if exist "generator\%%~nxf" (
        echo Menghapus file di luar folder: %%f ^(sudah ada di generator/^)
        del "%%f"
    )
    if exist "dev_scratch\%%~nxf" (
        echo Menghapus file di luar folder: %%f ^(sudah ada di dev_scratch/^)
        del "%%f"
    )
)

:: 4. Hapus cache folder scratch dari index git (jika sebelumnya pernah terunggah)
echo [2/5] Menghapus tracking folder dev_scratch dari index GitHub...
git rm -r --cached dev_scratch 2>nul
git rm --cached audit_deep.py audit_questions.py export_modular_assets.py find_duplicates.py find_js_lines.py inspect_analysis.py inspect_komputer.py print_early_komp.py print_komp.py verify_pool_integrity.py 2>nul

:: 5. Catat seluruh perubahan
echo [3/5] Merekam seluruh perubahan berkas (git add -A)...
git add -A

:: 6. Buat commit
echo [4/5] Menyimpan commit lokal...
git commit -m "Release v4.5.0: Update changelog rilis, footer copyright by fusionproject.id, dan optimasi pembersihan deploy.yml"

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
