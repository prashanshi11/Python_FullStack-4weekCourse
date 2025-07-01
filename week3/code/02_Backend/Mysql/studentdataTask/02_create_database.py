import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789"
)
cur = con.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS student_management")
print("✅ Database created successfully!")
