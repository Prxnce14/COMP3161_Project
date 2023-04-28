import csv
from faker import Faker
import random

fake = Faker()

data = [('Name', 'Lecturer ID', 'User ID')]

for i in range(50):
    Name = fake.first_name() + ' ' + fake.last_name()

    lecturer_id = '8' + str(random.randint(100000000, 999999999))
    while any(lecturer_id == row[1] for row in data):
        lecturer_id = '8' + str(random.randint(100000000, 999999999))

    user_id = '9' + str(random.randint(1000, 9999))
    while any(user_id == row[2] for row in data):
        user_id = '9' + str(random.randint(1000, 9999))

    data.append((Name, lecturer_id, user_id))

with open('lecturer.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)