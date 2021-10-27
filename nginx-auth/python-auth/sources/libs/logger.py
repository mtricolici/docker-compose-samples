import os
import sys
import logging

class AppLogger:
    def initialize():
        log_level = AppLogger._get_log_level()
        logging.basicConfig(format='%(levelname)s:%(asctime)s: %(message)s', level=log_level)

    def _get_log_level():
        if "LOG_LEVEL" not in os.environ:
            return "INFO" # default log level
        level = os.environ['LOG_LEVEL']
        if level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            # Cannot use logger before logging.basicConfig invokation
            print("!!!bad value in LOG_LEVEL env var. Fallback to default value: INFO", file=sys.stderr)
            return "INFO"
        return level
