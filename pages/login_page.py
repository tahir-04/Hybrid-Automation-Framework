from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    USERNAME = (
        By.NAME,
        "username"
    )

    PASSWORD = (
        By.NAME,
        "password"
    )

    LOGIN_BUTTON = (
        By.XPATH,
        "//button[@type='submit']"
    )

    ERROR_MESSAGE = (
    By.XPATH,
    "//p[contains(@class,'alert-content-text')]"
    )

    def enter_username(self, username):
        self.enter_text(
            self.USERNAME,
            username
        )

    def enter_password(self, password):
        self.enter_text(
            self.PASSWORD,
            password
        )

    def click_login(self):
        self.click(
            self.LOGIN_BUTTON
        )

    def login(self, username, password):

        self.enter_username(username)

        self.enter_password(password)

        self.click_login()

    def is_login_error_displayed(self):
        
        return self.is_displayed(
            self.ERROR_MESSAGE
        )