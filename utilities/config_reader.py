import configparser
import os


class ConfigReader:

    config = configparser.ConfigParser()

    config_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "config",
        "config.ini"
    )

    if not os.path.exists(config_path):
        raise FileNotFoundError(
            f"Config file not found: {config_path}"
        )

    config.read(config_path)

    @classmethod
    def get_value(cls, section, key):

        try:
            return cls.config.get(section, key)

        except Exception as e:
            raise Exception(
                f"Unable to read [{section}] {key}"
            ) from e

    @classmethod
    def get_url(cls):
        return cls.get_value("environment", "url")

    @classmethod
    def get_browser(cls):
        return cls.get_value("environment", "browser")

    @classmethod
    def get_timeout(cls):
        return cls.config.getint("environment", "timeout")

    @classmethod
    def get_implicit_wait(cls):
        return cls.config.getint(
            "environment",
            "implicit_wait"
        )