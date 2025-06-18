'''
# ✅ 1. Basic Function (No Parameters, No Return)
def greet():
    print("Hello! Welcome to Python.")

greet()
# Output: Hello! Welcome to Python.


# ✅ 2. Function with Parameters
def greet_name(name):
    print(f"Hello, {name}!")

greet_name("Prashanshi")
# Output: Hello, Prashanshi!


# ✅ 3. Function with Return Value
def add(a, b):
    return a + b

result = add(10, 20)
print("Sum:", result)
# Output: Sum: 30


# ✅ 4. Function with Default Parameter
def greet_default(name="Guest"):
    print(f"Hello, {name}!")

greet_default()
greet_default("Prashanshi")
# Output: Hello, Guest!
# Output: Hello, Prashanshi!


# ✅ 5. Function with Keyword Arguments
def profile(name, age):
    print(f"Name: {name}, Age: {age}")

profile(age=22, name="Prashanshi")
# Output: Name: Prashanshi, Age: 22


# ✅ 6. Function with *args (Variable-Length Positional Arguments)
def total_marks(*marks):
    print("Marks:", marks)
    print("Total:", sum(marks))

total_marks(90, 80, 85)
# Output: Marks: (90, 80, 85)
# Output: Total: 255


# ✅ 7. Function with **kwargs (Variable-Length Keyword Arguments)
def student_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

student_details(name="Prashanshi", age=22, course="Python")
# Output:
# name: Prashanshi
# age: 22
# course: Python


# ✅ 8. Lambda Function (Anonymous Function)
square = lambda x: x * x
print("Square of 5:", square(5))
# Output: Square of 5: 25


# ✅ 9. Recursive Function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))
# Output: Factorial of 5: 120


# ✅ 10. Nested Function
def outer():
    def inner():
        print("Inner function")
    print("Outer function")
    inner()

outer()
# Output:
# Outer function
# Inner function


# ✅ 11. Function with List as Argument
def print_list(items):
    for item in items:
        print(item)

fruits = ["apple", "banana", "mango"]
print_list(fruits)
# Output:
# apple
# banana
# mango


# ✅ 12. Function Returning Multiple Values
def calculate(a, b):
    return a + b, a - b, a * b

add_val, sub_val, mul_val = calculate(10, 5)
print("Add:", add_val)
print("Subtract:", sub_val)
print("Multiply:", mul_val)
# Output:
# Add: 15
# Subtract: 5
# Multiply: 50


# ✅ 13. Function as Argument
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet_func(func):
    print(func("Hello"))

greet_func(shout)   # Output: HELLO
greet_func(whisper) # Output: hello


# ✅ 14. Using map() with Lambda
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, nums))
print("Squares:", squares)
# Output: Squares: [1, 4, 9, 16]


# ✅ 15. Using filter() with Lambda
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers:", evens)
# Output: Even numbers: [2, 4, 6]


# ✅ 16. Using reduce() with Lambda
from functools import reduce

nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print("Product of all elements:", product)
# Output: Product of all elements: 24






'''








# **bill splitter according to the number of person**
# **unit comverter kilometers to miles**
# **total price according to the number of product with prices and the total of those**
# **Email evaluator**


'''
# ✅ 1. Bill Splitter Function

def split_bill(bill_amount, num_people):
    tax_rate = 0.10  # 10% tax
    tax = bill_amount * tax_rate
    total_with_tax = bill_amount + tax
    per_person = total_with_tax / num_people

    print(f"\nOriginal Bill: ₹{bill_amount:.2f}")
    print(f"Tax (10%): ₹{tax:.2f}")
    print(f"Total Amount with Tax: ₹{total_with_tax:.2f}")
    print(f"Each Person Should Pay: ₹{per_person:.2f}")

# Example usage
try:
    bill = float(input("Enter the total bill amount (in ₹): "))
    people = int(input("Enter the number of people to split the bill: "))
    if people > 0:
        split_bill(bill, people)
    else:
        print("Number of people must be greater than 0.")
except ValueError:
    print("Invalid input! Please enter numeric values.")


'''

'''
# ✅ 2. Unit Converter: Kilometers to Miles

def km_to_miles(km):
    miles = km * 0.621371
    return miles

# Example usage
km = float(input("Enter distance in kilometers: "))
converted = km_to_miles(km)
print(f"{km} kilometers is equal to {converted:.2f} miles.")

'''

'''
#✅ 3. Total Price Calculator (Product × Quantity)
def calculate_total(product_prices):
    total = 0
    print("\nItem-wise Breakdown:")
    for product, (price, qty) in product_prices.items():
        subtotal = price * qty
        total += subtotal
        print(f"{product}: ₹{price} x {qty} = ₹{subtotal}")
    return total

# Example usage
products = {
    "Pen": (10, 5),
    "Notebook": (50, 2),
    "Pencil": (5, 10)
}

total_bill = calculate_total(products)
print(f"\nTotal Price: ₹{total_bill}")

'''
'''
# ✅ 4. Email Evaluator Function

def is_valid_email(email):
    if "@" in email and "." in email.split("@")[-1] and " " not in email:
        return True
    return False

# Example usage
email = input("Enter your email: ")
if is_valid_email(email):
    print("✅ Valid Email")
else:
    print("❌ Invalid Email")
'''