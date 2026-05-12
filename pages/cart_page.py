from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger(__name__)
class CartPage(BasePage):

    #locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    CART_ITEM = (By.CSS_SELECTOR, "div.inventory_item_name")
    REMOVE_ITEM_BUTTON = (By.CSS_SELECTOR, "button[id^='remove-']")

    def get_page_title(self):
        logger.info("Fetching cart page title")
        return self.get_text(self.PAGE_TITLE)

    def get_added_item_name(self):
        logger.info("Fetching added item name to the cart")
        return self.get_text(self.CART_ITEM)

    def get_added_item_names(self):
        logger.info("Fetching all item names in cart")
        elements = self.driver.find_elements(*self.CART_ITEM)
        return [el.text for el in elements]

    def remove_item_from_cart(self):
        logger.info("Removing item from cart")

        self.wait.until(
            EC.element_to_be_clickable(self.REMOVE_ITEM_BUTTON)
        ).click()

    def continue_shopping(self):
        logger.info("Navigating to Products page by clicking continue shopping button")
        self.click(self.CONTINUE_SHOPPING_BUTTON)
        from pages.inventory_page import InventoryPage
        return InventoryPage(self.driver)

    def is_cart_empty(self):
        logger.info("Checking if cart is empty")
        elements = self.driver.find_elements(*self.CART_ITEM)
        return len(elements) == 0
