import pandas as pd
from faker import Faker

# Create a Faker object for generating fake data
fake = Faker()

# Read the input CSV file into a pandas DataFrame
courses_df = pd.read_csv('courses.csv')

# Generate fake data for each section using Faker
sections_df = pd.DataFrame({
    'Course_id': courses_df['course_id'],
    'Section_id': [fake.uuid4() for _ in range(len(courses_df))],
    'Section_title': [fake.catch_phrase() for _ in range(len(courses_df))]
})

# Save the new DataFrame to a CSV file
sections_df.to_csv('sections.csv', index=False)
