# 1. Arithmetic Operators
a = 10
b = 3
print("Arithmetic Operators:")
print("Addition:", a + b)          # 13
print("Subtraction:", a - b)       # 7
print("Multiplication:", a * b)    # 30
print("Division:", a / b)          # 3.3333333333333335
print("Floor Division:", a // b)   # 3
print("Modulus:", a % b)           # 1
print("Exponentiation:", a ** b)   # 1000

# 2. Assignment Operators
x = 5
print("\nAssignment Operators:")
x += 2
print("x += 2:", x)                # 7
x *= 3
print("x *= 3:", x)                # 21
x -= 4
print("x -= 4:", x)                # 17

# 3. Comparison Operators
print("\nComparison Operators:")
print("a == b:", a == b)           # False
print("a != b:", a != b)           # True
print("a > b:", a > b)             # True
print("a < b:", a < b)             # False
print("a >= b:", a >= b)           # True
print("a <= b:", a <= b)           # False

# 4. Logical Operators
print("\nLogical Operators:")
print("True and False:", True and False)   # False
print("True or False:", True or False)     # True
print("not True:", not True)               # False

# 5. Bitwise Operators
print("\nBitwise Operators:")
print("a & b:", a & b)             # 2  (1010 & 0011 = 0010)
print("a | b:", a | b)             # 11 (1010 | 0011 = 1011)
print("a ^ b:", a ^ b)             # 9  (1010 ^ 0011 = 1001)
print("~a:", ~a)                   # -11 (inverts bits and adds 1)
print("a << 1:", a << 1)           # 20 (left shift)
print("a >> 1:", a >> 1)           # 5  (right shift)

# 6. Membership Operators
print("\nMembership Operators:")
text = "hello"
print("'h' in text:", 'h' in text)           # True
print("'x' not in text:", 'x' not in text)   # True

# 7. Identity Operators
print("\nIdentity Operators:")
m = [1, 2, 3]
n = m
p = [1, 2, 3]
print("m is n:", m is n)           # True (same object)
print("m is p:", m is p)           # False (different objects)
print("m is not p:", m is not p)   # True


