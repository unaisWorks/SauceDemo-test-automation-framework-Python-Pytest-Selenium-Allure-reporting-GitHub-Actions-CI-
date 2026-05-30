import os
import tempfile
from datetime import datetime

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config.config import USERNAME, PASSWORD
from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def driver():

    options = Options()

    temp_profile = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={temp_profile}")

    # options.add_argument("--headless=new")
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")

    # Disable Chrome password manager & breach detection popup
    options.add_argument("--disable-features=PasswordLeakDetection")

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
        "profile.default_content_setting_values.notifications": 2
    }

    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(30)

    yield driver

    driver.quit()


@pytest.fixture(scope="function")
def login_page(driver):
    login_page = LoginPage(driver)
    login_page.open()
    return login_page


@pytest.fixture
def logged_in_user(login_page):
    return login_page.login(USERNAME, PASSWORD)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    extras = getattr(report, "extras", [])

    if report.when == "call" and report.failed:

        driver = (
            item.funcargs.get("driver")
            or getattr(item.funcargs.get("login_page", None), "driver", None)
            or getattr(item.funcargs.get("logged_in_user", None), "driver", None)
        )

        if driver:

            base_dir = os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))
            )

            screenshot_dir = os.path.join(
                base_dir,
                "reports",
                "screenshots"
            )

            os.makedirs(screenshot_dir, exist_ok=True)

            file_name = (
                f"{item.name}_"
                f"{datetime.now().strftime('%H-%M-%S')}.png"
            )

            file_path = os.path.join(
                screenshot_dir,
                file_name
            )

            driver.save_screenshot(file_path)

            print(
                f"Capturing screenshot for failed test: {item.name}"
            )

            allure.attach(
                driver.get_screenshot_as_png(),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            try:
                import pytest_html

                extras.append(
                    pytest_html.extras.image(file_path)
                )

            except ImportError:
                pass

            report.extras = extras