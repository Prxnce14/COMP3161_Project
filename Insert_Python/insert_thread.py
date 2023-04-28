import csv

with open('thread.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

queries = []
for row in data:
    query = "INSERT INTO yvle.DiscussionThread (Thread_id, Thread_Title, Thread_content, User_id, Forum_id) VALUES ('{}', '{}', '{}', '{}', '{}');".format(
        row['Thread_id'],
        row['Thread_Title'],
        row['Thread_content'],
        row['User_id'],
        row['Forum_id']
    )
    queries.append(query)

with open('insert_thread.sql', 'w') as sqlfile:
    sqlfile.write('\n'.join(queries))