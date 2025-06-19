# variable_example.py

# 🚀 Python Variable Examples Explained

# ✅ 1. Basic variable assignment
name = "Prashanshi"     # string variable
age = 21                # integer variable
height = 5.4            # float variable
is_student = True       # boolean variable

print("=== Basic Variables ===")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} feet")
print(f"Are you a student? {is_student}\n") 

# Output:
# === Basic Variables ===
# Name: Prashanshi
# Age: 21
# Height: 5.4 feet
# Are you a student? True




# ✅ 2. Reassigning variables
age = 22  # Changed the value
print("Updated Age:", age)

# Output: Updated Age: 22




# ✅ 3. Multiple variables in one line
city, country = "Jalandhar", "India"
print(f"\nLocation: {city}, {country}")

# Output: Location: Jalandhar, India




# ✅ 4. Same value to multiple variables
x = y = z = 100
print("\nx:", x, "y:", y, "z:", z)

# Output: x: 100 y: 100 z: 100




# ✅ 5. Type checking
print("\n=== Type of Each Variable ===")
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of height:", type(height))
print("Type of is_student:", type(is_student))

# Output:
# === Type of Each Variable ===     
# Type of name: <class 'str'>
# Type of age: <class 'int'>    
# Type of height: <class 'float'>
# Type of is_student: <class 'bool'>




# ✅ 6. Type casting
str_age = str(age)       # int to string
int_height = int(height) # float to int (loses decimal)
float_x = float(x)       # int to float

print("\n=== Type Casting ===")
print("str_age:", str_age, type(str_age))
print("int_height:", int_height, type(int_height))
print("float_x:", float_x, type(float_x))

# Output:
# === Type Casting ===  
# str_age: 22 <class 'str'>
# int_height: 5 <class 'int'>
# float_x: 100.0 <class 'float'>




# ✅ 7. Using variables in operations
math_score = 85
science_score = 90
total = math_score + science_score
average = total / 2

print("\n=== Calculations ===")
print("Math Score:", math_score)
print("Science Score:", science_score)
print("Total Score:", total)
print("Average Score:", average)

# Output:
# === Calculations ===
# Math Score: 85
# Science Score: 90
# Total Score: 175
# Average Score: 87.5




# ✅ 8. Constants (by convention, use all caps)
PI = 3.14159
GRAVITY = 9.8
print("\nConstants:")
print("PI:", PI)
print("Gravity:", GRAVITY)

# Output:
# Constants:
# PI: 3.14159
# Gravity: 9.8




# ✅ 9. Descriptive naming (recommended)
user_email = "prashanshi@example.com"
total_items_in_cart = 4
is_logged_in = True

print("\nDescriptive Variable Names:")
print("Email:", user_email)
print("Cart Items:", total_items_in_cart)
print("Login Status:", is_logged_in)

# Output:
# Descriptive Variable Names:
# Email: prashanshi@example.com
# Cart Items: 4
# Login Status: True


