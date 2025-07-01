import mysql.connector

# ✅ Step 1: Connect to MySQL Server
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789"
)
print("✅ Connected to MySQL")

# ✅ Step 2: Create cursor
mycursor = con.cursor()

# ✅ Step 3: Create database
mycursor.execute("CREATE DATABASE IF NOT EXISTS inventorydb")
print("✅ Database created successfully!")

# ✅ Step 4: Connect again — this time to the specific database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="inventorydb"
)
mycursor = con.cursor()

# ✅ Step 5: Create table
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        price FLOAT NOT NULL,
        stock INT NOT NULL
    )
""")
print("✅ Table created successfully!")

# ✅ Close connection
mycursor.close()
con.close()
print("🔌 Connection closed.")
