# Welcome to your Personal Python Knowledge Base!
# This file is a compilation of all the concepts and syntax you've learned and used across your projects.
# Use it as a quick reference to remind yourself how to do things in Python.

# ==============================================================================
# SECTION 1: PYTHON FUNDAMENTALS
# ==============================================================================

"""
### 1.1 Variables and Basic Data Types
Variables are used to store data. Python has several basic types.
"""
# Variable assignment
integer_variable = 67       # An integer
string_variable = "420"     # A string of characters
float_variable = 6.9        # A floating-point number (decimal)
boolean_variable = True     # A boolean (can be True or False)

print("--- 1.1 Variables and Data Types ---")
print(f"Integer: {integer_variable}")
print(f"String: {string_variable}")
print(f"Float: {float_variable}")
print(f"Boolean: {boolean_variable}\n")

"""
### 1.2 Basic Data Structures
These are containers for storing collections of data.
"""
# List: Ordered, mutable (changeable), allows duplicate elements.
my_list = [1, "Python", 3.5, "Python"]

# Tuple: Ordered, immutable (unchangeable), allows duplicate elements.
my_tuple = (1, 3, 5, 2)

# Set: Unordered, mutable, does *not* allow duplicate elements.
my_set = {'a', 'b', 'c', 'a'} # The second 'a' will be automatically removed.

# Dictionary (dict): Unordered, mutable, stores data in key-value pairs.
my_dict = {"name": "Alice", "email": "alice@example.com"}

print("--- 1.2 Data Structures ---")
print(f"List: {my_list}")
print(f"Tuple: {my_tuple}")
print(f"Set: {my_set}")
print(f"Dictionary: {my_dict}\n")


"""
### 1.3 Basic Operators
Used to perform operations on variables and values.
"""
# Arithmetic Operators
a = 10
b = 3
print("--- 1.3 Operators ---")
print(f"Addition (10 + 3): {a + b}")
print(f"Subtraction (10 - 3): {a - b}")
print(f"Multiplication (10 * 3): {a * b}")
print(f"Division (10 / 3): {a / b}")
print(f"Floor Division (10 // 3): {a // b}") # Division that rounds down
print(f"Modulus (10 % 3): {a % b}")      # Remainder of the division
print(f"Exponent (10 ** 3): {a ** b}\n")

# Comparison Operators (return True or False)
x = 5
y = 10
print(f"Is 5 == 10? {x == y}")
print(f"Is 5 != 10? {x != y}")
print(f"Is 5 > 10? {x > y}")
print(f"Is 5 < 10? {x < y}\n")

# Logical Operators
is_sunny = True
is_warm = False
print(f"Is it sunny AND warm? {is_sunny and is_warm}")
print(f"Is it sunny OR warm? {is_sunny or is_warm}")
print(f"Is it NOT sunny? {not is_sunny}\n")


"""
### 1.4 Getting User Input
The `input()` function prompts the user to enter data. It always returns a string.
"""
# name = input("What is your name? ")
# print(f"Hello, {name}!")


# ==============================================================================
# SECTION 2: BUILT-IN FUNCTIONS
# ==============================================================================

"""
Python comes with many useful built-in functions.
"""
text = "Hello World"
numbers = [1, 5, 2, 8, 3]

print("--- 2. Built-in Functions ---")
# len(): Returns the length (number of items).
print(f"Length of '{text}': {len(text)}")

# type(): Returns the data type of a variable.
print(f"Type of the number 5: {type(5)}")

# str(), int(), float(): Convert between data types.
num_string = "100"
converted_int = int(num_string)
print(f"'{num_string}' as an integer: {converted_int}")

# min(), max(), sum(): For sequences of numbers.
print(f"Min of {numbers}: {min(numbers)}")
print(f"Max of {numbers}: {max(numbers)}")
print(f"Sum of {numbers}: {sum(numbers)}")

# sorted(): Returns a new sorted list from the items in an iterable.
print(f"Sorted version of {numbers}: {sorted(numbers)}")

# range(): Generates a sequence of numbers.
# range(5) generates numbers from 0 up to (but not including) 5.
print(f"A list from range(5): {list(range(5))}\n")


# ==============================================================================
# SECTION 3: CONTROL FLOW
# ==============================================================================

"""
### 3.1 Conditional Statements (if, elif, else)
Execute code based on whether a condition is true.
"""
print("--- 3.1 Conditional Statements ---")
age = 18
if age < 13:
    print("You are a child.")
elif 13 <= age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.\n")


"""
### 3.2 For Loops
Iterate over a sequence (like a list, tuple, or string).
"""
print("--- 3.2 For Loops ---")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Current fruit: {fruit}")
print()

# Nested For Loops (a loop inside another loop)
numbers = [1, 2]
letters = ['a', 'b']
for num in numbers:
    for letter in letters:
        print(f"{num}{letter}", end=" ")
    print() # Newline after each outer loop iteration
print()


"""
### 3.3 While Loops
Execute a block of code as long as a condition is true.
"""
print("--- 3.3 While Loops ---")
count = 0
while count < 3:
    print(f"Count is {count}")
    count += 1
print()

"""
### 3.4 Loop Control (break, continue)
- `break`: Exits the loop entirely.
- `continue`: Skips the rest of the current iteration and moves to the next.
"""
print("--- 3.4 Loop Control ---")
for i in range(5):
    if i == 3:
        print("Found 3, breaking the loop.")
        break
    print(i)

for i in range(5):
    if i == 3:
        print("Found 3, continuing to the next iteration.")
        continue
    print(i)
print()


# ==============================================================================
# SECTION 4: WORKING WITH DATA STRUCTURES
# ==============================================================================

"""
### 4.1 String Methods
Strings have many built-in methods to manipulate them.
"""
my_string = "  Hello World  "
print("--- 4.1 String Methods ---")
print(f"Original: '{my_string}'")
print(f".lower(): '{my_string.lower()}'")
print(f".upper(): '{my_string.upper()}'")
print(f".strip(): '{my_string.strip()}'") # Removes leading/trailing whitespace
print(f".replace('World', 'Python'): '{my_string.replace('World', 'Python')}'")
print(f".split(): {my_string.split()}") # Splits the string into a list
print()

"""
### 4.2 List Methods
Lists are mutable, so you can change them after they are created.
"""
my_list = ["Python", "Java", "HTML"]
print("--- 4.2 List Methods ---")
print(f"Original list: {my_list}")

# .append(): Adds an item to the end.
my_list.append("Kotlin")
print(f".append('Kotlin'): {my_list}")

# .insert(): Adds an item at a specific index.
my_list.insert(1, "JavaScript")
print(f".insert(1, 'JavaScript'): {my_list}")

# .remove(): Removes the first occurrence of an item.
my_list.remove("Java")
print(f".remove('Java'): {my_list}")

# .pop(): Removes and returns the item at a given index.
popped_item = my_list.pop(2)
print(f".pop(2) removed '{popped_item}', list is now: {my_list}")

# .sort(): Sorts the list in place.
my_list.sort()
print(f".sort(): {my_list}")
print()


"""
### 4.3 Dictionary Methods
Dictionaries store data in key-value pairs.
"""
contacts = {"Bob": "bob@gmail.com", "Wendy": "wendy@wendy.com"}
print("--- 4.3 Dictionary Methods ---")
print(f"Original dict: {contacts}")

# Accessing a value by its key
print(f"Bob's email: {contacts['Bob']}")

# Adding a new key-value pair
contacts['Alex'] = 'alex@cool.com'
print(f"Added Alex: {contacts}")

# .pop(): Removes a key and returns its value
contacts.pop('Wendy')
print(f"Popped Wendy: {contacts}")

# .keys(), .values(), .items()
print(f"Keys: {contacts.keys()}")
print(f"Values: {contacts.values()}")
print(f"Items (key-value pairs): {contacts.items()}")

# Looping through a dictionary
for key, value in contacts.items():
    print(f"  {key}'s email is {value}")
print()


# ==============================================================================
# SECTION 5: FUNCTIONS
# ==============================================================================

"""
Functions are reusable blocks of code. They help organize your programs.
"""
print("--- 5. Functions ---")

# A simple function definition
def greet(name):
    """This function greets the person passed in as a parameter."""
    print(f"Hello, {name}!")

# Calling the function
greet("Danny")

# A function that returns a value
def add_numbers(a, b):
    return a + b

sum_result = add_numbers(5, 10)
print(f"The sum is: {sum_result}")
print()

"""
### 5.1 *args and **kwargs
Used to handle an arbitrary number of arguments in a function.

- `*args`: Gathers any number of positional arguments into a tuple.
- `**kwargs`: Gathers any number of keyword arguments into a dictionary.
"""
def tea_order(customer_name, tea_type, *args, **kwargs):
    print(f"{customer_name} ordered a {tea_type} tea.")
    # args will be a tuple: ('oat',)
    for arg in args:
        print(f" - Add {arg}")
    # kwargs will be a dictionary: {'sweetener': 'honey'}
    for key, value in kwargs.items():
        print(f" - Add {key}: {value}")

tea_order("Tony", "black", "oat", sweetener="honey")
print()


# ==============================================================================
# SECTION 6: ADVANCED CONCEPTS
# ==============================================================================

"""
### 6.1 List Comprehensions
A concise way to create lists.
Syntax: [expression for item in iterable if condition]
"""
print("--- 6.1 List Comprehensions ---")
# Simple example: square all numbers from 0 to 4
squares = [x**2 for x in range(5)]
print(f"Squares from range(5): {squares}")

# Example with a condition: get only even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(f"Even numbers from range(10): {evens}\n")


"""
### 6.2 Lambda Functions
Small, anonymous functions defined with the `lambda` keyword.
Syntax: lambda arguments: expression
"""
print("--- 6.2 Lambda Functions ---")
# A lambda function that adds 10 to a number
add_ten = lambda x: x + 10
print(f"Using lambda: 5 + 10 = {add_ten(5)}")

# Often used with functions like map() and filter()
numbers = [1, 2, 3, 4, 5]

# map(): applies a function to every item of an iterable.
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"map() to square numbers: {squared_numbers}")

# filter(): creates a list of elements for which a function returns true.
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"filter() for even numbers: {even_numbers}\n")


"""
### 6.3 Error Handling (try...except)
Allows you to handle errors gracefully instead of crashing the program.
"""
print("--- 6.3 Error Handling ---")
try:
    # Code that might cause an error
    result = 10 / 0
except ZeroDivisionError:
    # Code to run if that specific error occurs
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Incorrect value.")
finally:
    # This code runs no matter what
    print("Finished with the try-except block.\n")


"""
### 6.4 Decorators
A way to modify or enhance functions without changing their code.
A decorator is a function that takes another function as input, adds some functionality, and returns the enhanced function.
"""
print("--- 6.4 Decorators ---")
import time
from datetime import datetime, timedelta

def timer_dec(base_fn):
    # This is the decorator function.
    def enhanced_fn(*args, **kwargs):
        # This is the wrapper function that adds the new behavior.
        start_time = time.time()
        result = base_fn(*args, **kwargs) # Call the original function
        end_time = time.time()
        print(f"'{base_fn.__name__}' took {end_time - start_time:.4f} seconds to run.")
        return result
    return enhanced_fn

# Using the decorator with the '@' syntax
@timer_dec
def brew_tea(tea_type, steep_time):
    print(f"Brewing {tea_type} tea...")
    time.sleep(steep_time)
    return "Tea is ready!"

print(brew_tea("green", 1))
print()


# ==============================================================================
# SECTION 7: OBJECT-ORIENTED PROGRAMMING (OOP)
# ==============================================================================

"""
OOP is a way to structure code by bundling related properties (attributes) and behaviors (methods) into individual objects.
A `class` is the blueprint for creating objects.
"""
print("--- 7. Object-Oriented Programming ---")

class Character:
    # The __init__ method is the constructor, called when a new object is created.
    # `self` refers to the instance of the object being created.
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed

    # This is a method (a function inside a class).
    def take_damage(self, amount):
        self.health -= amount
        print(f"Took {amount} damage, health is now {self.health}.")

# Inheritance: The Warrior class inherits all attributes and methods from Character.
class Warrior(Character):
    def __init__(self, health, damage, speed, luck):
        # `super()` calls the constructor of the parent class (Character).
        super().__init__(health, damage, speed)
        # Add a new attribute specific to the Warrior class.
        self.luck = luck
        self.toughness_modifier = 0.9

    # Method Overriding: We can redefine a method from the parent class.
    def take_damage(self, amount):
        modified_amount = amount * self.toughness_modifier
        print(f"Warrior's toughness reduced damage!")
        # Call the original take_damage method from the parent class.
        super().take_damage(modified_amount)

# Create instances (objects) of the classes
ninja = Character(80, 40, 40)
warrior = Warrior(100, 50, 10, 67)

print(f"Warrior's initial health: {warrior.health}")
warrior.take_damage(ninja.damage)
print()


# ==============================================================================
# SECTION 8: MODULES AND LIBRARIES
# ==============================================================================

"""
### 8.1 Importing Modules
You can import code from other files (modules) to use in your current file.
"""
print("--- 8.1 Importing Modules ---")
import random # Imports the entire random module.
import json   # For working with JSON data.
from datetime import date # Imports only the 'date' class from the datetime module.

print(f"A random integer between 1 and 10: {random.randint(1, 10)}")
print(f"Today's date: {date.today()}\n")


"""
### 8.2 `if __name__ == '__main__':`
This is a common pattern in Python.
- The code inside this block will only run when the script is executed directly.
- It will *not* run if the script is imported as a module into another file.
- This is useful for separating reusable code (like functions and classes) from the code that should run when you start the program.
"""
if __name__ == '__main__':
    print("This script is being run directly, so this message appears.")
    # You might put your main program logic here.
    # For example: main_game_loop() or start_web_server()
print()


"""
### 8.3 File I/O (Input/Output)
Reading from and writing to files.
"""
print("--- 8.3 File I/O ---")
# Writing to a file
# 'w' mode overwrites the file if it exists.
try:
    with open("example.txt", "w") as file:
        file.write("This is a line of text.\n")
        file.write("This is another line.\n")

    # Reading from a file
    # 'r' mode is for reading.
    with open("example.txt", "r") as file:
        content = file.read()
        print("Content of example.txt:")
        print(content)

    # Working with JSON files (very common for data storage and APIs)
    leaderboard = [{"name": "Danny", "score": 100}, {"name": "Alice", "score": 150}]
    with open("leaderboard.json", "w") as file:
        json.dump(leaderboard, file, indent=4) # `indent=4` makes it human-readable

    with open("leaderboard.json", "r") as file:
        loaded_data = json.load(file)
        print("Loaded leaderboard data from JSON:")
        print(loaded_data)
        print()
except Exception as e:
    print(f"File operations skipped as they might not be supported in this environment. Error: {e}")


"""
### 8.4 Popular External Libraries (from your projects)
These are not built-in and need to be installed (e.g., `pip install pandas`).

- `requests`: For making HTTP requests to APIs.
    `response = requests.get("https://api.example.com/data")`
    `data = response.json()`

- `pandas`: A powerful data analysis library.
    `import pandas as pd`
    `df = pd.read_csv("my_data.csv")`
    `print(df.head())`

- `smtplib`: For sending emails (part of Python's standard library).
    Used to connect to an SMTP server and send emails, often with email formatting libraries.

- `flask`: A micro web framework for building APIs and web applications.
    `from flask import Flask, jsonify`
    `app = Flask(__name__)`
    `@app.route("/")`
    `def home(): return "Hello, World!"`

- `streamlit`: For creating and sharing web apps for data science and machine learning.
    `import streamlit as st`
    `st.title("My Awesome App")`
    `user_input = st.text_input("Enter some text:")`
    `st.write(f"You entered: {user_input}")`
"""

print("--- End of Knowledge Base ---")