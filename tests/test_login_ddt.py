import pytest

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

from utilities.data_provider import DataProvider


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.parametrize(
    "username,password",
    DataProvider.get_login_data()
)
def test_login_ddt(
        driver,
        username,
        password):

    login_page = LoginPage(driver)

    login_page.login(
        username,
        password
    )