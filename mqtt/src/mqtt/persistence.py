""" Functionality to persist incoming messages to (local) filesystem. """
import logging
import os
import time
import datetime
import pathlib
import json

from mqtt import config

from mqtt.logger import get_time_handled_logger

logger = logging.getLogger('iot_custom')


def persist_to_file(topic: str, decoded_message: str, **kwargs) -> None:
    """ 
        Wrapper function to persist `decoded_message` in filesystem. Directory will match the `topic`. 
        
        Args:
            topic: MQTT topic. E.g. 'sensors/humidity'
            decoded_message: Message from MQTT broker
            kwargs: Keyword arguments
    """
    log_to_file(topic, decoded_message, **kwargs)


def log_to_file(topic: str, decoded_message: str, **kwargs) -> None:
    """ 
        Creates directories that match the hierarchy of `topic` with respect to configuration. Uses 
        TimedRotatingFileHandler to create and maintain log files in this topic.
        
        Args:
            topic: MQTT topic. E.g. 'sensors/humidity'
            decoded_message: Message from MQTT broker
            kwargs: Keyword arguments
    """
    create_empty_dir_for_topic(topic, config.LOG_BASE_PATH)

    logger.debug(f'persisting: {decoded_message} in {topic}')

    file_logger = get_time_handled_logger(topic)

    assert isinstance(file_logger.handlers[0], logging.handlers.TimedRotatingFileHandler)
    assert file_logger.name == 'custom_timed_logger'

    file_logger.debug(format_measurement(decoded_message))


def create_empty_dir_for_topic(topic: str, base_path: str) -> None:
    """
        If necessary, create directories that represent the hierarchy of `topic` in extension of local `base_path`. 
        
        Args:
            topic: MQTT topic
            base_path: Path in filesystem that the directories for the topic should be added to
     
    """
    log_dir = pathlib.Path(base_path, topic)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)


def format_measurement(decoded_message: str) -> str:
    """ 
        Formatter for MQTT messages. To be used before persisting.
        
        Returns:
            Formatted message
    """
    return f'[{int(time.time())}] {decoded_message}'