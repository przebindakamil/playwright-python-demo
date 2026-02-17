# 🚀 Quickstart (5 Minutes)

## Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Install Chromium
playwright install chromium

# 3. Done! ✅
```

## Run Tests

```bash
pytest tests/ -v
```

**Result:**
- ✅ Tests pass → `test-results/` stays empty
- ❌ Test fails → Creates artifacts in `test-results/`

## When Test Fails

```bash
# See which artifacts exist
.\artifacts.ps1 list

# Analyze the failure (BEST WAY)
.\artifacts.ps1 trace test_name

# This opens Playwright Inspector showing:
# - Timeline of test execution
# - Screenshots at each step
# - DOM states (HTML snapshots)
# - Network requests/responses
# - Console logs and errors
```

## Other Artifact Views

```bash
.\artifacts.ps1 video test_name         # Watch screen recording
.\artifacts.ps1 screenshot test_name    # See page at failure
.\artifacts.ps1 clean                   # Delete all artifacts
```

## macOS / Linux

Replace `.\artifacts.ps1` with `./artifacts.sh`:

```bash
./artifacts.sh trace test_name
./artifacts.sh video test_name
./artifacts.sh list
./artifacts.sh clean
```

## In GitHub Actions CI

When test fails in CI:
1. Go to GitHub Actions → Failed Run
2. Artifacts section → Download `test-results`
3. Extract locally
4. Use `.\artifacts.ps1` to analyze

## That's It!

Everything works automatically. No configuration needed. ✨

👉 For more commands, see [HOW_TO.md](./HOW_TO.md)
