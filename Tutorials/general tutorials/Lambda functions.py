#lambda, param(s), operation

# Can have multiple parameters
# lambda num_1, num_2: (num_1 + num_2) ** 2

# Must be written on a single line of code

# Have different syntax from regular functions
        # no return statement
        # no name

lambda num: num ** 2

def square(num):
    return num ** 2

def transform_list(nums_list, transform_item):
    transformed_0 = transform_item(nums_list[0])
    transformed_1 = transform_item(nums_list[1])
    return [transformed_0, transformed_1]
print(transform_list([2, 3], lambda num: num ** 3))

#Built-in functions

# map = applies operation to each item in a list
number_list = [2, 3, 4, 5, 6]
print(list(map(lambda num: num ** 3, number_list)))

# filter = keeps items only if they meet a condition
print(list(filter(lambda num: num % 2 == 0, number_list))) # for example this one filters out odd numbers; keeps even