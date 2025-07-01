import mysql.connector

# Connect to the database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789" ,
    database="student_management"
)

cur = con.cursor()

# Sample courses to insert
courses = [
    ("Mathematics",),
    ("Physics",),
    ("Computer Science",),
    ("English",)
]

# Insert courses
cur.executemany("INSERT INTO courses (course_name) VALUES (%s)", courses)
con.commit()

print("✅ Courses added successfully!")
