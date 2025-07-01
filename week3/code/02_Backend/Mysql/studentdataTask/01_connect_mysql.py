import mysql.connector

# Connect to MySQL Server
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789"
)

print("✅ Connection created!")
