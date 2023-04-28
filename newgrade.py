import csv

# Define a dictionary to map letter grades to their corresponding percentage test results
grades_mapping = {
    'A+': 97, 'A': 93, 'A-': 90,
    'B+': 87, 'B': 83, 'B-': 80,
    'C+': 77, 'C': 73, 'C-': 70,
    'D+': 67, 'D': 63, 'F': 0
}

# Open the input and output CSV files
with open('grades.csv', 'r') as input_file, open('newGrades.csv', 'w', newline='') as output_file:
    # Create CSV reader and writer objects
    reader = csv.DictReader(input_file)
    writer = csv.DictWriter(output_file, fieldnames=reader.fieldnames + ['Percentage'])
    writer.writeheader()

    # Process each row in the input file
    for row in reader:
        # Look up the percentage for the letter grade in the row
        percentage = grades_mapping.get(row['Letter_grade'], None)

        # Add the percentage to the row as a new column
        row['Percentage'] = percentage

        # Write the updated row to the output file
        writer.writerow(row)
