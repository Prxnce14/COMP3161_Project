import csv

with open('account.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

queries = []
for row in data:
    query = "INSERT INTO yvle.Account (Account_name, Account_type, User_id) VALUES ('{}', '{}', '{}');".format(
        row['Account_name'],
        row['Account_type'],
        row['User_id']
    )
    queries.append(query)

with open('insert_accounts.sql', 'w') as sqlfile:
    sqlfile.write('\n'.join(queries))