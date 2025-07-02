import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="ecommerce_website"
)
cur = con.cursor()

# Create table if not exists
cur.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    message TEXT
)
""")

print("📨 Contact Us")

name = input("Your name: ")
email = input("Your email: ")
message = input("Your message: ")

cur.execute("INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)", (name, email, message))
con.commit()

print("✅ Message submitted successfully!")


