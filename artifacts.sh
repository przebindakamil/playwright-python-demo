#!/bin/bash
# Helper script do pracy z artefaktami Playwright

set -e

ARTIFACTS_DIR="test-results"
VIDEOS_DIR="$ARTIFACTS_DIR/videos"

show_help() {
    echo "🎬 Playwright Artifacts Helper"
    echo ""
    echo "Usage: ./artifacts.sh [command]"
    echo ""
    echo "Commands:"
    echo "  trace <test_name>    - Otwórz trace (.zip) w Playwright inspector"
    echo "  video <test_name>    - Otwórz video testów"
    echo "  screenshot <test_name> - Pokaż screenshot (requires image viewer)"
    echo "  clean                - Usuń wszystkie artefakty"
    echo "  list                 - Pokaż wszystkie artefakty"
    echo "  help                 - Pokaż tę wiadomość"
    echo ""
}

list_artifacts() {
    if [ ! -d "$ARTIFACTS_DIR" ]; then
        echo "❌ Brak katalogu $ARTIFACTS_DIR"
        return 1
    fi
    
    echo "📂 Artefakty w $ARTIFACTS_DIR:"
    echo ""
    
    # Traces
    if ls "$ARTIFACTS_DIR"/*.zip 1> /dev/null 2>&1; then
        echo "📍 Traces (.zip):"
        ls -lh "$ARTIFACTS_DIR"/*.zip | awk '{print "   " $9}'
    fi
    
    # Screenshots
    if ls "$ARTIFACTS_DIR"/*_failure.png 1> /dev/null 2>&1; then
        echo "📸 Screenshots (failure):"
        ls -lh "$ARTIFACTS_DIR"/*_failure.png | awk '{print "   " $9}'
    fi
    
    # Videos
    if [ -d "$VIDEOS_DIR" ] && ls "$VIDEOS_DIR"/*.webm 1> /dev/null 2>&1; then
        echo "🎬 Videos:"
        ls -lh "$VIDEOS_DIR"/*.webm | awk '{print "   " $9}'
    fi
    
    # JSON Results
    if [ -f "$ARTIFACTS_DIR/results.json" ]; then
        echo "📊 Results (JSON):"
        echo "   $ARTIFACTS_DIR/results.json"
    fi
    
    echo ""
}

show_trace() {
    local test_name=$1
    local trace_file="$ARTIFACTS_DIR/${test_name}.zip"
    
    if [ ! -f "$trace_file" ]; then
        echo "❌ Nie znaleziono: $trace_file"
        echo ""
        echo "Dostępne traces:"
        list_artifacts
        return 1
    fi
    
    echo "🔍 Otwieranie trace: $trace_file"
    npx playwright show-trace "$trace_file"
}

show_video() {
    local test_name=$1
    local video_file="$VIDEOS_DIR/${test_name}.webm"
    
    if [ ! -f "$video_file" ]; then
        echo "❌ Nie znaleziono: $video_file"
        return 1
    fi
    
    echo "🎬 Otwieranie video: $video_file"
    # Spróbuj różne playery
    if command -v vlc &> /dev/null; then
        vlc "$video_file"
    elif command -v mpv &> /dev/null; then
        mpv "$video_file"
    elif command -v ffplay &> /dev/null; then
        ffplay "$video_file"
    else
        echo "⚠️  Nie znaleziono playera (zainstaluj: vlc, mpv lub ffmpeg)"
        echo "   Plik: $video_file"
    fi
}

show_screenshot() {
    local test_name=$1
    local screenshot_file="$ARTIFACTS_DIR/${test_name}_failure.png"
    
    if [ ! -f "$screenshot_file" ]; then
        echo "❌ Nie znaleziono: $screenshot_file"
        return 1
    fi
    
    echo "📸 Otwieranie screenshot: $screenshot_file"
    
    # Spróbuj różne przeglądarki
    if command -v xdg-open &> /dev/null; then
        xdg-open "$screenshot_file"
    elif command -v open &> /dev/null; then
        open "$screenshot_file"
    elif command -v start &> /dev/null; then
        start "$screenshot_file"
    else
        echo "⚠️  Nie mogę otworzyć obrazka automatycznie"
        echo "   Plik: $screenshot_file"
    fi
}

clean_artifacts() {
    if [ -d "$ARTIFACTS_DIR" ]; then
        echo "🗑️  Usuwam artefakty z $ARTIFACTS_DIR..."
        rm -rf "$ARTIFACTS_DIR"
        echo "✅ Artefakty usunięte"
    else
        echo "ℹ️  Brak artefaktów do usunięcia"
    fi
}

# Main
case "${1:-help}" in
    trace)
        show_trace "$2"
        ;;
    video)
        show_video "$2"
        ;;
    screenshot)
        show_screenshot "$2"
        ;;
    list)
        list_artifacts
        ;;
    clean)
        clean_artifacts
        ;;
    help|--help|-h)
        show_help
        ;;
    *)
        echo "❌ Nieznane polecenie: $1"
        echo ""
        show_help
        exit 1
        ;;
esac
