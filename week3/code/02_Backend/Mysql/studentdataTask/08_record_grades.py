import mysql.connector

# Connect to the database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="student_management"
)

cur = con.cursor()

# Sample grades: (student_id, course_id, grade)
grades = [
    (1, 1, 85.5),   # Alice - Mathematics
    (1, 2, 90.0),   # Alice - Physics
    (2, 1, 78.0),   # Bob - Mathematics
    (2, 3, 88.0),   # Bob - CS
    (3, 1, 92.0),   # Charlie - Mathematics
    (3, 4, 75.0)    # Charlie - English
]

# Insert grades
cur.executemany("INSERT INTO grades (student_id, course_id, grade) VALUES (%s, %s, %s)", grades)
con.commit()

print("✅ Grades recorded successfully!")
