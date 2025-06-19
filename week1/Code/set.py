"""
# ✅ Creating Sets
a = {1, 2, 3, 4}
print("Set a:", a)  
# Output: Set a: {1, 2, 3, 4}

# ✅ Using set() to remove duplicates
b = set([1, 2, 2, 3])
print("Set b (from list with duplicates):", b)  
# Output: Set b (from list with duplicates): {1, 2, 3}

# ✅ Empty set
empty = set()
print("Empty set type:", type(empty))  
# Output: Empty set type: <class 'set'>

# ⚠️ {} creates a dictionary, not a set
not_a_set = {}
print("Type of {}:", type(not_a_set))  
# Output: Type of {}: <class 'dict'>

# ✅ Adding Elements
b.add(4)
print("After adding 4 to b:", b)  
# Output: After adding 4 to b: {1, 2, 3, 4}

# ✅ Removing Elements
b.remove(2)
print("After removing 2 from b:", b)  
# Output: After removing 2 from b: {1, 3, 4}

# ✅ Discard (no error if element not found)
b.discard(10)  
print("After discard(10):", b)  
# Output: After discard(10): {1, 3, 4}

# ✅ Pop (removes random item)
popped_item = b.pop()
print("Popped item:", popped_item)
print("After pop:", b)
# Output: Popped item: (1 or 3 or 4) [random]
#         After pop: Remaining elements

# ✅ Clear set
b.clear()
print("After clear():", b)  
# Output: After clear(): set()

# ✅ Set Operations
s1 = {1, 2, 3}
s2 = {3, 4, 5}

print("s1:", s1)  # Output: s1: {1, 2, 3}
print("s2:", s2)  # Output: s2: {3, 4, 5}

# Union
print("Union:", s1.union(s2))  
# Output: Union: {1, 2, 3, 4, 5}

# Intersection
print("Intersection:", s1.intersection(s2))  
# Output: Intersection: {3}

# Difference
print("Difference (s1 - s2):", s1.difference(s2))  
# Output: Difference (s1 - s2): {1, 2}

# Symmetric Difference
print("Symmetric Difference:", s1.symmetric_difference(s2))  
# Output: Symmetric Difference: {1, 2, 4, 5}

# ✅ Membership Test
colors = {"red", "green", "blue"}
print("Is 'green' in colors?", "green" in colors)  
# Output: Is 'green' in colors? True

print("Is 'yellow' in colors?", "yellow" in colors)  
# Output: Is 'yellow' in colors? False

# ✅ Looping through Set
for color in colors:
    print("Color:", color)
# Output: Color: red
#         Color: green
#         Color: blue
# (order may vary)

# ✅ Removing Duplicates from a List
nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = set(nums)
print("Unique numbers:", unique_nums)  
# Output: Unique numbers: {1, 2, 3, 4, 5}

# ✅ Frozen Set (Immutable set)
fset = frozenset([1, 2, 3])
print("Frozen set:", fset)  
# Output: Frozen set: frozenset({1, 2, 3})

# fset.add(4)  # ❌ Error: 'frozenset' object has no attribute 'add'
"""

"""
Task 1: Removing Duplicates 
USe Case: Cleaning a contact list.

contacts = ["Alice", "Bob", "Alice", "Charlie", "Bob"]

"""

"""
Task 2: Finding Common Elements(Intersection)
Use Case: Find users who are subscribed to both newsletters.
newsletter_a = {"Alice", "Bob", "Charlie"}
newsletter_b = {"Bob", "David", "Eve"}
"""

"""
Task 3: Finding Difference
Use Case: Find customer who bought last month but not this month.
last_month = {"Alice", "Bob", "Charlie"}
this_month = {"Bob", "David", "Eve"}
"""

"""
Task 4: Checking Membership
Use Case: Check if a user is part of a premium membership.
registered_users = {"Alice", "Bob", "Charlie"}
"""

"""
Task 5: Tags or Lables in Apps
UseCCase: Collect all unique tags used in blog posts.
tags = ["python", "coding", "python", "data science", "coding"]
Problem: Detacting Duplicate Email Adresses in a Signup System
Scenario:
You are managing a web application where users can sign up with their email addresses.
You want to ensure that each email address is unique in the system to prevent duplicate accounts.

You receive a list of email addresses from the signup form, and you need to filter out duplicates before storing them in your database.
"""