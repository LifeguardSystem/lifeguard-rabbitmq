"""
RabbitMQ Common Validations
"""
import traceback

from lifeguard.logger import lifeguard_logger as logger
from lifeguard import NORMAL, PROBLEM, change_status
from lifeguard.validations import ValidationResponse

from lifeguard_rabbitmq.context import RABBITMQ_PLUGIN_CONTEXT
from lifeguard_rabbitmq.rabbitmq.admin import count_consumers


def __check_consumers(rabbitmq_admin_instance, queues, details):
    details[rabbitmq_admin_instance] = []
    status = NORMAL

    for queue in queues:
        queue_status = {
            "queue": queue["name"],
            "status": NORMAL,
        }
        try:
            queue_status["number_of_consumers"] = count_consumers(
                rabbitmq_admin_instance, queue["name"]
            )
            if queue_status["number_of_consumers"] < queue["min_number_of_consumers"]:
                queue_status["status"] = PROBLEM
        except Exception as exception:
            logger.error(
                "error on recover queue infos %s",
                str(exception),
                extra={"traceback": traceback.format_exc()},
            )
            queue_status["status"] = PROBLEM
            queue_status["error"] = "error on recover queue infos"

        details[rabbitmq_admin_instance].append(queue_status)

        status = change_status(status, queue_status["status"])

    return status


def consumers_running_validation():
    """
    Validates number of consumers for a queue
    """
    options = RABBITMQ_PLUGIN_CONTEXT.consumers_validation_options
    status = NORMAL
    details = {}

    for rabbitmq_admin_instance in options["queues"]:
        queues = options["queues"][rabbitmq_admin_instance]

        status = change_status(
            status, __check_consumers(rabbitmq_admin_instance, queues, details)
        )
    return ValidationResponse("consumers_running_validation", status, details)
