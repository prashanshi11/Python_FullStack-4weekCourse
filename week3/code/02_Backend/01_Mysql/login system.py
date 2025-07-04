import mysql.connector
import bcrypt

# Connect to the MySQL database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="ecommerce_website"
)
cur = con.cursor()
print("✅ Connected to database")

# Ensure users table exists
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR(100) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL
    )
""")
con.commit()

# Signup function
def sign_up(email, password):
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    try:
        cur.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, hashed_pw))
        con.commit()
        print("✅ User registered successfully.")
    except mysql.connector.IntegrityError:
        print("⚠️ Email already registered! Try another.")

# Login function
def login(email, password):
    cur.execute("SELECT password FROM users WHERE email=%s", (email,))
    result = cur.fetchone()
    if result:
        stored_hash = result[0].encode('utf-8')
        if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
            print(f"✅ Welcome back, {email}!")
        else:
            print("❌ Incorrect password.")
    else:
        print("❌ Email not found.")

# Main loop
def main():
    while True:
        print("\n🔐 --- Login System ---")
        print("1. Sign Up")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            email = input("Enter email: ")
            password = input("Enter password: ")
            sign_up(email, password)
        elif choice == "2":
            email = input("Enter email: ")
            password = input("Enter password: ")
            login(email, password)
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

# Run main loop
if __name__ == "__main__":
    main()

# Clean up
cur.close()
con.close()
