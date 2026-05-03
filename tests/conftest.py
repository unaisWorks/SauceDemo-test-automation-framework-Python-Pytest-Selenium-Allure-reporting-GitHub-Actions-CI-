import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options

import os
from datetime import datetime

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def login_page(driver):
    login_page = LoginPage(driver)
    login_page.open()
    return login_page

@pytest.fixture
def logged_in_user(login_page):
    return login_page.login("standard_user", "secret_sauce")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver") or \
                 getattr(item.funcargs.get("login_page", None), "driver", None) or \
                 getattr(item.funcargs.get("logged_in_user", None), "driver", None)

        if driver:
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            SCREENSHOT_DIR = os.path.join(BASE_DIR, "reports", "screenshots")

            os.makedirs(SCREENSHOT_DIR, exist_ok=True)

            file_name = f"{item.name}_{datetime.now().strftime('%H-%M-%S')}.png"
            file_path = os.path.join(SCREENSHOT_DIR, file_name)

            driver.save_screenshot(file_path)

            #Attach screenshot to report
            try:
                import pytest_html
                extra.append(pytest_html.extras.image(file_path))
            except Exception:
                pass

            report.extra = extra
