import json
import sys
import time
import random
from argparse import ArgumentParser, FileType
from configparser import ConfigParser
from confluent_kafka import Producer
from avro.schema import parse
import io
from avro.io import DatumWriter, BinaryEncoder

def generate_individual():
    individual = {
        'size': round(random.uniform(1.0, 2.5), 2),
        'avg_speed': round(random.uniform(5.0, 20.0), 2),
        'age': random.randint(18, 80)
    }
    return individual

if __name__ == '__main__':
    # Parse the command line arguments
    parser = ArgumentParser()
    parser.add_argument('config_file', type=FileType('r'))
    args = parser.parse_args()

    # Parse the configuration
    config_parser = ConfigParser()
    config_parser.read_file(args.config_file)
    config = dict(config_parser['default'])

    # Load the Avro schema from a file or define it in your code
    avro_schema = parse(open('avro_schema.avsc', 'r').read())

    # Create a Kafka producer instance
    producer = Producer(config)

    # Define a delivery callback to handle produced messages
    def delivery_callback(err, msg):
        if err is not None:
            print(f'Message delivery failed: {err}')
        else:
            message_value = msg.value()
            plain_text = message_value.decode('utf-8')
            print(f"Produced event to topic {msg.topic()}: message = {plain_text}")




    # Define the Kafka topic to publish messages to
    topic = 'topic_individuals'

    # Continuously generate and publish messages to the Kafka topic
    while True:
        individual = generate_individual()

        # Serialize the message payload using Avro
        bytes_writer = io.BytesIO()
        encoder = BinaryEncoder(bytes_writer)
        writer = DatumWriter(avro_schema)
        writer.write(individual, encoder)
        encoded_message = bytes_writer.getvalue()

        producer.produce(topic, value=encoded_message, callback=delivery_callback)
        producer.poll(0)
        time.sleep(1)
