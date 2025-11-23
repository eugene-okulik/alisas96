import os
import csv
import dotenv
import mysql.connector as mysql

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASSW"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME"),
)

cursor = db.cursor(dictionary=True)

cursor.execute(
    """SELECT s.name, s.second_name,
	g.title AS group_title, b.title AS book_title,
	s2.title AS subject_title, l.title AS lesson_title,
	m.value AS mark_value
	FROM students s
	JOIN `groups` g ON s.group_id = g.id
    JOIN books b ON s.id = b.taken_by_student_id
    JOIN marks m ON s.id = m.student_id
    JOIN lessons l ON m.lesson_id  = l.id
    JOIN subjects s2 ON l.subject_id = s2.id"""
)
query = cursor.fetchall()

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
okulik_file_path = os.path.join(
    homework_path, "eugene_okulik", "Lesson_16", "hw_data", "data.csv"
)

with open(okulik_file_path, newline="") as csv_file:
    file_data = csv.DictReader(csv_file)
    data = []
    for row in file_data:
        row["mark_value"] = int(row["mark_value"])
        if row not in query:
            data.append(row)

print(data)

db.close()
