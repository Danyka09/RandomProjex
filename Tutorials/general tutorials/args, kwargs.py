# *args = were telling python the function can collect any number of positional arguments def func(this part of a function):
# the * tell python to put arguments into tuple, args can be anything like extra or var1

# **kwargs is for keyword arguments, similar but instead of doing ("green", 5) we do (tea_type="green", steep_time=5)
#same here the ** does the work kwargs is a commonly used variable

def tea_order(customer_name, tea_type, *args, ** kwargs):
    print(customer_name, "ordered a", tea_type, "tea")
    for arg in args:
        print(" - Add", arg)
    for key, value in kwargs.items():
        print(" - Add", key, ":", value)

tea_order("Alice", "chamomile")
tea_order("Bob", "black", milk="oat")
tea_order("Tony", "black", "oat", sweetener="honey")

def average_score(*args):
    list = [int(x) for x in args]
    return sum(list) / len(list)

print(average_score(85, 90, 78))   # Output: 84.333...
print(average_score(100, 95))      # Output: 97.5
print(average_score())             # Output: 0 (no scores given)