import unittest

from lifeguard_rabbitmq.context import RabbitMQPluginContext


class ContextTest(unittest.TestCase):
    def setUp(self):
        self.context = RabbitMQPluginContext()

    def test_serialize_context(self):
        self.assertEqual(
            self.context.get_attributes(),
            {
                "messages_increasing_validation_options": {
                    "actions": [],
                    "schedule": {"every": {"minutes": 1}},
                    "settings": {},
                    "queues": {},
                },
                "consumers_validation_options": {
                    "actions": [],
                    "schedule": {"every": {"minutes": 1}},
                    "settings": {},
                    "queues": {},
                },
            },
        )
