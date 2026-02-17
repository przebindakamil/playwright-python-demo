# 🎯 How-To: Practical Commands & Examples

## Run Tests

```bash
# Run all tests
pytest tests/ -v

# Run specific folder
pytest tests/triangle/ -v

# Run specific test
pytest tests/triangle/test_triangle.py::test_valid_triangle -v

# Run with keyword filter
pytest -k "triangle" -v
```

## Analyze Artifacts

### 📍 Trace (Most Detailed - Start Here!)

```bash
# Open in Playwright Inspector
.\artifacts.ps1 trace test_valid_triangle

# macOS/Linux
./artifacts.sh trace test_valid_triangle
```

**What you see:**
- Timeline of every action (click, fill, navigate, assert)
- Screenshots before & after each action
- DOM state at each step
- Network requests & responses
- JavaScript console logs
- Exact error point

### 📹 Video

```bash
.\artifacts.ps1 video test_valid_triangle

# Opens in default video player
# Shows screen recording of test run
```

### 📸 Screenshot

```bash
.\artifacts.ps1 screenshot test_valid_triangle

# Shows page state exactly when error occurred
```

## Manage Artifacts

### List What Exists

```bash
.\artifacts.ps1 list

# Shows:
# test_valid_triangle (trace + video + screenshot)
# test_invalid_triangle (trace + video + screenshot)
# ...
```

### Delete All Artifacts

```bash
.\artifacts.ps1 clean

# Removes:
# - test-results/ directory
# - All .zip (trace)
# - All .webm (video)  
# - All .png (screenshot)
```

### Manual Deletion

```bash
# Windows PowerShell
Remove-Item test-results -Recurse

# macOS/Linux
rm -rf test-results
```

## Intentionally Fail Test (for Testing)

**Edit test file**, change one assertion:

```python
# tests/triangle/test_triangle.py

def test_valid_triangle():
    page.fill("input[name='a']", "5")
    page.fill("input[name='b']", "5")
    page.fill("input[name='c']", "5")
    page.click("button[type='submit']")
    
    # MAKE THIS FAIL:
    assert page.locator("text=Invalid").is_visible()  # ← Change to wrong expectation
```

```bash
pytest tests/triangle/test_triangle.py::test_valid_triangle -v

# Now see artifacts:
.\artifacts.ps1 list
.\artifacts.ps1 trace test_valid_triangle
```

## GitHub Actions CI

### Check Results

1. GitHub → Actions tab
2. Click workflow run → Failed run
3. Artifacts section → `test-results` (download if failed)
4. Extract locally
5. Analyze with `.\artifacts.ps1 trace ...`

### Configure Retention (Optional)

Edit `.github/workflows/playwright-tests.yml`:

```yaml
      - uses: actions/upload-artifact@v4
        if: always()  # Always upload (pass or fail)
        with:
          name: test-results
          path: test-results/
          retention-days: 7  # ← Change this (default 30)
```

## Common Issues

### Error: "Can't find Chromium"

```bash
# Install it
playwright install chromium

# Or all browsers
playwright install
```

### Error: "Can't open trace"

```bash
# Make sure you have Node.js + npm
node --version
npm --version

# If missing, install from nodejs.org
```

### "Trace file is huge (40MB+)"

**Normal!** Traces capture screenshots at every step.
- Use `.\artifacts.ps1 clean` after analyzing
- Delete old traces regularly

## Pro Tips

| Task | Command |
|------|---------|
| See test with most details | `.\artifacts.ps1 trace test_name` |
| See page state at failure | `.\artifacts.ps1 screenshot test_name` |
| Watch test execution | `.\artifacts.ps1 video test_name` |
| Clean up after debugging | `.\artifacts.ps1 clean` |
| See console logs | In Trace → Console tab |
| See network calls | In Trace → Network tab |
| Check browser version | `.\artifacts.ps1 help` |

## Keyboard Shortcuts (in Playwright Inspector)

- `Space` - Play/Pause timeline
- `→` / `←` - Next/Prev action
- `1`, `2`, `3` - Tabs (Timeline, Screenshots, DOM)
- `N` - Network tab
- `C` - Console tab

## Multi-Browser Testing

```bash
# If you set up multiple browsers:
playwright install chromium firefox webkit

# Run tests against all
# (would need conftest.py modification)
```

## Share Artifacts with Team

1. **Locally:** `.\artifacts.ps1 list` → Show trace path
2. **Screenshot:** Send PNG file directly
3. **Full trace:** Zip trace + video files, send via Slack/Email
4. **CI:** Download from GitHub Actions Artifacts

## Keep test-results/ Clean

```bash
# Add to .gitignore (already done):
test-results/

# Before committing:
.\artifacts.ps1 clean
git status  # Should NOT show test-results/
```

## Helpful Links

- [Playwright Inspector Docs](https://playwright.dev/docs/inspector)
- [Playwright Trace Viewer](https://trace.playwright.dev/)
- [pytest Documentation](https://docs.pytest.org/)

---

Need more? Check [README_ARTIFACTS.md](./README_ARTIFACTS.md) for overview.
