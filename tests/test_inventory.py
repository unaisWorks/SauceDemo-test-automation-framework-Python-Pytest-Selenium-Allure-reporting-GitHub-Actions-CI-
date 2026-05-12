from coverage.files import actual_path


def test_page_title(logged_in_user):
    assert logged_in_user.get_page_title() == "Products"

def test_add_single_item_to_cart(logged_in_user):
    before = logged_in_user.get_cart_count() if logged_in_user.is_cart_badge_displayed() else "0"
    logged_in_user.add_to_cart()
    after = logged_in_user.get_cart_count()
    assert int(after) == int(before) + 1
    # Verify correct item name
    cart = logged_in_user.click_cart_icon()
    assert cart.get_added_item_name() == "Sauce Labs Backpack"

def test_remove_item_from_cart(logged_in_user):
    logged_in_user.add_to_cart()
    logged_in_user.remove_item_from_cart()
    assert not logged_in_user.is_cart_badge_displayed()

def test_logout(logged_in_user):
    login_page = logged_in_user.logout_account()
    assert login_page.driver.title == "Swag Labs"

def test_filter_price_low_to_high(logged_in_user):
    logged_in_user.sort_products("lohi")

    actual = logged_in_user.get_product_prices()
    assert actual == sorted(actual)

def test_filter_price_high_to_low(logged_in_user):
    logged_in_user.sort_products("hilo")

    actual = logged_in_user.get_product_prices()
    assert actual == sorted(actual, reverse=True)

def test_filter_price_A_to_Z(logged_in_user):
    logged_in_user.sort_products("az")
    assert logged_in_user.get_current_sort_value() == "az"

def test_filter_price_Z_to_A(logged_in_user):
    logged_in_user.sort_products("za")
    assert logged_in_user.get_current_sort_value() == "za"

