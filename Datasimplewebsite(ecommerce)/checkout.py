import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="ecommerce_website"
)
cur = con.cursor()

email = input("Enter your email to checkout: ")
cur.execute("SELECT id FROM users WHERE email = %s", (email,))
user = cur.fetchone()

if not user:
    print("❌ User not found.")
else:
    user_id = user[0]
    cur.execute("""
        SELECT product_id, quantity, p.price
        FROM cart c
        JOIN products p ON c.product_id = p.id
        WHERE c.user_id = %s
    """, (user_id,))
    
    items = cur.fetchall()
    if not items:
        print("🛒 Cart is empty!")
    else:
        total_amount = sum([qty * price for _, qty, price in items])
        cur.execute("INSERT INTO orders (user_id, total_amount) VALUES (%s, %s)", (user_id, total_amount))
        order_id = cur.lastrowid

        for product_id, quantity, price in items:
            cur.execute("""
                INSERT INTO order_items (order_id, product_id, quantity, price) 
                VALUES (%s, %s, %s, %s)
            """, (order_id, product_id, quantity, price))

        cur.execute("DELETE FROM cart WHERE user_id = %s", (user_id,))
        con.commit()
        print(f"✅ Order placed! Order ID: {order_id}, Total: ₹{total_amount}")

cur.close()
con.close()
