import pytest

def test_successful_login(login_page):
    inventory = login_page.login("standard_user","secret_sauce")
    assert inventory.get_page_title() == "Products"

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

def test_invalid_login(login_page, username, password, expected_error):
    login_page.open()   # ✅ RESET PAGE EVERY ITERATION
    login_page.login(username, password)
    error_message = login_page.get_error_message()
    assert error_message == expected_error

def test_find_error_message_element(login_page):
    login_page.login("locked_out_user", "secret_sauce")
    element = login_page.find_element(login_page.ERROR_SECTION)
    assert element.is_displayed()
