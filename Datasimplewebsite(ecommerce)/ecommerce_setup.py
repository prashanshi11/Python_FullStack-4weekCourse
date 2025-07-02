import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789"
)
cur = con.cursor()

# Create DB
cur.execute("CREATE DATABASE IF NOT EXISTS ecommerce_website")
con.database = "ecommerce_website"

# Users table
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255)
)
""")

# Products
cur.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    description TEXT,
    price DECIMAL(10,2),
    image_path VARCHAR(255)
)
""")

# Cart
cur.execute("""
CREATE TABLE IF NOT EXISTS cart (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
)
""")

# Orders
cur.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    total_amount DECIMAL(10,2),
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
""")

# Order items
cur.execute("""
CREATE TABLE IF NOT EXISTS order_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    price DECIMAL(10,2),
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
)
""")

# Insert sample products
cur.executemany("""
INSERT INTO products (name, description, price, image_path) 
VALUES (%s, %s, %s, %s)
""", [
    ("T-shirt", "Cotton, Blue", 499.99, "product1.webp"),
    ("Laptop", "8GB RAM, SSD", 45999.00, "product2.webp"),
    ("Shoes", "Running shoes", 1499.00, "product3.webp")
])

con.commit()
print("✅ Database and Tables Created with Sample Products")
cur.close()
con.close()
