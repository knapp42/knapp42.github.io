import argparse

from mqtt import config
from mqtt.logger import setup_logging

setup_logging()


def cli():
    parser = argparse.ArgumentParser(description='CLI for MQTT Client',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('client_id',
                        help=f'ID of MQTT client.')

    parser.add_argument('password',
                        help='Password for authorizing user at MQTT broker. ')

    parser.add_argument('--username',
						default='test',
                        help='Username to authorize at mqtt broker.')

    parser.add_argument('--broker_host',
                        default=config.BROKER_HOST,
                        help=f'Broker host.')

    parser.add_argument('--broker_port',
                        default=config.BROKER_PORT,
                        help=f'Broker port.')

    parser.add_argument('--topic',
                        default=config.TOPIC,
                        help=f'Broker port.')

    parser.add_argument('--qos',
                        default=config.QOS,
                        help=f'Broker port.')

    parser.add_argument('--client_up_time_seconds',
                        default=config.SUBSCRIBER_UPTIME_SEC,
                        help=f'Broker port.')

    parser.add_argument('--clean_session',  
                        default=True,	# if True, will remove all info to client with the broker
                        help=f'Broker port.')

    return parser.parse_args()
