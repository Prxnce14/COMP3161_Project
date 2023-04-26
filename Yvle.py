

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
    
    

