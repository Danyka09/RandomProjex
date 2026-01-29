# you can use it to simplify imports
from .math_util import add # dot is important; makes it look in the current package (folder?)
from .string_util import capitalize

#depending on where you run the code it will behave differently, running the init now wont work cause its a relative import
#initializes package by running code whenver imported

print("imported utils")

