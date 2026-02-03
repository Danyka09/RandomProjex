# ==================================================
#        PYTHON CHEAT SHEET — CLEAN & COMPLETE
#        (operators, logic, types, examples)
# ==================================================

# This file is meant to be READ, not memorized.
# Scroll, tweak values, run pieces of it, break it.

# ==================================================
# 1) COMMENTS & STYLE
# ==================================================

# Single-line comments start with #
# Use comments to explain WHY, not WHAT

"""
This is a multi-line string.
Often used as documentation.
"""

# ==================================================
# 2) VARIABLES & BASIC DATA TYPES
# ==================================================

integer1 = 67            # int    -> whole numbers
float1   = 6.9           # float  -> decimals
string1  = "420"          # str    -> text
boolean  = True          # bool   -> True / False
noneval  = None          # None   -> absence of value

# Collections
list1  = [1, 2, 3]                     # list  -> ordered, mutable
tuple1 = (1, 3, 5, 2)                  # tuple -> ordered, immutable
set1   = {1, 2, 3, 3, 2}               # set   -> unique values
dict1  = {"name": "Danny", "age": 16}  # dict  -> key : value

# ==================================================
# 3) ASSIGNMENT OPERATORS
# ==================================================

x = 5        # assign
x += 1       # x = x + 1
x -= 1       # x = x - 1
x *= 2       # x = x * 2
x /= 2       # x = x / 2      (float)
x //= 2      # x = x // 2     (floor)
x %= 2       # x = x % 2      (remainder)
x **= 3      # x = x ** 3     (power)

# ==================================================
# 4) ARITHMETIC OPERATORS
# ==================================================

# +   addition
# -   subtraction
# *   multiplication
# /   division (always float)
# //  floor division (rounds DOWN)
# %   modulo (remainder)
# **  exponent

5 + 3     # 8
5 - 3     # 2
5 * 3     # 15
5 / 2     # 2.5
5 // 2    # 2
5 % 2     # 1
2 ** 3    # 8

# ==================================================
# 5) MODULO (%) — THE LOGIC YOU USED FOR TREES
# ==================================================

# % gives the REMAINDER after division

# EVEN / ODD CHECK
n = 7
n % 2        # 1 -> odd

n = 8
n % 2        # 0 -> even

# Explanation:
# 7 = 2 * 3 + 1
# 8 = 2 * 4 + 0

# ==================================================
# 6) COMPARISON OPERATORS (RESULT IS True / False)
# ==================================================

# ==   equal
# !=   not equal
# >    greater than
# <    less than
# >=   greater or equal
# <=   less or equal

5 == 5     # True
5 != 3     # True
5 > 3      # True
5 <= 4     # False

# ==================================================
# 7) LOGICAL OPERATORS
# ==================================================

# and  -> both must be True
# or   -> at least one True
# not  -> flips value

x = 5
x > 0 and x < 10     # True
x == 3 or x == 5     # True
not x == 0           # True

# ==================================================
# 8) LOOPS
# ==================================================

# for loop
for i in range(5):
    print("i =", i)

# while loop
count = 0
while count < 3:
    print("count =", count)
    count += 1

# break & continue
for i in range(5):
    if i == 3:
        break
    print("break example:", i)

for i in range(5):
    if i == 2:
        continue
    print("continue example:", i)

# ==================================================
# 9) USING % IN LOOPS (TREE PATTERN)
# ==================================================

for i in range(6):
    if i % 2 == 0:
        print(i, "even -> tree A")
    else:
        print(i, "odd  -> tree B")

# ==================================================
# 10) FUNCTIONS
# ==================================================

def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

# ==================================================
# 11) MEMBERSHIP & IDENTITY
# ==================================================

# in / not in
"a" in "apple"        # True
3 in [1, 2, 3]        # True

# is / is not
x = None
x is None            # True

# ==================================================
# 12) BUILT-IN FUNCTIONS (MOST COMMON)
# ==================================================

len([1, 2, 3])
int("123")
float(5)
str(42)
type(42)
range(5)
list(range(5))
min([1, 2, 3])
max([1, 2, 3])
sum([1, 2, 3])
sorted((3, 1, 2))

# ==================================================
# END OF CHEAT SHEET
# ==================================================
