import unittest

from lifeguard_rabbitmq.settings import (
    LIFEGUARD_RABBITMQ_DEFAULT_ADMIN_BASE_URL,
    LIFEGUARD_RABBITMQ_DEFAULT_ADMIN_PASSWD,
    LIFEGUARD_RABBITMQ_DEFAULT_ADMIN_USER,
    LIFEGUARD_RABBITMQ_DEFAULT_ADMIN_VHOST,
    SETTINGS_MANAGER,
    get_rabbitmq_admin_instances,
)


class SettingsTest(unittest.TestCase):
    def test_lifeguard_rabbitmq_admin_base_url(self):
        self.assertEqual(
            LIFEGUARD_RABBITMQ_DEFAULT_ADMIN_BASE_URL, "http://localhost:15672"
        )
        self.assertEqual(
            SETTINGS_MANAGER.settings["LIFEGUARD_RABBITMQ_DEFAULT_ADMIN_BASE_URL"][
                "description"
            ],
            "RabbitMQ admin base url of default instance",
        )

    def test_lifeguard_rabbitmq_admin_user(self):
        self.assertEqual(LIFEGUARD_RABBITMQ_DEFAULT_ADMIN_USER, "guest")
        self.assertEqual(
            SETTINGS_MANAGER.settings["LIFEGUARD_RABBITMQ_DEFAULT_ADMIN_USER"][
                "description"
            ],
            "RabbitMQ admin user of default instance",
        )

    def test_lifeguard_rabbitmq_admin_passwd(self):
        self.assertEqual(LIFEGUARD_RABBITMQ_DEFAULT_ADMIN_PASSWD, "guest")
        self.assertEqual(
            SETTINGS_MANAGER.settings["LIFEGUARD_RABBITMQ_DEFAULT_ADMIN_PASSWD"][
                "description"
            ],
            "RabbitMQ admin password of default instance",
        )

    def test_lifeguard_rabbitmq_admin_vhost(self):
        self.assertEqual(LIFEGUARD_RABBITMQ_DEFAULT_ADMIN_VHOST, "/")
        self.assertEqual(
            SETTINGS_MANAGER.settings["LIFEGUARD_RABBITMQ_DEFAULT_ADMIN_VHOST"][
                "description"
            ],
            "RabbitMQ admin virtual host of default instance",
        )

    def test_lifeguard_rabbitmq_admin_get_instances_attributes(self):
        default_instance = get_rabbitmq_admin_instances()["default"]

        self.assertEqual(
            default_instance["base_url"], LIFEGUARD_RABBITMQ_DEFAULT_ADMIN_BASE_URL
        )
        self.assertEqual(
            default_instance["user"], LIFEGUARD_RABBITMQ_DEFAULT_ADMIN_USER
        )
        self.assertEqual(
            default_instance["passwd"], LIFEGUARD_RABBITMQ_DEFAULT_ADMIN_PASSWD
        )
        self.assertEqual(
            default_instance["vhost"], LIFEGUARD_RABBITMQ_DEFAULT_ADMIN_VHOST
        )
