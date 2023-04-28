import pandas as pd

# Read data from CSV into a pandas dataframe
df = pd.read_csv('cContent.csv')

# Generate SQL queries using dataframe operations
queries = df.apply(
    lambda row: f"INSERT INTO yvle.CourseContent(Content_id, Content_name, Course_id, Content_type, Lecturer_id, Section_id) \
VALUES ('{row['Content_id']}', '{row['Content_name']}', '{row['Course_id']}', '{row['Content_type']}', '{row['Lecturer_id']}', '{row['Section_id']}');",
    axis=1
).tolist()

# Write queries to file
with open('insert_courseContents.sql', 'w') as sqlfile:
    sqlfile.write('\n'.join(queries))
