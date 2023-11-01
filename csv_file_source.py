import csv
import random
from faker import Faker

#create 11,000 records of random data
data = []
fake = Faker()
for _ in range(11000):
    user = {
        'Name': fake.name(),
        'Age': random.randint(0, 105),
        'Location': fake.city(),
    }
    data.append(user)

#save data into a csv file
csv_file = 'random_data.csv'
columns = ['Name', 'Age', 'Location']

with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()

    for row in data:
        writer.writerow(row)