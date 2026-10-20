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

# 3. Lepaskan tracking dev_scratch jika sebelumnya pernah terunggah
Write-Host "[1/4] Menghapus tracking cache file lama & folder scratch dari index GitHub..." -ForegroundColor Green
git rm -r --cached dev_scratch/ 2>$null
$scratchFiles = @(
    "audit_deep.py", "audit_questions.py", "export_modular_assets.py",
    "find_duplicates.py", "find_js_lines.py", "inspect_analysis.py",
    "inspect_komputer.py", "print_early_komp.py", "print_komp.py",
    "verify_pool_integrity.py"
)
foreach ($f in $scratchFiles) {
    git rm --cached $f 2>$null
}

# 4. Rekam seluruh pemindahan file ke generator/ dan penghapusan di root
Write-Host "[2/4] Merekam seluruh pemindahan file (git add -A)..." -ForegroundColor Green
git add -A

# 5. Commit perubahan
Write-Host "[3/4] Membuat commit..." -ForegroundColor Green
git commit -m "Refactor: Pindahkan seluruh file python ke folder generator dan rapikan repositori"

# 6. Push ke remote
Write-Host "[4/4] Mengunggah perubahan ke GitHub..." -ForegroundColor Green
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
