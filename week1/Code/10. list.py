"""
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

"""


""" **Task 1: To-Do List Manager(simple)**
add tasks, remove tasks, and display the current list of tasks.



# Initialize empty to-do list
todo_list = []

# Adding tasks
todo_list.append("Buy groceries")
todo_list.append("Complete Python assignment")
todo_list.append("Call Mom")

# Display current tasks
print("Current To-Do List:")
for i, task in enumerate(todo_list, start=1):
    print(f"{i}. {task}")

# Removing a task
todo_list.remove("Call Mom")  # Remove specific task

# Display updated list
print("\nUpdated To-Do List:")
for i, task in enumerate(todo_list, start=1):
    print(f"{i}. {task}")


Expected Output:

Current To-Do List:
1. Buy groceries
2. Complete Python assignment
3. Call Mom

Updated To-Do List:
1. Buy groceries
2. Complete Python assignment



"""

"""
Task 2: StudentScores
list of student names and their scores, calculate average score, find highest and lowest scores.


code:
# Task 2: StudentScores

# List of students and their scores
students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("David", 90),
    ("Eva", 88)
]

# Calculate average score
total_score = sum(score for _, score in students)  # Sum all scores
average_score = total_score / len(students)        # Divide by number of students

# Find the highest score
highest_student = max(students, key=lambda x: x[1])  # Student with highest score

# Find the lowest score
lowest_student = min(students, key=lambda x: x[1])   # Student with lowest score

# Display the results
print("Student Scores:")
for name, score in students:
    print(f"{name}: {score}")

print(f"\nAverage Score: {average_score:.2f}")  # Display average with 2 decimal places
print(f"Highest Score: {highest_student[0]} with {highest_student[1]}")
print(f"Lowest Score: {lowest_student[0]} with {lowest_student[1]}")


Expected Output:
Student Scores:
Alice: 85
Bob: 92
Charlie: 78
David: 90
Eva: 88

Average Score: 86.60
Highest Score: Bob with 92
Lowest Score: Charlie with 78
"""


"""
Task 3: Guest list for a party
create a list of guests, add new guests, remove guests, and print the final list.

code:
"""

# Initial guest list
guest_list = ["Alice", "Bob", "Charlie"]

# Print initial list
print("Initial Guest List:")
print(guest_list)

# Adding new guests
guest_list.append("David")        # Add one guest at the end
guest_list.extend(["Eva", "Frank"])  # Add multiple guests at once

# Removing guests
guest_list.remove("Bob")          # Remove 'Bob' from the list

# Final guest list
print("\nFinal Guest List:")
for i, guest in enumerate(guest_list, start=1):
    print(f"{i}. {guest}")

""" 
Expected Output:

Initial Guest List:
['Alice', 'Bob', 'Charlie']

Final Guest List:
1. Alice
2. Charlie
3. David
4. Eva
5. Frank



"""