import json
import logging

import pika

from crossover.crossover import apply_crossover
from message_handler.message_handler import MessageHandler
from population.individual import Individual, IndividualEncoder
from utilities import utils


def receive_crossover_callback(channel, method, properties, body):
    queue_name = utils.get_messaging_source()

    pair_dict = json.loads(body)
    pair = []
    for ind_dict in pair_dict:
        pair.append(Individual(ind_dict["solution"], ind_dict["fitness"]))

    logging.info("rMQ:{queue_}: Received crossover request for pair: {pair_}".format(
        queue_=queue_name,
        pair_=pair,
    ))

    crossed_pair = apply_crossover(pair[0], pair[1])

    for pair in crossed_pair:
        send_message_to_queue(
            channel=channel,
            payload=pair
        )


def send_message_to_queue(channel, payload):
    # Route the message to the next queue in the model.
    next_recipient = utils.get_messaging_target()
    channel.queue_declare(queue=next_recipient, auto_delete=True, durable=True)

    # Send message to given recipient.
    logging.info("rMQ: Sending '{body_}' to {dest_}.".format(
        body_=payload,
        dest_=next_recipient,
    ))
    channel.basic_publish(
        exchange="",
        routing_key=next_recipient,
        body=json.dumps(payload, cls=IndividualEncoder),
        # Delivery mode 2 makes the broker save the message to disk.
        # This will ensure that the message be restored on reboot even
        # if RabbitMQ crashes before having forwarded the message.
        properties=pika.BasicProperties(
            delivery_mode=2,
        ),
    )


class RabbitMessageQueue(MessageHandler):
    def __init__(self, pga_id):
        # Establish connection to rabbitMQ.
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host="rabbitMQ--{id_}".format(id_=pga_id),
            socket_timeout=30,
        ))

    def receive_messages(self):
        # Define communication channel.
        channel = self.connection.channel()

        # Create queue for crossover.
        queue_name = utils.get_messaging_source()
        channel.queue_declare(queue=queue_name, auto_delete=True, durable=True)

        # Actively listen for messages in queue and perform callback on receive.
        channel.basic_consume(
            queue=queue_name,
            on_message_callback=receive_crossover_callback,
        )
        logging.info("rMQ:{queue_}: Waiting for crossover requests.".format(
            queue_=queue_name
        ))
        channel.start_consuming()

    def send_message(self, pair):
        # Define communication channel.
        channel = self.connection.channel()
        send_message_to_queue(
            channel=channel,
            payload=pair
        )
