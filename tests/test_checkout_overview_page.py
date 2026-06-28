from data.products import BACKPACK
from data.address import FIRST_NAME,LAST_NAME,ZIP_CODE

def test_checkout_overview_page_title(logged_in_user):
    logged_in_user.add_to_cart(BACKPACK)
    cart = logged_in_user.click_cart_icon()
    checkout = cart.checkout()
    checkout.fill_address_form(FIRST_NAME, LAST_NAME, ZIP_CODE)
    overview_page = checkout.proceed_to_overview_page()
    title = overview_page.get_title_name()

    assert title == "Checkout: Overview"

def test_overview_data(logged_in_user):
    logged_in_user.add_to_cart(BACKPACK)
    cart = logged_in_user.click_cart_icon()
    cart_products_list = cart.get_added_item_names()
    checkout = cart.checkout()
    checkout.fill_address_form(FIRST_NAME, LAST_NAME, ZIP_CODE)
    overview_page = checkout.proceed_to_overview_page()
    products = overview_page.fetch_products_name()

    assert cart_products_list == products

def test_cancel_order(logged_in_user):
    logged_in_user.add_to_cart(BACKPACK)
    cart = logged_in_user.click_cart_icon()
    checkout = cart.checkout()
    checkout.fill_address_form(FIRST_NAME, LAST_NAME, ZIP_CODE)
    overview_page = checkout.proceed_to_overview_page()
    overview_page.cancel_order()
    title = logged_in_user.get_page_title()

    assert title == "Products"

def test_finish_order(logged_in_user):
    logged_in_user.add_to_cart(BACKPACK)
    cart = logged_in_user.click_cart_icon()
    checkout = cart.checkout()
    checkout.fill_address_form(FIRST_NAME, LAST_NAME, ZIP_CODE)
    overview_page = checkout.proceed_to_overview_page()
    finish_page = overview_page.finish_order()
    title = finish_page.get_title()
