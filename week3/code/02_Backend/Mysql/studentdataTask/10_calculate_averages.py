import mysql.connector

# Connect to the database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="student_management"
)

cur = con.cursor()

# Fetch average grades
cur.execute("""
SELECT 
    s.student_id,
    s.name AS student_name,
    ROUND(AVG(g.grade), 2) AS average_grade
FROM 
    grades g
JOIN 
    students s ON g.student_id = s.student_id
GROUP BY 
    s.student_id, s.name
""")

# Print results
print("📊 Student Averages:")
print("-" * 40)
for student_id, name, avg in cur.fetchall():
    print(f"ID: {student_id} | Name: {name} | Avg Grade: {avg}")
