import csv
from faker import Faker

# Load data from course.csv
with open('course.csv', 'r') as course_file:
    course_reader = csv.reader(course_file)
    next(course_reader)  # Skip header row
    courses = [row[0] for row in course_reader]

# Generate fake data for assignments
fake = Faker()
assignments = []
for course in courses:
    for i in range(3):  # Generate 3 assignments per course
        assignment_id = fake.uuid4()
        assignment_url = fake.url()
        assignments.append((course, assignment_id, assignment_url))

# Save data to assignment.csv
with open('assignment.csv', 'w', newline='') as assignment_file:
    assignment_writer = csv.writer(assignment_file)
    assignment_writer.writerow(['Course ID', 'Assignment ID', 'Assignment URL'])
    assignment_writer.writerows(assignments)
