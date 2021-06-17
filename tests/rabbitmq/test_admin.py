import unittest

from unittest.mock import patch, MagicMock

from lifeguard_rabbitmq.rabbitmq.admin import count_consumers, number_of_messages


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

    @patch("lifeguard_rabbitmq.rabbitmq.admin.get")
    def test_number_of_messages(self, mock_get):

        mock_response = MagicMock(name="response")
        mock_response.content = '{"messages": 0}'

        mock_get.return_value = mock_response

        self.assertEqual(number_of_messages("default", "queue"), 0)

        mock_get.assert_called_with(
            "http://localhost:15672/api/queues/%2f/queue",
            auth=("guest", "guest"),
        )

    @patch("lifeguard_rabbitmq.rabbitmq.admin.get")
    @patch("lifeguard_rabbitmq.rabbitmq.admin.get_rabbitmq_admin_instances")
    def test_replace_vhost(self, mock_get_rabbitmq_admin_instances, mock_get):

        mock_get_rabbitmq_admin_instances.return_value = {
            "default": {
                "base_url": "url",
                "user": "guest",
                "passwd": "guest",
                "vhost": "vhost",
            }
        }

        mock_response = MagicMock(name="response")
        mock_response.content = '{"messages": 0}'

        mock_get.return_value = mock_response

        self.assertEqual(number_of_messages("default", "queue"), 0)

        mock_get.assert_called_with(
            "url/api/queues/vhost/queue", auth=("guest", "guest")
        )
