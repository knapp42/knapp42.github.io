""" Mqtt V3.11 publisher client for retrieving messages from a topic. """
import logging

import paho.mqtt.client as mqtt

from mqtt.cli import cli
from mqtt.logger import setup_logging

setup_logging()
logger = logging.getLogger('iot_custom')


def on_log(client, userdata, level, buf):
    logger.debug(f"{buf}")


def main(**kwargs):
    logger.debug(kwargs)

    # Client setup
    client = mqtt.Client(client_id=kwargs['client_id'])
    client.on_log = on_log
    client.username_pw_set(kwargs['username'], kwargs['password'])

    # Connect client
    client.connect(host=kwargs['broker_host'], port=kwargs['broker_port'])

    client.loop_start()

    client.publish("u3/rooms/kitchen/sensors/humidity", "100.1",
                   qos=kwargs['qos'])

    client.loop_stop()

    logger.info(f'Closing publisher {kwargs["client_id"]}')


if __name__ == '__main__':
    args = cli()
    main(**vars(args))
