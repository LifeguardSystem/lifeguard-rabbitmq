import unittest

from unittest.mock import patch, MagicMock

from lifeguard_rabbitmq.rabbitmq.admin import count_consumers


class RabbitMQAdminTest(unittest.TestCase):
    @patch("lifeguard_rabbitmq.rabbitmq.admin.get")
    def test_count_consumers(self, mock_get):

        mock_response = MagicMock(name="response")
        mock_response.content = '{"consumer_details": []}'

        mock_get.return_value = mock_response

        self.assertEqual(count_consumers("default", "queue"), 0)

        mock_get.assert_called_with(
            "http://localhost:15672/api/queues/%2f/queue",
            auth=("guest", "guest"),
        )
