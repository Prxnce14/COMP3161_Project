CREATE DATABASE Yvle;
USE Yvle;

-- DROP DATABASE Yvle;

SELECT * FROM User;
SELECT * FROM Course;
SELECT * FROM Member;
SELECT * FROM Lecturer;
SELECT * FROM CalendarEvent;
SELECT * FROM Student;
SELECT * FROM Account;
SELECT * FROM CourseContent;
SELECT * FROM DiscussionForum;
SELECT * FROM DiscussionThread;
SELECT * FROM Section;
SELECT * FROM SectionItem;
SELECT * FROM Assignment; 
SELECT * FROM Grade;
SELECT * FROM Department;
SELECT * FROM  Program;
SELECT * FROM Enrol;
SELECT * FROM Must_take;
SELECT * FROM Teach_connect;



SELECT * FROM User WHERE user_id = 6200000 
HAVING Password = 'my_password14';


INSERT INTO yvle.User (User_id, Username, Password) VALUES ('56153', '4178265049', 'WVJFFmrl');
INSERT INTO yvle.User (User_id, Username, Password) VALUES ('51772', '4960858992', 'OFv2fCOr');
INSERT INTO yvle.Account (Account_name, Account_type, User_id) VALUES ('Belinda Riley', 'Admin', '98594');
INSERT INTO yvle.Member (Member_id, User_id, Course_id) VALUES ('8386875367', 98594, 'ARTS500');
INSERT INTO yvle.Student (Student_id, Name, User_id) VALUES ('6601440755', 'Robert Summers', '51772');

INSERT INTO Course (Course_id, Course_Name, Course_admin) VALUES ('ARTS500', 'Contemporary Art Criticism', '98594');

INSERT INTO yvle.Lecturer (Lecturer_id, Name, User_id) VALUES ('8762052873', 'Adam Harper', '51772');
INSERT INTO yvle.Lecturer (Lecturer_id, Name, User_id) VALUES ('8386875367', 'Christopher Scott', '98594');

INSERT INTO yvle.DiscussionForum (Forum_id, Forum_name, Course_id) VALUES ('ebb9f2dd-f7c1-4c42-8894-80f7ce62acd8', 'labs', 'ACCT501');

INSERT INTO yvle.DiscussionThread (Thread_id, Thread_Title, Thread_content, User_id, Forum_id) VALUES ('ce324b16b79a43eb8182bd699b2609e9', 'Name discover issue second girl hit somebody.', 
'Point him beyond ok president international. Near catch plan if force admit ever. Head your sort like. Wrong sometimes difficult statement.
Ahead rate charge. Executive drug shake still get trial drive.', '10087', 'ebb9f2dd-f7c1-4c42-8894-80f7ce62acd8');

-- Insert query for Discussion thread;

INSERT INTO yvle.CalendarEvent (Event_id, Event_name, Event_description, Event_date, Course_id) VALUES 
('45df727c-8832-4743-89f9-c53ce9df9d3d', 'Decentralized disintermediate portal', 'Auditing taught by Richard Dennis', '2023-11-20', 'ACCT501');

INSERT INTO yvle.Section (Section_id, Section_title, Course_id) VALUES 
('a1f4bcf6-e472-401d-9546-d87fd19e9aeb', 'Organized demand-driven matrices', 'ARTS500');


INSERT INTO yvle.SectionItem (Item_id, Item_name, Item_type, Item_url, Section_id) VALUES 
('b29f6a23-231c-4e64-9ade-9d7aa0e94adc', 'administration', 'video', 'http://www.hunt-howard.com/', 'a1f4bcf6-e472-401d-9546-d87fd19e9aeb');


INSERT INTO yvle.CourseContent(Content_id, Content_name, Course_id, Content_type, Lecturer_id, Section_id) VALUES 
('7233ecea-1ac5-4330-8b49-0e5c82665a0b', 'https://dummyimage.com/322x28', 'ARTS500', 'image', '8762052873', 'a1f4bcf6-e472-401d-9546-d87fd19e9aeb');


INSERT INTO yvle.Assignment (Assignment_id, Assignment_url, Course_id) VALUES
 ('8a175bc4-64a6-4269-8756-6c97f8c2c950', 'https://www.barrett.com/', 'ACCT501');


INSERT INTO yvle.Grade (Grade_id, Letter_grade, Assignment_id, Student_id) VALUES 
('0353c8b0-f138-41d1-9678-8fb83d827f0c', 'F', '8a175bc4-64a6-4269-8756-6c97f8c2c950', '6601440755');


-- Insert query for Department, Program ;

INSERT INTO yvle.Enrol (Student_id, Course_id) VALUES ('6601440755', 'ARTS500');

-- Insert query for must_take

INSERT INTO yvle.Teach_connect (Course_id, Lecturer_ID) VALUES ('ACCT501', '8762052873');


SELECT Course_id, Course_Name FROM course;

SELECT course.Course_id, course.Course_Name FROM course JOIN Enrol ON course.Course_id = Enrol.Course_id JOIN 
Student on Student.Student_id = Enrol.Student_id WHERE Student.Student_id = 6601440755;

SELECT course.Course_id, course.Course_Name FROM course JOIN Lecturer ON course.Course_admin = Lecturer.User_id 
WHERE Lecturer.User_id = 51772;


INSERT INTO yvle.Course (course_id, Course_Name, Course_admin) VALUES ('BIOL610', 'Evolutionary Biology', 16112);


INSERT INTO yvle.Member (Member_id, User_id, Course_id) VALUES ('8762052873', 10087, 'ARTS500');


INSERT INTO yvle.Section (Section_id, Section_title, Course_id) VALUES ('3acae0ec-c41a-4426-a747-766af4d24f4e', 'Cross-platform multimedia array', 'ACCT501');

INSERT INTO yvle.Section (Section_id, Section_title, Course_id) VALUES ('8cb7a0a3-1376-4ea6-8f54-ccc9c059af94', 'Multi-channeled demand-driven protocol', 'WGS401');


SELECT  CourseContent.Lecturer_id FROM CourseContent JOIN Lecturer ON CourseContent.Lecturer_id = Lecturer.Lecturer_id 
WHERE Lecturer.Lecturer_id = 8762052873;

SELECT Lecturer_id FROM Lecturer WHERE Lecturer.Lecturer_id = 8762052873;


INSERT INTO yvle.Assignment (Assignment_id, Assignment_url, Course_id) VALUES 
('0a2bd463-409a-473b-90e3-fa6700a812cd', 'https://www.dorsey.com/', 'ARTS500');

INSERT INTO yvle.Assignment (Assignment_id, Assignment_url, Course_id) VALUES 
('6c8a99e6-ab0f-43f1-8c28-52061e1e1ad5', 'https://www.thompson.com/', 'WGS401');


SELECT * FROM Assignment WHERE Assignment.Assignment_id = "0a2bd463-409a-473b-90e3-fa6700a812cd";


INSERT INTO yvle.Grade (Grade_id, Letter_grade, Grade, Assignment_id, Student_id) VALUES 
('702e90e7-2ebe-4c22-aab2-f302e0af0eab', 'C', '73', '0a2bd463-409a-473b-90e3-fa6700a812cd', '6601440766');

INSERT INTO yvle.Grade (Grade_id, Letter_grade, Grade, Assignment_id, Student_id) VALUES 
('441057f6-c117-4dd3-b5bd-7d17be0b6adc', 'B', '83', '6c8a99e6-ab0f-43f1-8c28-52061e1e1ad5', '6601440766');

DELETE FROM Grade WHERE Grade.Assignment_id = '8a175bc4-64a6-4269-8756-6c97f8c2c950';

SELECT Student_id FROM Student WHERE Student.Student_id = '6601440766' ;

SELECT Grade FROM Grade WHERE Student_id = '6601440766';
SELECT AVG(Grade) AS Grade_Average FROM Grade WHERE Student_id = '6601440766';

SELECT Grade.Student_id, Student.Name, AVG(Grade) AS Grade_Average  FROM Grade
JOIN Student ON Grade.Student_id = Student.Student_id WHERE Student.Student_id = '6601440766'
GROUP BY Grade.Student_id;

SELECT DiscussionForum.Forum_id FROM DiscussionForum
WHERE DiscussionForum.Forum_id = '01dd892a-a93e-4802-b874-3c77ea77e6a0';


INSERT INTO yvle.DiscussionForum (Forum_id, Forum_name, Course_id) VALUES 
('01dd892a-a93e-4802-b874-3c77ea77e6a0', 'labs', 'ACCT501');

INSERT INTO yvle.DiscussionForum (Forum_id, Forum_name, Course_id) VALUES 
('41fac694-27d2-4df7-aa16-bfbf607fe40f', 'Quiz', 'BIOL610');

INSERT INTO yvle.DiscussionForum (Forum_id, Forum_name, Course_id) VALUES 
('2bb9283c-cec0-493b-a56c-ad0c68440d56', 'midsemesters', 'WGS401');


INSERT INTO yvle.DiscussionThread (Thread_id, Thread_Title, Thread_content, User_id, Forum_id) VALUES 
('e0176f8bbe24472fa3b59ed5baed7d9c', 'Daughter west past recently win stop. Wish yeah story drive.
Small billion always simply.', 'News enjoy fight. Us instead agree same data professional true. Call since people give meeting. 
Around now suddenly really realize person.', '10497', '01dd892a-a93e-4802-b874-3c77ea77e6a0');


-- query to run calendar events for a particular course for a particular student

SELECT Student.Student_id, CalendarEvent.Event_date, CalendarEvent.Course_id FROM CalendarEvent JOIN Enrol ON CalendarEvent.Course_id = Enrol.Course_id
JOIN Student ON Student.Student_id = Enrol.Student_id ;

-- query to run final average

SELECT Grade.Student_id, Student.Name, AVG(Grade) AS Grade_Average FROM Grade 
JOIN Student ON Grade.Student_id = Student.Student_id 
GROUP BY Grade.Student_id;


SELECT * FROM Lecturer WHERE Lecturer.User_id = 51772;

DELETE FROM LECTURER WHERE Lecturer.User_id = 51772;
DELETE FROM User WHERE user_id = 51772;

SELECT * FROM User WHERE User_id = 51772;

SELECT * FROM User WHERE User_id = 51772;


SELECT * FROM DiscussionThread WHERE DiscussionThread.Forum_id = '7f1c386a-e904-47d1-9ab1-2b4fe693b9vt' ;

SELECT * FROM CourseContent WHERE CourseContent.Course_id =  'PYTH1000' ;

SELECT * FROM Student5_orMore ;

SELECT * FROM Enrol WHERE Course_id = "ANTH501";
SELECT * FROM Enrol WHERE  Student_id = 6100026654;

SELECT * FROM Member WHERE member_id = 8102237614;

SELECT * FROM Account;

SELECT * FROM Account WHERE Account.User_id Between 51772 AND 59232;



SELECT * FROM Account WHERE user_id = '56190' and Account.Account_type = 'Admin';



CREATE VIEW Course50 AS 
SELECT course_id, COUNT(*) AS num_students
FROM enrol
GROUP BY course_id
HAVING COUNT(*) > 50;

CREATE VIEW Student5_orMore AS
SELECT student_id, COUNT(*) AS num_courses
FROM enrol
GROUP BY student_id
HAVING COUNT(*) >= 5;

CREATE VIEW Lecturer3_orMore AS
SELECT Lecturer_id, COUNT(*) AS num_courses
FROM Teach_connect
GROUP BY lecturer_id
HAVING COUNT(*) >= 3;

CREATE VIEW Most_Enrolled AS
SELECT course_id, COUNT(*) AS num_students
FROM enrol
GROUP BY course_id
ORDER BY num_students DESC
LIMIT 10;

CREATE VIEW Avg_Grade AS
SELECT student_id, AVG(Grade) AS avg_grade
FROM grade
GROUP BY student_id
ORDER BY avg_grade DESC
LIMIT 10;



-- DROP TABLE User;
-- DROP TABLE Account;
-- DROP TABLE Member;
-- DROP TABLE Student;
-- DROP TABLE Lecturer;
-- DROP TABLE Course;
-- DROP TABLE DiscussionForum;
-- DROP TABLE DiscussionThread;
-- DROP TABLE CalendarEvent;
-- DROP TABLE Section;
-- DROP TABLE SectionItem;
-- DROP TABLE CourseContent;
-- DROP TABLE Assignment; 
-- DROP TABLE Grade;
-- DROP TABLE Department;
-- DROP TABLE  Program;
-- DROP TABLE Enrol;
-- DROP TABLE Must_take;
-- DROP TABLE Teach_connect; 



CREATE TABLE User(
User_id INT NOT NULL,
Username BIGINT NOT NULL,
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
Student_id BIGINT NOT NULL,
Name varchar(255) NOT NULL,
User_id INT NOT NULL,
PRIMARY KEY (Student_id),
FOREIGN KEY (User_id) REFERENCES User(User_id)
);

CREATE TABLE Lecturer(
Lecturer_id BIGINT NOT NULL,
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
FOREIGN KEY (Course_admin) REFERENCES Account(User_id)
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
Lecturer_id BIGINT NOT NULL,
Section_id varchar(255) NOT NULL,
PRIMARY KEY (Content_id),
FOREIGN KEY (Course_id)  REFERENCES Course(Course_id),
FOREIGN KEY (Lecturer_id) REFERENCES Lecturer(Lecturer_id),
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
Grade INT NOT NULL,
Assignment_id varchar(255) NOT NULL,
Student_id BIGINT NOT NULL,
PRIMARY KEY (Grade_id),
FOREIGN KEY (Assignment_id) REFERENCES Assignment(Assignment_id),
FOREIGN KEY (Student_id) REFERENCES Student(Student_id)
);

CREATE TABLE Department(
Dept_id varchar(255) NOT NULL,
Dept_name varchar(255) NOT NULL,
Lecture_id INT NOT NULL,
PRIMARY KEY (Dept_id),
FOREIGN KEY (Lecture_id) REFERENCES Lecture(Lecturer_id)
);

CREATE TABLE Program(
Program_id varchar(25) NOT NULL,
Program_name varchar(255) NOT NULL,
Student_id BIGINT NOT NULL,
Dept_id varchar(25) NOT NULL,
PRIMARY KEY (Program_id),
FOREIGN KEY (Student_id) REFERENCES Student(Student_id), 
FOREIGN KEY (Dept_id) REFERENCES Department(Dept_id)
);


CREATE TABLE Enrol(
Student_id BIGINT NOT NULL,
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
Lecturer_id BIGINT NOT NULL,
PRIMARY KEY (Course_id,Lecturer_id),
FOREIGN KEY (Course_id) REFERENCES Course (Course_id),
FOREIGN KEY (Lecturer_id) REFERENCES Lecturer(Lecturer_id)
);








