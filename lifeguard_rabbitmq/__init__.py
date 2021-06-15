"""
Lifeguard integration with RabbitMQ
"""

from lifeguard.validations import validation

from lifeguard_rabbitmq.validations import consumers_validation


class RabbitMQContext:
    """
    RabbitMQ Context
    """

    def __init__(self):
        self._consumers_validation_options = {
            "actions": [],
            "schedule": {"every": {"minutes": 1}},
            "settings": {},
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
        """
        self._consumers_validation_options = value


RABBITMQ_PLUGIN_CONTEXT = RabbitMQContext()


def init(lifeguard_context):
    validation(
        "RabbitMQ Consumers Validation",
        RABBITMQ_PLUGIN_CONTEXT.consumers_validation_options["actions"],
        RABBITMQ_PLUGIN_CONTEXT.consumers_validation_options["schedule"],
        RABBITMQ_PLUGIN_CONTEXT.consumers_validation_options["settings"],
    )(consumers_validation)
