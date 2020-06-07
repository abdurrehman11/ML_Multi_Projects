import logging

from test3.utils.Constants import Constants


class Demo3:
    def __init__(self):
        self.logger = logging.getLogger(Constants.LOGGER_NAME)

    def mul(self, x, y):
        self.logger.info(f'Going to multiply {x} and {y}.')
        multiplication = x * y
        self.logger.info(f'Multiplied {x} and {y} successfully.')

        return multiplication
