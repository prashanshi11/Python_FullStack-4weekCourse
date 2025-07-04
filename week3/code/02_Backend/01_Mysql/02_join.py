# 📌 Importing required modules
import mysql.connector

# ✅ Step 1: Connect to the MySQL database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",        # Replace with your MySQL password
    database="your_database_name"    # Replace with your database name
)

# ✅ Step 2: Create a cursor object to execute queries
cur = con.cursor()

# -------------------------------
# 🔄 INNER JOIN: Returns rows where there's a match in both tables
# -------------------------------
print("\n🔄 INNER JOIN (Customers with Orders):")
cur.execute("""
    SELECT customers.name, orders.product_name
    FROM customers
    INNER JOIN orders ON customers.customer_id = orders.customer_id;
""")
for row in cur.fetchall():
    print(row)

# -------------------------------
# ⬅️ LEFT JOIN: Returns all customers, even if they have no orders
# -------------------------------
print("\n⬅️ LEFT JOIN (All Customers, even if no Orders):")
cur.execute("""
    SELECT customers.name, orders.product_name
    FROM customers
    LEFT JOIN orders ON customers.customer_id = orders.customer_id;
""")
for row in cur.fetchall():
    print(row)

# -------------------------------
# ➡️ RIGHT JOIN: Returns all orders, even if the customer is missing
# -------------------------------
print("\n➡️ RIGHT JOIN (All Orders, even if customer is missing):")
cur.execute("""
    SELECT customers.name, orders.product_name
    FROM customers
    RIGHT JOIN orders ON customers.customer_id = orders.customer_id;
""")
for row in cur.fetchall():
    print(row)

# -------------------------------
# 🌐 FULL OUTER JOIN: Combines LEFT and RIGHT JOIN (not supported directly in MySQL)
# We'll simulate FULL OUTER JOIN using UNION
# -------------------------------
print("\n🌐 FULL OUTER JOIN (Simulated using UNION):")
cur.execute("""
    SELECT customers.name, orders.product_name
    FROM customers
    LEFT JOIN orders ON customers.customer_id = orders.customer_id
    UNION
    SELECT customers.name, orders.product_name
    FROM customers
    RIGHT JOIN orders ON customers.customer_id = orders.customer_id;
""")
for row in cur.fetchall():
    print(row)

# -------------------------------
# ✖️ CROSS JOIN: Every customer with every product (Cartesian Product)
# -------------------------------
print("\n✖️ CROSS JOIN (Every customer × every order):")
cur.execute("""
    SELECT customers.name, orders.product_name
    FROM customers
    CROSS JOIN orders;
""")
for row in cur.fetchall():
    print(row)

# -------------------------------
# 🔁 SELF JOIN: Join a table with itself (e.g., employees and managers)
# -------------------------------
print("\n🔁 SELF JOIN (Employees with their Managers):")
cur.execute("""
    SELECT A.name AS Employee, B.name AS Manager
    FROM employees A
    JOIN employees B ON A.manager_id = B.employee_id;
""")
for row in cur.fetchall():
    print(row)

# ✅ Step 3: Close the cursor and connection
cur.close()
con.close()
