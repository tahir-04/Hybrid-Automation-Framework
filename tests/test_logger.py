from utilities.Logger.logger import get_logger

log = get_logger()

def test_logger():

    log.info("Browser Opened")

    log.info("Login Started")

    log.success("Login Successful")