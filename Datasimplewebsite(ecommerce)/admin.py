import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        database="ecommerce_website"
    )

def view_users():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT id, name, email FROM users")
    print("\n👥 All Users:")
    for u in cur.fetchall():
        print(f"ID: {u[0]} | Name: {u[1]} | Email: {u[2]}")
    cur.close()
    con.close()

def view_orders():
    con = connect()
    cur = con.cursor()
    cur.execute("""
        SELECT o.id, u.name, o.total_amount, o.order_date
        FROM orders o
        JOIN users u ON o.user_id = u.id
        ORDER BY o.order_date DESC
    """)
    print("\n📦 All Orders:")
    for o in cur.fetchall():
        print(f"Order ID: {o[0]} | User: {o[1]} | Total: ₹{o[2]} | Date: {o[3]}")
    cur.close()
    con.close()

def view_order_details():
    order_id = int(input("Enter Order ID to view details: "))
    con = connect()
    cur = con.cursor()
    cur.execute("""
        SELECT p.name, oi.quantity, oi.price
        FROM order_items oi
        JOIN products p ON oi.product_id = p.id
        WHERE oi.order_id = %s
    """, (order_id,))
    print(f"\n📄 Details for Order ID {order_id}:")
    for item in cur.fetchall():
        print(f"Product: {item[0]} | Qty: {item[1]} | ₹{item[2]} each")
    cur.close()
    con.close()

# Admin Menu
while True:
    print("\n🔐 Admin Panel")
    print("1. View All Users")
    print("2. View All Orders")
    print("3. View Order Details")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    if choice == '1':
        view_users()
    elif choice == '2':
        view_orders()
    elif choice == '3':
        view_order_details()
    elif choice == '4':
        print("🚪 Exiting Admin Panel.")
        break
    else:
        print("❌ Invalid choice.")
