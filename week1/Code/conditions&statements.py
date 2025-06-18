# 1. Simple if statement
x = 10
if x > 5:
    print("x is greater than 5")  # Output: x is greater than 5

# 2. if-else statement
y = 2
if y >= 5:
    print("y is greater than or equal to 5")
else:
    print("y is less than 5")  # Output: y is less than 5

# 3. if-elif-else statement
z = 7
if z > 10:
    print("z is greater than 10")
elif z == 7:
    print("z is 7")  # Output: z is 7
else:
    print("z is less than 7")

# 4. Nested if statement
a = 8
if a > 0:
    if a % 2 == 0:
        print("a is a positive even number")  # Output: a is a positive even number
    else:
        print("a is a positive odd number")
else:
    print("a is not positive")

# 5. Logical operators with if
b = 6
if b > 3 and b < 10:
    print("b is between 3 and 10")  # Output: b is between 3 and 10

# 6. Using 'or' operator
c = 1
if c < 2 or c > 5:
    print("c is either less than 2 or greater than 5")  # Output: c is either less than 2 or greater than 5

# 7. Using 'not' operator
d = 4
if not d > 5:
    print("d is NOT greater than 5")  # Output: d is NOT greater than 5
