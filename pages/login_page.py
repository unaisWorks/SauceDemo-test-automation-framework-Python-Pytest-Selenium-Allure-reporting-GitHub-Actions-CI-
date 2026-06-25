from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from utils.logger import get_logger
from config.config import BASE_URL
from selenium.webdriver.support import expected_conditions as EC


logger = get_logger(__name__)
class LoginPage(BasePage):

    #Locators
    USER_NAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_SECTION = (By.CSS_SELECTOR, "h3[data-test='error']")
    PAGE_TITLE = (By.CLASS_NAME, "login_logo")

    def open(self):
        logger.info("opening login page")
        self.driver.get(BASE_URL)

    def _fill_credentials(self,username, password):

        self.clear_field(self.USER_NAME_FIELD)
        self.clear_field(self.PASSWORD_FIELD)
        self.enter_text(self.USER_NAME_FIELD, username)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        logger.info(f"Logging in as {username}")
        self._fill_credentials(username, password)
        from pages.inventory_page import InventoryPage
        inventory = InventoryPage(self.driver)
        inventory.wait_for_visibility(inventory.PAGE_TITLE)
        return inventory

    def attempt_login(self, username, password):
        logger.info(f"Logging in as {username}")
        self._fill_credentials(username,password)
        return self

    def get_error_message(self):
        element = self.wait.until(
            EC.visibility_of_element_located(self.ERROR_SECTION)
        )
        return element.text.strip()

