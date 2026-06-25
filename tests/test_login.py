import pytest
import allure
from config.config import USERNAME, PASSWORD


@pytest.mark.regression
@pytest.mark.smoke
@allure.feature("Login")
@allure.title("Verify Successful Login")
@allure.severity(allure.severity_level.CRITICAL)
def test_successful_login(login_page):
    inventory = login_page.login(USERNAME,PASSWORD)
    title = inventory.get_page_title()
    assert title == "Products"

@pytest.mark.regression
@allure.feature("Login")
@allure.title("Verify Login Page URL")
@allure.severity(allure.severity_level.NORMAL)
def test_page_url(login_page):
    page_url = login_page.get_current_url()
    assert page_url == "https://www.saucedemo.com/"

@pytest.mark.regression
@pytest.mark.negative
@pytest.mark.parametrize(
    "username,password,expected_error",
    [
        ("wrong_user","secret_sauce",
         "Epic sadface: Username and password do not match any user in this service"),

        ("standard_user","wrong_password",
         "Epic sadface: Username and password do not match any user in this service"),

        ("","secret_sauce",
         "Epic sadface: Username is required"),

        ("standard_user","",
         "Epic sadface: Password is required"),

        ("","",
         "Epic sadface: Username is required"),

        ("locked_out_user","secret_sauce",
         "Epic sadface: Sorry, this user has been locked out."),
    ],
    ids=[
        "invalid_username",
        "invalid_password",
        "empty_username",
        "empty_password",
        "empty_username_and_password",
        "locked_user"

    ],
)
@pytest.mark.regression
@pytest.mark.negative
@allure.feature("Login")
@allure.title("Verify Invalid Login Scenarios")
@allure.severity(allure.severity_level.MINOR)
def test_invalid_login(login_page, username, password, expected_error):
    login_page.open()
    login_page.attempt_login(username, password)
    error_message = login_page.get_error_message()
    assert error_message == expected_error

@pytest.mark.regression
@pytest.mark.negative
@allure.feature("Login")
@allure.title("Verify Error Message Displayed")
@allure.severity(allure.severity_level.CRITICAL)
def test_find_error_message_element(login_page):
    login_page.attempt_login("locked_out_user", "secret_sauce")
    element = login_page.find_element(login_page.ERROR_SECTION)
    assert element.is_displayed()
