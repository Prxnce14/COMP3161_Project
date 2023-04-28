from flask import Flask, jsonify, request, make_response
import mysql.connector

app = Flask(__name__)

#Get courses that have 50 or more students

@app.route('/courses50', methods=['GET'])
def get_courses50():
    try:
        # connect to database
        con = mysql.connector.connect(user='project1_user', password='password123',
                                       host='127.0.0.1',
                                       database='yvle')
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM Course50")
        course_list = []
        for course_id, num_students in cursor:
            course = {}
            course['course_id'] = course_id
            course['num_students'] = num_students
            course_list.append(course)
        cursor.close()
        con.close()
        return make_response(jsonify(course_list), 200)

    except Exception as e:
        print(e)
        return make_response(jsonify({'error': 'An error occurred while retreiving this view'}), 500)


#get all student that does more than 5 courses

@app.route('/student5_orMore', methods=['GET'])
def get_student5_orMore():
    try:
        # connect to database
        con = mysql.connector.connect(user='project1_user', password='password123',
                                       host='127.0.0.1',
                                       database='yvle')
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM student5_orMore")
        student_list = []
        for student_id, num_courses in cursor:
            student = {}
            student['student_id'] = student_id
            student['num_courses'] = num_courses
            student_list.append(student)
        cursor.close()
        con.close()
        return make_response(jsonify(student_list), 200)

    except Exception as e:
        print(e)
        return make_response(jsonify({'error': 'An error occurred while retreiving this view'}), 500)


#get all lectures that teach 3 or more courses 
@app.route('/Lecturer3_orMore', methods=['GET'])
def get_Lecturer3_orMore():
    try:
        # connect to database
        con = mysql.connector.connect(user='project1_user', password='password123',
                                       host='127.0.0.1',
                                       database='yvle')
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM Lecturer3_orMore")
        lecturer_list = []
        for Lecturer_id, num_courses in cursor:
            lecturer = {}
            lecturer['Lecturer_id'] = Lecturer_id
            lecturer['num_courses'] = num_courses
            lecturer_list.append(lecturer)
        cursor.close()
        con.close()
        return make_response(jsonify(lecturer_list), 200)

    except Exception as e:
        print(e)
        return make_response(jsonify({'error': 'An error occurred while retreiving this view'}), 500)

# get the 10 most enrolled courses

@app.route('/Most_Enrolled', methods=['GET'])
def get_Most_Enrolled():
    try:
        # connect to database
        con = mysql.connector.connect(user='project1_user', password='password123',
                                       host='127.0.0.1',
                                       database='yvle')
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM Most_Enrolled")
        enrol_list = []
        for course_id, num_students in cursor:
            enrol = {}
            enrol['course_id'] = course_id
            enrol['num_courses'] = num_students
            enrol_list.append(enrol)
        cursor.close()
        con.close()
        return make_response(jsonify(enrol_list), 200)

    except Exception as e:
        print(e)
        return make_response(jsonify({'error': 'An error occurred while retreiving this view'}), 500)


# get top 10 student woth the highest overall average
@app.route('/Avg_Grade ', methods=['GET'])
def get_Avg_Grade ():
    try:
        # connect to database
         con = mysql.connector.connect(user='project1_user', password='password123',
                                       host='127.0.0.1',
                                       database='yvle')
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM Avg_Grade ")
        student_list = []
        for student_id, avg_grade in cursor:
            student = {}
            student['student_id'] = student_id
            student['avg_grade'] = avg_grade
            student_list.append(student)
        cursor.close()
        con.close()
        return make_response(jsonify(student_list), 200)

    except Exception as e:
        print(e)
        return make_response(jsonify({'error': 'An error occurred while retreiving this view'}), 500)




if __name__ == '__main__':
    app.run(port=5000)
