import csv

with open('user.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

queries = []
for row in data:
    query = "INSERT INTO yvle.User (User_id, Username, Password) VALUES ('{}', '{}', '{}');".format(
        row['User_id'],
        row['Username'],
        row['Password']
    )
    queries.append(query)

with open('insert_users.sql', 'w') as sqlfile:
    sqlfile.write('\n'.join(queries))