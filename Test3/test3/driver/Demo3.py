import logging

from test3.utils.Constants import Constants
from test3.bl.MultiplyNumbers import MultiplyNumbers


class Demo3:
    def __init__(self):
        self.logger = logging.getLogger(Constants.LOGGER_NAME)

    @staticmethod
    def perform_multiplication(x, y):
        MultiplyNumbers.multiply(x, y)
