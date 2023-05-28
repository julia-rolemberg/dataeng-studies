from argparse import ArgumentParser, FileType
from configparser import ConfigParser
import json
from confluent_kafka import Consumer, OFFSET_BEGINNING, KafkaError

if __name__ == '__main__':
    # Parse the command line.
    parser = ArgumentParser()
    parser.add_argument('config_file', type=FileType('r'))
    parser.add_argument('--reset', action='store_true')
    args = parser.parse_args()
    
    config_parser = ConfigParser()
    config_parser.read_file(args.config_file)
    config = dict(config_parser['default'])
    config.update(config_parser['consumer'])

    # Create Consumer instance
    consumer = Consumer(config)

    # Set up a callback to handle the '--reset' flag.
    def reset_offset(consumer, partitions):
        if args.reset:
            for p in partitions:
                p.offset = OFFSET_BEGINNING
            consumer.assign(partitions)

    # Subscribe to topic
    topic = "topic_teste"
    consumer.subscribe([topic], on_assign=reset_offset)

    # Consume messages from the Kafka topic
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    print('End of partition reached')
                else:
                    print('Error while consuming message: {}'.format(msg.error()))
            else:
                message = json.loads(msg.value().decode('utf-8'))
                print('Received message: {}'.format(message))
                size = message['size']
                avg_speed = message['avg_speed']
                age = message['age']
                # Do something with the individual's characteristics
                print('Size: {}, Avg Speed: {}, Age: {}'.format(size, avg_speed, age))

    except KeyboardInterrupt:
        pass

    finally:
        # Close the Kafka consumer instance
        consumer.close()
