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
    cur.execute("""
        SELECT p.name, c.quantity, p.price, (c.quantity * p.price) AS total
        FROM cart c
        JOIN products p ON c.product_id = p.id
        WHERE c.user_id = %s
    """, (user_id,))
    
    items = cur.fetchall()
    print("\n🧺 Your Cart:")
    grand_total = 0
    for name, qty, price, total in items:
        print(f"{name} | Qty: {qty} | ₹{price} each | Subtotal: ₹{total}")
        grand_total += total
    print(f"💰 Grand Total: ₹{grand_total}")

cur.close()
con.close()
