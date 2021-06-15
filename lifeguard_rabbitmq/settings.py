"""
Lifeguard RabbitMQ Settings
"""
from lifeguard.settings import SettingsManager

SETTINGS_MANAGER = SettingsManager(
    {
        "LIFEGUARD_RABBITMQ_ADMIN_BASE_URL": {
            "default": "http://localhost:15672",
            "description": "RabbitMQ admin base url",
        }
    }
)

LIFEGUARD_RABBITMQ_ADMIN_BASE_URL = SETTINGS_MANAGER.read_value(
    "LIFEGUARD_RABBITMQ_ADMIN_BASE_URL"
)
