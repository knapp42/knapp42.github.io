# MQTT CLIENT
BROKER_HOST = "127.0.0.1"
BROKER_PORT = 1883

TOPIC = 'rooms/kitchen/sensors/humidity'
QOS = 0

SUBSCRIBER_UPTIME_SEC = 120

# TIMED-ROTATING-FILE-LOGGER CONFIG
LOG_BASE_PATH = r'C:\'  # where to store incoming messages from broker
LOG_FILE_NAME = r'log'  # filename to store incoming messages
LOG_WHEN = 'H'
LOG_INTERVAL = 1
LOG_BACKUP_COUNT = 47  # logger will manage one logfile + n backup logfiles for a mqtt topic
LOG_UTC_TIME = True
