"""
RabbitMQ Common Validations
"""
import traceback

from lifeguard import NORMAL, PROBLEM, change_status
from lifeguard.logger import lifeguard_logger as logger
from lifeguard.validations import ValidationResponse

from lifeguard_rabbitmq.context import RABBITMQ_PLUGIN_CONTEXT
from lifeguard_rabbitmq.rabbitmq.admin import count_consumers, number_of_messages


def __check_queue_validation_base(
    rabbitmq_admin_instance, queues, details, queue_validation
):
    details[rabbitmq_admin_instance] = []
    status = NORMAL

    for queue in queues:
        queue_status = {
            "queue": queue["name"],
            "status": NORMAL,
        }
        try:
            queue_validation(queue_status, queue)
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


def __check_consumers(rabbitmq_admin_instance, queues, details):
    def queue_validation(queue_status, queue):
        queue_status["number_of_consumers"] = count_consumers(
            rabbitmq_admin_instance, queue["name"]
        )
        if queue_status["number_of_consumers"] < queue["min_number_of_consumers"]:
            queue_status["status"] = PROBLEM

    return __check_queue_validation_base(
        rabbitmq_admin_instance, queues, details, queue_validation
    )


def __check_message_increasing(rabbitmq_admin_instance, queues, details):
    def queue_validation(queue_status, queue):
        messages = number_of_messages(rabbitmq_admin_instance, queue["name"])
        queue_status["number_of_messages"] = messages

        last_content = queue.get(
            "last_content", {"number_of_messages": 0, "counter": 0, "status": NORMAL}
        )

        if messages > last_content["number_of_messages"]:
            last_content["counter"] += 1
            last_content["number_of_messages"] = messages

        if (
            messages >= last_content["number_of_messages"]
            and last_content["counter"] > queue["count_before_alert"]
        ):
            last_content["status"] = change_status(last_content["status"], PROBLEM)
            queue_status["status"] = PROBLEM

        if messages < last_content["number_of_messages"] or messages == 0:
            queue_status["status"] = NORMAL
            last_content["status"] = NORMAL
            last_content["counter"] = 0
            last_content["number_of_messages"] = messages

        queue_status["content"] = last_content
        queue["last_content"] = last_content

    return __check_queue_validation_base(
        rabbitmq_admin_instance, queues, details, queue_validation
    )


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
    return ValidationResponse(
        status, details, validation_name="consumers_running_validation"
    )


def messages_increasing_validation():
    """
    Validates message incresing for a queue
    """

    options = RABBITMQ_PLUGIN_CONTEXT.messages_increasing_validation_options
    status = NORMAL
    details = {}

    for rabbitmq_admin_instance in options["queues"]:
        queues = options["queues"][rabbitmq_admin_instance]

        status = change_status(
            status, __check_message_increasing(rabbitmq_admin_instance, queues, details)
        )

    return ValidationResponse(
        status, details, validation_name="messages_increasing_validation"
    )
