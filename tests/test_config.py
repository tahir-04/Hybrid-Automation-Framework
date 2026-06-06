from utilities.config_reader import ConfigReader


def test_read_config():

    print("URL :", ConfigReader.get_url())
    print("Browser :", ConfigReader.get_browser())
    print("Timeout :", ConfigReader.get_timeout())