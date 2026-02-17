# ✨ Playwright Artifacts - Trace + Video + Screenshot

```
On FAIL ❌ → Get artifacts automatically
On PASS ✅ → Zero overhead, no artifacts
```

| Type | Size | Content |
|------|------|---------|
| **Trace** 📍 | 10-50MB | Screenshots, DOM snapshots, network, console logs |
| **Video** 📹 | 50-200MB | Screen recording (WebM) |
| **Screenshot** 📸 | 100-500KB | Full-page screenshot at failure |

---

## 🚀 Quick Start

```bash
# Install & run
pip install -r requirements.txt
playwright install chromium
pytest tests/ -v

# When test fails, you see:
# 📸 Screenshot zapisany: test-results/test_name_failure.png
# 🔍 Trace zapisany: test-results/test_name.zip

# Analyze it:
.\artifacts.ps1 trace test_name    # Windows
./artifacts.sh trace test_name     # macOS/Linux
```

→ Opens Playwright Inspector with full test timeline 🎉

---

## 📚 Documentation

| File | What's Inside | Time |
|------|---------------|------|
| **QUICKSTART.md** | 5-min copy-paste setup | 5 min |
| **HOW_TO.md** | Practical commands & examples | 10 min |
| **README_ARTIFACTS.md** | This file - overview | 5 min |

---

## 🛠️ Helper Scripts

```bash
# Windows (PowerShell)
.\artifacts.ps1 trace test_name      # 🌟 BEST - opens inspector
.\artifacts.ps1 video test_name      # watch video
.\artifacts.ps1 screenshot test_name # see screenshot
.\artifacts.ps1 list                 # what exists
.\artifacts.ps1 clean                # delete all

# macOS/Linux (Bash)
./artifacts.sh trace test_name       # same as above
```

---

## 🔄 What Actually Happens

```
Test Runs
  ├─ On PASS ✅
  │   └─ Artifacts deleted → clean folder
  │
  └─ On FAIL ❌  
      └─ Artifacts saved:
          ├─ test-results/test_name.zip (trace)
          ├─ test-results/videos/test_name.webm (video)
          └─ test-results/test_name_failure.png (screenshot)
```

---

## 📊 How to Debug

1. **Test fails locally** → See message with artifact path
2. **Run helper script** → `.\artifacts.ps1 trace test_name`
3. **Inspector opens** → Full test timeline with:
   - Screenshots at each action
   - DOM state (HTML snapshots)
   - Network requests/responses
   - JavaScript console logs
4. **Click actions** → See before/after screenshots
5. **Find the bug** → Fix code, re-run test

---

## ⚙️ What's Configured

✅ `tests/conftest.py` - Fixtures for trace + video + screenshot  
✅ `pyproject.toml` - Pytest configuration  
✅ `.github/workflows/playwright-tests.yml` - GitHub Actions CI/CD  
✅ `artifacts.ps1` + `artifacts.sh` - Helper scripts  

**That's it!** Ready to use, no extra setup.

---

## 💡 Pro Tips

- Trace is most useful → use `.\artifacts.ps1 trace`
- Pass tests = no artifacts = zero overhead
- `.\artifacts.ps1 clean` when done analyzing
- GitHub Actions: artifacts auto-download on failure
- Traces keep: screenshots, network, console (everything)

---

## 📖 Next

- 👉 **Read** [QUICKSTART.md](./QUICKSTART.md) (5 min)
- 👉 **Reference** [HOW_TO.md](./HOW_TO.md) (commands & examples)
- 👉 **Run** `pytest tests/ -v`
- 👉 **Analyze** `.\artifacts.ps1 trace test_name`

Happy debugging! 🚀
