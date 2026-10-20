# ==============================================================================
# sync_github.ps1 - Script Otomatisasi Sinkronisasi Perubahan ke GitHub
# ==============================================================================

Write-Host "==============================================================================" -ForegroundColor Cyan
Write-Host "SINKRONISASI PERUBAHAN STRUKTUR KE GITHUB" -ForegroundColor Cyan
Write-Host "CBT Simulasi Ujian Perangkat Desa Kabupaten Tuban" -ForegroundColor Cyan
Write-Host "==============================================================================" -ForegroundColor Cyan
Write-Host ""

# 1. Cek apakah Git tersedia
$gitCmd = Get-Command git -ErrorAction SilentlyContinue
if (-not $gitCmd) {
    Write-Host "[PERINGATAN] Perintah 'git' belum terpasang di sistem ini." -ForegroundColor Yellow
    Write-Host "Silakan unduh dan pasang Git melalui: https://git-scm.com/download/win" -ForegroundColor White
    Write-Host "Setelah diinstal, jalankan kembali script ini." -ForegroundColor White
    Write-Host ""
    Read-Host "Tekan Enter untuk keluar..."
    exit 1
}

# 2. Cek apakah folder .git ada
if (-not (Test-Path ".git")) {
    Write-Host "[INFO] Inisialisasi repositori Git lokal baru..." -ForegroundColor Yellow
    git init
    git branch -M main
    Write-Host ""
}

# 3. Jalankan Pembersihan Seluruh File Tidak Diperlukan & Optimasi Aset
Write-Host "[1/5] Menjalankan pembersihan file liar dan optimasi aset (CSS, JS, SVG, HTML)..." -ForegroundColor Green
$pythonCmd = Get-Command python -ErrorAction SilentlyContinue
if ($pythonCmd) {
    python generator/optimize_assets.py
} else {
    Write-Host "[INFO] Python tidak terdeteksi di PATH, melewati optimasi lokal..." -ForegroundColor Yellow
}

# 4. Lepaskan tracking dev_scratch, file liar, dan file usang dari index GitHub
Write-Host "[2/5] Menghapus tracking cache file lama & folder scratch dari index GitHub..." -ForegroundColor Green
git rm -r --cached dev_scratch/ 2>$null
$legacyFiles = @(
    "audit_deep.py", "audit_questions.py", "export_modular_assets.py",
    "find_duplicates.py", "find_js_lines.py", "inspect_analysis.py",
    "inspect_komputer.py", "print_early_komp.py", "print_komp.py",
    "verify_pool_integrity.py", "expand_bank.py", "expand_bank_300.py",
    "expand_bank_400.py", "expand_bank_500.py", "expand_bank_agama.py",
    "expand_bank_bahasa.py", "expand_bank_komputer.py", "validate_data.py"
)
foreach ($f in $legacyFiles) {
    git rm --cached $f 2>$null
}
git rm -r --cached generator/__pycache__ 2>$null
git rm -r --cached __pycache__ 2>$null

# 5. Rekam seluruh perubahan
Write-Host "[3/5] Merekam seluruh berkas (git add -A)..." -ForegroundColor Green
git add -A

# 6. Commit perubahan
Write-Host "[4/5] Membuat commit..." -ForegroundColor Green
git commit -m "Release v5.1.0: Pembersihan mendalam seluruh folder repositori, optimasi aset, dan perbaikan popup changelog"

# 7. Push ke remote
Write-Host "[5/5] Mengunggah perubahan ke GitHub..." -ForegroundColor Green
git push origin main
if ($LASTEXITCODE -ne 0) {
    Write-Host "Mencoba push ke branch 'master'..." -ForegroundColor Yellow
    git push origin master
}

Write-Host ""
Write-Host "==============================================================================" -ForegroundColor Cyan
Write-Host "SELESAI: Perubahan struktur repositori telah disinkronkan ke GitHub!" -ForegroundColor Green
Write-Host "GitHub Actions (.github/workflows/deploy.yml) akan otomatis:" -ForegroundColor Yellow
Write-Host " 1. Menjalankan seluruh pengujian (test suite)." -ForegroundColor White
Write-Host " 2. Men-deploy aplikasi web ke GitHub Pages secara online dan langsung aktif!" -ForegroundColor White
Write-Host "==============================================================================" -ForegroundColor Cyan
Write-Host ""
Read-Host "Tekan Enter untuk menutup..."
