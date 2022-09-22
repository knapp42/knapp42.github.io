""" Mqtt V3.11 subscriber client for retrieving messages from a topic. """
import logging
import time

import paho.mqtt.client as mqtt

from mqtt.cli import cli

from mqtt.persistence import persist_to_file

logger = logging.getLogger('iot_custom')


def decode_message(msg, encoding='utf-8'):
    return msg.payload.decode(encoding)


def on_message(client, userdata, message):
    logger.info(f'[{message.topic}][QOS {message.qos}] {str(message.payload.decode("utf-8"))} ')  # log to stdout

    persist_to_file(topic=message.topic,
                    decoded_message=str(decode_message(message)))


def on_log(client, userdata, level, buf):
    logger.debug(f"{buf}")  # log to stdout


def main(**kwargs):
    logger.debug(kwargs)

    # Client setup
    client = mqtt.Client(client_id=kwargs['client_id'],
                         clean_session=kwargs['clean_session'])  # True for non-persistent session

    logger.info(f'Connecting subscriber {kwargs["client_id"]}')

    client.on_message = on_message
    client.on_log = on_log
    client.username_pw_set(username=kwargs['username'], password=kwargs['password'])

    # Connect client
    client.connect(host=kwargs['broker_host'], port=kwargs['broker_port'])

    client.loop_start()
    client.subscribe(topic=kwargs['topic'], qos=kwargs['qos'])  # also retrieve retained messages
    time.sleep(kwargs['client_up_time_seconds'])
    client.loop_stop()

    logger.info(f'Closing subscriber {kwargs["client_id"]}')


if __name__ == '__main__':
    cli_args = cli()
    main(**vars(cli_args))
