import mysql.connector as mysql


db = mysql.connect(
    user="st-onl",
    passwd="AVNS_tegPDkI5BlB2lW5eASC",
    host="db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com",
    port=25060,
    database="st-onl",
)


cursor = db.cursor(dictionary=True)
cursor.execute("INSERT INTO students (name, second_name) VALUES ('Томара', 'Хорошая')")
student_id = cursor.lastrowid

cursor.execute(
    "INSERT INTO `groups` (title, start_date, end_date) VALUES ('Smart people', 'nov 2025', 'jan 2026')"
)
group_id = cursor.lastrowid
cursor.execute(f"UPDATE students SET group_id = {group_id} WHERE id = {student_id}")

insert_query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, NULL)"
cursor.executemany(
    insert_query,
    [
        ("7 steps to stable self-esteem",),
        ("5 steps to become rich",),
        ("Love language",),
    ],
)
update_query = "UPDATE books SET taken_by_student_id = %s WHERE title = %s"
cursor.executemany(
    update_query,
    [
        (student_id, "7 steps to stable self-esteem"),
        (student_id, "5 steps to become rich"),
        (student_id, "Love language"),
    ],
)

cursor.execute("INSERT INTO subjects (title) VALUES ('Philosophy')")
philosophy_id = cursor.lastrowid
cursor.execute("INSERT INTO subjects (title) VALUES ('History of arts')")
history_of_arts_id = cursor.lastrowid
cursor.execute("INSERT INTO subjects (title) VALUES ('English')")
english_id = cursor.lastrowid

cursor.execute(
    f"INSERT INTO lessons (title, subject_id) VALUES ('Ancient Greeks', {philosophy_id})"
)
ancient_greeks_lesson_id = cursor.lastrowid
cursor.execute(
    f"INSERT INTO lessons (title, subject_id) VALUES ('Immanuel Kant', {philosophy_id})"
)
immanuel_kant_lesson_id = cursor.lastrowid
cursor.execute(
    f"INSERT INTO lessons (title, subject_id) VALUES ('Renaissance', {history_of_arts_id})"
)
renaissance_lesson_id = cursor.lastrowid
cursor.execute(
    f"INSERT INTO lessons (title, subject_id) VALUES ('Antiquity', {history_of_arts_id})"
)
antiquity_lesson_id = cursor.lastrowid
cursor.execute(
    f"INSERT INTO lessons (title, subject_id) VALUES ('Present Simple', {english_id})"
)
present_simple_lesson_id = cursor.lastrowid
cursor.execute(
    f"INSERT INTO lessons (title, subject_id) VALUES ('Past Simple', {english_id})"
)
past_simple_lesson_id = cursor.lastrowid

insert_query2 = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.executemany(
    insert_query2,
    [
        (5, ancient_greeks_lesson_id, student_id),
        (4, immanuel_kant_lesson_id, student_id),
        (4, renaissance_lesson_id, student_id),
        (3, antiquity_lesson_id, student_id),
        (2, present_simple_lesson_id, student_id),
        (5, past_simple_lesson_id, student_id),
    ],
)

db.commit()

cursor.execute(f"SELECT * FROM marks WHERE student_id = {student_id}")
print(cursor.fetchall())

cursor.execute(f"SELECT * FROM books WHERE taken_by_student_id  = {student_id}")
print(cursor.fetchall())

cursor.execute(f"SELECT * FROM `groups` WHERE id = {group_id}")
print(cursor.fetchone())

cursor.execute(
    f"""
    SELECT s.name, s.second_name, g.title, g.start_date,
        g.end_date, b.title, m.value, l.title, s2.title
    FROM students s
    JOIN `groups` g ON s.group_id = g.id
    JOIN books b ON s.id = b.taken_by_student_id
    JOIN marks m ON s.id = m.student_id
    JOIN lessons l ON m.lesson_id  = l.id
    JOIN subjects s2 ON l.subject_id = s2.id
    WHERE s.id = {student_id}"""
)
print(cursor.fetchall())


db.close()
