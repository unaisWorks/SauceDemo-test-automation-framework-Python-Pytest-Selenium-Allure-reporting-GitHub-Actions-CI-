from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.checkout_address_page import CheckoutAddressPage
from utils.logger import get_logger

logger = get_logger(__name__)


class CartPage(BasePage):
    #Locators
    PAGE_TITLE = (By.CLASS_NAME,"title")
    CONTINUE_SHOPPING_BUTTON = (By.ID,"continue-shopping")
    CART_ITEM = (By.CSS_SELECTOR,"div.inventory_item_name")
    REMOVE_ITEM_BUTTON = (By.CSS_SELECTOR,"button[id^='remove-']")
    CHECKOUT = (By.ID, "checkout")

    def get_page_title(self):

        logger.info(
            "Fetching cart page title"
        )

        return self.get_text(
            self.PAGE_TITLE
        )

    def get_added_item_name(self):

        logger.info(
            "Fetching added item name"
        )

        return self.get_text(
            self.CART_ITEM
        )

    def get_added_item_names(self):

        logger.info(
            "Fetching all item names in cart"
        )

        elements = self.find_elements(
            *self.CART_ITEM
        )

        return [
            element.text
            for element in elements
        ]

    def remove_item_from_cart(self):

        logger.info(
            "Removing item from cart"
        )

        self.click(
            self.REMOVE_ITEM_BUTTON
        )

        self.wait.until(
            lambda driver:
            len(
                driver.find_elements(
                    *self.CART_ITEM
                )
            ) == 0
        )

    def continue_shopping(self):

        logger.info(
            "Navigating back to inventory page"
        )

        self.click(
            self.CONTINUE_SHOPPING_BUTTON
        )

        from pages.inventory_page import (
            InventoryPage
        )

        return InventoryPage(
            self.driver
        )

    def is_cart_empty(self):

        logger.info(
            "Checking if cart is empty"
        )

        elements = self.find_elements(
            *self.CART_ITEM
        )

        return len(elements) == 0

    def checkout(self):
        logger.info("Checking out and move to address page")
        self.click(self.CHECKOUT)
        return CheckoutAddressPage(self.driver)

