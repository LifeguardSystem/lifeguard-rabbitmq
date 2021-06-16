"""
Lifeguard integration with RabbitMQ
"""

from lifeguard.validations import validation

from lifeguard_rabbitmq.context import RABBITMQ_PLUGIN_CONTEXT
from lifeguard_rabbitmq.validations import consumers_running_validation


def init(_lifeguard_context):
    validation(
        "RabbitMQ Consumers Validation",
        RABBITMQ_PLUGIN_CONTEXT.consumers_validation_options["actions"],
        RABBITMQ_PLUGIN_CONTEXT.consumers_validation_options["schedule"],
        RABBITMQ_PLUGIN_CONTEXT.consumers_validation_options["settings"],
    )(consumers_running_validation)
