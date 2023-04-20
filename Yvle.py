

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
        cur.execute(f"INSERT INTO User VALUES('{u_id}','{u_name}','{p_word}')")
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
    

