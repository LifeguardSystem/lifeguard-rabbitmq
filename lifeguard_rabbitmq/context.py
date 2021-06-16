"""
RabbitMQ Plugin Context
"""


class RabbitMQPluginContext:
    """
    RabbitMQ Context
    """

    def __init__(self):
        self._consumers_validation_options = {
            "actions": [],
            "schedule": {"every": {"minutes": 1}},
            "settings": {},
            "queues": {},
        }

    @property
    def consumers_validation_options(self):
        """
        Getter for consumers validation options
        """
        return self._consumers_validation_options

    @consumers_validation_options.setter
    def consumers_validation_options(self, value):
        """
        Setter for consumers validation options

        Example:

        {
            "actions": [],
            "schedule": {"every": {"minutes": 1}},
            "settings": {},
            "queues": {
                "rabbitmq_admin_instance": [{"name": "queue_name", "min_number_of_consumers": 1}]
            }
        }
        """
        self._consumers_validation_options = value


RABBITMQ_PLUGIN_CONTEXT = RabbitMQPluginContext()
