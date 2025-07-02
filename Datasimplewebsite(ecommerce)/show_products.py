import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="ecommerce_website"
)
cur = con.cursor()

cur.execute("SELECT id, name, price FROM products")
products = cur.fetchall()

print("🛒 Available Products:")
print("--------------------------------")
for prod in products:
    print(f"ID: {prod[0]} | Name: {prod[1]} | Price: ₹{prod[2]}")
print("--------------------------------")

cur.close()
con.close()
