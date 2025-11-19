INSERT INTO students (name, second_name) VALUES ('Ivan', 'Petrov')
 
INSERT INTO `groups` (title, start_date, end_date) VALUES ('Smart people', 'nov 2025', 'jan 2026')

UPDATE students SET group_id = 21524 WHERE id = 21633

INSERT INTO books (title, taken_by_student_id) VALUES ('7 steps to stable self-esteem', 21633)

INSERT INTO books (title, taken_by_student_id) VALUES ('5 steps to become rich', 21633)

INSERT INTO books (title, taken_by_student_id) VALUES ('Love language', 21633)

INSERT INTO lessons (title, subject_id) VALUES ('Ancient Greeks', 12798)

INSERT INTO lessons (title, subject_id) VALUES ('Immanuel Kant', 12798)

INSERT INTO lessons (title, subject_id) VALUES ('Renaissance', 12799)

INSERT INTO lessons (title, subject_id) VALUES ('Antiquity', 12799)

INSERT INTO lessons (title, subject_id) VALUES ('Present Simple', 12800)

INSERT INTO lessons (title, subject_id) VALUES ('Past Simple', 12800)

INSERT INTO marks (value, lesson_id, student_id) VALUES (5, 73230, 21633)

INSERT INTO marks (value, lesson_id, student_id) VALUES (4, 73231, 21633)

INSERT INTO marks (value, lesson_id, student_id) VALUES (4, 73232, 21633)

INSERT INTO marks (value, lesson_id, student_id) VALUES (3, 73233, 21633)

INSERT INTO marks (value, lesson_id, student_id) VALUES (2, 73234, 21633)

INSERT INTO marks (value, lesson_id, student_id) VALUES (5, 73235, 21633)

INSERT INTO subjects (title) VALUES ('Philosophy')

INSERT INTO subjects (title) VALUES ('History of arts')

INSERT INTO subjects (title) VALUES ('English')

SELECT * FROM marks WHERE student_id = 21633

SELECT * FROM books WHERE taken_by_student_id = 21633

SELECT * FROM `groups` WHERE title = 'Smart people'

SELECT s.name, s.second_name, g.title, g.start_date, g.end_date, b.title, m.value, l.title, s2.title   
FROM students s 
JOIN `groups` g ON s.group_id = g.id
JOIN books b ON s.id = b.taken_by_student_id 
JOIN marks m ON s.id = m.student_id 
JOIN lessons l ON m.lesson_id  = l.id 
JOIN subjects s2 ON l.subject_id = s2.id 
WHERE s.id = 21633
