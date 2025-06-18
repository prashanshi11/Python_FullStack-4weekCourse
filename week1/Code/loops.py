# 1. FOR LOOP EXAMPLE
print("1. For Loop Example:")
for i in range(5):
    print(i)  # Output: 0 1 2 3 4

# 2. WHILE LOOP EXAMPLE
print("\n2. While Loop Example:")
i = 0
while i < 5:
    print(i)  # Output: 0 1 2 3 4
    i += 1

# 3. NESTED FOR LOOP
print("\n3. Nested For Loop:")
for i in range(2):
    for j in range(3):
        print(f"i={i}, j={j}")  
# Output:
# i=0, j=0
# i=0, j=1
# i=0, j=2
# i=1, j=0
# i=1, j=1
# i=1, j=2

# 4. BREAK STATEMENT IN FOR LOOP
print("\n4. Break Statement in For Loop:")
for i in range(5):
    if i == 3:
        break
    print(i)  # Output: 0 1 2

# 5. CONTINUE STATEMENT IN FOR LOOP
print("\n5. Continue Statement in For Loop:")
for i in range(5):
    if i == 3:
        continue
    print(i)  # Output: 0 1 2 4

# 6. PASS STATEMENT EXAMPLE
print("\n6. Pass Statement Example:")
for i in range(3):
    pass  # No output, just placeholder
print("Loop executed with pass")  # Output: Loop executed with pass

# 7. ENUMERATE IN FOR LOOP
print("\n7. Enumerate in For Loop:")
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(f"{index}: {name}")
# Output:
# 0: Alice
# 1: Bob
# 2: Charlie
