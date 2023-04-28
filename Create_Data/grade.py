import csv
import random
from faker import Faker

def read_csv(file_path):
    with open(file_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row

def write_csv(file_path, rows, fieldnames):
    with open(file_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

# Read assigned courses in chunks of 10,000 rows
assigned_courses = read_csv('assigned_courses.csv')
chunk_size = 10000
while True:
    rows = []
    for _ in range(chunk_size):
        try:
            row = next(assigned_courses)
            rows.append(row)
        except StopIteration:
            break
    if not rows:
        break

    # Read assignments
    assignments = list(read_csv('assignment.csv'))

    # Generate grades for this chunk of assigned courses
    grades = []
    fake = Faker()
    for course in rows:
        if course['course_id'] and course['student_id']:
            # Find assignments for this course
            course_assignments = [a for a in assignments if a['course_id'] == course['course_id']]
            for assignment in course_assignments:
                grade = random.choice(['A', 'B', 'C', 'D', 'F'])
                grades.append({
                    'grade_id': fake.uuid4(),
                    'course_id': course['course_id'],
                    'student_id': course['student_id'],
                    'assignment_id': assignment['assignment_id'],
                    'grade': grade,
                })

    # Write grades for this chunk to file
    write_csv('grades.csv', grades, ['grade_id', 'course_id', 'student_id', 'assignment_id', 'grade'])
