

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
def user_login(u_id, pass_word): 
    try:
        con = mysql.connector.connect(user='project1_user', password ='password123',
                                    host = '127.0.0.1',
                                    database = 'Yvle')
        #this creates a cursor
        cur = con.cursor()
        #string formating
        cur.execute(f"SELECT * FROM user WHERE user_id = '{u_id}' HAVING Password = '{pass_word}';") 
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
            return make_response(user, 200)
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

        # get course details from request body
        content = request.json
        c_id = content['Course_id']
        c_name = content['Course_name']
        Adm_id = content['Admin_id']

        cur.execute(f"SELECT * FROM Account WHERE user_id = '{Adm_id}' and Account.Account_type = 'Admin';")
        row = cur.fetchone()
        if row is not None:
            # insert course into database
            cur.execute(f"INSERT INTO Course (Course_id, Course_Name, Course_admin) VALUES ('{c_id}', '{c_name}', '{Adm_id}')")
        else:
            return make_response({'Error': 'This Account is not of type Admin'})
        con.commit()
        cur.close()
        con.close()
        return make_response(jsonify({'message': 'Course created successfully'}), 201)

    except Exception as e:
        print(e)
        return make_response({'error': str(e)}, 400) 
    


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

        # my_list = []
        content = request.json
        username = content.get('Student ID') 
        lec_id = content['Lecturer ID']
        c_id = content['Course ID']
        user_id = content['User ID']
        name = content['Name']

        cur.execute(f"SELECT * FROM course WHERE Course_id = %s", (c_id,))
        course = cur.fetchone()
        if not course:
            return make_response(jsonify({'error': 'Course not found'}), 404)
        cur.execute(f"SELECT * FROM Account WHERE User_id = %s", (user_id,))
        account = cur.fetchone()
        # my_list.append(account)
        # print(my_list[0])
        print(lec_id)

        if account is None:
            return make_response(jsonify({'error': 'Invalid user ID or user type'}), 401)
        print("me")
        if lec_id.startswith('8'):
            cur.execute(f"SELECT * FROM teach_connect WHERE Course_id = '{c_id}';")
            print("hi")
            lecturer = cur.fetchone()
            if lecturer is not None:
                return make_response(jsonify({'error': 'Another lecturer is already assigned to the course'}), 409)
            else:
                cur.execute(f"INSERT INTO yvle.Lecturer (Lecturer_id, Name, User_id) VALUES ('{lec_id}', '{name}', '{user_id}');")
                cur.execute(f"INSERT INTO yvle.Member (Member_id, User_id, Course_id) VALUES ('{lec_id}', '{user_id}', '{c_id}');")
                cur.execute(f"INSERT INTO yvle.Teach_connect (Course_id, Lecturer_ID) VALUES ('{c_id}', '{lec_id}');")
                print("bye")
        elif username.startswith('6'):
            cur.execute("SELECT * FROM Enrol WHERE Course_id = %s AND Student_id = %s", (c_id, username))
            existing_registration = cur.fetchone()
            if existing_registration is not None:
                return make_response(jsonify({'error': 'Student already registered for the course'}), 409)
            else:
                cur.execute(f"INSERT INTO yvle.Student (Student_id, Name, User_id) VALUES ('{username}', '{name}', '{user_id}');")
                cur.execute(f"INSERT INTO yvle.Enrol (Student_id, Course_id) VALUES ('{username}', '{c_id}');")
                cur.execute(f"INSERT INTO yvle.Member (Member_id, User_id, Course_id) VALUES ('{username}', '{user_id}', '{c_id}');")

        con.commit()
        cur.close()
        con.close()

        return make_response(jsonify({'success': True}), 200)
    
    except Exception as e:
        print(e)
        return make_response({'error': 'This User has already been registered'}, 400)



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

        #check if the forum exists
        cur.execute(f"SELECT DiscussionForum.Forum_id FROM DiscussionForum \
                    WHERE DiscussionForum.Forum_id = '{tr_fid}';")
        row = cur.fetchone()
        if row is not None:
            # create thread for forum
            cur.execute(f"INSERT INTO yvle.DiscussionThread (Thread_id, Thread_Title, Thread_content, User_id, Forum_id) VALUES \
                        ('{tr_id}', '{tr_title}', '{tr_content}', '{tr_uid}', '{tr_fid}');")
        else:           
            return make_response({'error': "Discussion forum does not exist"}, 400)
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

        # check if content exists
        cur.execute(f"SELECT Lecturer_id FROM Lecturer WHERE Lecturer.Lecturer_id = '{lect_id}';")
        row = cur.fetchone()
        if row is not None:
            #create the course content
            cur.execute(f"INSERT INTO yvle.CourseContent(Content_id, Content_name, Course_id, Content_type, Lecturer_id, Section_id) VALUES \
                         ('{cont_id}', '{cont_name}', '{c_id}', '{cont_type}', '{lect_id}', '{sect_id}');")
        else:            
            return make_response({'error': "Content already exists"}, 400)

        
        con.commit()
        cur.close()
        con.close()
        return make_response({'message': 'Course content created'}, 200)

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
    



@Yvle.route('/student_assignment', methods=['POST'])
def student_assignment():
    try:
        # connect to database
        con = mysql.connector.connect(user='project1_user', password ='password123',
                                    host = '127.0.0.1',
                                    database = 'Yvle')
        cur = con.cursor()
        
        # get discussio thread from request body
        content = request.json
        
        assign_id = content['Assignment ID']
        assign_url = content['Assignment URL']
        c_id = content['Course ID']

        # submit assignment for student
        cur.execute(f"INSERT INTO yvle.Assignment (Assignment_id, Assignment_url, Course_id) VALUES \
                    ('{assign_id}', '{assign_url}', '{c_id}');")
        con.commit()
        cur.close()
        con.close()
        return make_response({'message': 'Assignment Succesfully submitted'}, 200)

    except Exception as e:
        print(e)
        return make_response({'error': "An error occurred while submitting the student's assignment"}, 500)



@Yvle.route('/student_grade', methods=['POST'])
def student_grade():
    try:
        # connect to database
        con = mysql.connector.connect(user='project1_user', password ='password123',
                                    host = '127.0.0.1',
                                    database = 'Yvle')
        cur = con.cursor()
        
        # get discussio thread from request body
        content = request.json
        
        g_id = content['Grade ID']
        l_grade = content['Letter Grade']
        grade = content['Grade']
        assign_id = content['Assignment ID']
        stud_id = content['Student ID']

        cur.execute(f"SELECT Student_id FROM Student WHERE Student.Student_id = '{stud_id}' ;")
        row = cur.fetchone()
        if row is not None:
            # submit assignment for student
            cur.execute(f"INSERT INTO yvle.Grade (Grade_id, Letter_grade, Grade, Assignment_id, Student_id) VALUES \
                        ('{g_id}', '{l_grade}', '{grade}', '{assign_id}', '{stud_id}');")
        else:            
            return make_response({'error': "Student does not exists"}, 400)
            
            
        con.commit()
        cur.close()
        con.close()
        return make_response({'message': 'Assignment grade succesfully submitted'}, 200)

    except Exception as e:
        print(e)
        return make_response({'error': "An error occurred while submitting the student's assignment grade"}, 500)



@Yvle.route('/get_final_avg/<stud_id>', methods = ['GET'])
def get_final_avg(stud_id):
    try:
        # connect to database
        con = mysql.connector.connect(user='project1_user', password ='password123',
                                    host = '127.0.0.1',
                                    database = 'Yvle')
        #this creates a cursor
        cur = con.cursor()
        #string formating
        cur.execute(f"SELECT Grade.Student_id, Student.Name, AVG(Grade) AS Grade_Average FROM Grade \
                    JOIN Student ON Grade.Student_id = Student.Student_id WHERE Student.Student_id = '{stud_id}'\
                    GROUP BY Grade.Student_id;")
        row = cur.fetchone()
        #customer = {}
        if row is not None:
            stud_id, stud_name, avg, = row
            Content = {}
            Content['Student ID'] = stud_id
            Content['Student Name'] = stud_name
            Content['Grade Average'] = avg
        
            cur.close()
            con.close()
            return make_response(Content, 200)
        else:
            return make_response({'error': 'Could not load student Average '}, 400)
    
    except Exception as e:
        return make_response({'error': str(e)}, 400)
    


###########################################################################################    


@Yvle.route('/courses50', methods=['GET'])
def get_courses50():
    try:
        # connect to database
        con = mysql.connector.connect(user='project1_user', password ='password123',
                                    host = '127.0.0.1',
                                    database = 'Yvle')
        
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
        con = mysql.connector.connect(user='project1_user', password ='password123',
                                    host = '127.0.0.1',
                                    database = 'Yvle')
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM Student5_orMore ")
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
        con = mysql.connector.connect(user='project1_user', password ='password123',
                                    host = '127.0.0.1',
                                    database = 'Yvle')
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
        con = mysql.connector.connect(user='project1_user', password ='password123',
                                    host = '127.0.0.1',
                                    database = 'Yvle')
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
        con = mysql.connector.connect(user='project1_user', password ='password123',
                                    host = '127.0.0.1',
                                    database = 'Yvle')
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
    Yvle.run(port=5000)