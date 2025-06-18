'''
# -----------------------------------
# 1. Built-in Module: math
# -----------------------------------
import math

# Using math module functions
print("Square root of 36:", math.sqrt(36))     # Output: 6.0
print("Value of Pi:", math.pi)                 # Output: 3.141592653589793
print("Factorial of 5:", math.factorial(5))    # Output: 120

# -----------------------------------
# 2. Built-in Module: random
# -----------------------------------
import random

# Generating random values
print("Random number (0-1):", random.random())              # Output: e.g., 0.5748392
print("Random integer (1-10):", random.randint(1, 10))      # Output: e.g., 7
print("Random choice:", random.choice(['apple', 'banana'])) # Output: e.g., 'banana'

# -----------------------------------
# 3. Built-in Module: datetime
# -----------------------------------
import datetime

# Working with date and time
now = datetime.datetime.now()
print("Current date and time:", now)           # Output: e.g., 2025-06-18 10:22:43.123456

today = datetime.date.today()
print("Today's date:", today)                  # Output: e.g., 2025-06-18

# -----------------------------------
# 4. Built-in Module: os and sys
# -----------------------------------
import os
import sys

# OS and System utilities
print("Current working directory:", os.getcwd())  # Output: path where this script runs
print("Python path (sys.path):", sys.path)        # Output: list of search paths

# -----------------------------------
# 5. User-defined Module
# -----------------------------------
# Make sure this file exists in the same directory: my_module.py
# Content of my_module.py:
# -------------------------------
# def greet(name):
#     return f"Hello, {name}!"
#
# pi_value = 3.14159
#
# def area_of_circle(radius):
#     return pi_value * radius * radius
# -------------------------------

import my_module

print(my_module.greet("Prashanshi"))              # Output: Hello, Prashanshi!
print("Pi:", my_module.pi_value)                  # Output: Pi: 3.14159
print("Area of circle with r=3:", my_module.area_of_circle(3))  # Output: 28.27431

# -----------------------------------
# 6. Python Package Example
# -----------------------------------
# Folder structure:
# math_pkg/
# ├── __init__.py
# ├── addition.py
# └── subtraction.py

# addition.py content:
# ------------------------
# def add(a, b):
#     return a + b
# ------------------------

# subtraction.py content:
# ------------------------
# def subtract(a, b):
#     return a - b
# ------------------------

# __init__.py content:
# ------------------------
# from .addition import add
# from .subtraction import subtract
# ------------------------

# Ensure math_pkg folder is in same directory as this main.py
from math_pkg import add, subtract

print("Addition:", add(10, 5))             # Output: 15
print("Subtraction:", subtract(10, 5))     # Output: 5

# -----------------------------------
# 7. Different Import Styles
# -----------------------------------

# Full module import
import math
print("Power using full import:", math.pow(2, 3))      # Output: 8.0

# Module import with alias
import math as m
print("Square root using alias:", m.sqrt(49))          # Output: 7.0

# Import specific function
from math import factorial
print("Factorial using direct function:", factorial(6))  # Output: 720

# Import all (not recommended)
from math import *
print("Sine of 0:", sin(0))                            # Output: 0.0

# -----------------------------------
# 8. Exploring module contents using dir()
# -----------------------------------
print("Contents of math module:", dir(math))  # Output: list of functions and constants in math

# -----------------------------------
# 9. Summary Table Using Code
# -----------------------------------
# Install the tabulate library using: pip install tabulate

from tabulate import tabulate

table = [
    ["Module", "Use Case", "Example Function"],
    ["math", "Mathematical operations", "sqrt(), factorial()"],
    ["random", "Random data generation", "randint(), choice()"],
    ["datetime", "Dates and times", "now(), today()"],
    ["os", "Operating system tasks", "getcwd(), listdir()"],
    ["sys", "Python runtime info", "path, argv"]
]

print(tabulate(table, headers="firstrow", tablefmt="fancy_grid"))

# Output (formatted table):
# ┌────────────┬───────────────────────────────┬──────────────────────────┐
# │ Module     │ Use Case                     │ Example Function          │
# ├────────────┼───────────────────────────────┼──────────────────────────┤
# │ math       │ Mathematical operations       │ sqrt(), factorial()      │
# │ random     │ Random data generation        │ randint(), choice()      │
# │ datetime   │ Dates and times               │ now(), today()           │
# │ os         │ Operating system tasks        │ getcwd(), listdir()      │
# │ sys        │ Python runtime info           │ path, argv               │
# └────────────┴───────────────────────────────┴──────────────────────────┘
'''