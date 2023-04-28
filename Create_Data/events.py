import pandas as pd
from faker import Faker

# Create a Faker object for generating fake data
fake = Faker()

# Read the input CSV file into a pandas DataFrame
courses_df = pd.read_csv('courses.csv')

# Generate fake data for each course using Faker
events_df = pd.DataFrame({
    'Course_id': courses_df['course_id'],
    'Event_id': [fake.uuid4() for _ in range(len(courses_df))],
    'Event_name': [fake.catch_phrase() for _ in range(len(courses_df))],
    'Event_description': [f"{event_name} taught by {fake.name()}" for event_name in courses_df['Course_Name']],
    'Event_date': [fake.date_between(start_date='-1y', end_date='+1y') for _ in range(len(courses_df))]
})

# Save the new DataFrame to a CSV file
events_df.to_csv('events.csv', index=False)
