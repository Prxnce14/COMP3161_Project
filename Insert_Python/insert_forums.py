import csv

with open('forums.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

queries = []
for row in data:
    query = "INSERT INTO yvle.DiscussionForum (Forum_id, Forum_name, Course_id) VALUES ('{}', '{}', '{}');".format(
        row['Forum_id'],
        row['Forum_name'],
        row['Course_id']
    )
    queries.append(query)

with open('insert_forums.sql', 'w') as sqlfile:
    sqlfile.write('\n'.join(queries))