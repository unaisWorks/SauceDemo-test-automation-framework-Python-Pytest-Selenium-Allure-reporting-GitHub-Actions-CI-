from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger(__name__)


class InventoryPage(BasePage):
    #Locators
    PAGE_TITLE = (By.CSS_SELECTOR, '[data-test="title"]')
    ADD_TO_CART_BUTTON = (By.ID,"add-to-cart-sauce-labs-backpack")
    REMOVE_FROM_CART_BUTTON = (By.ID,"remove-sauce-labs-backpack")
    CART_ICON = (By.CSS_SELECTOR,"a.shopping_cart_link")
    CART_COUNT_BADGE = (By.CSS_SELECTOR,"span.shopping_cart_badge")
    MENU_ICON = (By.ID,"react-burger-menu-btn")
    LOGOUT_LINK = (By.ID,"logout_sidebar_link")
    SORT_DROPDOWN = (By.CSS_SELECTOR,"select.product_sort_container")
    PRODUCT_PRICES = (By.CLASS_NAME,"inventory_item_price")

    def get_page_title(self):
        logger.info("Fetching inventory page title")
        return self.get_text(self.PAGE_TITLE)

    def get_add_to_cart_button(self, product):
        slug = product.lower().replace(" " , "-")
        return (By.ID, f"add-to-cart-" + slug)

    def get_remove_product_button(self, product):
        slug = product.lower().replace(" ", "-")
        return (By.ID, f"remove-" + slug)

    def add_to_cart(self, product):
        logger.info("Adding item to cart")
        self.click(self.get_add_to_cart_button(product))
        logger.info(
            "Item successfully added to cart."
        )

    def get_cart_count(self):

        logger.info("Fetching cart count")

        try:
            return self.get_text(
                self.CART_COUNT_BADGE
            )

        except TimeoutException:
            return "0"

    def remove_item_from_cart(self, product):
        logger.info("Removing item from cart")

        self.click(self.get_remove_product_button(product))


    def is_cart_badge_displayed(self):

        try:
            return self.find_element(
                self.CART_COUNT_BADGE
            ).is_displayed()

        except TimeoutException:
            return False

    def click_cart_icon(self):

        logger.info(
            "Navigating to cart page"
        )

        self.click(self.CART_ICON)

        from pages.cart_page import CartPage

        cart_page = CartPage(self.driver)

        cart_page.wait.until(
            EC.visibility_of_element_located(
                cart_page.PAGE_TITLE
            )
        )

        return cart_page

    def open_menu(self):

        logger.info("Opening menu")

        self.click(self.MENU_ICON)

    def logout_account(self):

        logger.info("Logging out user")

        self.open_menu()

        self.click(self.LOGOUT_LINK)

        from pages.login_page import LoginPage

        return LoginPage(self.driver)

    def sort_products(self, sort_option):

        logger.info(
            f"Sorting products by {sort_option}"
        )

        dropdown = Select(
            self.find_element(
                self.SORT_DROPDOWN
            )
        )

        dropdown.select_by_value(sort_option)

    def get_current_sort_value(self):

        logger.info(
            "Getting current sort value"
        )

        dropdown = Select(
            self.find_element(
                self.SORT_DROPDOWN
            )
        )

        return dropdown.first_selected_option.get_attribute(
            "value"
        )

    def get_product_prices(self):

        prices = self.find_elements(
            self.PRODUCT_PRICES
        )

        return [
            float(
                price.text.replace("$", "")
            )
            for price in prices
        ]