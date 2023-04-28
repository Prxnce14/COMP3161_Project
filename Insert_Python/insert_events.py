import csv

with open('events.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

queries = []
for row in data:
    query = "INSERT INTO yvle.CalendarEvent (Event_id, Event_name, Event_description, Event_date, Course_id) VALUES ('{}', '{}', '{}', '{}', '{}');".format(
        row['Event_id'],
        row['Event_name'],
        row['Event_description'],
        row['Event_date'],
        row['Course_id']
    )
    queries.append(query)

with open('insert_events.sql', 'w') as sqlfile:
    sqlfile.write('\n'.join(queries))