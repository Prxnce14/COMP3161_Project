import csv

with open('newGrades.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

queries = []
for row in data:
    query = "INSERT INTO yvle.Grade (Grade_id, Letter_grade, Grade, Assignment_id, Student_id) VALUES ('{}', '{}', '{}', '{}', '{}');".format(
        row['Grade_id'],
        row['Letter_grade'],
        row['Grade'],
        row['Assignment_id'],
        row['Student_id']
    )
    queries.append(query)

with open('insert_grades.sql', 'w') as sqlfile:
    sqlfile.write('\n'.join(queries))