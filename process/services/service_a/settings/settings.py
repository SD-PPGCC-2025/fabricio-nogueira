from enum import Enum

from decouple import config

# Broker
RABBITMQ_USER = config("RABBITMQ_USER", default="rabbit")
RABBITMQ_PASS = config("RABBITMQ_PASS", default="rabbit")
RABBITMQ_HOST = config("RABBITMQ_HOST", default="localhost")
RABBITMQ_PORT = config("RABBITMQ_PORT", default=5672, cast=int)
CONFIG_NAMEKO = {
    "AMQP_URI": (
        f"amqp://{RABBITMQ_USER}:{RABBITMQ_PASS}"
        f"@{RABBITMQ_HOST}:{RABBITMQ_PORT}"
    )
}

# Enums
class ProcessType(str, Enum):
    INIT = "INIT"
    END = "END"
    ERROR = "ERROR"


class ActionType(str, Enum):
    LIST = "LIST"
    CREATE = "CREATE"
    DELETE = "DELETE"
    PATCH = "PATCH"
    VALIDATE = "VALIDATE"
    FIX = "FIX"
