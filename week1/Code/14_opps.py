# -----------------------------------------------------------
# 🧠 Python OOPs Concepts with Detailed Examples and Comments
# Covers:
# 1. Class & Object
# 2. Encapsulation
# 3. Inheritance (All types)
# 4. Polymorphism (Overriding & Duck Typing)
# 5. Abstraction (abc module)
# -----------------------------------------------------------

# -----------------------------------------------------------
# 1️⃣ CLASS AND OBJECT EXAMPLE
# -----------------------------------------------------------

# Define a class called Person
class Person:
    # Constructor (__init__) with parameters
    def __init__(self, name, age):
        self.name = name      # Instance variable
        self.age = age

    # Method to display person details
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating objects (instances) of the class
p1 = Person("Alice", 30)
p2 = Person("Bob", 25)

# Calling methods on the objects
p1.display()   # Output: Name: Alice, Age: 30
p2.display()   # Output: Name: Bob, Age: 25


# -----------------------------------------------------------
# 2️⃣ ENCAPSULATION EXAMPLE
# -----------------------------------------------------------

# Define a class with private attributes
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())  # Output: 1500
acc.withdraw(300)
print(acc.get_balance())  # Output: 1200
# Trying to access private variable directly: will fail
# print(acc.__balance)    # ❌ AttributeError


# -----------------------------------------------------------
# 3️⃣ INHERITANCE EXAMPLES (Single, Multiple, Multilevel, Hierarchical, Hybrid)
# -----------------------------------------------------------

# 🔹 SINGLE INHERITANCE
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Inherits from Animal
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()  # Output: Animal speaks
d.bark()   # Output: Dog barks


# 🔹 MULTILEVEL INHERITANCE
class Grandparent:
    def house(self):
        print("Grandparent’s house")

class Parent(Grandparent):
    def car(self):
        print("Parent’s car")

class Child(Parent):
    def bike(self):
        print("Child’s bike")

c = Child()
c.house()  # Output: Grandparent’s house
c.car()    # Output: Parent’s car
c.bike()   # Output: Child’s bike


# 🔹 MULTIPLE INHERITANCE
class Father:
    def profession(self):
        print("Engineer")

class Mother:
    def hobby(self):
        print("Painting")

class Son(Father, Mother):
    def activity(self):
        print("Playing football")

s = Son()
s.profession()  # Output: Engineer
s.hobby()       # Output: Painting
s.activity()    # Output: Playing football


# 🔹 HIERARCHICAL INHERITANCE
class Base:
    def base_method(self):
        print("Method of Base class")

class Derived1(Base):
    def feature1(self):
        print("Feature of Derived1")

class Derived2(Base):
    def feature2(self):
        print("Feature of Derived2")

obj1 = Derived1()
obj2 = Derived2()
obj1.base_method()  # Output: Method of Base class
obj1.feature1()     # Output: Feature of Derived1
obj2.feature2()     # Output: Feature of Derived2


# 🔹 HYBRID INHERITANCE (Combination)
class A:
    def method_A(self):
        print("A")

class B(A):
    def method_B(self):
        print("B")

class C:
    def method_C(self):
        print("C")

class D(B, C):  # Hybrid of B (which inherits A) and C
    def method_D(self):
        print("D")

obj = D()
obj.method_A()  # Output: A
obj.method_B()  # Output: B
obj.method_C()  # Output: C
obj.method_D()  # Output: D


# -----------------------------------------------------------
# 4️⃣ POLYMORPHISM EXAMPLES
# -----------------------------------------------------------

# 🔹 METHOD OVERRIDING
class Bird:
    def fly(self):
        print("Bird can fly")

class Penguin(Bird):
    def fly(self):  # Overrides parent method
        print("Penguins cannot fly")

b = Bird()
p = Penguin()
b.fly()  # Output: Bird can fly
p.fly()  # Output: Penguins cannot fly


# 🔹 DUCK TYPING (Different classes, same method names)
class Laptop:
    def code(self):
        print("Coding in VS Code")

class Mobile:
    def code(self):
        print("Coding in Pydroid")

def editor(device):
    device.code()

editor(Laptop())  # Output: Coding in VS Code
editor(Mobile())  # Output: Coding in Pydroid


# -----------------------------------------------------------
# 5️⃣ ABSTRACTION EXAMPLE USING abc MODULE
# -----------------------------------------------------------

# Import Abstract Base Class module
from abc import ABC, abstractmethod

# Define abstract class
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# Concrete subclass
class Bike(Vehicle):
    def start(self):
        print("Bike started")

    def stop(self):
        print("Bike stopped")

b = Bike()
b.start()  # Output: Bike started
b.stop()   # Output: Bike stopped

# Cannot create object of abstract class
# v = Vehicle()  # ❌ Error: Can't instantiate abstract class

# -----------------------------------------------------------
# ✅ End of OOPs Python Concepts with Examples
# -----------------------------------------------------------

# -----------------------------------------
# ✅ Example 1: Basic Class and Object
# -----------------------------------------

# Define a simple class
class Dog:
    # Constructor to initialize the object
    def __init__(self, name):
        self.name = name  # Instance variable

    # Method to make the dog bark
    def bark(self):
        print(f"{self.name} says Woof!")

# Create object of Dog
dog1 = Dog("Tommy")
dog1.bark()  # Output: Tommy says Woof!


# -----------------------------------------
# ✅ Example 2: Class Variables vs Instance Variables
# -----------------------------------------

class  Student:
    college = "LPU"  # Class variable shared by all instances

    def __init__(self, name):
        self.name = name  # Instance variable unique to each object

# Create two students
s1 = Student("Prashanshi")
s2 = Student("Rahul")

print(s1.name)     # Output: Prashanshi
print(s2.college)  # Output: LPU

# -----------------------------------------
# ✅ Example 3: Inheritance
# -----------------------------------------

# Base class
class Animal:
    def speak(self):
        print("Animal speaks")

# Derived class
class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Create object of Cat
c = Cat()
c.speak()  # Output: Cat meows

# -----------------------------------------
# ✅ Example 4: Static Method
# -----------------------------------------

class Math:
    @staticmethod
    def add(a, b):
        return a + b

# Call static method without creating an object
print(Math.add(10, 5))  # Output: 15

# -----------------------------------------
# ✅ Example 5: Class Method
# -----------------------------------------

class School:
    name = "ABC School"

    @classmethod
    def get_school_name(cls):
        return cls.name

# Call class method
print(School.get_school_name())  # Output: ABC School

# -----------------------------------------
# ✅ Example 6: Encapsulation (Private variable)
# -----------------------------------------

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
print(acc.get_balance())   # Output: 1000
# print(acc.__balance)    # Error: attribute is private

# -----------------------------------------
# ✅ Example 7: Polymorphism
# -----------------------------------------

class Bird:
    def fly(self):
        print("Bird can fly")

class Ostrich(Bird):
    def fly(self):
        print("Ostrich can't fly")

b = Bird()
o = Ostrich()

b.fly()  # Output: Bird can fly
o.fly()  # Output: Ostrich can't fly

# -----------------------------------------
# ✅ Example 8: Multiple Inheritance
# -----------------------------------------

class Father:
    def skills(self):
        print("Father: Gardening, Cooking")

class Mother:
    def skills(self):
        print("Mother: Art, Music")

class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Child: Programming")

c = Child()
c.skills()
# Output:
# Father: Gardening, Cooking
# Mother: Art, Music
# Child: Programming

# -----------------------------------------
# ✅ Example 9: Inner (Nested) Class
# -----------------------------------------

class Laptop:
    def __init__(self, brand):
        self.brand = brand
        self.specs = self.Specs()

    class Specs:
        def __init__(self):
            self.ram = "16GB"
            self.cpu = "i7"

        def display(self):
            print("RAM:", self.ram)
            print("CPU:", self.cpu)

laptop = Laptop("Dell")
laptop.specs.display()
# Output:
# RAM: 16GB
# CPU: i7

# -----------------------------------------
# ✅ Example 10: Data Class (Python 3.7+)
# -----------------------------------------

from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int

b1 = Book("Python 101", "Prashanshi", 200)
print(b1)
# Output: Book(title='Python 101', author='Prashanshi', pages=200)




# -----------------------------------------
# 🚀 Problem 1: Create a class to represent a bank account
# Class should have methods for deposit, withdraw, and displaying balance

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrawn ₹{amount}. Remaining balance: ₹{self.balance}")

    def display(self):
        print(f"{self.owner}'s Balance: ₹{self.balance}")

# Test
acc = BankAccount("Prashanshi", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.display()
# Output:
# Deposited ₹500. New balance: ₹1500
# Withdrawn ₹300. Remaining balance: ₹1200
# Prashanshi's Balance: ₹1200




# 🚀 Problem 2: Create a class that counts number of instances created

class Counter:
    count = 0  # class variable

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print(f"Total objects created: {cls.count}")

# Test
c1 = Counter()
c2 = Counter()
c3 = Counter()
Counter.show_count()
# Output: Total objects created: 3




# 🚀 Problem 3: Create a class that checks if a string is a palindrome

class PalindromeChecker:
    def __init__(self, text):
        self.text = text

    def is_palindrome(self):
        return self.text == self.text[::-1]

# Test
p1 = PalindromeChecker("radar")
print(p1.is_palindrome())  # Output: True

p2 = PalindromeChecker("python")
print(p2.is_palindrome())  # Output: False




# 🚀 Problem 4: Employee class to store and display employee details

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Salary: ₹{self.salary}")

# Test
e1 = Employee(101, "Prashanshi", 50000)
e1.display()
# Output: ID: 101, Name: Prashanshi, Salary: ₹50000



# 🚀 Problem 5: Create a class to calculate area and perimeter of rectangle

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Test
r = Rectangle(5, 3)
print("Area:", r.area())           # Output: Area: 15
print("Perimeter:", r.perimeter()) # Output: Perimeter: 16



# 🚀 Problem 6: Student class that calculates average marks and grade

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # List of marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "F"

# Test
s1 = Student("Ankit", [95, 88, 92])
print(s1.name, "Grade:", s1.grade())  # Output: Ankit Grade: A



# 🚀 Problem 7: Shape class with area() method to be overridden by child classes

class Shape:
    def area(self):
        pass  # abstract method

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

# Test
c = Circle(5)
s = Square(4)
print("Circle Area:", c.area())  # Output: Circle Area: 78.5
print("Square Area:", s.area())  # Output: Square Area: 16


# ---------------------------------------------
# 🚗 Problem : Car class with default values
# ---------------------------------------------
# Create a class Car with attributes: make, model, and year
# The constructor should use default values if no arguments are given
# Create a few car objects using different sets of arguments

class Car:
    def __init__(self, make="Toyota", model="Corolla", year=2020):
        self.make = make        # Car brand (e.g., Toyota)
        self.model = model      # Car model (e.g., Corolla)
        self.year = year        # Manufacturing year (e.g., 2020)

    def display(self):
        print(f"{self.year} {self.make} {self.model}")

# ✅ Creating car objects with different sets of arguments

# Object 1: Using all default values
car1 = Car()
car1.display()  
# Output: 2020 Toyota Corolla

# Object 2: Providing make and model, default year
car2 = Car("Honda", "Civic")
car2.display()  
# Output: 2020 Honda Civic

# Object 3: Providing all custom values
car3 = Car("Ford", "Mustang", 2023)
car3.display()  
# Output: 2023 Ford Mustang

# Object 4: Only make provided, others default
car4 = Car("Hyundai")
car4.display()
# Output: 2020 Hyundai Corolla



# -----------------------------------------------------
# 🎓 Problem: Student Information System
# -----------------------------------------------------
# Create a class 'Student' with the following attributes:
# - name
# - rollno
# - grade
# Use a constructor (__init__) to initialize these values
# Create two Student objects and display their information

class Student:
    def __init__(self, name, rollno, grade):
        self.name = name         # Student's name
        self.rollno = rollno     # Student's roll number
        self.grade = grade       # Student's grade (e.g., A, B, C)

    def display_info(self):
        # Display student details
        print(f"Name: {self.name}")
        print(f"Roll No: {self.rollno}")
        print(f"Grade: {self.grade}")
        print("-------------------------")

# ✅ Create two student objects with sample data

student1 = Student("Prashanshi", 101, "A")
student2 = Student("Rahul", 102, "B")

# ✅ Display their information
student1.display_info()
# Output:
# Name: Prashanshi
# Roll No: 101
# Grade: A
# -------------------------

student2.display_info()
# Output:
# Name: Rahul
# Roll No: 102
# Grade: B
# -------------------------
