import random
import csv

# Open the CSV files and read the data
with open('students.csv', mode='r') as students_file, open('courses.csv', mode='r') as courses_file:
    students_reader = csv.reader(students_file)
    courses_reader = csv.reader(courses_file)

    # Convert the CSV data to lists
    students = list(students_reader)[1:]  # skip the header row
    courses = [row[0] for row in courses_reader][1:]  # use the first column and skip the header row

# Define the maximum and minimum number of courses per student
max_courses = 6
min_courses = 3

# Shuffle the list of courses
random.shuffle(courses)

# Create a dictionary to store the assigned courses for each student
assigned_courses = {}

# Assign courses to each student
for student in students:
    # Choose a random number of courses between the minimum and maximum
    num_courses = random.randint(min_courses, max_courses)

    # Choose a random subset of courses from the shuffled list
    student_courses = random.sample(courses, num_courses)

    # Add the assigned courses to the dictionary
    assigned_courses[student[1]] = student_courses

# Write the results to a new CSV file
with open('assigned_courses.csv', mode='w', newline='') as assigned_courses_file:
    writer = csv.writer(assigned_courses_file)

    # Write the header row
    writer.writerow(['Student ID', 'Assigned Courses'])

    # Write the assigned courses for each student
    for student_id, courses in assigned_courses.items():
        for course in courses:
            writer.writerow([student_id, course])
