import pytest

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@pytest.mark.smoke
@pytest.mark.functional
def test_valid_login(driver):

    login_page = LoginPage(driver)

    dashboard_page = DashboardPage(driver)

    login_page.login(
        "Admin",
        "admin123"
    )

    assert dashboard_page.is_dashboard_displayed()