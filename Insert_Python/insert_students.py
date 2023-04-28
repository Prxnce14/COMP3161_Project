import csv

with open('students.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

queries = []
for row in data:
    query = "INSERT INTO yvle.Student (Student_id, Name, User_id) VALUES ('{}', '{}', '{}');".format(
        row['Student_id'],
        row['Name'],
        row['User_id']
    )
    queries.append(query)

with open('insert_students.sql', 'w') as sqlfile:
    sqlfile.write('\n'.join(queries))