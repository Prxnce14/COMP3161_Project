import csv

with open('member.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

queries = []
for row in data:
    query = "INSERT INTO yvle.Member (Member_id, User_id, Course_id) VALUES ('{}', '{}', '{}');".format(
        row['Member_id'],
        row['User_id'],
        row['Course_id']
    )
    queries.append(query)

with open('insert_member.sql', 'w') as sqlfile:
    sqlfile.write('\n'.join(queries))