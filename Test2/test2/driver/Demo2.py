import logging

from test2.utils.Constants import Constants
from test2.bl.SubtractNumbers import SubtractNumbers


class Demo2:
    def __init__(self):
        self.logger = logging.getLogger(Constants.LOGGER_NAME)

    @staticmethod
    def perform_subtraction(x, y):
        SubtractNumbers.subtract(x, y)
