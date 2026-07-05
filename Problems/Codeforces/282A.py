X = 0
for i in range(int(input())):
    operation = input()[1]
    if operation == "+": # boom bitch i figured out the middle character is always the same
        X +=1
    elif operation == "-":
        X -=1

print(X) # reference for future me: dont put the print into else cause the range runs out by that point so it just doesnt print but i figured it out myself so proud at myself. did everything by myself. only thing i looked at was how to slice from a previous bit of tutorial code i had saved.