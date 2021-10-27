import os
import yaml
import logging

class AppConfig:
    get = None

    # Not thread-save. call this once in main py file when app is starting
    def load():
        AppConfig._validate_config_present()

        config_file = os.environ['APP_CONFIG_FILE']
        logging.info("Reading config from '%s'", config_file)
        with open(config_file) as cf:
            AppConfig.get = yaml.load(cf, Loader=yaml.FullLoader)
            logging.debug(AppConfig.get)
            AppConfig._validate_config_entries()

    def _validate_config_entries():
        logging.warning("TODO: config entries validation not implemented yet ;(")

    def _validate_config_present():
        if "APP_CONFIG_FILE" not in os.environ:
            logging.error("APP_CONFIG_FILE environment var not set")
            exit(1)

