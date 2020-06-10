import logging

from CommonExceps.commonexceps.SubtractionOperationException import SubtractionOperationException
from test2.utils.Constants import Constants


class SubtractNumbers:

    logger = logging.getLogger(Constants.LOGGER_NAME)

    @classmethod
    def subtract(cls, x, y):
        try:
            cls.logger.info(f'Going to sub {x} and {y}.')
            subtraction = x - y
            cls.logger.info(f'Subtracted {x} and {y} successfully.')
            cls.logger.info(f'Subtraction of {x} and {y}: {subtraction}')
        except Exception as exp:
            cls.logger.error('Exception occurred while subtracting numbers.')
            raise SubtractionOperationException(exp)
