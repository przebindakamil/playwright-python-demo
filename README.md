# Playwright Python Automation Framework

A comprehensive test automation framework using Playwright and Python with the Page Object Model pattern.

## 🚀 Tech Stack

- **Python** 3.11+
- **Playwright** 1.42.0 - Browser automation
- **Pytest** 8.0.2 - Testing framework
- **Ruff** 0.15.0 - Fast Python linter and formatter
- **Mypy** 1.19.1 - Static type checker
- **Pre-commit** 4.5.1 - Git hooks for code quality

## 📁 Project Structure

```
playwright-python-demo/
├── .github/
│   └── workflows/
│       └── python-ci.yml          # CI/CD pipeline
├── pages/                          # Page Object Model
│   ├── basic_cart_page.py         # BasicCart application page
│   ├── seven_char_val_page.py     # 7-char validation page
│   └── triangle_page.py           # Triangle validation page
├── src/
│   └── base_page.py               # Base page class with common methods
├── tests/
│   ├── conftest.py                # Pytest fixtures and configuration
│   ├── basic_cart/                # BasicCart test suite
│   ├── basics/                    # Basic application iteration tests
│   ├── seven_char_val/            # 7-character validation tests
│   └── triangle/                  # Triangle type validation tests
├── docs/                          # Test plan documentation
├── .pre-commit-config.yaml        # Pre-commit hooks configuration
├── pyproject.toml                 # Python project and tool configuration
└── requirements.txt               # Python dependencies

```

## 🔧 Setup

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd playwright-python-demo
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # Linux/Mac
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers**
   ```bash
   playwright install chromium
   ```

5. **Install pre-commit hooks** (optional but recommended)
   ```bash
   pre-commit install
   ```

## 🧪 Running Tests

### Run all tests
```bash
pytest
```

### Run specific test suite
```bash
pytest tests/basic_cart/
pytest tests/triangle/
pytest tests/seven_char_val/
```

### Run with verbose output
```bash
pytest -v
```

### Run with visible browser (non-headless)
```bash
# Set environment variable before running tests
# Windows PowerShell
$env:PW_HEADLESS="0"; pytest

# Linux/Mac
PW_HEADLESS=0 pytest
```

### Run specific test
```bash
pytest tests/basic_cart/test_basic_cart.py::test_add_item_to_cart
```

## 🔍 Code Quality

### Linting and Formatting with Ruff
```bash
# Check code style
ruff check .

# Auto-fix issues
ruff check . --fix

# Format code
ruff format .

# Check formatting without modifying files
ruff format --check .
```

### Type Checking with Mypy
```bash
mypy .
```

### Run all quality checks
```bash
pre-commit run --all-files
```

## 🪝 Pre-commit Hooks

Pre-commit hooks automatically run before each commit to ensure code quality:

- **Ruff** - Auto-fixes linting issues and formats code
- **Mypy** - Validates type hints

To run hooks manually:
```bash
pre-commit run --all-files
```

To skip hooks (not recommended):
```bash
git commit --no-verify
```

## ✨ Test Artifacts (Trace + Video + Screenshot)

On **test failure**, automatically capture:
- **📍 Trace** (10-50MB) - Full execution timeline with screenshots, DOM snapshots, network events
- **📹 Video** (50-200MB) - Screen recording of test run  
- **📸 Screenshot** (100-500KB) - Page state at failure moment

**Analyze with:** `.\artifacts.ps1 trace test_name` → Opens Playwright Inspector

👉 See [README_ARTIFACTS.md](./README_ARTIFACTS.md) (2-min read) or [QUICKSTART.md](./QUICKSTART.md) (5-min setup)

---

## 🤖 CI/CD

The project uses GitHub Actions for continuous integration:

**Workflow triggers:**
- Push to `main` branch
- Pull requests

**CI Pipeline includes:**
1. Code formatting check (Ruff)
2. Linting (Ruff)
3. Type checking (Mypy)
4. Browser installation
5. Test execution (Pytest)
6. Auto-upload test artifacts on failure (30-day retention)

## 📊 Test Coverage

The framework includes tests for:
- **Basic Cart** (12 tests) - E-commerce shopping cart functionality
- **Triangle Validation** (7 tests) - Triangle type identification
- **Seven Character Validation** (8 tests) - Input validation rules
- **Basic Iterations** (15 tests) - Application availability checks

**Total: 42 tests**

## 🏗️ Page Object Model

The framework uses the Page Object Model pattern to:
- Separate test logic from page interactions
- Improve code maintainability
- Reduce code duplication
- Make tests more readable

Example:
```python
# Page Object
class TrianglePage(BasePage):
    def enter_sides(self, side1: int, side2: int, side3: int) -> None:
        self.side1_input.fill(str(side1))
        # ...

# Test
def test_equilateral_triangle(app_pages):
    triangle_page = app_pages.triangle
    triangle_page.enter_sides(5, 5, 5)
    triangle_page.click_identify()
    assert "Equilateral" in triangle_page.get_result()
```

## 📚 Additional Resources

- [Playwright Python Docs](https://playwright.dev/python/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)

## 🤝 Contributing

1. Create a feature branch
2. Make your changes
3. Ensure all tests pass: `pytest`
4. Check code quality: `pre-commit run --all-files`
5. Submit a pull request

## 📝 License

ISC
