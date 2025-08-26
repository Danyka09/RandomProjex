# or, in, and, not (!=), for, print, while True, try, break, except, str, int, input, if, else, elif,
# .lower(), .append(), .insert(), .extend([]), .clear(), remove(), pop(), list = [ ], tuple = (),

    # Variables:

integer1 = 67
string1 = "420"
float1 = 6.9
list1 = [1, 2, 3]
tuple1 = (1, 3, 5, 2)
text = "  HELLO world"
list2 = ["Python", "Java", "HTML", "Kotlin", "Python"]
tuple2 = (1, 3, 5, 2)


    # Functions:

# print() -Displays output
print("Hello World!")

# input() -Gets user input
#input("How are you?")

# len() -Returns the number of items in a sequence
print(len("text"))
print(len(list1))

# str() -Converts value to a string
print(str(float1))

# int() -Converts value to an integer
print(int(string1))

# float() -Convert value to a float
print(float(integer1))

# type() -Gives you the type of an object
print(type(float1))
print(type(string1))
print(type(integer1))

# range() -Generates a sequence of numbers
print(range(5))
print(list(range(5)))

# min(), max(), sum() -Finds the minimum, maximum, or sum of a sequence of numbers.
print(min(list1))
print(max(list1))
print(sum(list1))

# sorted -Returns a sorted list from the items in a sequence
print(sorted(tuple1))

    # Keywords:



    # String Methods:

# .lower(), .upper() -Converts a string to lowercase or uppercase
print(text)
print(text.lower())
print(text.upper())

# .strip() -Removes leading and trailing whitespace
print(text.strip())

# .split() -Splits a string into a list of substrings
print(text.split())

# .replace() -Replaces a specified phrase with another
print(text.replace('world', 'universe'))

# .find() -Searches for a substring and returns its index
print(text.find("Galaxy"))


    # List Methods:

# .append() -Adds an item to the end of the list
list1.append(100)
print(list1)

# .insert() -Adds an item at a specific index
list1.insert(1, 55)
print(list1)

# .extend() -Appends all items from another list
list1.extend(tuple1)
print(list1)

# .remove() -Removes the first occurrence of an item
list1.remove(1)
print(list1)

# .pop() -Removes and returns an item at a specific index
print(list2)
popped = list2.pop(2)
print(list2)
print(popped)

# count() -Counts the number of times an item appears
print(list2.count("Python"))

# .sort() -Sorts the list in place
list2.sort()
print(list2)

# .clear() -Empties the list
list2.clear()
print(list2)


    # Operations:
