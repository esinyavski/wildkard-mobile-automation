import os
import logging

from datetime import datetime

from src.utils.data_parser import format_datetime


class Logger:

    log_to_console: bool = os.environ.get('LOG_TO_CONSOLE', True)
    log_to_file: bool = os.environ.get('LOG_TO_FILE', True)
    log_path = os.path.join(os.path.dirname(__file__),
                            f"../../output/log_{format_datetime(datetime.now())}.txt")
    debug: bool = os.environ.get('DEBUG', True)

    @classmethod
    def get_logger(cls, name=None):
        logger = logging.getLogger(name)

        if not len(logger.handlers):
            logger.setLevel(logging.DEBUG) if cls.debug else logger.setLevel(logging.INFO)
            log_formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt='%m/%d/%Y %I:%M:%S %p')

            if cls.log_to_console:
                console_handler = logging.StreamHandler()
                console_handler.setFormatter(log_formatter)
                logger.addHandler(console_handler)

            if cls.log_to_file:
                file_handler = logging.FileHandler(cls.log_path, encoding='utf-8')
                file_handler.setFormatter(log_formatter)
                logger.addHandler(file_handler)

        return logger
