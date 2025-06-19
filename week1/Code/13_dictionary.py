# ✅ 1. Creating a simple dictionary
student = {
    "name": "Alice",
    "age": 21,
    "course": "Python"
}
print(student)
# Output: {'name': 'Alice', 'age': 21, 'course': 'Python'}

# ✅ 2. Accessing values using keys
print(student["name"])
# Output: Alice

# ✅ 3. Using get() method (returns None if key not found)
print(student.get("email"))
# Output: None

# ✅ 4. Adding a new key-value pair
student["email"] = "alice@example.com"
print(student)
# Output: {'name': 'Alice', 'age': 21, 'course': 'Python', 'email': 'alice@example.com'}

# ✅ 5. Updating existing value
student["age"] = 22
print(student)
# Output: {'name': 'Alice', 'age': 22, 'course': 'Python', 'email': 'alice@example.com'}

# ✅ 6. Removing a key-value pair using pop()
student.pop("course")
print(student)
# Output: {'name': 'Alice', 'age': 22, 'email': 'alice@example.com'}

# ✅ 7. Getting all keys
print(student.keys())
# Output: dict_keys(['name', 'age', 'email'])

# ✅ 8. Getting all values
print(student.values())
# Output: dict_values(['Alice', 22, 'alice@example.com'])

# ✅ 9. Getting all key-value pairs
print(student.items())
# Output: dict_items([('name', 'Alice'), ('age', 22), ('email', 'alice@example.com')])

# ✅ 10. Looping through dictionary
for key, value in student.items():
    print(key, ":", value)
# Output:
# name : Alice
# age : 22
# email : alice@example.com

# ✅ 11. Using dict() constructor
person = dict(name="Bob", age=30)
print(person)
# Output: {'name': 'Bob', 'age': 30}

# ✅ 12. Creating dictionary from two lists using zip()
keys = ['a', 'b', 'c']
values = [1, 2, 3]
zipped_dict = dict(zip(keys, values))
print(zipped_dict)
# Output: {'a': 1, 'b': 2, 'c': 3}

# ✅ 13. Dictionary comprehension
squared = {x: x*x for x in range(5)}
print(squared)
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# ✅ 14. Nested dictionary
nested = {
    "student1": {"name": "John", "marks": 85},
    "student2": {"name": "Emma", "marks": 90}
}
print(nested["student1"]["name"])
# Output: John

# ✅ 15. Checking if key exists
if "name" in student:
    print("Key exists")
# Output: Key exists

# ✅ 16. Copying dictionary (shallow copy)
copy_dict = student.copy()
print(copy_dict)
# Output: {'name': 'Alice', 'age': 22, 'email': 'alice@example.com'}

# ✅ 17. Clearing dictionary
copy_dict.clear()
print(copy_dict)
# Output: {}


"""myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
print(myfamily)#{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}
"""

