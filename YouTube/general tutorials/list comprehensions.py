# they are useful for simple list operations to minimize functions by condensing them, has performance benefits too.
nums = [1, 2, 3, 4, 5]
# operation; for var in; original_list
nums_sq = [n**2 for n in nums]
print(nums_sq)

tv_shows = ["friends", "HEATED RIVALRY", "modern FAMILY", "oTeCkoVIa", "the Office"]

tv_shows_cap = []
for show in tv_shows:
    show_cap = show.title()
    tv_shows_cap.append(show_cap)
print(tv_shows_cap)

tv_shows_cap2 = [show.title() for show in tv_shows]
print(tv_shows_cap2)

#conditionals
tv_shows_cap_conditional = []
for show in tv_shows:
    if len(show) >= 10:
        show_cap = show.title()
        tv_shows_cap_conditional.append(show_cap)
print(tv_shows_cap_conditional)

tv_shows_cap_conditional2 = [show.title() for x in tv_shows if len(x) >= 10]
print(tv_shows_cap_conditional2)

# creating a new list
new_nums_sq = [n**2 for n in range(1, 11)]
print(new_nums_sq)

# List comprehensions provide a shorthand for creating lists: [expression for item in iterable if condition]
# Unlike functions, they are self-contained expressions that return a list immediately without a 'return' statement.
# They replace multi-line 'for' loops, combining element selection and transformation into one readable line.

# A list comprehension consists of: [expression for item in iterable if condition]
# 1. Expression: The operation performed on each element (the output).
# 2. Item: The temporary variable representing the current element.
# 3. Iterable: The source data you are looping through (list, range, etc.).
# 4. Condition (Optional): A filter that only includes items where the test is True.