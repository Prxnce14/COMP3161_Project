#This is the Project 1 for GROUP 25 - COMP 3161

To acces the cmd from your file explorer, type cmd

virtual environment is a space that runs a python environment sepearte apart form the python on your local machine
Installing virtual environment:

pip install virtualenv
if you're experiencig priveleges error, use:

pip install virtualenv --user

Creating the virtual environment:

virtualenv <name of your environment goes here>

then enter this code to activate your virtual environment

<name of env>\Scripts\activate

connecting to MYSQL Database

pip install mysql-connector-python

Installing flask:

pip install flask

test if flask has been installed:

type python

then: 

from flask import Flask

Starting  you server:  

flask --app <name of python file>.py --debug run
_________________________________________________________________________________

Switch to current environmnet:

Yvle_env\Scripts\activate

Accitvate server

flask --app Yvle.py --debug run





database information

(user='project1_user', password ='password123',host = '127.0.0.1', database = 'Yvle')




Sample data for Register User

Postman- Post Requesuest- Body - Raw - Json


{
    "Username": "your name",
    "Password": "you password",
    "Account_type": "Student"
}







