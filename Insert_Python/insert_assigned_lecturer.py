import csv

with open('assigned_lecturer.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

queries = []
for row in data:
    query = "INSERT INTO yvle.Teach_connect (Course_id, Lecturer_ID) VALUES ('{}', '{}');".format(
        row['Course_code'],
        row['Lecturer_ID']
    )
    queries.append(query)

with open('insert_Teach_connect.sql', 'w') as sqlfile:
    sqlfile.write('\n'.join(queries))