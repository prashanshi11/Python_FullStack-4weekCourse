"""# -------------------------------------------
# 🧠 What is a Tuple?
# A tuple is an ordered, immutable collection in Python.
# -------------------------------------------

# Creating Tuples
t1 = ()  # Empty Tuple
print(t1)  # Output: ()

t2 = (1, 2, 3)  # Tuple with integers
print(t2)  # Output: (1, 2, 3)

t3 = (10, "AI", 3.14)  # Mixed data types
print(t3)  # Output: (10, 'AI', 3.14)

t4 = (1, (2, 3), ["a", "b"])  # Nested tuple
print(t4)  # Output: (1, (2, 3), ['a', 'b'])

# -------------------------------------------
# Accessing Tuple Elements
# -------------------------------------------
t = (100, 200, 300)
print(t[0])     # Output: 100 (First element)
print(t[-1])    # Output: 300 (Last element)

# -------------------------------------------
# Tuple Operations
# -------------------------------------------
t = (1, 2, 3)
print(len(t))  # Output: 3 (Length of tuple)

print(t + (4, 5))  # Output: (1, 2, 3, 4, 5) (Concatenation)

print(t * 2)  # Output: (1, 2, 3, 1, 2, 3) (Repetition)

print(2 in t)  # Output: True (Membership check)

# -------------------------------------------
# Tuple Methods
# -------------------------------------------
t = (1, 2, 2, 3, 4)
print(t.count(2))   # Output: 2 (Count of value 2)
print(t.index(3))   # Output: 3 (Index of value 3)

# -------------------------------------------
# Tuple as Dictionary Key
# -------------------------------------------
location = {(28.61, 77.23): "Delhi"}
print(location[(28.61, 77.23)])  # Output: Delhi

# -------------------------------------------
# Looping Through a Tuple
# -------------------------------------------
languages = ("Python", "Java", "C++")
for lang in languages:
    print(lang)
# Output:
# Python
# Java
# C++

# -------------------------------------------
# Tuple Packing and Unpacking
# -------------------------------------------
person = ("Prashanshi", 21, "Python")  # Packing
name, age, lang = person               # Unpacking
print(name)  # Output: Prashanshi
print(age)   # Output: 21
print(lang)  # Output: Python

# -------------------------------------------
# Tuple Comparison with Lists (For Reference)
# -------------------------------------------
tuple1 = (1, 2, 3)
list1 = [1, 2, 3]

print(type(tuple1))  # Output: <class 'tuple'>
print(type(list1))   # Output: <class 'list'>
"""


"""
Task 1: Flight Data Analytics

Given a tuple of flight(flight_number, origin, destination, duration),
flight=(
    ("AA123","NYC","LAX",300)
    ("BA456","LAX","CHI",270)
    ("DL789","CHI","NYC",200)
    ("UA101","NYC","MIA",250)
    ("SW202","MIA","LAX",320)
)

# Task: Write a Python program to analyze flight data using tuples.
Print all flights originating from NYC.
Sort by duration and print the sorted flights.
Find the flight with the longest duration.
"""
# Flight Data Tuple
flight = (
    ("AA123", "NYC", "LAX", 300),
    ("BA456", "LAX", "CHI", 270),
    ("DL789", "CHI", "NYC", 200),
    ("UA101", "NYC", "MIA", 250),
    ("SW202", "MIA", "LAX", 320)
)

# -------------------------------------------
# 1. Print all flights originating from NYC
print("Flights originating from NYC:")
for f in flight:
    if f[1] == "NYC":
        print(f)
# Output:
# ('AA123', 'NYC', 'LAX', 300)
# ('UA101', 'NYC', 'MIA', 250)

# -------------------------------------------
# 2. Sort by duration and print the sorted flights
sorted_flights = sorted(flight, key=lambda x: x[3])
print("\nFlights sorted by duration:")
for f in sorted_flights:
    print(f)
# Output:
# ('DL789', 'CHI', 'NYC', 200)
# ('UA101', 'NYC', 'MIA', 250)
# ('BA456', 'LAX', 'CHI', 270)
# ('AA123', 'NYC', 'LAX', 300)
# ('SW202', 'MIA', 'LAX', 320)

# -------------------------------------------
# 3. Find the flight with the longest duration
longest_flight = max(flight, key=lambda x: x[3])
print("\nFlight with the longest duration:")
print(longest_flight)
# Output:
# ('SW202', 'MIA', 'LAX', 320)
