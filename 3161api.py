#Register user
from flask import Flask, jsonify, request, make_response
import mysql.connector

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    # Parse request data
    data = request.get_json()
    user_id=['user_id']
    username = data['username']
    password = data['password']
    
    # Hash password
    hashed_password = generate_hashed_password(password)
    
    # Insert new user into database
    cursor = cnx.cursor()
    insert_query = "INSERT INTO Users (user_id,username, hashed_password, role) VALUES (%s, %s, %s)"
    values = (user_id, username, hashed_password)
    cursor.execute(insert_query, values)
    cnx.commit()
    user_id = cursor.lastrowid
    cursor.close()
    
    # Return success response
    response_data = {'user_id': user_id}
    response = make_response(jsonify(response_data), 201)
    return response



#Add course
from flask import Flask, jsonify, request, make_response
import mysql.connector

app = Flask(__name__)

@app.route('/add_course', methods=['POST'])
def add_course():
    try:
        # connect to database
        con = mysql.connector.connect(user='admin', password='password',
                                       host='localhost',
                                       database='yvle')
        cursor = con.cursor()

        # check if user is an admin
        auth_header = request.headers.get('Authorization')
        if auth_header != 'Bearer admin_token':
            return make_response(jsonify({'error': 'Unauthorized access'}), 401)

        # get course details from request body
        content = request.json
        c_id = content['c_id']
        c_name = content['c_name']

        # insert course into database
        cursor.execute(f"INSERT INTO courses (c_id, c_name) VALUES ('{c_id}', '{c_name}')")
        con.commit()

        cursor.close()
        con.close()
        return make_response(jsonify({'message': 'Course created successfully'}), 201)

    except Exception as e:
        print(e)
        return make_response(jsonify({'error': 'An error occurred while creating the course'}), 500)


#Get course
from flask import Flask, jsonify, request, make_response
import mysql.connector

app = Flask(__name__)

@app.route('/courses', methods=['GET'])
def get_courses():
    try:
        # connect to database
        con = mysql.connector.connect(user='admin', password='password',
                                       host='localhost',
                                       database='yvle')
        cursor = con.cursor()

        # get query parameters
        student_id = request.args.get('student_id')
        lecturer_id = request.args.get('lecturer_id')

        # retrieve courses based on query parameters
        if student_id:
            cursor.execute(f"SELECT course.c_id, course.c_name FROM course INNER JOIN student ON student.c_id = courses.id WHERE student.student_id = '{student_id}'")
        elif lecturer_id:
            cursor.execute(f"SELECT course.name, course.description FROM course INNER JOIN lecturer ON lecturer.c_id = courses.id WHERE lecturer.lecturer_id = '{lecturer_id}'")
        else:
            cursor.execute("SELECT name, description FROM course")
        
        course = cursor.fetchall()

        cursor.close()
        con.close()
        return make_response(jsonify({'course': course}), 200)

    except Exception as e:
        print(e)
        return make_response(jsonify({'error': 'An error occurred while retrieving courses'}), 500)


#Register for a course
from flask import Flask, jsonify, request, make_response
import mysql.connector

app = Flask(__name__)

@app.route('/register_course', methods=['POST'])
def register_course():
    try:
        # connect to database
        con = mysql.connector.connect(user='admin', password='password',
                                       host='localhost',
                                       database='yvle')
        cursor = con.cursor()

        # check if user is a student
        auth_header = request.headers.get('Authorization')
        if not auth_header.startswith('Bearer student_token'):
            return make_response(jsonify({'error': 'Unauthorized access'}), 401)

        # get course id from request body
        content = request.json
        c_id = content['c_id']

        # check if course exists
        cursor.execute(f"SELECT * FROM course WHERE id = '{c_id}'")
        course = cursor.fetchone()
        if not course:
            return make_response(jsonify({'error': 'Course not found'}), 404)

        # check if student is already registered for the course
        student_id = auth_header.split()[1]
        cursor.execute(f"SELECT * FROM student WHERE student_id = '{student_id}' AND c_id = '{c_id}'")
        existing_registration = cursor.fetchone()
        if existing_registration:
            return make_response(jsonify({'error': 'Student already registered for the course'}), 409)

        # register student for the course
        cursor.execute(f"INSERT INTO student (student_id, c_id) VALUES ('{student_id}', '{c_id}')")
        con.commit()

        cursor.close()
        con.close()
        return make_response(jsonify({'message': 'Student registered for course successfully'}), 201)

    except Exception as e:
        print(e)
        return make_response(jsonify({'error': 'An error occurred while registering for the course'}), 500)

#Retrieve members
from flask import Flask, jsonify, request, make_response
import mysql.connector

app = Flask(__name__)

@app.route('/members/<int:c_id>', methods=['GET'])
def get_members(c_id):
    try:
        # connect to database
        con = mysql.connector.connect(user='admin', password='password',
                                       host='localhost',
                                       database='yvle')
        cursor = con.cursor()

        # retrieve course members
        cursor.execute(f"SELECT student.id, student.name, student.user_id FROM student INNER JOIN student ON student.student_id = student.id WHERE student.c_id = '{c_id}'")
        members = cursor.fetchall()

        cursor.close()
        con.close()
        return make_response(jsonify({'members': members}), 200)

    except Exception as e:
        print(e)
        return make_response(jsonify({'error': 'An error occurred while retrieving course members'}), 500)

    
    
from flask import Flask, jsonify, request, make_response
import mysql.connector

app = Flask(__name__)

# Connect to the database
con = mysql.connector.connect(user='admin', password='password', host='localhost', database='yvle')
cursor = con.cursor()

# Endpoint to retrieve all the forums for a particular course
@app.route('/discussionforums/<int:c_id>', methods=['GET'])
def get_forums(c_id):
    try:
        # Query the database for all forums for the specified course
        cursor.execute(f"SELECT * FROM forums WHERE c_id = {c_id}")
        discussionforums = cursor.fetchall()

        # Return the forums as JSON
        return jsonify(discussionforums), 200

    except Exception as e:
        print(e)
        return make_response(jsonify({'error': 'An error occurred while retrieving the forums'}), 500)

# Endpoint to create a forum for a particular course
@app.route('/forums', methods=['POST'])
def create_forum():
    try:
        # Get the forum details from the request body
        content = request.json
        c_id = content['c_id']
        forum_id = content['forum_id']
        forum_name = content['forum_name']

        # Insert the forum into the database
        cursor.execute(f"INSERT INTO discussionforums (c_id, forum_name) VALUES ({c_id}, '{forum_id}','{forum_name}')")
        con.commit()

        return make_response(jsonify({'message': 'Forum created successfully'}), 201)

    except Exception as e:
        print(e)
        return make_response(jsonify({'error': 'An error occurred while creating the forum'}), 500)

if __name__ == '__main__':
    app.run()



from flask import Flask, jsonify, request, make_response
import mysql.connector

app = Flask(__name__)

# Connect to the database
con = mysql.connector.connect(user='admin', password='password', host='localhost', database='yvle')
cursor = con.cursor()

# Endpoint to retrieve all the discussion threads for a particular forum
@app.route('/discussionthreads/<int:forum_id>', methods=['GET'])
def get_discussion_threads(forum_id):
    try:
        # Query the database for all discussion threads for the specified forum
        cursor.execute(f"SELECT * FROM discussion_threads WHERE forum_id = {forum_id}")
        discussion_threads = cursor.fetchall()

        # Return the discussion threads as JSON
        return jsonify(discussion_threads), 200

    except Exception as e:
        print(e)
        return make_response(jsonify({'error': 'An error occurred while retrieving the discussion threads'}), 500)

# Endpoint to add a new discussion thread to a forum
@app.route('/discussionthreads', methods=['POST'])
def create_discussion_thread():
    try:
        # Get the discussion thread details from the request body
        content = request.json
        thread_id = content['thread_id']
        forum_id = content['forum_id']
        user_id = content['user_id']
        thread_title = content['thread_title']
        thread_content = content['thread_content']

        # Insert the discussion thread into the database
        cursor.execute(f"INSERT INTO discussion_threads (thread_id, forum_id, user_id, thread_title, thread_content) VALUES ({thread_id},'{forum_id}','{user_id}', '{thread_title}', '{thread_content}')")
        con.commit()

        return make_response(jsonify({'message': 'Discussion thread created successfully'}), 201)

    except Exception as e:
        print(e)
        return make_response(jsonify({'error': 'An error occurred while creating the discussion thread'}), 500)

# Endpoint to add a new reply to a discussion thread
@app.route('/discussionthreads/<int:thread_id>/replies', methods=['POST'])
def add_reply(thread_id):
    try:
        # Get the reply details from the request body
        content = request.json
        user_id = content['user_id']
        thread_content = content['thread_content']
        thread_id = content.get('thread_id', None)

        # Insert the reply into the database
        cursor.execute(f"INSERT INTO replies (thread_id, user_id, thread_content, thread_id) VALUES ({thread_id}, {user_id}, '{thread_content}', {thread_id})")
        con.commit()

        return make_response(jsonify({'message': 'Reply added successfully'}), 201)

    except Exception as e:
        print(e)
        return make_response(jsonify({'error': 'An error occurred while adding the reply'}), 500)

if __name__ == '__main__':
    app.run()


