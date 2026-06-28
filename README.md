# Selenium Python Automation Framework

A UI test automation framework for [SauceDemo](https://www.saucedemo.com/) built with Selenium, Pytest, and Allure — following the Page Object Model design pattern.

![CI](https://github.com/unaisLearning/selenium-python-framework/actions/workflows/automation.yml/badge.svg)

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.11 | Language |
| Selenium 4 | Browser automation |
| Pytest | Test runner |
| Allure | Test reporting |
| pytest-html | HTML report |
| GitHub Actions | CI/CD |

---

## Project Structure

```
selenium-python-framework/
├── .github/
│   └── workflows/
│       └── automation.yml       # CI pipeline
├── config/
│   └── config.py                # Base URL, timeout, browser, credentials
├── data/
│   ├── products.py              # Product name constants
│   └── address.py               # Checkout address constants
├── pages/
│   ├── base_page.py             # Shared wait/interaction methods
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_address_page.py
│   ├── checkout_overview_page.py
│   └── checkout_success_page.py
├── tests/
│   ├── conftest.py              # Driver fixture, logged-in fixture, screenshot hook
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   ├── test_checkout_address_page.py
│   ├── test_checkout_overview_page.py
│   └── test_checkout_success_page.py
├── utils/
│   └── logger.py                # Structured file logger
├── reports/                     # Generated artifacts (gitignored)
├── requirements.in              # Direct dependencies
├── requirements.txt             # Pinned lockfile (pip-compile)
└── pytest.ini
```

---

## Features

- **Page Object Model** — each page is a class; tests never touch locators directly
- **BasePage** — centralised explicit waits, click, enter_text, get_text via `WebDriverWait`
- **Dynamic locators** — product buttons built from name slugs, no hardcoded IDs per product
- **Fixture chaining** — `driver` → `login_page` → `logged_in_user` → `item_in_cart`
- **Parametrized negative tests** — 6 invalid login scenarios in one test
- **Allure reporting** — feature, title, severity decorators on every test
- **Screenshot on failure** — captured automatically, attached to Allure and HTML report
- **Structured logging** — per-module loggers writing to `reports/logs/test.log`
- **Cross-browser** — Chrome and Firefox supported via `BROWSER` env var
- **CI/CD** — GitHub Actions runs the full suite headless on every push

---

## Setup

**1. Clone the repo**

```bash
git clone https://github.com/unaisLearning/selenium-python-framework.git
cd selenium-python-framework
```

**2. Create and activate a virtual environment**

```bash
python3.11 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

---

## Running Tests

**Run all tests**

```bash
pytest -v
```

**Run by marker**

```bash
pytest -v -m smoke
pytest -v -m regression
pytest -v -m negative
```

**Run a specific test file**

```bash
pytest tests/test_login.py -v
```

**Run with a different browser**

```bash
BROWSER=firefox pytest -v
```

---

## Allure Report

Allure results are written to `reports/allure-results` automatically (configured in `pytest.ini`).

To view the report locally:

```bash
allure serve reports/allure-results
```

---

## Environment Variables

| Variable | Default | Description |
|---|---|---|
| `SAUCEDEMO_USERNAME` | `standard_user` | Login username |
| `SAUCEDEMO_PASSWORD` | `secret_sauce` | Login password |
| `BROWSER` | `chrome` | Browser to run (`chrome` or `firefox`) |
| `CI` | unset | Set to `true` to enable headless mode |

---

## Test Coverage

| Area | Tests |
|---|---|
| Login | Valid login, 6 invalid scenarios (wrong credentials, empty fields, locked user) |
| Inventory | Page load, add to cart, remove from cart, cart badge, 4 sort filters |
| Cart | Page load, item presence, remove item, continue shopping |
| Checkout | Address form, overview data, order completion |
