from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from utils.logger import get_logger
from config.config import BASE_URL,USERNAME,PASSWORD
from selenium.webdriver.support import expected_conditions as EC
from config.config import TIMEOUT

logger = get_logger(__name__)
class LoginPage(BasePage):

    #Locators
    USER_NAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_SECTION = (By.CSS_SELECTOR, "h3[data-test='error']")

    def open(self):
        logger.info("opening login page")
        self.driver.get(BASE_URL)

    def login(self, username, password):
        self.find_element(self.USER_NAME_FIELD).clear()
        self.find_element(self.PASSWORD_FIELD).clear()

        self.enter_text(self.USER_NAME_FIELD, username)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)

        from pages.inventory_page import InventoryPage
        return InventoryPage(self.driver)

    def get_error_message(self):
        element = self.wait.until(
            EC.visibility_of_element_located(self.ERROR_SECTION)
        )
        return element.text.strip()

