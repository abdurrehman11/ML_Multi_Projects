import logging

from CommonExceps.commonexceps.AdditionOperationException import AdditionOperationException
from test1.utils.Constants import Constants


class AddNumbers:

    logger = logging.getLogger(Constants.LOGGER_NAME)

    @classmethod
    def add(cls, x, y):
        try:
            cls.logger.info(f'Going to add {x} and {y}.')
            addition = x + y
            cls.logger.info(f'Added {x} and {y} successfully.')
            cls.logger.info(f'Sum of {x} and {y}: {addition}')
        except Exception as exp:
            cls.logger.error('Exception occurred while adding numbers.')
            raise AdditionOperationException(exp)
