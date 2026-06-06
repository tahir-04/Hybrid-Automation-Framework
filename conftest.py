import pytest
import pytest_html

from utilities.config_reader import ConfigReader
from utilities.browser_factory import BrowserFactory
from utilities.logger import get_logger

from utilities.screenshot_util import ScreenshotUtil

from pytest_metadata.plugin import metadata_key

log = get_logger()


@pytest.fixture(scope="function")
def driver():

    browser = ConfigReader.get_browser()

    log.info(f"Launching {browser}")

    driver = BrowserFactory.get_browser(browser)

    url = ConfigReader.get_url()

    log.info(f"Opening URL: {url}")

    driver.get(url)

    yield driver

    log.info("Closing Browser")

    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(

        item,
        call):
    
    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get(
            "driver"
        )

        if driver:

           path = ScreenshotUtil.capture(
                driver,
                item.name
            )
           
           extra = getattr(
               
                report,
                "extras",
                []
        )

        extra.append(
            pytest_html.extras.png(
                path
            )
        )

        report.extras = extra

def pytest_html_report_title(report):

    report.title = (
        "Hybrid Automation Framework Report"
    )

def pytest_configure(config):

    config.stash[
        metadata_key
    ]["Project"] = (
        "Hybrid Automation Framework"
    )

    config.stash[
        metadata_key
    ]["Tester"] = (
        "Mohamed Tahir"
    )

    config.stash[
        metadata_key
    ]["Framework"] = (
        "Selenium-PyTest"
    )

    