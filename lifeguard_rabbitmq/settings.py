"""
Lifeguard RabbitMQ Settings
"""
from lifeguard.settings import SettingsManager

SETTINGS_MANAGER = SettingsManager(
    {
        "LIFEGUARD_RABBITMQ_DEFAULT_ADMIN_BASE_URL": {
            "default": "http://localhost:15672",
            "description": "RabbitMQ admin base url of default instance",
        },
        "LIFEGUARD_RABBITMQ_DEFAULT_ADMIN_USER": {
            "default": "guest",
            "description": "RabbitMQ admin user of default instance",
        },
        "LIFEGUARD_RABBITMQ_DEFAULT_ADMIN_PASSWD": {
            "default": "guest",
            "description": "RabbitMQ admin password of default instance",
        },
        "LIFEGUARD_RABBITMQ_DEFAULT_ADMIN_VHOST": {
            "default": "/",
            "description": "RabbitMQ admin virtual host of default instance",
        },
    }
)

LIFEGUARD_RABBITMQ_DEFAULT_ADMIN_BASE_URL = SETTINGS_MANAGER.read_value(
    "LIFEGUARD_RABBITMQ_DEFAULT_ADMIN_BASE_URL"
)

LIFEGUARD_RABBITMQ_DEFAULT_ADMIN_USER = SETTINGS_MANAGER.read_value(
    "LIFEGUARD_RABBITMQ_DEFAULT_ADMIN_USER"
)

LIFEGUARD_RABBITMQ_DEFAULT_ADMIN_PASSWD = SETTINGS_MANAGER.read_value(
    "LIFEGUARD_RABBITMQ_DEFAULT_ADMIN_PASSWD"
)

LIFEGUARD_RABBITMQ_DEFAULT_ADMIN_VHOST = SETTINGS_MANAGER.read_value(
    "LIFEGUARD_RABBITMQ_DEFAULT_ADMIN_VHOST"
)


def get_rabbitmq_admin_instances():
    """
    Recover attributes of each RabbitMQ Admin instances
    """
    return {
        "default": {
            "base_url": LIFEGUARD_RABBITMQ_DEFAULT_ADMIN_BASE_URL,
            "user": LIFEGUARD_RABBITMQ_DEFAULT_ADMIN_USER,
            "passwd": LIFEGUARD_RABBITMQ_DEFAULT_ADMIN_PASSWD,
            "vhost": LIFEGUARD_RABBITMQ_DEFAULT_ADMIN_VHOST,
        }
    }
