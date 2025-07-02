import mysql.connector
import bcrypt

# Connect to MySQL
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

# Get the hashed password from DB for the given email
cur.execute("SELECT password FROM users WHERE email = %s", (email,))
result = cur.fetchone()

if result:
    stored_hash = result[0].encode('utf-8')  # Convert to bytes
    if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
        print(f"✅ Welcome, {email}!")
    else:
        print("❌ Incorrect password.")
else:
    print("❌ Email not found.")
