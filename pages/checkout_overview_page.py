from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.checkout_success_page import CheckoutSuccessPage
from pages.inventory_page import InventoryPage
from utils.logger import get_logger

logger = get_logger(__name__)

class CheckoutOverviewPage(BasePage):

    #Locators
    TITLE = (By.CSS_SELECTOR, '[data-test="title"]')
    PRODUCTS_NAME = (By.CSS_SELECTOR, '[data-test="inventory-item-name"]')
    CANCEL_BUTTON = (By.ID, "cancel")
    FINISH_BUTTON = (By.ID, "finish")

    def get_title_name(self):
        logger.info(
            "Fetching title name"
        )
        return self.get_text(self.TITLE)

    def fetch_products_name(self):
        logger.info("Fetching products name")
        products  = self.find_elements(self.PRODUCTS_NAME)

        return [product.text for product in products]
    def cancel_order(self):
        self.click(self.CANCEL_BUTTON)
        return InventoryPage(self.driver)

    def finish_order(self):
        self.click(self.FINISH_BUTTON)
        return CheckoutSuccessPage(self.driver)
