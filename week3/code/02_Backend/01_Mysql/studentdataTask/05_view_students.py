import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="student_management"
)

cur = con.cursor()
cur.execute("SELECT * FROM students")

for row in cur.fetchall():
    print(row)
