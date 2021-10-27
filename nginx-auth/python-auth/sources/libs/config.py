import os
import yaml

class AppConfig:
    get = None

    # Not thread-save. call this once in main py file when app is starting
    def load():
        AppConfig._validate_config_present()

        config_file = os.environ['APP_CONFIG_FILE']
        print("Reading config from '{}'".format(config_file))
        with open(config_file) as cf:
            AppConfig.get = yaml.load(cf, Loader=yaml.FullLoader)
            print(AppConfig.get) # debug. TODO: use a logger with logLevel
            AppConfig._validate_config_entries()

    def _validate_config_entries():
        print("TODO: config entries validation not implemented yet ;(")

    def _validate_config_present():
        print("Loading application configuration")
        if "APP_CONFIG_FILE" not in os.environ:
            print("Error: APP_CONFIG_FILE environment var not set")
            exit(1)

