import random
import time
from google.cloud import pubsub_v1

project_id = "espm-dataops-2023"
topic_id = "testing-dataflow"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

# Define the attributes and the time to run the code (in seconds)
attributes = ['a', 'b', 'c', 'd', 'e']
run_time = 10 * 60  # 20 minutes in seconds

# Generate random numbers for each attribute
def generate_random_numbers():
    return [random.random() for _ in range(len(attributes))]

# Generate and output one individual every half second
start_time = time.time()
while time.time() - start_time < run_time:
    individual_str = str({attr: val for attr, val in zip(attributes, generate_random_numbers())})
    print(individual_str)
    individual = individual_str.encode("utf-8")
    future = publisher.publish(topic_path, individual)
    print(future.result())
    time.sleep(0.5)
