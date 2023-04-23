CREATE DATABASE Yvle;
USE Yvle;

-- DROP DATABASE Yvle;

SELECT * FROM User;
SELECT * FROM Course;
SELECT * FROM Member;
SELECT * FROM Lecture;

ALTER TABLE Member
ADD Course_id VARCHAR(255);

SELECT * FROM User WHERE user_id = 6200000 
HAVING Password = 'my_password14';

DELETE FROM User WHERE Username LIKE '%4178265050%' ;

ALTER TABLE Course
RENAME COLUMN C_name TO Course_Name;

INSERT INTO yvle.User (User_id, Username, Password) VALUES ('56151', '4178265050', 'WVJFFmrj');
INSERT INTO yvle.User (User_id, Username, Password) VALUES ('56153', '4178265050', 'WVJFFmrj');
INSERT INTO yvle.Account (Account_name, Account_type, User_id) VALUES ('Belinda Riley', 'Admin', '56152');
INSERT INTO yvle.Member (Member_id, User_id, Course_id) VALUES ('8386875367', 62000, 'ARTS500');
INSERT INTO yvle.Student (Student_id, Name, User_id) VALUES ('6601440755', 'Robert Summers', '56119');

INSERT INTO Course (Course_id, Course_Name, Course_admin) VALUES ('ARTS500', 'Contemporary Art Criticism', '98594');
INSERT INTO Lecture (Lecturer_id, Name, User_id) VALUES ('8762052873', 'Adam Harper', 34874);

DROP TABLE User;
DROP TABLE Account;
DROP TABLE Member;
DROP TABLE Student;
DROP TABLE Lecture;
DROP TABLE Course;
DROP TABLE DiscussionForum;
DROP TABLE DiscussionThread;
DROP TABLE CalendarEvent;
DROP TABLE Section;
DROP TABLE SectionItem;
DROP TABLE CourseContent;
DROP TABLE Assignment; 
DROP TABLE Grade;
DROP TABLE Department;
DROP TABLE  Program;
DROP TABLE Enrol;
DROP TABLE Must_take;
DROP TABLE Teach_connect;



CREATE TABLE User(
User_id INT NOT NULL,
Username varchar(255) NOT NULL,
Password varchar(255) NOT NULL,
PRIMARY KEY (User_id)
);

CREATE TABLE Account(
Account_name varchar(255) NOT NULL,
Account_type varchar(255) NOT NULL,
User_id INT NOT NULL,
PRIMARY KEY (User_id),
FOREIGN KEY (User_id) REFERENCES User(User_id)

);

CREATE TABLE Member(
Member_id varchar(255) NOT NULL,
User_id INT NOT NULL,
Course_id varchar(255) NOT NULL,
PRIMARY KEY (Member_id, Course_id),
FOREIGN KEY (User_id) REFERENCES User(User_id),
FOREIGN KEY (Course_id) REFERENCES Course (Course_id)
);

CREATE TABLE Student(
Student_id INT NOT NULL,
Name varchar(255) NOT NULL,
User_id INT NOT NULL,
PRIMARY KEY (Student_id),
FOREIGN KEY (User_id) REFERENCES User(User_id)
);

CREATE TABLE Lecturer(
Lecturer_id INT NOT NULL,
Name varchar(255) NOT NULL,
User_id INT NOT NULL,
PRIMARY KEY (Lecturer_id),
FOREIGN KEY (User_id) REFERENCES User(User_id)
);

CREATE TABLE Course(
Course_id varchar(255) NOT NULL,
Course_Name varchar(255) NOT NULL,
Course_admin INT NOT NULL,
PRIMARY KEY (Course_id),
FOREIGN KEY (Course_admin) REFERENCES Lecturer(User_id)
);

CREATE TABLE DiscussionForum(
Forum_id varchar(255) NOT NULL,
Forum_name varchar(255) NOT NULL,
Course_id varchar(255) NOT NULL,
PRIMARY KEY (Forum_id),
FOREIGN KEY (Course_id) REFERENCES Course(Course_id)
);

CREATE TABLE DiscussionThread(
Thread_id varchar(255) NOT NULL,
Thread_Title varchar(255) NOT NULL,
Thread_content varchar(255) NOT NULL,
User_id int NOT NULL,
Forum_id varchar(255) NOT NULL,
PRIMARY KEY (Thread_id),
FOREIGN KEY (User_id) REFERENCES User(User_id),
FOREIGN KEY (Forum_id) REFERENCES DiscussionForum(Forum_id)
);

CREATE TABLE CalendarEvent(
Event_id varchar(255) NOT NULL,
Event_name varchar(255) NOT NULL,
Event_description varchar(255) NOT NULL,
Event_date date NOT NULL,
Course_id varchar(255) NOT NULL,
PRIMARY KEY (Event_id),
FOREIGN KEY (Course_id) REFERENCES Course(Course_id)
);

CREATE TABLE Section(
Section_id varchar(255) NOT NULL,
Section_title varchar(255) NOT NULL,
Course_id varchar(255) NOT NULL,
PRIMARY KEY (Section_id),
FOREIGN KEY (Course_id) REFERENCES Course(Course_id)
);

CREATE TABLE SectionItem(
Item_id varchar(255) NOT NULL,
Item_name varchar(255) NOT NULL,
Item_type varchar(255) NOT NULL,
Item_url varchar(255) NOT NULL,
Section_id varchar(255) NOT NULL,
PRIMARY KEY (Item_id),
FOREIGN KEY (Section_id) REFERENCES Section(Section_id)
);

CREATE TABLE CourseContent(
Content_id varchar(255) NOT NULL,
Content_name varchar(255) NOT NULL,
Course_id varchar(255) NOT NULL,
Content_type VARCHAR(255) NOT NULL,
Lecture_id varchar(255) NOT NULL,
Section_id varchar(255) NOT NULL,
PRIMARY KEY (Content_id),
FOREIGN KEY (Course_id)  REFERENCES Course(Course_id),
FOREIGN KEY (Lecture_id) REFERENCES Lecture(Lecturer_id),
FOREIGN KEY (Section_id) REFERENCES Section(Section_id) 
);

CREATE TABLE Assignment(
Assignment_id varchar(255) NOT NULL,
Assignment_url varchar(255) NOT NULL,
Course_id varchar(255) NOT NULL,
PRIMARY KEY (Assignment_id),
FOREIGN KEY (Course_id) REFERENCES Course(Course_id)
);

CREATE TABLE Grade(
Grade_id varchar(255) NOT NULL,
Letter_grade varchar(5) NOT NULL,
Assignment_id varchar(255) NOT NULL,
Student_id varchar(255) NOT NULL,
PRIMARY KEY (Grade_id),
FOREIGN KEY (Assignment_id) REFERENCES Assignment(Assignment_id),
FOREIGN KEY (Student_id) REFERENCES Student(Student_id)
);

CREATE TABLE Department(
Dept_id varchar(255) NOT NULL,
Dept_name varchar(255) NOT NULL,
Lecture_id varchar(255) NOT NULL,
PRIMARY KEY (Dept_id),
FOREIGN KEY (Lecture_id) REFERENCES Lecture(Lecturer_id)
);

CREATE TABLE Program(
Program_id varchar(25) NOT NULL,
Program_name varchar(255) NOT NULL,
Student_id varchar(255) NOT NULL,
Dept_id varchar(25) NOT NULL,
PRIMARY KEY (Program_id),
FOREIGN KEY (Student_id) REFERENCES Student(Student_id), 
FOREIGN KEY (Dept_id) REFERENCES Department(Dept_id)
);


CREATE TABLE Enrol(
Student_id INT NOT NULL,
Course_id varchar(255) NOT NULL,
PRIMARY KEY ( Student_id, Course_id), 
FOREIGN KEY (Student_id) REFERENCES Student(Student_id),
FOREIGN KEY (Course_id) REFERENCES Course (Course_id)
);


CREATE TABLE Must_take(
Course_id VARCHAR (255) NOT NULL,
Department_id VARCHAR (255) NOT NULL,
PRIMARY KEY (Course_id, Department_id) ,
FOREIGN KEY (Department_id) REFERENCES Program(Dept_id),
FOREIGN KEY (Course_id) REFERENCES Course (Course_id)
);


CREATE TABLE Teach_connect(
Course_id varchar(255) NOT NULL,
Lecturer_id varchar(255) NOT NULL,
PRIMARY KEY (Course_id,Lecturer_id),
FOREIGN KEY (Course_id) REFERENCES Course (Course_id),
FOREIGN KEY (Lecturer_id) REFERENCES Lecturer(Lecturer_id)
);








