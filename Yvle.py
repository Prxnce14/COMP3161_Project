

from flask import Flask, jsonify, request, make_response
import mysql.connector

Yvle = Flask(__name__)

users = []

@Yvle.route('/tester', methods = ['GET'])
def tester():
    return "This is my tester for Project 1"


@Yvle.route('/register_user', methods=['POST'])
def register_user():
    try:
        con = mysql.connector.connect(user='project1_user', password ='password123',
                                    host = '127.0.0.1',
                                    database = 'Yvle')
        #this creates a cursor
        cur = con.cursor()
        content = request.json
        u_id = content['Id_Number']
        u_name = content['Username']
        p_word = content['Password']
        #Insert code to test against existing records
        cur.execute(f"INSERT INTO User (User_id, Username, Password) VALUES('{u_id}','{u_name}','{p_word}')")
        con.commit()    
        cur.close()
        con.close()
        return make_response(jsonify({'message': 'User has been registered successfully'}), 201)
    
    except Exception as e:
        print(e)
        return make_response({'error': 'This User has already been registered'}, 400)
    

#User Login
@Yvle.route('/user_login/<u_id>/<pass_word>', methods=['GET']) #
def user_login(u_id, pass_word): #<pass_word>
    try:
        con = mysql.connector.connect(user='project1_user', password ='password123',
                                    host = '127.0.0.1',
                                    database = 'Yvle')
        #this creates a cursor
        cur = con.cursor()
        #string formating
        cur.execute(f'SELECT * FROM user WHERE user_id = {u_id} HAVING Password = {pass_word};') 
        row = cur.fetchone()
         # If the user exists in the database and the password is correct, log them in
        #customer = {}
        if row is not None:
            user_id, name, pass_w = row 
            user = {}
            user['User_id'] = user_id
            user['Name'] = name
            user['Password'] = pass_w
            cur.close()
            con.close()
            return make_response('User succesfully logged in', 200)
        else:
            return make_response({'error':  'Invalid Id number or password'})       

    except Exception as e:
        return make_response({'error': str(e)}, 400) 
    


@Yvle.route('/add_course', methods=['POST'])
def add_course():
    try:
        # connect to database
        con = mysql.connector.connect(user='project1_user', password ='password123',
                                    host = '127.0.0.1',
                                    database = 'Yvle')
        #this cretaes a cursor
        cur = con.cursor()

        # check if user is an admin
        # auth_header = request.headers.get('Authorization')
        # if auth_header != 'Bearer admin_token':
        #     return make_response(jsonify({'error': 'Unauthorized access'}), 401)

        # get course details from request body
        content = request.json
        c_id = content['Course_id']
        c_name = content['Course_name']
        Adm_id = content['Admin_id']

        # insert course into database
        cur.execute(f"INSERT INTO Course (Course_id, Course_Name, Course_admin) VALUES ('{c_id}', '{c_name}', '{Adm_id}')")
        con.commit()
        cur.close()
        con.close()
        return make_response(jsonify({'message': 'Course created successfully'}), 201)

    except Exception as e:
        print(e)
        return make_response({'error': str(e)}, 400) 
    
        #return make_response(jsonify({'error': 'An error occurred while creating the course'}), 500)



@Yvle.route('/get_courses', methods=['GET'])
def get_courses():
    try:
        # connect to database
        con = mysql.connector.connect(user='project1_user', password ='password123',
                                    host = '127.0.0.1',
                                    database = 'Yvle')
        #this cretaes a cursor
        cur = con.cursor()
        cur.execute('SELECT Course_id, Course_Name FROM course;')
        c_list = []
        for c_id, c_name in cur:
            courses={}
            courses['Course Id'] = c_id
            courses['Course Name']= c_name
            c_list.append(courses)
        cur.close()
        con.close()
        return c_list
    except Exception as e:
        return make_response({'error': str(e)}, 400)
    


@Yvle.route('/get_stud_courses/<stud_id>', methods=['GET'])
def get_stud_courses(stud_id):
    try:
        # connect to database
        con = mysql.connector.connect(user='project1_user', password ='password123',
                                    host = '127.0.0.1',
                                    database = 'Yvle')
        #this cretaes a cursor
        cur = con.cursor()
        #string formating
        cur.execute(f'SELECT course.Course_id, course.Course_Name FROM course \
                     JOIN Enrol ON course.Course_id = Enrol.Course_id JOIN Student on Student.Student_id = Enrol.Student_id\
                     WHERE Student.Student_id = {stud_id};')
        sc_list= []
        for c_id, c_name in cur:
            courses={}
            courses['Course Id'] = c_id
            courses['Course Name']= c_name
            sc_list.append(courses)
        cur.close()
        con.close()
        return sc_list
    except Exception as e:
        return make_response({'error': str(e)}, 400)
    

    
@Yvle.route('/get_lec_courses/<lec_id>', methods=['GET'])
def get_lec_courses(lec_id):
    try:
        # connect to database
        con = mysql.connector.connect(user='project1_user', password ='password123',
                                    host = '127.0.0.1',
                                    database = 'Yvle')
        #this cretaes a cursor
        cur = con.cursor()
        #string formating
        cur.execute(f'SELECT course.Course_id, course.Course_Name FROM course JOIN \
                    Lecturer ON course.Course_admin = Lecturer.User_id WHERE Lecturer.User_id ={lec_id};')
        lc_list= []
        for c_id, c_name in cur:
            courses={}
            courses['Course Id'] = c_id 
            courses['Course Name']= c_name
            lc_list.append(courses)
        cur.close()
        con.close()
        return lc_list
    except Exception as e:
        return make_response({'error': str(e)}, 400)
    
    
@Yvle.route('/register_course', methods=['POST'])
def register_course():
    try:
        # connect to database
        con = mysql.connector.connect(user='project1_user', password ='password123',
                                    host = '127.0.0.1',
                                    database = 'Yvle')
        cur = con.cursor()
        # check if user is a student
        # auth_header = request.headers.get('Authorization')
        # if not auth_header.startswith('Bearer student_token'):
        #     return make_response(jsonify({'error': 'Unauthorized access'}), 401)

        # get course id from request body
        content = request.json
        
        stud_name = content['Student Name']
        stud_id = content['Student ID']
        c_id = content['Course ID']
        adm_id = content['Admin ID']


        # check if course exists
        cur.execute(f"SELECT * FROM course WHERE course.Course_id = '{c_id}'")
        course = cur.fetchone()
        if not course:
            return make_response(jsonify({'error': 'Course not found'}), 404)

        # check if student is already registered for the course
        # student_id = auth_header.split()[1]
        cur.execute(f"SELECT * FROM Student JOIN Enrol on Student.Student_id = Enrol.Student_id JOIN \
                        course on course.Course_id = Enrol.Course_id where Student.Student_id = '{stud_id}' and \
                        course.Course_id = '{c_id}'")
        existing_registration = cur.fetchone()
        if existing_registration:
            return make_response(jsonify({'error': 'Student already registered for the course'}), 409)
        else :

            # register student for the course
            cur.execute(f"INSERT INTO yvle.Student (Student_id, Name, User_id) VALUES ('{stud_id}', '{stud_name}', '{adm_id}');")

            cur.execute(f"INSERT INTO yvle.Enrol (Student_id, Course_id) VALUES ('{stud_id}', '{c_id}');")

            cur.execute(f"INSERT INTO yvle.Member (Member_id, User_id, Course_id) VALUES ('{stud_id}', '{adm_id}', '{c_id}');")

        con.commit()
        cur.close()
        con.close()
        return make_response(jsonify({'message': 'Student Succesfully registered and enrolled'}), 201)

    except Exception as e:
        print(e)
        return make_response(jsonify({'error': 'An error occurred while registering for the course'}), 500)




@Yvle.route('/get_members/<course_id>', methods=['GET'])
def get_members(course_id):
    try:
        # connect to database
        con = mysql.connector.connect(user='project1_user', password ='password123',
                                    host = '127.0.0.1',
                                    database = 'Yvle')
        #this cretaes a cursor
        cur = con.cursor()
        cur.execute(f"SELECT * FROM Member WHERE Member.Course_id = '{course_id}' ;")
        mem_list = []
        
        for memb_id, u_id, c_id in cur:
            Member = {}
            Member['Member ID'] = memb_id
            Member['User ID'] = u_id
            Member['Course ID'] = c_id
            mem_list.append(Member)
        cur.close()
        con.close()
        return mem_list
    
    except Exception as e:
        return make_response({'error': str(e)}, 400)