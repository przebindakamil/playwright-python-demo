# 🧪 Jak Testować Artefakty - Kroki

## Setup (Jednorazowo)

```bash
# 1. Przygotuj środowisko
pip install -r requirements.txt
playwright install chromium

# 2. Sprawdź że conftest.py ma fixture do artefaktów
# (patrz: tests/conftest.py)
```

---

## Test Na Szybko

### Krok 1: Stwórz Test, Który Failuje

```python
# tests/triangle/test_artifacts_check.py

def test_intentional_failure(page):
    """Test że failuje, aby stworzyć artefakty."""
    page.goto("https://testpages.herokuapp.com/styled/calculator")
    assert page.locator("text=This Text Does Not Exist").is_visible()
```

### Krok 2: Uruchom Test

```bash
python -m pytest tests/triangle/test_artifacts_check.py -v
```

**Oczekiwany output:**
```
FAILED tests/triangle/test_artifacts_check.py::test_intentional_failure
📸 Screenshot zapisany: test-results\test_intentional_failure_failure.png
🔍 Trace zapisany: test-results\test_intentional_failure.zip
   ✓ Screenshots
   ✓ DOM Snapshots
   ✓ Network Events
```

### Krok 3: Sprawdź Czy Pliki Istnieją

```bash
ls test-results/ -Recurse -File
```

**Szukaj:**
- ✅ `test_intentional_failure.zip` (~500KB-1MB) - Trace
- ✅ `test_intentional_failure_failure.png` (~100KB) - Screenshot
- ✅ `videos/[hash].webm` (~50KB) - Video

### Krok 4: Analiza (Najpierw Sam Sprawdź format)

```bash
# Otworz screenshot
.\artifacts.ps1 screenshot test_intentional_failure

# Otworz trace w Playwright Inspector
npx playwright show-trace test-results/test_intentional_failure.zip
```

**W Inspectorze:**
- Kliknij "Timeline" tab → Widzisz każdy action
- Kliknij action → Widzisz screenshoty before/after
- "Network" tab → API calls
- "Console" tab → Błędy JS

### Krok 5: Cleanup

```bash
.\artifacts.ps1 clean
# Lub manualnie:
Remove-Item test-results -Recurse
```

---

## Full Test Suite (Ze Wszystkim)

```bash
# Run all tests
python -m pytest tests/ -v

# Rezultat:
# - Passing tests: 0 artefaktów
# - Failing tests: Full artifacts

# Check co failnęło
ls test-results/ -Recurse -File

# Analyze failures
npx playwright show-trace test-results/[test_name].zip
```

---

## Checklist: Czy Artefakty Działają?

| Co Testować | Krok | Wynik |
|---|---|---|
| **Screenshot on fail** | Failnij test, sprawdź `*_failure.png` | Plik istnieje + ma treść |
| **Video on fail** | Failnij test, sprawdź `videos/*.webm` | Plik istnieje (~50KB+) |
| **Trace on fail** | Failnij test, sprawdź `*.zip` | Plik istnieje (~500KB+) |
| **No artifacts on pass** | Passuj testy, sprawdź `test-results/` | Folder pusty |
| **Inspector works** | `npx playwright show-trace *.zip` | UI otwiera się |

---

## Kiedy Testować?

| Scenariusz | Co Robić |
|---|---|
| Po zmianie conftest.py | Uruchom test-failure test |
| Przed committem | Weryfikuj że passing testy = no artifacts |
| Po CI change | Download artifacts z GitHub Actions |
| Nowa feature | Dodaj test, failnij, sprawdź trace |

---

## Szybki Test (2 Min)

```bash
# Terminal
python -m pytest tests/triangle/test_artifacts_check.py -v

# Czekaj na FAILED
# Szukaj: "📸 Screenshot zapisany" + "🔍 Trace zapisany"

# Done! ✅
```

---

## Troubleshooting

| Problem | Solution |
|---|---|
| Brak pliku `test-results/` | Test nie failnął - check assert |
| ZIP plik pusty | conftest.py nie save'uje - check hooks |
| Inspector nie otwiera | `npm install -g @playwright/test` |
| Encoding error (.ps1) | Używaj `npx playwright show-trace` zamiast |

