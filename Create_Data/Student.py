import csv
from faker import Faker
import random

#createing an instance of the faker library whiich is used to generate the fake students
fake = Faker()

#creating an empty list that contains one tuple with the headers for the csv file
data = [('Full Name', 'Student ID', 'User ID')]
#creates two empty set one to hold the studentid and user id
student_ids = set()
user_ids = set()

#looping through 100,000 iterations to generate the student data
for i in range(100000):
    #generating a unique 10 digit student id that begins with 6
    while True:
        student_id = '6' + str(random.randint(100000000, 999999999))
        if student_id not in student_ids: #checks to ensure the student id does not already exist in the set
            student_ids.add(student_id) #adds the student id to the set after checking it does not exist in the set
            break #exists the while loop and continue to the next iteration in  the for loop 

    #generating a unique 5 digit user id that begins with 7        
    while True:
        user_id = '7' + str(random.randint(1000, 9999))
        if user_id not in user_ids: #checks to ensure the user id is not in the set
            user_ids.add(user_id) #adds the user id after checking it does not already exist
            break #exists the while loop and continue to the next iteration in  the for loop 

    #uusinf the fake object generates a fake first name and last name then concatinating it to form a full string 
    full_name = fake.first_name() + ' ' + fake.last_name()
    data.append((full_name, student_id, user_id)) #creates a new tuple with the fake data and appends it to the data list 

#concatenate the header with the data and sort by student id
data = data[0] + sorted(data[1:], key=lambda x: x[1])

#opens a new student.csv file and creating a csv.writer object to writes each element from the data list to the student.csv file
with open('students.csv', mode='w', newline='') as file:
    writer = csv.writer(file) 
    writer.writerows(data)
