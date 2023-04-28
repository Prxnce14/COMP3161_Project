import csv

with open('sectionItem.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

queries = []
for row in data:
    query = "INSERT INTO yvle.SectionItem (Item_id, Item_name, Item_type, Item_url, Section_id) VALUES ('{}', '{}', '{}', '{}', '{}');".format(
        row['Item_id'],
        row['Item_name'],
        row['Item_type'],
        row['Item_url'],
        row['Section_id']
    )
    queries.append(query)

with open('insert_sectionItem.sql', 'w') as sqlfile:
    sqlfile.write('\n'.join(queries))