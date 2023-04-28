import csv
from faker import Faker

# Create a Faker instance
faker = Faker()

# Open the original CSV file for reading
with open('sections.csv', 'r') as infile:
    reader = csv.reader(infile)

    # Create a new CSV file for writing
    with open('sectionItem.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)

        # Write the headings for the new CSV file
        writer.writerow(['Section_ID', 'Item_ID', 'Item_Name', 'Item_Type', 'Item_URL'])

        # Loop through each row in the original CSV file
        for row in reader:
            section_id = row[0]

            # Generate a random Item ID, name, type, and URL using Faker
            item_id = faker.uuid4()
            item_name = faker.word()
            item_type = faker.random_element(elements=('audio', 'video', 'text'))
            item_url = faker.url()

            # Write the row to the new CSV file with the new data
            writer.writerow([section_id, item_id, item_name, item_type, item_url])
