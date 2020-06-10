import logging
from os.path import dirname

from test1.utils.Constants import Constants
from test1.init.InitializationHandler import InitializationHandler
from test1.bl.AddNumbers import AddNumbers

from commonexceps.AdditionOperationException import AdditionOperationException
from commonexceps.SubtractionOperationException import SubtractionOperationException
from commonexceps.MultiplicationOperationException import MultiplicationOperationException

from test2 import Demo2
from test3 import Demo3


class Demo1:

    def __init__(self):
        InitializationHandler.initialize_logger(str(dirname(dirname(dirname(__file__)))) +
                                                str(Constants.LOGGER_PROPERTIES_FILE_PATH))
        self.logger = logging.getLogger(Constants.LOGGER_NAME)

    def main(self):
        try:
            AddNumbers.add(5, '3')
            Demo2.perform_subtraction(5, 3)
            Demo3.perform_multiplication(5, 3)
        except AdditionOperationException as exp:
            self.logger.error("Exception occurred in Addition")
            raise exp
        except SubtractionOperationException as exp:
            self.logger.error("Exception occurred in Subtraction")
            raise exp
        except MultiplicationOperationException as exp:
            self.logger.error("Exception occurred in Multiplication")
            raise exp
        except Exception as exp:
            raise exp


if __name__ == '__main__':
    d1 = Demo1()
    d1.main()
