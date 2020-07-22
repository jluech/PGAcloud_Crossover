from message_handler.rabbit_message_queue import RabbitMessageQueue
from utilities.utils import MessageHandlers, Crossers, __set_crosser, get_pga_id, set_property

MESSAGE_HANDLER = MessageHandlers.RabbitMQ
CROSSER = Crossers.OnePoint
RELEVANT_PROPERTIES = ["CROSSOVER_RATE"]


def listen_for_crossover():
    pga_id = get_pga_id()

    message_handler = get_message_handler(pga_id)
    message_handler.receive_messages()



def get_message_handler(pga_id):
    if MESSAGE_HANDLER == MessageHandlers.RabbitMQ:
        return RabbitMessageQueue(pga_id)
    else:
        raise Exception("No valid MessageHandler defined!")


if __name__ == "__main__":
    __set_crosser(CROSSER)
    listen_for_crossover()
