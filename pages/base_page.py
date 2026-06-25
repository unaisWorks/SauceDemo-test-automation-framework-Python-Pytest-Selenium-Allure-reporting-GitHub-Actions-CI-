from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from config.config import TIMEOUT

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUT)

    def get_current_url(self):
        return self.driver.current_url

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def is_element_visible(self, locator):
        try:
            return self.find_element(locator).is_displayed()
        except TimeoutException:
            return False

    def wait_for_element_to_disappear(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))

    def click(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    def wait_for_visibility(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    def get_elements_text(self, locator):
        elements = self.find_elements(locator)
        return [el.text for el in elements]

    def clear_field(self, locator):
        self.find_element(locator).clear()

    def is_element_enabled(self, locator):
        return self.find_element(locator).is_enabled()
