from data.products import BACKPACK
from data.address import FIRST_NAME,LAST_NAME,ZIP_CODE

def test_checkout_address_page_title(logged_in_user):

    logged_in_user.add_to_cart(BACKPACK)
    cart = logged_in_user.click_cart_icon()

    checkout = cart.checkout()
    title = checkout.get_title_name()

    assert title == "Checkout: Your Information"

def test_succesfull_checkout_flow(logged_in_user):
    logged_in_user.add_to_cart(BACKPACK)
    cart = logged_in_user.click_cart_icon()
    checkout = cart.checkout()
    checkout.fill_address_form(FIRST_NAME,LAST_NAME,ZIP_CODE)
    overview = checkout.proceed_to_overview_page()
    overview_page_title = overview.get_title_name()
    assert overview_page_title == "Checkout: Overview"