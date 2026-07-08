username = input()
number = len(set(username))

if number % 2 == 1:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")