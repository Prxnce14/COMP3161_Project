import pandas as pd

# Read CSV file into a Pandas DataFrame
df = pd.read_csv('course.csv')

# Generate SQL queries using DataFrame.apply() method
queries = df.apply(lambda row: f"INSERT INTO yvle.Course (course_id, Course_Name, Course_admin) VALUES ('{row['course_id']}', '{row['Course_Name']}', '{row['Course_admin']}');", axis=1)

# Write queries to a SQL file
with open('insert_courses.sql', 'w') as sqlfile:
    sqlfile.write('\n'.join(queries))
