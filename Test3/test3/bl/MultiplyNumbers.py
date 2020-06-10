import logging

from CommonExceps.commonexceps.MultiplicationOperationException import MultiplicationOperationException
from test2.utils.Constants import Constants


class MultiplyNumbers:

    logger = logging.getLogger(Constants.LOGGER_NAME)

    @classmethod
    def multiply(cls, x, y):
        try:
            cls.logger.info(f'Going to multiply {x} and {y}.')
            multiplication = x * y
            cls.logger.info(f'Multiplied {x} and {y} successfully.')
            cls.logger.info(f'Multiplication of {x} and {y}: {multiplication}')
        except Exception as exp:
            cls.logger.error('Exception occurred while subtracting numbers.')
            raise MultiplicationOperationException(exp)
