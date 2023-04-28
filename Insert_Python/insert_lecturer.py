import csv

with open('lecturer.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

queries = []
for row in data:
    query = "INSERT INTO yvle.Lecturer (Lecturer_id, Name, User_id) VALUES ('{}', '{}', '{}');".format(
        row['Lecturer_id'],
        row['Name'],
        row['User_id']
    )
    queries.append(query)

with open('insert_lecturer.sql', 'w') as sqlfile:
    sqlfile.write('\n'.join(queries))