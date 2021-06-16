"""
RabbitMQ admin resources
"""
import json

from lifeguard.http_client import get

from lifeguard_rabbitmq.settings import get_rabbitmq_admin_instances

BASE_URL = "{}"
QUEUE = "/api/queues/{}/{}"


def count_consumers(instance_name, queue):
    """
    Get consumers for a queue
    """
    instance_attributes = get_rabbitmq_admin_instances()[instance_name]
    url = __url(QUEUE, instance_attributes["base_url"]).format(
        __vhost(instance_attributes["vhost"]), queue
    )
    response = __get(url, instance_attributes["user"], instance_attributes["passwd"])

    print("\n\n\n")
    print(response)
    print("\n\n\n")

    return len(response["consumer_details"])


def __get(url, user, password):
    return json.loads(get(url, auth=(user, password)).content)


def __url(api, admin):
    return BASE_URL.format(admin) + api


def __vhost(vhost):
    return vhost.replace(vhost, "%2f")
