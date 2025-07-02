import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="ecommerce_website"
)
cur = con.cursor()

print("📋 Signup")

name = input("Enter your name: ")
email = input("Enter your email: ")
password = input("Enter password: ")

try:
    cur.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", (name, email, password))
    con.commit()
    print("✅ Signup successful!")
except Exception as e:
    print("❌ Error:", e)

cur.close()
con.close()
