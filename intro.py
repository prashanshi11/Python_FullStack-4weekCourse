# This is a simple Python script that greets the user
# and welcomes them to the Python FullStack Training course.
# print("Welcom to Python FullStack Training")
# data = input("Enter your name: ")
# print(f"Hello {data}, welcome to the course!")

""" Great! Here's a comparison of **3 common ways to format strings in Python**, with examples:

---

## 🔸 1. **f-Strings (Recommended for Python 3.6+)**

```python
name = "Prashanshi"
age = 21
print(f"My name is {name} and I am {age} years old.")
```

✅ Output:

```
My name is Prashanshi and I am 21 years old.
```

---

## 🔸 2. **`str.format()` Method**

```python
name = "Prashanshi"
age = 21
print("My name is {} and I am {} years old.".format(name, age))
```

✅ Output:

```
My name is Prashanshi and I am 21 years old.
```

You can also use **placeholders with indexes**:

```python
print("My name is {0} and I am {1} years old. {0} is learning Python.".format(name, age))
```

✅ Output:

```
My name is Prashanshi and I am 21 years old. Prashanshi is learning Python.
```

---

## 🔸 3. **`%` Formatting (Old Style - Not recommended)**

```python
name = "Prashanshi"
age = 21
print("My name is %s and I am %d years old." % (name, age))
```

✅ Output:

```
My name is Prashanshi and I am 21 years old.
```

---

## ✅ Summary Table

| Method           | Introduced In  | Recommended? | Example                   |
| ---------------- | -------------- | ------------ | ------------------------- |
| `f"{}"`          | Python 3.6     | ✅ Yes        | `f"Hello {name}"`         |
| `"{}".format()`  | Python 2.7/3.x | 👍 Okay      | `"Hello {}".format(name)` |
| `"%"` formatting | Old (Python 2) | ❌ No         | `"Hello %s" % name`       |

---

"""


# This code snippet demonstrates how to use f-strings, str.format(), and % formatting in Python.
# It provides examples of each method and their outputs.


# ✅ 2. Daily Routine Reminder

name = input("Enter your name: ")
task = input("What is your main task today? ")
time = input("When will you do it? ")

print(f"Hi {name}, remember to do '{task}' at {time}. Good luck!")
