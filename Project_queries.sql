CREATE DATABASE Yvle;
USE Yvle;

-- DROP DATABASE Yvle;

CREATE TABLE User(
User_id int NOT NULL,
Username varchar(255) NOT NULL,
Password varchar(255) NOT NULL,
PRIMARY KEY (User_id)
);

CREATE TABLE Account(
Account_name varchar(255) NOT NULL,
Account_type varchar(255) NOT NULL,
User_id INT NOT NULL,
PRIMARY KEY (Account_name),
FOREIGN KEY (User_id) REFERENCES User(User_id)

);

CREATE TABLE Member(
Member_id varchar(255) NOT NULL,
User_id int NOT NULL,
PRIMARY KEY (Member_id),
FOREIGN KEY (User_id) REFERENCES User(User_id)  
);

CREATE TABLE Student(
Student_id varchar(255) NOT NULL,
Name varchar(255) NOT NULL,
User_id int NOT NULL,
PRIMARY KEY (Student_id),
FOREIGN KEY (User_id) REFERENCES User(User_id)
);

CREATE TABLE Lecture(
Lecturer_id varchar(255) NOT NULL,
Name varchar(255) NOT NULL,
User_id int NOT NULL,
PRIMARY KEY (Lecturer_id),
FOREIGN KEY (User_id) REFERENCES User(User_id)
);

CREATE TABLE Course(
Course_id varchar(255) NOT NULL,
C_name varchar(255) NOT NULL,
Lecture_id varchar(255) NOT NULL,
PRIMARY KEY (Course_id),
FOREIGN KEY (Lecture_id) REFERENCES Lecture(Lecturer_id)
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
PRIMARY KEY (Content_id),
FOREIGN KEY (Course_id)  REFERENCES Course(Course_id) 
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
Student_id varchar(255) NOT NULL,
Course_id varchar(255) NOT NULL,
Grade INT NOT NULL,
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
FOREIGN KEY (Lecturer_id) REFERENCES Lecture(Lecturer_id)
);








