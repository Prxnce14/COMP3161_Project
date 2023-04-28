import csv

with open('assigned_courses.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

queries = []
for row in data:
    query = "INSERT INTO yvle.Enrol (Student_id, Course_id) VALUES ('{}', '{}');".format(
        row['Student_id'],
        row['Course_id']
    )
    queries.append(query)

with open('insert_enrol.sql', 'w') as sqlfile:
    sqlfile.write('\n'.join(queries))