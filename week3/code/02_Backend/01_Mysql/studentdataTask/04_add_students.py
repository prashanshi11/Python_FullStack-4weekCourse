import mysql.connector

# Connect to the database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="student_management"
)

cur = con.cursor()

# Sample students to insert
students = [
    ("Alice Johnson", "alice@example.com"),
    ("Bob Smith", "bob@example.com"),
    ("Charlie Lee", "charlie@example.com")
]

# Insert students
cur.executemany("INSERT INTO students (name, email) VALUES (%s, %s)", students)
con.commit()

print("✅ Students added successfully!")
