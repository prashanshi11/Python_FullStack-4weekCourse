import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="ecommerce_website"
)
cur = con.cursor()

email = input("Enter your email: ")
cur.execute("SELECT id FROM users WHERE email = %s", (email,))
user = cur.fetchone()

if not user:
    print("❌ User not found.")
else:
    user_id = user[0]
    product_id = int(input("Enter Product ID to add to cart: "))
    quantity = int(input("Enter quantity: "))

    cur.execute("INSERT INTO cart (user_id, product_id, quantity) VALUES (%s, %s, %s)",
                (user_id, product_id, quantity))
    con.commit()
    print("✅ Product added to cart!")

cur.close()
con.close()
