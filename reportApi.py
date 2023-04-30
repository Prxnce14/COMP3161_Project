from flask import Flask, jsonify, request, make_response
import mysql.connector

Yvle = Flask(__name__)

#Get courses that have 50 or more students

@Yvle.route('/courses50', methods=['GET'])
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

@Yvle.route('/student5_orMore', methods=['GET'])
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
@Yvle.route('/Lecturer3_orMore', methods=['GET'])
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

@Yvle.route('/Most_Enrolled', methods=['GET'])
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
@Yvle.route('/Avg_Grade ', methods=['GET'])
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


@Yvle.route('/register_course', methods=['POST'])
def register_course():
    try:
        con = mysql.connector.connect(user='root', password='Ashur@2018',
                                   host='localhost',
                                   database='yvle')
        cur = con.cursor()

        content = request.json
        username = content.get('Student ID') or content.get('Lecturer ID')
        c_id = content['Course ID']
        user_id = content['User ID']
        cur.execute(f"SELECT * FROM course WHERE Course_id = %s", (c_id,))
        course = cur.fetchone()
        if not course:
            return make_response(jsonify({'error': 'Course not found'}), 404)
        cur.execute(f"SELECT * FROM Account WHERE User_id = %s", (user_id,))
        account = cur.fetchone()
        if not account:
            return make_response(jsonify({'error': 'Invalid user ID or user type'}), 401)
        if account[1] == 'Lecturer':
            cur.executef(f"SELECT * FROM teach_connect WHERE Course_id = %s", (c_id,))
            lecturer = cur.fetchone()
            if lecturer:
                return make_response(jsonify({'error': 'Another lecturer is already assigned to the course'}), 409)
            cur.execute(f"INSERT INTO yvle.Member (Member_id, User_id, Course_id) VALUES ('{username}', '{user_id}', '{c_id}');")
            cur.execute(f"INSERT INTO yvle.teach_connect (Lecturer_id, Course_id) VALUES ('{username}', '{c_id}');")
        elif account[1] == 'Student':
            cur.execute("SELECT * FROM Enrol WHERE Course_id = %s AND Student_id = %s", (c_id, username))
            existing_registration = cur.fetchone()
            if existing_registration:
                return make_response(jsonify({'error': 'Student already registered for the course'}), 409)
            cur.execute(f"INSERT INTO yvle.Enrol (Student_id, Course_id) VALUES ('{username}', '{c_id}');")
            cur.execute(f"INSERT INTO yvle.Member (Member_id, User_id, Course_id) VALUES ('{username}', '{user_id}', '{c_id}');")

        con.commit()
        cur.close()
        con.close()

        return make_response(jsonify({'success': True}), 200)
    
    except Exception as e:
        print(e)
        return make_response({'error': 'This User has already been registered'}, 400)
    

if __name__ == '__main__':
    Yvle.run(port=5000)
