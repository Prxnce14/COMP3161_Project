import csv

with open('assignment.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

queries = []
for row in data:
    query = "INSERT INTO yvle.Assignment (Assignment_id, Assignment_url, Course_id) VALUES ('{}', '{}', '{}');".format(
        row['Assignment_id'],
        row['Assignment_url'],
        row['Course_id']
    )
    queries.append(query)

with open('insert_assignment.sql', 'w') as sqlfile:
    sqlfile.write('\n'.join(queries))