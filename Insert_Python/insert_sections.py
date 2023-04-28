import csv

with open('sections.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

queries = []
for row in data:
    query = "INSERT INTO yvle.Section (Section_id, Section_title, Course_id) VALUES ('{}', '{}', '{}');".format(
        row['Section_id'],
        row['Section_title'],
        row['Course_id']
    )
    queries.append(query)

with open('insert_sections.sql', 'w') as sqlfile:
    sqlfile.write('\n'.join(queries))