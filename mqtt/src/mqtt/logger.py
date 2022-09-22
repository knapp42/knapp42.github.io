""" Provides helpful classes and functions for logging"""
import os
import logging
import pathlib

from logging.config import dictConfig
from logging.handlers import TimedRotatingFileHandler

from mqtt import config


def setup_logging():
    """
        Setup of logging module via dict config. Recommended to call this as soon as possible after module start. 
    """

    develop = os.getenv('ENV', default='DEV').lower() == 'dev'

    dictConfig({
        'version': 1,
        'formatters': {
            'default': {
                'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
            }  # ,
            # 'dmv_format': {  # custom format based on class
            #    'format': '[%(id)s] [%(levelname)s] [%(asctime)s] [%(method)s] %(full_path)s: %(message)s',
            #    'class': 'dmv.logger.RequestFormatter'
            # }
        },
        'handlers': {
            'iot': {  # "default" project handler
                'class': 'logging.StreamHandler',
                'stream': 'ext://sys.stdout',
                'formatter': 'default'
            }
        },
        'loggers': {
            'iot_custom': {
                'handlers': ['iot'],
                'level': 'DEBUG' if develop else 'INFO',
                'propagate': False
            }
        }
    })


def get_time_handled_logger(topic: str):
    """
        Dynamic timed file logger that can be used to write content to files.
        Since each logger (possibly) works for a different topic it must be configured and returned on demand. Not
        possible to do this in `setup_logging()`.
    """

    logger = logging.getLogger()
    logger.name = 'custom_timed_logger'

    log_path = pathlib.Path(config.LOG_BASE_PATH, topic, config.LOG_FILE_NAME)

    handler = TimedRotatingFileHandler(log_path,
                                       when=config.LOG_WHEN,
                                       interval=config.LOG_INTERVAL,
                                       backupCount=config.LOG_BACKUP_COUNT,
                                       utc=config.LOG_UTC_TIME)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger
