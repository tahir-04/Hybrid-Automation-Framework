from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DashboardPage(BasePage):

    DASHBOARD_HEADER = (
        By.XPATH,
        "//h6[text()='Dashboard']"
    )

    def is_dashboard_displayed(self):

        return self.is_displayed(
            self.DASHBOARD_HEADER
        )