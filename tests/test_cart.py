
def test_verify_cart_page_loaded(logged_in_user):
    cart = logged_in_user.click_cart_icon()
    assert  cart.get_page_title() == "Your Cart"

def test_continue_shopping_button(logged_in_user):
    cart = logged_in_user.click_cart_icon()
    inventory = cart.continue_shopping()
    assert inventory.get_page_title() == "Products"

def test_item_appear_in_cart(logged_in_user):
    logged_in_user.add_to_cart()
    cart = logged_in_user.click_cart_icon()

    assert cart.get_added_item_name() == "Sauce Labs Backpack"

def test_item_remove_from_cart(logged_in_user):
    logged_in_user.add_to_cart()
    cart = logged_in_user.click_cart_icon()

    cart.remove_item_from_cart()

    assert cart.is_cart_empty()

    inventory = cart.continue_shopping()
    assert not inventory.is_cart_badge_displayed()




