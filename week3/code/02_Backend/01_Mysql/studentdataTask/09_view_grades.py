import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="student_management"
)

cur = con.cursor()
cur.execute("""
SELECT g.grade_id, s.name AS student_name, c.course_name, g.grade
FROM grades g
JOIN students s ON g.student_id = s.student_id
JOIN courses c ON g.course_id = c.course_id
""")

for row in cur.fetchall():
    print(row)
