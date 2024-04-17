"""
Assorted utilities for the project
"""
import logging
import sys
from logging import Logger
from typing import Optional, List

from common.constants import DEFAULT_LOG_FORMAT, PROJECT_NAME


class DefaultLogger:
    """
    Having a class is a bit convoluted, but necessary since logging kept failing when I initialized
    the log from endpoints.py without a wrapper class. My theory is that this happened because I needed to add state
    """

    def __init__(
            self,
            logger_name: Optional[str] = PROJECT_NAME,
            use_file: Optional[bool] = False,
            filename: Optional[str] = ""
    ):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(DEFAULT_LOG_FORMAT)

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)

        self.logger.addHandler(console_handler)
        if use_file:
            log_filename = f"{filename if filename else 'default'}.log"
            file_handler = logging.FileHandler(f"/app/resources/{log_filename}")
            file_handler.setFormatter(formatter)
            file_handler.setLevel(logging.DEBUG)
            self.logger.addHandler(file_handler)

    def get_logger(self) -> Logger:
        return self.logger


def batches(items: list, size: int) -> List[list]:
    """
    Utility method to break lists into batches

    Args:
        items: Input list to be split
        size: The size of each chunk (last chunk can be smaller)
    Returns:
        list of lists, each containing sub-elements of requested size
    """
    if size <= 0:
        raise ValueError("Less or equal to zero? Seriously dude?")

    i = 0
    while i < len(items):
        yield list(items[i:i + size])
        i = i + size
