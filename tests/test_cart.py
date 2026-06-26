import allure
import pytest
from data.products import BACKPACK


@pytest.mark.regression
@allure.feature("Cart")
@allure.title("Verify Cart Page Loaded Successfully")
@allure.severity(allure.severity_level.CRITICAL)
def test_verify_cart_page_loaded(logged_in_user):
    cart = logged_in_user.click_cart_icon()
    assert  cart.get_page_title() == "Your Cart"

@pytest.mark.regression
@allure.feature("Cart")
@allure.title("Verify continue shopping button works")
@allure.severity(allure.severity_level.NORMAL)
def test_continue_shopping_button(logged_in_user):
    cart = logged_in_user.click_cart_icon()
    inventory = cart.continue_shopping()
    assert inventory.get_page_title() == "Products"

@pytest.mark.regression
@allure.feature("Cart")
@allure.title("Verify Item Displayed in Cart")
@allure.severity(allure.severity_level.CRITICAL)
def test_item_appears_in_cart(item_in_cart):
    cart = item_in_cart.click_cart_icon()
    assert cart.get_added_item_name() == BACKPACK

@pytest.mark.smoke
@pytest.mark.regression
@allure.feature("Cart")
@allure.title("Verify item removed from cart")
@allure.severity(allure.severity_level.CRITICAL)
def test_remove_button_on_cart(logged_in_user):
    logged_in_user.add_to_cart(BACKPACK)
    cart = logged_in_user.click_cart_icon()

    cart.remove_item_from_cart()

    assert cart.is_cart_empty()

    inventory = cart.continue_shopping()
    assert not inventory.is_cart_badge_displayed()




