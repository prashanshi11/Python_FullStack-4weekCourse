import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="ecommerce_website"
)
cur = con.cursor()

print("🔐 Login")

email = input("Enter email: ")
password = input("Enter password: ")

cur.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))
user = cur.fetchone()

if user:
    print(f"✅ Welcome, {user[1]}!")
else:
    print("❌ Invalid credentials")

cur.close()
con.close()
