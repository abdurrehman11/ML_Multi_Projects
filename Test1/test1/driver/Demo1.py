import logging
from os.path import dirname

from test1.utils.Constants import Constants
from test1.init.InitializationHandler import InitializationHandler

from test2 import Demo2
from test3 import Demo3


class Demo1:

    def __init__(self):
        InitializationHandler.initialize_logger(str(dirname(dirname(dirname(__file__)))) +
                                                str(Constants.LOGGER_PROPERTIES_FILE_PATH))
        self.logger = logging.getLogger(Constants.LOGGER_NAME)

    def add(self, x, y):
        self.logger.info(f'Going to add {x} and {y}.')
        addition = x + y
        self.logger.info(f'Added {x} and {y} successfully.')
        return addition


if __name__ == '__main__':
    d1 = Demo1()
    add_result = d1.add(5, 2)
    print(add_result)

    d2 = Demo2()
    sub_result = d2.sub(5, 2)
    print(sub_result)

    d3 = Demo3()
    mul_result = d3.mul(5, 2)
    print(mul_result)
