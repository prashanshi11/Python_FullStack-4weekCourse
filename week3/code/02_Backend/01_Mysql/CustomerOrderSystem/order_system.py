import mysql.connector
from datetime import date

# Step 1: Connect to MySQL Server
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789"  # Change this if needed
)
cursor = con.cursor()
print("✅ Connected to MySQL")

# Step 2: Create Database
cursor.execute("CREATE DATABASE IF NOT EXISTS ShopDB")
print("✅ Database 'ShopDB' created")

# Step 3: Use Database
cursor.execute("USE ShopDB")

# Step 4: Create Tables
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Customers (
        customer_id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(100),
        email VARCHAR(100)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Orders (
        order_id INT PRIMARY KEY AUTO_INCREMENT,
        customer_id INT,
        product_name VARCHAR(100),
        amount DECIMAL(10,2),
        order_date DATE,
        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
    )
""")
print("✅ Tables 'Customers' and 'Orders' created")

# Step 5: Delete previous data and reset auto-increment
cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
cursor.execute("DELETE FROM Orders")
cursor.execute("DELETE FROM Customers")
cursor.execute("ALTER TABLE Customers AUTO_INCREMENT = 1")
cursor.execute("ALTER TABLE Orders AUTO_INCREMENT = 1")
cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
print("🧹 Old data cleared")


# Step 6: Insert Sample Customers
cursor.executemany("""
    INSERT INTO Customers (name, email) VALUES (%s, %s)
""", [
    ('Alice', 'alice@example.com'),
    ('Bob', 'bob@example.com'),
    ('Charlie', 'charlie@example.com')
])

con.commit()  # ✅ Commit customers before inserting orders

# Step 7: Insert Sample Orders
cursor.executemany("""
    INSERT INTO Orders (customer_id, product_name, amount, order_date)
    VALUES (%s, %s, %s, %s)
""", [
    (1, 'Laptop', 999.99, date(2025, 6, 29)),
    (1, 'Mouse', 25.00, date(2025, 6, 30)),
    (2, 'Keyboard', 45.00, date(2025, 6, 30)),
])

con.commit()
print("✅ Sample data inserted")

# Step 8: All orders with customer details
print("\n📦 All Orders with Customer Details:")
cursor.execute("""
    SELECT o.order_id, c.name, c.email, o.product_name, o.amount, o.order_date
    FROM Orders o
    JOIN Customers c ON o.customer_id = c.customer_id
""")
for row in cursor.fetchall():
    print(row)

# Step 9: Customers who haven’t placed any orders
print("\n🧍 Customers with No Orders:")
cursor.execute("""
    SELECT c.customer_id, c.name, c.email
    FROM Customers c
    LEFT JOIN Orders o ON c.customer_id = o.customer_id
    WHERE o.order_id IS NULL
""")
for row in cursor.fetchall():
    print(row)

# Step 10: Total number of orders per customer
print("\n📈 Order Count per Customer:")
cursor.execute("""
    SELECT c.name, COUNT(o.order_id) as total_orders
    FROM Customers c
    LEFT JOIN Orders o ON c.customer_id = o.customer_id
    GROUP BY c.customer_id, c.name
""")
for row in cursor.fetchall():
    print(row)

# Close connection
cursor.close()
con.close()
print("\n✅ MySQL connection closed.")
