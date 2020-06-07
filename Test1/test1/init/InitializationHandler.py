import logging
import logging.config
import yaml


class InitializationHandler:

    @staticmethod
    def initialize_logger(log_properties_file_path):
        with open(log_properties_file_path, 'rt') as file:
            config = yaml.safe_load(file.read())
            logging.config.dictConfig(config)
