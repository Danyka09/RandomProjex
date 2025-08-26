# ===============================
#   PYTHON CHEAT SHEET - COMPLETE
# ===============================

# -------------------------------
#  COMMENTS & READABILITY
# -------------------------------
# Comments (#) explain code, important for understanding and maintaining code later
# Use them to describe variables, logic, or why something is done

# -------------------------------
#  VARIABLES & DATA TYPES
# -------------------------------
integer1 = 67           # Integer - whole numbers
float1 = 6.9            # Float - decimal numbers
string1 = "420"         # String - text
text = "  HELLO world"  # String with spaces
list1 = [1, 2, 3]       # List - ordered, mutable, allows duplicates
tuple1 = (1, 3, 5, 2)   # Tuple - ordered, immutable, allows duplicates
dict1 = {"name": "Danny", "age": 16, "lang": "Python"}  # Dictionary - key-value pairs
set1 = {1, 2, 3, 3, 2}  # Set - unique items, unordered
list2 = ["Python", "Java", "HTML", "Kotlin", "Python"]
tuple2 = (1, 3, 5, 2)
set2 = {3, 4, 5}

# -------------------------------
#  WHY DIFFERENT TYPES
# -------------------------------
# Tuples: immutable → safer for fixed data
coords = (10, 20)
# Lists: mutable → can add/remove items
fruits = ["apple", "banana"]
# Sets: fast membership checks, no duplicates
usernames = {"alice", "bob", "carol"}

# -------------------------------
#  KEYWORDS WITH EXAMPLES
# -------------------------------

# Conditional logic: if, elif, else
x = 42
if x > 50:
    print("x is greater than 50")
elif x == 42:
    print("x is exactly 42")
else:
    print("x is less than 50 and not 42")

# Loops
# for loop
for fruit in ["apple", "banana", "cherry"]:
    print(fruit)

# while loop
count = 0
while count < 3:
    print("Counting:", count)
    count += 1

# break & continue
for n in range(5):
    if n == 3:
        break  # exit loop
    print("Break example:", n)

for n in range(5):
    if n == 2:
        continue  # skip iteration
    print("Continue example:", n)

# Logical & membership operators
a = True
b = False
print(a and b)     # False
print(a or b)      # True
print(not a)       # False
languages = ["Python", "Java", "HTML"]
print("Python" in languages)   # True
print("C++" not in languages)  # True
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x is y)      # True
print(x is z)      # False
print(x is not z)  # True

# Boolean values
flag = True
print(flag)
flag = False
print(flag)

# Functions & error handling
def greet(name):
    return f"Hello, {name}!"
print(greet("Danny"))

def add(a, b):
    return a + b
print(add(5, 7))

try:
    num = int("abc")
except ValueError:
    print("Conversion failed")

# Importing
import math
from math import sqrt as root
print(math.ceil(4.2))  # 5
print(root(16))        # 4

# Classes & dunder methods
class Dog:
    def __init__(self, name):  # constructor
        self.name = name

    def bark(self):
        return f"{self.name} says woof!"

dog = Dog("Buddy")
print(dog.name)
print(dog.bark())

# -------------------------------
#  BUILT-IN FUNCTIONS
# -------------------------------
print("Hello World!")
# input() - get user input
# name = input("Enter your name: ")
len("text")         # length of sequence
str(123)             # convert to string
int("456")           # convert to integer
float(5)             # convert to float
type(42)             # get type
range(5)             # sequence of numbers
list(range(5))       # convert to list
min(list1)
max(list1)
sum(list1)
sorted(tuple1)

# -------------------------------
#  STRINGS
# -------------------------------
print(text.lower())
print(text.upper())
print(text.strip())
print(text.split())
print(text.replace("world", "universe"))
print(text.find("HELLO"))
# f-strings - modern formatting
name = "Danny"; age = 16
print(f"My name is {name} and I am {age} years old")

# -------------------------------
#  LIST METHODS
# -------------------------------
list1.append(100)
list1.insert(1, 55)
list1.extend(tuple1)
list1.remove(1)
popped = list2.pop(2)
print(list1, list2, popped)
print(list2.count("Python"))
list2.sort()
list2.reverse()
copy_list = list2.copy()
print(list2.index("Java"))
list2.clear()

# -------------------------------
#  TUPLE METHODS
# -------------------------------
tuple2.index(3)
tuple2.count(2)

# -------------------------------
#  DICTIONARY METHODS
# -------------------------------
dict1.keys()
dict1.values()
dict1.items()
dict1["age"] = 17
dict1["school"] = "Gymnazium"
del dict1["lang"]

# -------------------------------
#  SET METHODS & OPERATORS
# -------------------------------
set1.add(10)
set1.remove(2)
set1.discard(999)  # safe removal
print(set1 | set2)  # union
print(set1 & set2)  # intersection
print(set1 - set2)  # difference

# -------------------------------
#  FILE I/O
# -------------------------------
# Writing to a file
with open("my_file.txt", "w") as f:
    f.write("Hello, World!")

# Reading from a file
with open("my_file.txt", "r") as f:
    content = f.read()
    print(content)
