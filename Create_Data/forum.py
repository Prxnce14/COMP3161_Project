import csv
from faker import Faker

fake = Faker()

# Read courses data from CSV file
courses = []
with open('courses.csv', mode='r') as courses_file:
    courses_reader = csv.reader(courses_file)
    next(courses_reader) # skip header row
    for row in courses_reader:
        course = {'id': row[0], 'name': row[1]}
        courses.append(course)

# Generate forums data
forums = []
forum_titles = ['labs', 'midsemesters', 'final exam', 'tutorials', 'No Classes', 'Class Participation', 'Class Rep.', 'Quiz']
used_titles = {}
for course in courses:
    used_titles[course['id']] = []
    # Generate two forums for each course
    for i in range(2):
        title = fake.random.choice(forum_titles)
        while title in used_titles[course['id']]:
            title = fake.random.choice(forum_titles)
        used_titles[course['id']].append(title)
        forum = {'id': fake.uuid4(), 'course_code': course['id'], 'course_name': course['name'], 'title': title}
        forums.append(forum)

    # If the course still has less than two forums, generate more
    while len([forum for forum in forums if forum['course_code'] == course['id']]) < 2:
        title = fake.random.choice(forum_titles)
        while title in used_titles[course['id']]:
            title = fake.random.choice(forum_titles)
        used_titles[course['id']].append(title)
        forum = {'id': fake.uuid4(), 'course_code': course['id'], 'course_name': course['name'], 'title': title}
        forums.append(forum)

# Write forums data to CSV file
with open('forums.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['id', 'course_code', 'course_name', 'title'])
    writer.writeheader()
    for forum in forums:
        writer.writerow(forum)
