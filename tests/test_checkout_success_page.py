
from data.address import first_name, last_name, zip_code
from data.products import BACKPACK


def test_checkout_success_page_title(logged_in_user):
    logged_in_user.add_to_cart(BACKPACK)
    cart = logged_in_user.click_cart_icon()
    checkout = cart.checkout()
    checkout.fill_address_form(first_name, last_name, zip_code)
    overview_page = checkout.proceed_to_overview_page()
    success_page = overview_page.finish_order()
    title = success_page.get_title()

    assert title == "Checkout: Complete!"

def test_success_message_content(logged_in_user):
    logged_in_user.add_to_cart(BACKPACK)
    cart = logged_in_user.click_cart_icon()
    checkout = cart.checkout()
    checkout.fill_address_form(first_name, last_name, zip_code)
    overview_page = checkout.proceed_to_overview_page()
    success_page = overview_page.finish_order()
    success_message = success_page.fetch_success_message()

    assert success_message == "Thank you for your order!"