# Numeric Types
integer_value = 10               # <class 'int'>
float_value = 10.5               # <class 'float'>
complex_value = 3 + 4j           # <class 'complex'>

# Text Type
string_value = "Hello, Python!"  # <class 'str'>

# Sequence Types
list_value = [1, 2, 3, 4]        # <class 'list'>
tuple_value = (5, 6, 7)          # <class 'tuple'>
range_value = range(5)         # <class 'range'>

# Mapping Type
dict_value = {"name": "Alice", "age": 22}  # <class 'dict'>

# Set Types
set_value = {1, 2, 3}            # <class 'set'>
frozenset_value = frozenset([4, 5, 6])  # <class 'frozenset'>

# Boolean Type
bool_value = True                # <class 'bool'>

# Binary Types
bytes_value = b"hello"           # <class 'bytes'>
bytearray_value = bytearray(5)   # <class 'bytearray'>
memoryview_value = memoryview(bytes(5))  # <class 'memoryview'>

# Print all types with values
print("Data Types in Python:")
print(f"Integer: {integer_value} → {type(integer_value)}")             # Integer: 10 → <class 'int'>
print(f"Float: {float_value} → {type(float_value)}")                   # Float: 10.5 → <class 'float'>
print(f"Complex: {complex_value} → {type(complex_value)}")             # Complex: (3+4j) → <class 'complex'>
print(f"String: {string_value} → {type(string_value)}")                # String: Hello, Python! → <class 'str'>
print(f"List: {list_value} → {type(list_value)}")                      # List: [1, 2, 3, 4] → <class 'list'>
print(f"Tuple: {tuple_value} → {type(tuple_value)}")                   # Tuple: (5, 6, 7) → <class 'tuple'>
print(f"Range: {list(range_value)} → {type(range_value)}")             # Range: [0, 1, 2, 3, 4] → <class 'range'>
print(f"Dictionary: {dict_value} → {type(dict_value)}")                # Dictionary: {'name': 'Alice', 'age': 22} → <class 'dict'>
print(f"Set: {set_value} → {type(set_value)}")                         # Set: {1, 2, 3} → <class 'set'>
print(f"Frozenset: {frozenset_value} → {type(frozenset_value)}")       # Frozenset: frozenset({4, 5, 6}) → <class 'frozenset'>
print(f"Boolean: {bool_value} → {type(bool_value)}")                   # Boolean: True → <class 'bool'>
print(f"Bytes: {bytes_value} → {type(bytes_value)}")                   # Bytes: b'hello' → <class 'bytes'>
print(f"Bytearray: {bytearray_value} → {type(bytearray_value)}")       # Bytearray: bytearray(b'\x00\x00\x00\x00\x00') → <class 'bytearray'>
print(f"Memoryview: {memoryview_value} → {type(memoryview_value)}")    # Memoryview: <memory at 0x...> → <class 'memoryview'>


# Creating complex numbers
c1 = 3 + 4j        # 3 is real, 4j is imaginary
c2 = complex(5, 2) # another way using the complex() function

# Access real and imaginary parts
print("Complex Number:", c1)                # Complex Number: (3+4j)
print("Real Part:", c1.real)                # Real Part: 3.0
print("Imaginary Part:", c1.imag)           # Imaginary Part: 4.0

# Arithmetic with complex numbers
add = c1 + c2
sub = c1 - c2
mul = c1 * c2
div = c1 / c2

print("Addition:", add)                     # Addition: (8+6j)
print("Subtraction:", sub)                  # Subtraction: (-2+2j)
print("Multiplication:", mul)               # Multiplication: (7+26j)
print("Division:", div)                     # Division: (0.6551724137931034+0.4482758620689655j)

# Type checking
print("Type of c1:", type(c1))              # <class 'complex'>
