from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import random
import json
from confluent_kafka import Consumer, OFFSET_BEGINNING, KafkaError
from argparse import ArgumentParser, FileType
from configparser import ConfigParser
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
# socketio = SocketIO(app, ping_timeout=600, ping_interval=10)

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

def on_message(consumer, message):
    message = json.loads(message.value().decode('utf-8'))
    print(f"kafka -----{message}")
    size = message['size']
    data = {'size': size}
    socketio.emit('update', data)

# Subscribe to topic
topic = "topic_teste"
consumer.subscribe([topic], on_message=on_message)


# # Generate some random data for initial plot
def generate_data():
    data = []
    for i in range(30):
        data.append([i, random.randint(0, 100)])
    return data

# Handle WebSocket connections
@socketio.on('connect')
def handle_connect():
    socketio.emit('connect')
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

# Update chart data with Kafka messages
def update_chart():
    try:
        while True:
            msg = consumer.poll(0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    print('End of partition reached')
                else:
                    print('Error while consuming message: {}'.format(msg.error()))
            else:
                message = json.loads(msg.value().decode('utf-8'))
                print(f"kafka -----{message}")
                # size = message['size']
                data = {'size': 12}
                socketio.emit('update', data) 

    except KeyboardInterrupt:
        pass
    finally:
        # Close the Kafka consumer instance
        consumer.close()

# Start the Kafka consumer thread
import threading
kafka_thread = threading.Thread(target=update_chart)
# kafka_thread = socketio.start_background_task(update_chart)
kafka_thread.start()

# Render the template and send initial chart data
@app.route('/')
def index():
    data = generate_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    socketio.run(app, debug=True)
