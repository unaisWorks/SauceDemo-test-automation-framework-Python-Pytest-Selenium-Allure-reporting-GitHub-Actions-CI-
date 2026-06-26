import allure
import pytest
from data.products import BACKPACK

@pytest.mark.regression
@allure.feature("Inventory Page")
@allure.title("Verify Inventory Page Loaded Successfully")
@allure.severity(allure.severity_level.CRITICAL)
def test_page_title(logged_in_user):
    assert logged_in_user.get_page_title() == "Products"

@pytest.mark.regression
@allure.feature("Inventory Page")
@allure.title("Verify Inventory page URL")
@allure.severity(allure.severity_level.CRITICAL)
def test_page_url(logged_in_user):
    page_url = logged_in_user.get_current_url()
    assert "inventory" in page_url

@pytest.mark.regression
@allure.feature("Inventory Page")
@allure.title("Verify add to cart button enabled")
@allure.severity(allure.severity_level.MINOR)
def test_add_to_cart_button_enabled(logged_in_user):
    assert logged_in_user.is_element_enabled(
        logged_in_user.ADD_TO_CART_BUTTON
    )
@pytest.mark.smoke
@pytest.mark.regression
@allure.feature("Inventory Page")
@allure.title("Verify item add to cart")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_single_item_to_cart(logged_in_user):
    logged_in_user.add_to_cart(BACKPACK)
    assert logged_in_user.get_cart_count() == "1"
    # Verify correct item name
    cart = logged_in_user.click_cart_icon()
    assert cart.get_added_item_name() == BACKPACK

@pytest.mark.smoke
@pytest.mark.regression
@allure.feature("Inventory Page")
@allure.title("Verify item removed from cart")
@allure.severity(allure.severity_level.CRITICAL)
def test_remove_button_on_inventory(logged_in_user):
    logged_in_user.add_to_cart(BACKPACK)
    logged_in_user.remove_item_from_cart(BACKPACK)
    assert not logged_in_user.is_cart_badge_displayed()

@pytest.mark.regression
@allure.feature("Inventory Page")
@allure.title("Verify account logged out")
@allure.severity(allure.severity_level.CRITICAL)
def test_logout(logged_in_user):
    login_page = logged_in_user.logout_account()
    assert login_page.driver.title == "Swag Labs"

@pytest.mark.regression
@allure.feature("Inventory Page")
@allure.title("Verify filter price low to high as expected")
@allure.severity(allure.severity_level.NORMAL)
def test_filter_price_low_to_high(logged_in_user):
    logged_in_user.sort_products("lohi")

    actual = logged_in_user.get_product_prices()
    assert actual == sorted(actual)

@pytest.mark.regression
@allure.feature("Inventory Page")
@allure.title("Verify filter price high to low")
@allure.severity(allure.severity_level.NORMAL)
def test_filter_price_high_to_low(logged_in_user):
    logged_in_user.sort_products("hilo")

    actual = logged_in_user.get_product_prices()
    assert actual == sorted(actual, reverse=True)

@pytest.mark.regression
@allure.feature("Inventory Page")
@allure.title("Verify filter alphabetic A to Z")
@allure.severity(allure.severity_level.NORMAL)
def test_filter_price_A_to_Z(logged_in_user):
    logged_in_user.sort_products("az")
    actual = logged_in_user.get_product_names()
    assert actual == sorted(actual)

@pytest.mark.regression
@allure.feature("Inventory Page")
@allure.title("Verify filter alphabetic order Z to A")
@allure.severity(allure.severity_level.NORMAL)
def test_filter_price_Z_to_A(logged_in_user):
    logged_in_user.sort_products("za")
    actual = logged_in_user.get_product_names()
    assert actual == sorted(actual, reverse=True)

