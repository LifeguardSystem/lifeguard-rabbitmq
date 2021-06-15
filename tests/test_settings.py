import unittest

from lifeguard_rabbitmq.settings import (
    SETTINGS_MANAGER,
    LIFEGUARD_RABBITMQ_ADMIN_BASE_URL,
)


class SettingsTest(unittest.TestCase):
    def test_lifeguard_tinydb_database(self):
        self.assertEqual(LIFEGUARD_RABBITMQ_ADMIN_BASE_URL, "http://localhost:15672")
        self.assertEqual(
            SETTINGS_MANAGER.settings["LIFEGUARD_RABBITMQ_ADMIN_BASE_URL"][
                "description"
            ],
            "RabbitMQ admin base url",
        )
