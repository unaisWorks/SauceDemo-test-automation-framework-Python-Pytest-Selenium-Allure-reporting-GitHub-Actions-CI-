from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage

class InventoryPage(BasePage):

    #Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    ADD_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_ITEM_BUTTON = (By.ID, "remove-sauce-labs-backpack")

    CART_ICON = (By.CSS_SELECTOR, "a.shopping_cart_link")
    CART_COUNT_BADGE = (By.CSS_SELECTOR,  "span.shopping_cart_badge")

    MENU_ICON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    SORT_DROPDOWN = (By.CSS_SELECTOR, "select.product_sort_container")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")

    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    def add_to_cart(self):
        self.click(self.ADD_CART_BUTTON)
        self.wait.until(EC.presence_of_element_located(self.CART_COUNT_BADGE))

    def get_cart_count(self):
        try:
            return self.get_text(self.CART_COUNT_BADGE)
        except:
            return "0"

    def remove_item_from_cart(self):
        self.click(self.REMOVE_ITEM_BUTTON)

    def is_cart_badge_displayed(self):
        try:
            return self.find_element(self.CART_COUNT_BADGE).is_displayed()
        except Exception:
            return False

    def click_cart_icon(self):
        self.click(self.CART_ICON)
        from pages.cart_page import CartPage
        return CartPage(self.driver)

    def open_menu(self):
        self.click(self.MENU_ICON)

    def logout_account(self):
        self.open_menu()
        self.click(self.LOGOUT_LINK)
        from pages.login_page import LoginPage
        return LoginPage(self.driver)

    def sort_products(self, sort_option):
        """
        Sort products by option
        Options: 'az' (A-Z), 'za' (Z-A), 'lohi' (low to high), 'hilo' (high to low)
        """
        dropdown = Select(self.find_element(self.SORT_DROPDOWN))
        dropdown.select_by_value(sort_option)

    def get_current_sort_value(self):
        """Get currently selected sort option"""
        dropdown = Select(self.find_element(self.SORT_DROPDOWN))
        return dropdown.first_selected_option.get_attribute("value")