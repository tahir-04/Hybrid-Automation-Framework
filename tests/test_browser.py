import pytest

@pytest.mark.smoke
def test_launch_browser(driver):

    print(driver.current_url)

    assert "orangehrm" in driver.current_url.lower()