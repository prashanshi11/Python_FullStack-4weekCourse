import mysql.connector

# Step 1: Connect to MySQL server (no database yet)
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789"
)
cursor = con.cursor()

# Step 2: Create and use database
cursor.execute("DROP DATABASE IF EXISTS ShopDB")
cursor.execute("CREATE DATABASE ShopDB")
cursor.execute("USE ShopDB")

# Step 3: Create tables
cursor.execute("""
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100)
)
""")

cursor.execute("""
CREATE TABLE Orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    product_name VARCHAR(100),
    amount DECIMAL(10,2),
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
)
""")

# Step 4: Insert data into Customers
cursor.executemany("""
INSERT INTO Customers (name, email)
VALUES (%s, %s)
""", [
    ('Alice', 'alice@example.com'),
    ('Bob', 'bob@example.com'),
    ('Charlie', 'charlie@example.com')
])

# Step 5: Insert data into Orders
cursor.executemany("""
INSERT INTO Orders (customer_id, product_name, amount, order_date)
VALUES (%s, %s, %s, %s)
""", [
    (1, 'Laptop', 999.99, '2025-06-29'),
    (1, 'Mouse', 25.00, '2025-06-30'),
    (2, 'Keyboard', 45.00, '2025-06-30')
])

con.commit()

# Step 6: Query 1 - All orders with customer details
print("\n🔹 All Orders with Customer Details:")
cursor.execute("""
SELECT Orders.order_id, Customers.name, Customers.email, Orders.product_name, Orders.amount, Orders.order_date
FROM Orders
JOIN Customers ON Orders.customer_id = Customers.customer_id
""")
for row in cursor.fetchall():
    print(row)

# Step 7: Query 2 - Customers who haven’t placed any orders
print("\n🔹 Customers Who Haven’t Placed Any Orders:")
cursor.execute("""
SELECT name, email FROM Customers
WHERE customer_id NOT IN (SELECT DISTINCT customer_id FROM Orders)
""")
for row in cursor.fetchall():
    print(row)

# Step 8: Query 3 - Total number of orders per customer
print("\n🔹 Total Number of Orders Per Customer:")
cursor.execute("""
SELECT Customers.name, COUNT(Orders.order_id) AS total_orders
FROM Customers
LEFT JOIN Orders ON Customers.customer_id = Orders.customer_id
GROUP BY Customers.customer_id
""")
for row in cursor.fetchall():
    print(row)

# Close the connection
cursor.close()
con.close()
