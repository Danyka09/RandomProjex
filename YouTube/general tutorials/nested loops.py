#
numbers = [1, 2, 3, 4, 5] # so adding here make it add more vertical lines
letters = ['a','b','c'] # and adding here makes it have more per line

for x in numbers:
    for y in letters: # for y in letters means: "Take the first item ('a'), do the code below, then take the second item ('b'), and so on.
        print(f"{x}{y}", end=" ") #end=" " makes it be on the same; there are three letters so it ends after three going out the inner loop into the outer loop, so print move to next number and back into inner loop
    print()


# Representing the spreadsheet as a nested list
students_scores = [
    ["Alice", 85, 88, 95],
    ["Bob", 70, 90, 87],
    ["Charlie", 92, 86, 90],
    ["Diana", 78, 82, 85],
    ["Ethan", 89, 95, 84]
]

# Using a nested loop to calculate total scores
for student in students_scores:
    name = student[0]
    total = 0
    for score in student[1:]:  # Skip the name, sum only scores
        total += score
    print(f"{name}: {total}")