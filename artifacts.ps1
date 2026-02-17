# PowerShell helper script do pracy z artefaktami Playwright
param(
    [Parameter(Position = 0)]
    [string]$Command = "help",
    
    [Parameter(Position = 1)]
    [string]$TestName
)

$ArtifactsDir = "test-results"
$VideosDir = Join-Path $ArtifactsDir "videos"

function Show-Help {
    Write-Host "
🎬 Playwright Artifacts Helper (PowerShell)

Usage: .\artifacts.ps1 [command] [test_name]

Commands:
  trace <test_name>      - Otwórz trace (.zip) w Playwright inspector
  video <test_name>      - Otwórz video testów
  screenshot <test_name> - Pokaż screenshot
  clean                  - Usuń wszystkie artefakty
  list                   - Pokaż wszystkie artefakty
  help                   - Pokaż tę wiadomość
" -ForegroundColor Cyan
}

function List-Artifacts {
    if (-not (Test-Path $ArtifactsDir)) {
        Write-Host "❌ Brak katalogu $ArtifactsDir" -ForegroundColor Red
        return
    }
    
    Write-Host "📂 Artefakty w $ArtifactsDir:" -ForegroundColor Green
    Write-Host ""
    
    # Traces
    $traces = Get-ChildItem -Path $ArtifactsDir -Filter "*.zip" -ErrorAction SilentlyContinue
    if ($traces.Count -gt 0) {
        Write-Host "📍 Traces (.zip):" -ForegroundColor Yellow
        foreach ($trace in $traces) {
            $size = [math]::Round($trace.Length / 1MB, 2)
            Write-Host "   $($trace.Name) ($size MB)" -ForegroundColor Gray
        }
    }
    
    # Screenshots
    $screenshots = Get-ChildItem -Path $ArtifactsDir -Filter "*_failure.png" -ErrorAction SilentlyContinue
    if ($screenshots.Count -gt 0) {
        Write-Host "📸 Screenshots (failure):" -ForegroundColor Yellow
        foreach ($screenshot in $screenshots) {
            Write-Host "   $($screenshot.Name)" -ForegroundColor Gray
        }
    }
    
    # Videos
    if (Test-Path $VideosDir) {
        $videos = Get-ChildItem -Path $VideosDir -Filter "*.webm" -ErrorAction SilentlyContinue
        if ($videos.Count -gt 0) {
            Write-Host "🎬 Videos:" -ForegroundColor Yellow
            foreach ($video in $videos) {
                $size = [math]::Round($video.Length / 1MB, 2)
                Write-Host "   $($video.Name) ($size MB)" -ForegroundColor Gray
            }
        }
    }
    
    # JSON Results
    if (Test-Path "$ArtifactsDir/results.json") {
        Write-Host "📊 Results (JSON):" -ForegroundColor Yellow
        Write-Host "   $ArtifactsDir/results.json" -ForegroundColor Gray
    }
    
    Write-Host ""
}

function Show-Trace {
    param([string]$TestName)
    
    if (-not $TestName) {
        Write-Host "❌ Musisz podać nazwę testu" -ForegroundColor Red
        Write-Host "Usage: .\artifacts.ps1 trace <test_name>" -ForegroundColor Yellow
        return
    }
    
    $traceFile = Join-Path $ArtifactsDir "$TestName.zip"
    
    if (-not (Test-Path $traceFile)) {
        Write-Host "❌ Nie znaleziono: $traceFile" -ForegroundColor Red
        Write-Host ""
        List-Artifacts
        return
    }
    
    Write-Host "🔍 Otwieranie trace: $traceFile" -ForegroundColor Green
    & npx playwright show-trace $traceFile
}

function Show-Video {
    param([string]$TestName)
    
    if (-not $TestName) {
        Write-Host "❌ Musisz podać nazwę testu" -ForegroundColor Red
        return
    }
    
    $videoFile = Join-Path $VideosDir "$TestName.webm"
    
    if (-not (Test-Path $videoFile)) {
        Write-Host "❌ Nie znaleziono: $videoFile" -ForegroundColor Red
        return
    }
    
    Write-Host "🎬 Otwieranie video: $videoFile" -ForegroundColor Green
    & $videoFile
}

function Show-Screenshot {
    param([string]$TestName)
    
    if (-not $TestName) {
        Write-Host "❌ Musisz podać nazwę testu" -ForegroundColor Red
        return
    }
    
    $screenshotFile = Join-Path $ArtifactsDir "$TestName`_failure.png"
    
    if (-not (Test-Path $screenshotFile)) {
        Write-Host "❌ Nie znaleziono: $screenshotFile" -ForegroundColor Red
        return
    }
    
    Write-Host "📸 Otwieranie screenshot: $screenshotFile" -ForegroundColor Green
    & $screenshotFile
}

function Clean-Artifacts {
    if (Test-Path $ArtifactsDir) {
        Write-Host "🗑️  Usuwam artefakty z $ArtifactsDir..." -ForegroundColor Yellow
        Remove-Item -Path $ArtifactsDir -Recurse -Force
        Write-Host "✅ Artefakty usunięte" -ForegroundColor Green
    }
    else {
        Write-Host "ℹ️  Brak artefaktów do usunięcia" -ForegroundColor Gray
    }
}

# Main dispatcher
switch ($Command.ToLower()) {
    "trace" {
        Show-Trace -TestName $TestName
    }
    "video" {
        Show-Video -TestName $TestName
    }
    "screenshot" {
        Show-Screenshot -TestName $TestName
    }
    "list" {
        List-Artifacts
    }
    "clean" {
        Clean-Artifacts
    }
    "help" {
        Show-Help
    }
    default {
        Write-Host "❌ Nieznane polecenie: $Command" -ForegroundColor Red
        Write-Host ""
        Show-Help
        exit 1
    }
}
