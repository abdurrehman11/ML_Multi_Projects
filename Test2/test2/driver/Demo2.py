import logging

from test2.utils.Constants import Constants


class Demo2:
    def __init__(self):
        self.logger = logging.getLogger(Constants.LOGGER_NAME)

    def sub(self, x, y):
        self.logger.info(f'Going to sub {x} and {y}.')
        subtraction = x - y
        self.logger.info(f'Subtracted {x} and {y} successfully.')

        return subtraction

