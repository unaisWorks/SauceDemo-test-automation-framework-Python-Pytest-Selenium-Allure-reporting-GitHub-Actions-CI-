# 🚀 Selenium Pytest Automation Framework

## 📌 Overview

This project is a **UI automation testing framework** built using **Selenium, Python, and Pytest** following the **Page Object Model (POM)** design pattern.

It demonstrates a scalable and maintainable automation structure with features like reusable fixtures, parametrized tests, HTML reporting, and automatic screenshot capture on failures.

---

## 🛠 Tech Stack

* Python
* Selenium WebDriver
* Pytest
* pytest-html

---

## 📁 Project Structure

```
Python_Automation_template/
│
├── pages/                # Page Object Models
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
│
├── tests/                # Test files
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_inventory.py
│   └── test_cart.py
│
├── reports/              # Test reports & screenshots
│   ├── report.html
│   └── screenshots/
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Features

✔ Page Object Model (POM)
✔ Pytest Fixtures for setup/teardown
✔ Parametrized tests (`@pytest.mark.parametrize`)
✔ HTML test reports
✔ Automatic screenshot capture on test failure
✔ Screenshots embedded in HTML report
✔ Clean and maintainable structure

---

## ▶️ How to Run Tests

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run tests with HTML report

```bash
pytest -v --html=reports/report.html --self-contained-html
```

---

## 📸 Reporting & Screenshots

* HTML report is generated at:

```
reports/report.html
```

* Screenshots are captured automatically on failure:

```
reports/screenshots/
```

* Failed test screenshots are embedded inside the HTML report for easy debugging.

---

## 🧪 Test Coverage

### 🔐 Login Tests

* Valid login
* Invalid username/password
* Empty fields
* Locked user

### 🛒 Inventory Tests

* Add item to cart
* Remove item from cart
* Cart badge validation
* Product sorting

### 🧺 Cart Tests

* Cart page validation
* Continue shopping flow
* Item presence in cart
* Remove item from cart

---

## 💡 Key Concepts Demonstrated

* Page Object Model (POM)
* Fixture dependency chaining
* Data-driven testing with Pytest
* Explicit waits for stability
* Clean test design & reusability

---

## 🚀 Future Improvements

* Logging integration
* Cross-browser testing
* CI/CD integration (GitHub Actions)
* API testing integration

---

## 👨‍💻 Author

Automation framework developed as part of learning and building a professional QA portfolio.

---
