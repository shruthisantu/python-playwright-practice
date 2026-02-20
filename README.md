# Playwright Practice — python-playwright-practice

This repository is a small collection of Playwright-based Python tests used for practicing and brushing up end-to-end testing skills with Playwright and pytest. It includes simple example tests (TodoMVC, GitHub page checks) as well as a few recorded/recording-style tests against a demo e-commerce site.

Use this project as a learning sandbox: experiment with selectors, waits, role-based locators, browser contexts, and CI integration (there is an `azure-pipelines.yml` included as an example).

## Table of contents
- Project overview
- Prerequisites
- Install and setup
- Running tests
- Files and purpose
- Tips & best practices
- CI notes

## Prerequisites
- Python 3.9+ (project was used with Python 3.10+ in development)
- pip
- (Optional) a virtual environment such as `venv` or `conda`
- Playwright and browser binaries (installed via `playwright` CLI)

## Install and setup
1. Clone the repository (if you haven't already):

```bash
git clone <repo-url>
cd python-playwright-practice
```

2. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate   # zsh / bash on macOS / Linux
# on Windows (PowerShell): .\.venv\Scripts\Activate.ps1
```

3. Install Python dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

4. Install Playwright browser binaries:

```bash
python -m playwright install
```

If you need only specific browsers, e.g. Chromium, use:

```bash
python -m playwright install chromium
```

## Running the tests
The project uses `pytest`. Run all tests with:

```bash
pytest -q
```

Run a single test file:

```bash
pytest -q tests/test_demo.py
```

Run a specific test function by node id:

```bash
pytest -q tests/test_demo.py::test_add_todo_item
```

If you want to see the browser UI during test runs, ensure tests are launching Playwright with `headless=False` (some example scripts do this). When running in CI, leave headless mode on (the default) or use a container/VM with the proper dependencies.

## Files and purpose
- `requirements.txt` — Python dependencies for this repository (Playwright + pytest etc.).
- `azure-pipelines.yml` — example Azure Pipelines configuration (can be adapted to your CI).
- `tests/test_demo.py` — lightweight beginner tests against the TodoMVC demo and GitHub. Short tests demonstrating:
  - page navigation and title assertion
  - filling inputs and keyboard actions
  - counting and asserting DOM elements
  - basic use of `expect` and `wait_for_timeout` (the latter only for demo/debugging)
- `tests/test_rec1.py` — recorded-style Playwright script interacting with https://rahulshettyacademy.com/loginpagePractise/. Shows role-based locators, filtering `app-card` elements and adding items to a cart. Useful for experimenting with role selectors and locator filtering.
- `PyTestPython/` — another set of pytest tests / fixtures. Contains `conftest.py` and example tests for pytest practice.
- `tests/*` — other test examples used while practicing Playwright flows and UI validation.

## Quick reference: what's in `tests/test_demo.py` (selected block)
- `test_add_todo_item` navigates to the TodoMVC demo, types a new todo into the `.new-todo` input, presses Enter, then uses `.todo-list li` to count items and asserts the expected count. It demonstrates basic locators, `fill`, `press`, and simple assertions.

## Tips & best practices
- Prefer deterministic waits: use `locator.wait_for()`, `expect(locator).to_be_visible()` or `expect(locator).to_have_text()` instead of `page.wait_for_timeout()` unless you're debugging.
- Use role-based locators and data-test attributes when available — they produce more maintainable selectors.
- Avoid hard-coded secrets and credentials in tests; read them from environment variables or a secure vault instead.
- Keep tests independent and idempotent: each test should set up and tear down its own data or run in a fresh browser context.
- Use `playwright codegen` to generate initial selectors, then refine them for resilience.

## CI notes
- An `azure-pipelines.yml` is present for example purposes. When running Playwright in CI:
  - make sure browsers are installed (`python -m playwright install --with-deps` for Linux containers sometimes)
  - run tests in headless mode or use XVFB / an appropriate display environment

## Contributing / Extending this repo
- Add more focused tests (form validations, navigation flows, API mocks) as you learn.
- Add a small `README` per folder if you split this repo into multiple projects.

## Troubleshooting
- Playwright install errors: re-run `python -m pip install -r requirements.txt` and `python -m playwright install`.
- Browser won't launch in CI: check missing system dependencies (fonts, libs) or run with `--with-deps` for Linux.

## License
This is a personal practice repository — adapt license terms as needed for sharing or team use.

---

Happy testing — use this repo to experiment, learn, and build more robust Playwright test suites.
