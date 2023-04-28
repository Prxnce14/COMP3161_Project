

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
    



@Yvle.route('/get_cevent/<course_id>', methods = ['GET'])
def get_cevent(course_id):
    try:
         # connect to database
        con = mysql.connector.connect(user='project1_user', password ='password123',
                                    host = '127.0.0.1',
                                    database = 'Yvle')
        #this creates a cursor
        cur = con.cursor()
        #string formating
        cur.execute(f'SELECT * FROM CalendarEvent WHERE CalendarEvent.Course_id = {course_id};')
        row = cur.fetchone()
        #customer = {}
        if row is not None:
            event_id, event_name, event_des,event_date, c_id = row
            calendar = {}
            calendar['Event ID'] = event_id
            calendar['Event Name'] = event_name
            calendar['Event Description'] = event_des
            calendar['Event Date'] = event_date
            calendar['Course Id'] = c_id
            cur.close()
            con.close()
            return make_response(calendar, 200)
        else:
            return make_response({'error': 'Calendar event not found'}, 400)
    
    except Exception as e:
        return make_response({'error': str(e)}, 400)
    



@Yvle.route('/get_cevent_stud/<stud_id>/<event_date>', methods = ['GET'])
def get_cevent_stud(stud_id,event_date):
    try:
         # connect to database
        con = mysql.connector.connect(user='project1_user', password ='password123',
                                    host = '127.0.0.1',
                                    database = 'Yvle')
        #this creates a cursor
        cur = con.cursor()
        #string formating
        cur.execute(f'SELECT * FROM CalendarEvent JOIN Enrol on CalendarEvent.Course_id = Enrol.Course_id \
                    WHERE Enrol.Student_id = {stud_id} and CalendarEvent.Event_date = {event_date};')
        row = cur.fetchone()
        #customer = {}
        if row is not None:
            event_id, event_name, event_des,event_date, c_id, sid, c_id = row
            calendar = {}
            calendar['Event ID'] = event_id
            calendar['Event Name'] = event_name
            calendar['Event Description'] = event_des
            calendar['Event Date'] = event_date
            calendar['Course Id'] = c_id
            calendar['Student ID'] = sid
            cur.close()
            con.close()
            return make_response(calendar, 200)
        else:
            return make_response({'error': 'Calendar event not found'}, 400)
    
    except Exception as e:
        return make_response({'error': str(e)}, 400)
        



@Yvle.route('/Create_cal_event', methods=['POST'])
def Create_cal_event():
    try:
        con = mysql.connector.connect(user='project1_user', password ='password123',
                                    host = '127.0.0.1',
                                    database = 'Yvle')
        #this creates a cursor
        cur = con.cursor()
        content = request.json
        event_id = content['Event ID']
        event_name = content['Event Name']
        event_des = content['Event Description']
        event_date = content['Event Date']
        event_course = content['Course Id']
    
        cur.execute(f"INSERT INTO yvle.CalendarEvent (Event_id, Event_name, Event_description, Event_date, Course_id) VALUES \
                    ('{event_id}', '{event_name}', '{event_des}', '{event_date}', '{event_course}');")
        con.commit()    
        cur.close()
        con.close()
        return make_response({'message': 'Calendar Event created'}, 200)
    
    except Exception as e:
        print(e)
        return make_response({'error': str(e)}, 400)



    

@Yvle.route('/get_dsic_forums/<course_id>', methods=['GET'])
def get_dsic_forums(course_id):
    try:
        # connect to database
        con = mysql.connector.connect(user='project1_user', password ='password123',
                                    host = '127.0.0.1',
                                    database = 'Yvle')
        #this cretaes a cursor
        cur = con.cursor()
        cur.execute(f"SELECT * FROM DiscussionForum WHERE DiscussionForum.Course_id = '{course_id}' ;")
        forum_list = []
        
        for forum_id, forum_name, c_id in cur:
            Forum = {}
            Forum['Forum ID'] = forum_id
            Forum['Forum Name'] = forum_name
            Forum['Course ID'] = c_id
            forum_list.append(Forum)
        cur.close()
        con.close()
        return forum_list
    
    except Exception as e:
        return make_response({'error': str(e)}, 400)
    



@Yvle.route('/Create_forum', methods=['POST'])
def Create_forum():
    try:
        con = mysql.connector.connect(user='project1_user', password ='password123',
                                    host = '127.0.0.1',
                                    database = 'Yvle')
        #this creates a cursor
        cur = con.cursor()
        content = request.json
        forum_id = content['Forum ID']
        forum_name = content['Forum Name']
        c_id = content['Course ID']
        
        cur.execute(f"INSERT INTO yvle.DiscussionForum (Forum_id, Forum_name, Course_id) VALUES \
                    ('{forum_id}', '{forum_name}', '{c_id}');")
        con.commit()    
        cur.close()
        con.close()
        return make_response({'message': 'Discussion Forum created'}, 200)
    
    except Exception as e:
        print(e)
        return make_response({'error': str(e)}, 400)
    


    
@Yvle.route('/get_disc_thread/<for_id>', methods=['GET'])
def get_disc_thread(for_id):
    try:
        # connect to database
        con = mysql.connector.connect(user='project1_user', password ='password123',
                                    host = '127.0.0.1',
                                    database = 'Yvle')
        #this cretaes a cursor
        cur = con.cursor()
        #string formating
        cur.execute(f'SELECT DiscussionThread.Thread_id, DiscussionThread.Thread_Title, DiscussionThread.Thread_content, \
                      DiscussionThread.User_id, DiscussionThread.Forum_id FROM DiscussionThread \
                        JOIN DiscussionForum ON DiscussionThread.Forum_id = DiscussionForum.Forum_id \
                        WHERE DiscussionForum.Forum_id = {for_id};')
        frum_list= []
        for tr_id, tr_title, tr_content, tr_uid, tr_fid in cur:
            Threads={}
            Threads['Thread ID'] = tr_id 
            Threads['Thread Title']= tr_title
            Threads['Thread Content'] = tr_content
            Threads['User ID'] = tr_uid
            Threads['Forum ID'] = tr_fid
            frum_list.append(Threads)
        cur.close()
        con.close()
        return frum_list
    except Exception as e:
        return make_response({'error': str(e)}, 400)
    




# @Yvle.route('/Create_thread', methods=['POST'])
# def Create_thread():
#     try:
#         # connect to database
#         con = mysql.connector.connect(user='project1_user', password ='password123',
#                                     host = '127.0.0.1',
#                                     database = 'Yvle')
#         cur = con.cursor()
        
#         # get discussio thread from request body
#         content = request.json
        
#         tr_id = content['Thread ID']
#         tr_title = content['Thread Title']
#         tr_content = content['Thread Content']
#         tr_uid = content['User ID']
#         tr_fid = content['Forum ID']


#         # check if forum exists

#         cur.execute(f"SELECT DiscussionThread.Thread_id, DiscussionThread.Thread_Title, DiscussionThread.Thread_content, \
#                       DiscussionThread.User_id, DiscussionThread.Forum_id FROM DiscussionThread \
#                         JOIN DiscussionForum ON DiscussionThread.Forum_id = DiscussionForum.Forum_id \
#                         WHERE DiscussionForum.Forum_id = '{tr_fid}';")
#         existing_forum = cur.fetchone()
#         if existing_forum:
#             # create thread for forum
#             cur.execute(f"INSERT INTO yvle.DiscussionThread (Thread_id, Thread_Title, Thread_content, User_id, Forum_id) VALUES \
#                         ('{tr_id}', '{tr_title}', '{tr_content}', '{tr_uid}', '{tr_fid}');")
#         con.commit()
#         cur.close()
#         con.close()
#         return make_response({'message': 'Discussion thread created'}, 200)

#     except Exception as e:
#         print(e)
#         return make_response({'error': 'An error occurred while Creating the thread'}, 500)




@Yvle.route('/make_thread', methods=['POST'])
def make_thread():
    try:
        # connect to database
        con = mysql.connector.connect(user='project1_user', password ='password123',
                                    host = '127.0.0.1',
                                    database = 'Yvle')
        cur = con.cursor()
        
        # get discussio thread from request body
        content = request.json
        
        tr_id = content['Thread ID']
        tr_title = content['Thread Title']
        tr_content = content['Thread Content']
        tr_uid = content['User ID']
        tr_fid = content['Forum ID']

        # create thread for forum
        cur.execute(f"INSERT INTO yvle.DiscussionThread (Thread_id, Thread_Title, Thread_content, User_id, Forum_id) VALUES \
                    ('{tr_id}', '{tr_title}', '{tr_content}', '{tr_uid}', '{tr_fid}');")
        con.commit()
        cur.close()
        con.close()
        return make_response({'message': 'Discussion thread created'}, 200)

    except Exception as e:
        print(e)
        return make_response({'error': 'An error occurred while Creating the thread'}, 500)




@Yvle.route('/Create_Course_cont', methods=['POST'])
def Create_Course_cont():
    try:
        # connect to database
        con = mysql.connector.connect(user='project1_user', password ='password123',
                                    host = '127.0.0.1',
                                    database = 'Yvle')
        cur = con.cursor()
        
        # get discussio thread from request body
        content = request.json
        
        cont_id = content['Content ID']
        cont_name = content['Content Name']
        c_id = content['Course ID']
        cont_type = content['Content Type']
        lect_id = content['Lecture ID']
        sect_id = content['Section ID']
        t_list = []

        # check if content exists
        cur.execute(f"SELECT CourseContent.Content_id, CourseContent.Content_name, CourseContent.Course_id,\
                     CourseContent.Content_type, CourseContent.Lecturer_id, CourseContent.Section_id \
                     FROM CourseContent JOIN Lecturer ON CourseContent.Lecturer_id = Lecturer.Lecturer_id \
                     WHERE Lecturer.Lecturer_id = '{lect_id}';")
        existing_forum = cur.fetchone()
        t_list.append(existing_forum)
        print(t_list)
        if t_list == []:
            #create the course content
            cur.execute(f'INSERT INTO yvle.CourseContent(Content_id, Content_name, Course_id, Content_type, Lecturer_id, Section_id) VALUES \
                         ({cont_id}, {cont_name}, {c_id}, {cont_type}, {lect_id}, {sect_id});')
        else:
            return make_response({'error': "Content already exists"}, 400)
        con.commit()
        cur.close()
        con.close()
        return make_response({'message': 'Course content created......'}, 200)

    except Exception as e:
        print(e)
        return make_response({'error': 'An error occurred while reading info for course content'}, 500)




@Yvle.route('/get_course_cont/<course_id>', methods = ['GET'])
def get_course_cont(course_id):
    try:
         # connect to database
        con = mysql.connector.connect(user='project1_user', password ='password123',
                                    host = '127.0.0.1',
                                    database = 'Yvle')
        #this creates a cursor
        cur = con.cursor()
        #string formating
        cur.execute(f'SELECT * FROM CourseContent WHERE CourseContent.Course_id = {course_id};')
        row = cur.fetchone()
        #customer = {}
        if row is not None:
            cont_id, cont_name, c_id, cont_type, lect_id, sect_id = row
            Content = {}
            Content['Content ID'] = cont_id
            Content['Content Name'] = cont_name
            Content['Course ID'] = c_id
            Content['Content Type'] = cont_type
            Content['Lecture ID'] = lect_id
            Content['Section ID'] = sect_id
            cur.close()
            con.close()
            return make_response(Content, 200)
        else:
            return make_response({'error': 'Course content is not found'}, 400)
    
    except Exception as e:
        return make_response({'error': str(e)}, 400)