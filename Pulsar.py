from pulsar import Client
from faker import Faker

# Create a Pulsar client
client = Client(f'http://localhost:8080')

# Create a producer
producer = client.create_producer('assessment3')

# Create a Faker instance
fake = Faker()

# Generate and publish random data for more than 1100 records
import time

for i in range(1100):
    name = fake.name()
    age = fake.random_int(18, 80)
    location = fake.city()

    data = f"Name: {name}, Age: {age}, Location: {location}"
    producer.send(data.encode('utf-8'))
    print(f"Sent: {data}")

# Close the Pulsar client
client.close()
