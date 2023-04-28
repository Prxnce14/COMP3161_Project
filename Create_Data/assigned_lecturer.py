import csv

# Define the input file paths
lecturer_file = "lecturer.csv"
courses_file = "courses.csv"

# Define the output file path
output_file = "assigned_lecturer.csv"

# Read in the lecturer data
with open(lecturer_file, 'r') as f:
    lecturer_data = list(csv.reader(f))[1:]  # skip the first row

# Read in the courses data
with open(courses_file, 'r') as f:
    courses_data = list(csv.reader(f))[1:]  # skip the first row

# Assign courses to lecturers
assignments = []
for course in courses_data:
    # Find a lecturer who can teach this course
    lecturer_found = False
    for lecturer in lecturer_data:
        if lecturer[1] not in [x[1] for x in assignments] and len([x for x in assignments if x[0] == lecturer[1]]) < 5:
            # check lecturer has not been assigned a course yet and is not teaching five courses
            assignments.append([course[0], lecturer[1]])
            lecturer_found = True
            break
    # If no suitable lecturer was found, assign the course to the lecturer with the least number of assigned courses
    if not lecturer_found:
        min_assigned_courses = min([len([x for x in assignments if x[1] == lecturer[1]]) for lecturer in lecturer_data])
        lecturer_with_min_courses = [lecturer for lecturer in lecturer_data if len([x for x in assignments if x[1] == lecturer[1]]) == min_assigned_courses][0]
        assignments.append([course[0], lecturer_with_min_courses[1]])

# Write the assignments to a new CSV file
with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Course_code", "Lecturer_ID"])  # write the headings
    writer.writerows(assignments)
