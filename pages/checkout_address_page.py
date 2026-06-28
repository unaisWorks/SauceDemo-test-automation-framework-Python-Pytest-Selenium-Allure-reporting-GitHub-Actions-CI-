from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.checkout_overview_page import CheckoutOverviewPage
from utils.logger import get_logger

logger = get_logger(__name__)


class CheckoutAddressPage(BasePage):
    #Locators
    TITLE = (By.CSS_SELECTOR, '[data-test="title"]')
    FIRST_NAME_LOCATOR = (By.ID, "first-name")
    LAST_NAME_LOCATOR = (By.ID, "last-name")
    ZIP_CODE_LOCATOR = (By.ID, "postal-code")
    CANCEL_BUTTON = (By.ID, "cancel")
    CONTINUE_BUTTON = (By.ID, "continue")


    def get_title_name(self):
        logger.info(
            "Fetching title name"
        )
        return self.get_text(self.TITLE)

    def fill_address_form(self, FIRST_NAME,LAST_NAME,ZIP_CODE):
        logger.info("filling delivery address form")
        self.enter_text(self.FIRST_NAME_LOCATOR,FIRST_NAME)
        self.enter_text(self.LAST_NAME_LOCATOR, LAST_NAME)
        self.enter_text(self.ZIP_CODE_LOCATOR, ZIP_CODE)

    def proceed_to_overview_page(self):
        logger.info("Proceed to checkout overview page")
        self.click(self.CONTINUE_BUTTON)
        return CheckoutOverviewPage(self.driver)

