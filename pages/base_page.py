from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator, timeout=10):
        element = WebDriverWait(
            self.driver,
            timeout
        ).until(
            EC.element_to_be_clickable(locator)
        )

        element.click()

    def enter_text(self, locator, text, timeout=10):
        element = WebDriverWait(
            self.driver,
            timeout
        ).until(
            EC.visibility_of_element_located(locator)
        )

        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=10):
        element = WebDriverWait(
            self.driver,
            timeout
        ).until(
            EC.visibility_of_element_located(locator)
        )

        return element.text

    def is_displayed(self, locator, timeout=10):
        try:
            WebDriverWait(
                self.driver,
                timeout
            ).until(
                EC.visibility_of_element_located(locator)
            )

            return True

        except:
            return False