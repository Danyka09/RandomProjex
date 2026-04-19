# 4A
weight = int(input())

if 1 <= weight <= 100:
    if weight % 2 == 0 and weight != 2: # third times the charm. ykw i learned != atleast.
        print("YES")
    else:
        print("NO")
else:
    print("Input a weight between 1 and 100")