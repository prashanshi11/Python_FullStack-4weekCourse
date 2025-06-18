# -----------------------------
# Python Lists - Full Tutorial
# -----------------------------

# A list is an ordered, mutable collection of elements.
# It can contain different data types.

# Creating lists
numbers = [10, 20, 30, 40]        # List of integers
names = ["Alice", "Bob", "Charlie"]  # List of strings
mixed = [1, "Hello", 3.14, True]     # Heterogeneous list

print(numbers)     # Output: [10, 20, 30, 40]
print(names)       # Output: ['Alice', 'Bob', 'Charlie']
print(mixed)       # Output: [1, 'Hello', 3.14, True]

# -----------------------------
# Accessing List Elements
# -----------------------------

# Indexing (positive and negative)
print(names[1])    # Output: Bob
print(numbers[-1]) # Output: 40

# -----------------------------
# Slicing a List
# -----------------------------

print(numbers[1:3])    # Output: [20, 30]
print(numbers[::-1])   # Output: [40, 30, 20, 10] (reversed list)

# -----------------------------
# Modifying Elements
# -----------------------------

numbers[2] = 300
print(numbers)     # Output: [10, 20, 300, 40]

# -----------------------------
# Adding Elements
# -----------------------------

numbers.append(50)      # Adds 50 to the end
print(numbers)          # Output: [10, 20, 300, 40, 50]

numbers.extend([60, 70])  # Adds multiple values
print(numbers)            # Output: [10, 20, 300, 40, 50, 60, 70]

numbers.insert(2, 25)     # Inserts 25 at index 2
print(numbers)            # Output: [10, 20, 25, 300, 40, 50, 60, 70]

# -----------------------------
# Removing Elements
# -----------------------------

numbers.remove(300)       # Removes first occurrence of 300
print(numbers)            # Output: [10, 20, 25, 40, 50, 60, 70]

popped = numbers.pop()    # Pops last element (70)
print(popped)             # Output: 70
print(numbers)            # Output: [10, 20, 25, 40, 50, 60]

# -----------------------------
# List Comprehension
# -----------------------------

# Create a list of squares from 0 to 4
squares = [x**2 for x in range(5)]
print(squares)            # Output: [0, 1, 4, 9, 16]

# -----------------------------
# Nested Lists
# -----------------------------

matrix = [[1, 2], [3, 4], [5, 6]]  # List of lists
print(matrix[1][1])       # Output: 4 (2nd row, 2nd column)

# -----------------------------
# Sorting and Reversing
# -----------------------------

names.sort()              # Sorts alphabetically
print(names)              # Output: ['Alice', 'Bob', 'Charlie']

numbers.sort()            # Sorts numerically
print(numbers)            # Output: [10, 20, 25, 40, 50, 60]

numbers.reverse()         # Reverses the list
print(numbers)            # Output: [60, 50, 40, 25, 20, 10]

# -----------------------------
# Copying a List
# -----------------------------

copy_list = numbers.copy()
print(copy_list)          # Output: [60, 50, 40, 25, 20, 10]

# -----------------------------
# Clearing a List
# -----------------------------

copy_list.clear()
print(copy_list)          # Output: []

# -----------------------------
# List Methods Recap
# -----------------------------

print(numbers.count(50))     # Output: 1 (occurrences of 50)
print(numbers.index(25))     # Output: 3 (position of 25)

# -----------------------------
# List Visualization
# -----------------------------

sample = ['a', 'b', 'c', 'd']
print(sample[0])         # Output: a
print(sample[-1])        # Output: d
print(sample[1:3])       # Output: ['b', 'c']
