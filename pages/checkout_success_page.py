from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger(__name__)

class CheckoutSuccessPage(BasePage):
    TITLE = (By.CSS_SELECTOR, '[data-test="title"]')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '[data-test="complete-header"]')

    def get_title(self):
        logger.info(
            "Fetching title name"
        )
        return self.get_text(self.TITLE)

    def fetch_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)