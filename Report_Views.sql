
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
