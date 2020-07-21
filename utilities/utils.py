from enum import Enum

__CROSSER = None


class MessageHandlers(Enum):
    RabbitMQ = "rabbitMQ",


class Crossers(Enum):
    OnePoint = "one_point",
    MultiPoint = "multi_point",
    Uniform = "uniform",


def forward_crosser():
    return __CROSSER


def __set_crosser(selector):
    global __CROSSER
    __CROSSER = selector
