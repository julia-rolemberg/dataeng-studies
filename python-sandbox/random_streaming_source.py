import random
import time

# Define the attributes and the time to run the code (in seconds)
attributes = ['a', 'b', 'c', 'd', 'e']
run_time = 10 * 60  # 20 minutes in seconds

# Generate random numbers for each attribute
def generate_random_numbers():
    return [random.random() for _ in range(len(attributes))]

# Generate and output one individual every half second
start_time = time.time()
while time.time() - start_time < run_time:
    individual = {attr: val for attr, val in zip(attributes, generate_random_numbers())}
    print(individual)
    time.sleep(0.5)
