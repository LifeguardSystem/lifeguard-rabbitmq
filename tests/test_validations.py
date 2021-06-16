import unittest

from unittest.mock import patch

from lifeguard import NORMAL, PROBLEM
from lifeguard_rabbitmq.context import RABBITMQ_PLUGIN_CONTEXT
from lifeguard_rabbitmq.validations import consumers_running_validation


class ValidationTest(unittest.TestCase):
    def setUp(self):
        RABBITMQ_PLUGIN_CONTEXT.consumers_validation_options = {
            "actions": [],
            "schedule": {"every": {"minutes": 1}},
            "settings": {},
            "queues": {
                "rabbitmq_admin_instance": [
                    {"name": "queue_name", "min_number_of_consumers": 1}
                ]
            },
        }

    @patch("lifeguard_rabbitmq.validations.count_consumers")
    def test_consumers_running_validation_when_normal(self, mock_count_consumers):
        mock_count_consumers.return_value = 1

        response = consumers_running_validation()

        self.assertEqual(response.status, NORMAL)
        self.assertEqual(
            response.details,
            {
                "rabbitmq_admin_instance": [
                    {
                        "queue": "queue_name",
                        "number_of_consumers": 1,
                        "status": "NORMAL",
                    }
                ]
            },
        )

    @patch("lifeguard_rabbitmq.validations.count_consumers")
    def test_consumers_running_validation_normal_with_more_than_min(
        self, mock_count_consumers
    ):
        mock_count_consumers.return_value = 2

        response = consumers_running_validation()

        self.assertEqual(response.status, NORMAL)
        self.assertEqual(
            response.details,
            {
                "rabbitmq_admin_instance": [
                    {
                        "queue": "queue_name",
                        "number_of_consumers": 2,
                        "status": "NORMAL",
                    }
                ]
            },
        )

    @patch("lifeguard_rabbitmq.validations.count_consumers")
    def test_consumers_running_validation_when_problem(self, mock_count_consumers):
        mock_count_consumers.return_value = 0

        response = consumers_running_validation()

        mock_count_consumers.assert_called_with("rabbitmq_admin_instance", "queue_name")
        self.assertEqual(response.validation_name, "consumers_running_validation")
        self.assertEqual(response.status, PROBLEM)
        self.assertEqual(
            response.details,
            {
                "rabbitmq_admin_instance": [
                    {
                        "queue": "queue_name",
                        "number_of_consumers": 0,
                        "status": "PROBLEM",
                    }
                ]
            },
        )

    @patch("lifeguard_rabbitmq.validations.count_consumers")
    @patch("lifeguard_rabbitmq.validations.logger")
    def test_consumers_running_validation_when_problem_because_integration_error(
        self, mock_logger, mock_count_consumers
    ):
        mock_count_consumers.side_effect = [Exception("error")]

        response = consumers_running_validation()

        mock_count_consumers.assert_called_with("rabbitmq_admin_instance", "queue_name")
        self.assertEqual(response.status, PROBLEM)
        self.assertEqual(
            response.details,
            {
                "rabbitmq_admin_instance": [
                    {
                        "error": "error on recover queue infos",
                        "queue": "queue_name",
                        "status": "PROBLEM",
                    }
                ]
            },
        )