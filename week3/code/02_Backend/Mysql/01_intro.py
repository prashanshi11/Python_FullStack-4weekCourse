import mysql.connector
from datetime import date

# Step 1: Connect to MySQL server
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789"
)
print("Connection created:", con)

# Step 2: Create a new database
mycursor = con.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS impactlpu")
print("Database created successfully!")

# Step 3: Connect to the newly created database
con.database = "impactlpu"

# Step 4: Create table
mycursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    fee FLOAT,
    join_date DATE,
    is_active BOOLEAN
)
""")
print("Table created successfully!")

# Step 5: Insert multiple records
query = """
INSERT INTO students(name, age, fee, join_date, is_active)
VALUES (%s, %s, %s, %s, %s)
"""
data = [
    ("Preet", 23, 4500.0, date(2025, 6, 16), True),
    ("Sneha", 24, 4700.0, date(2025, 6, 17), True),
    ("Preet Kaur", 25, 4800.0, date(2025, 6, 18), False),
    ("Gurmukh", 22, 4300.0, date(2025, 6, 17), True),
    ("Manu", 21, 4700.0, date(2025, 6, 16), False)
]
mycursor.executemany(query, data)
con.commit()
print(mycursor.rowcount, "records inserted")

# Step 6: Read the data
mycursor.execute("SELECT * FROM students")
for row in mycursor.fetchall():
    print(row)

# Optional: update, delete, or drop
