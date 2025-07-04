import mysql.connector
from datetime import date

# Step 1: Connect to MySQL server
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789"
)
print("✅ Connection created")

# Step 2: Create Database
cur = con.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS student_management")
print("✅ Database created")

# Step 3: Connect to the database
con.database = "student_management"

# Step 4: Create tables
cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100)
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS grades (
    grade_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    grade FLOAT,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
)
""")
print("✅ Tables created")

# Step 5: Insert sample students
students = [
    ("Alice Johnson", "alice@example.com"),
    ("Bob Smith", "bob@example.com"),
    ("Charlie Lee", "charlie@example.com")
]
cur.executemany("INSERT INTO students (name, email) VALUES (%s, %s)", students)
con.commit()
print("✅ Students inserted")

# Step 6: Insert sample courses
courses = [
    ("Mathematics",),
    ("Physics",),
    ("Computer Science",),
    ("English",)
]
cur.executemany("INSERT INTO courses (course_name) VALUES (%s)", courses)
con.commit()
print("✅ Courses inserted")

# Step 7: Record grades
grades = [
    (1, 1, 85.5),   # Alice - Mathematics
    (1, 2, 90.0),   # Alice - Physics
    (2, 1, 78.0),   # Bob - Mathematics
    (2, 3, 88.0),   # Bob - CS
    (3, 1, 92.0),   # Charlie - Mathematics
    (3, 4, 75.0)    # Charlie - English
]
cur.executemany("INSERT INTO grades (student_id, course_id, grade) VALUES (%s, %s, %s)", grades)
con.commit()
print("✅ Grades recorded")

# Step 8: View student averages
cur.execute("""
SELECT 
    s.name AS student_name,
    ROUND(AVG(g.grade), 2) AS average_grade
FROM 
    grades g
JOIN 
    students s ON g.student_id = s.student_id
GROUP BY 
    s.student_id, s.name
""")

print("\n📊 Average Grades per Student:")
for name, avg in cur.fetchall():
    print(f"{name}: {avg}")
