from message_handler.rabbit_message_queue import RabbitMessageQueue
from utilities.utils import MessageHandlers, Crossers, __set_crosser

MESSAGE_HANDLER = MessageHandlers.RabbitMQ
CROSSER = Crossers.OnePoint


def listen_for_crossover():
    message_handler = get_message_handler()
    message_handler.receive_messages()


def get_message_handler():
    if MESSAGE_HANDLER == MessageHandlers.RabbitMQ:
        return RabbitMessageQueue()
    else:
        raise Exception("No valid MessageHandler defined!")


if __name__ == "__main__":
    __set_crosser(CROSSER)
    listen_for_crossover()
