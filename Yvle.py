#Register User

from flask import Flask, jsonify, request

Yvle = Flask(__name__)

users = []

@Yvle.route('/tester', methods = ['GET'])
def tester():
    return "This is my tester for Project 1"


@Yvle.route('/register_user', methods=['POST'])
def register_user():

    u_name = request.json.get('Username')
    p_word = request.json.get('Password')
    acc_type = request.json.get('Account_type')
    
    # Check if the user already exists
    for user in users:
        if user['Username'] == u_name:
            return jsonify({'error': 'User already exists! Try again'}), 400
    
    # Create a new user
    user = {'Username': u_name, 'Password': p_word, 'Account_type': acc_type}
    users.append(user)
    
    return jsonify({'message': 'User has been registered successfully'}), 201



#User Login
@Yvle.route('/user_login', methods=['POST'])
def user_login():
    u_name = request.json.get('Username')
    p_word = request.json.get('Password')
    
    # Find the user
    for user in users:
        if user['Username'] == u_name and user['Password'] == p_word:
            return jsonify({'message': 'Login was successful', 'account_type': user['account_type']}), 200
        else:
            return jsonify({'error': 'Invalid'}), 401





@Yvle.route('/users', methods=['GET'])
def get_users():
    # if admin
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({'error': 'Missing authorization token'}), 401
    
    auth_token = auth_header.split(' ')[1]
    if auth_token != 'admin_token':
        return jsonify({'error': 'Unauthorized'}), 401
    
    # Return users
    added_users = [{'username': user['project1_user'], 'account_type': user['account_type']} for user in users]
    return jsonify({'users': added_users}), 200





#Register for Course

# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy

# Yvle = Flask(__name__)
# Yvle.config['SQLALCHEMY_DATABASE_URI'] = ''
# db = SQLAlchemy(Yvle)

# # Course 
# class Course(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     c_name = db.Column(db.String(100), nullable=False)
#     description = db.Column(db.String(500))
#     is_active = db.Column(db.Boolean, default=True)
#     student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
#     lecturer_id = db.Column(db.Integer, db.ForeignKey('lecturer.id'))

#     def __repr__(self):
#         return f'<Course {self.name}>'

# # Student
# class Student(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     courses = db.relationship('Course', backref='student')

#     def __repr__(self):
#         return f'<Student {self.name}>'

# # Lecturer
# class Lecturer(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     lecturer_name = db.Column(db.String(100), nullable=False)
#     courses = db.relationship('Course', backref='lecturer')

#     def __repr__(self):
#         return f'<Lecturer {self.name}>'


# @Yvle.route('/students/<int:student_id>/courses/<int:course_id>', methods=['POST'])
# def register_student_for_course(student_id, course_id):
#     # Get the student and course from the database
#     student = Student.query.get(student_id)
#     course = Course.query.get(course_id)
#     if not student:
#         return 'Student Not found', 404
#     if not course:
#         return 'Course Not found', 404
    
#     # if  course is active
#     if not course.is_active:
#         return 'Course is not ready for registration', 400
    
#     # Check if the course already has a student assigned to it
#     if course.student_id:
#         return 'Course already has a student assigned to it', 400
    
#     # Assign the student to the course
#     course.student_id = student.id
#     db.session.commit()
    
#     return 'Student has been registered for the course', 201

if __name__ == '__main__':
    Yvle.run(debug=True)