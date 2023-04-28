import csv
from faker import Faker
from lorem_text import lorem
import random

# Create a Faker object and generate fake data
fake = Faker()

# List of valid content types and their corresponding content generation functions
valid_content_types = {
    "text": lambda: fake.text(),
    "image": lambda: fake.image_url(),
    "link": lambda: fake.url(),
    
}

# Read section ids from sections.csv file
with open('sections.csv', 'r') as f:
    reader = csv.reader(f)
    section_ids = [row[0] for row in reader]

# Generate content and write to cContent.csv file
with open('courseContent.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['section_id', 'content_id', 'content_type', 'content'])
    for section_id in section_ids:
        content_id = fake.uuid4()
        content_type = random.choice(list(valid_content_types.keys()))
        content = valid_content_types[content_type]()
        writer.writerow([section_id, content_id, content_type, content])
