# Barista https://youtu.be/IXr0-J5XXMA?si=Hc8t1IaoHawlUdD5
import time

yes = ["yes", "yea", "yeah", "yepp", "yep", "y", "yo", "sure", "yas", "ya", "yah", "ye"]
no = ["no", "nah", "nein", "nope", "nae", "n"]
bad_people = ["adam", "patricia", "vladimir putin", "elon musk", "donald trump", "loki"]

print("Hello, welcome to Danny's awesome café!!!!!")
time.sleep(0.5)

name = input("What is your name? \n")
time.sleep(0.5)

if name.lower() in bad_people:
    evil_status = input("Are you an evil person?\n")
    deeds = int(input("How many good deeds have you done today?\n"))
    if evil_status.lower() in yes and deeds < 4:
        print("Fuck off bitch")
        exit()
    else:
        print("Damn, you're one of the good ones, here is a lollypop!")
else:
    print("Hello " + name + ", thank you so much for comming in today!")
    time.sleep(1)

print("What would you like to order today, " + name + "?")
time.sleep(1)

while True:
    order = input(
        "We have Black Coffee for $3\n        Cappucino for $5\n        Latte for $7.50\n        Frappucino for $9.99\n")
    time.sleep(0.5)

    if order.lower() == "black coffee":
        price = 3
        break
    elif order.lower() == "cappucino":
        price = 5
        break
    elif order.lower() == "latte":
        while True:
            time.sleep(0.5)
            cream = input("Would you like whipped cream for an extra $2.50?\n")
            if cream.lower() in yes:
                price = 10
                break
            elif cream.lower() in no:
                price = 7.50
                break
            else:
                print("Yes or no?")
        break
    elif order.lower() == "frappucino":
        price = 9.99
        break
    else:
        print("\nSorry, we don't have " + order + ". \nPlease choose from our menu.")

print("And how many would you like to order, " + name + "?")
print("Each cup costs $" + str(price))

while True:
    amount = input()
    time.sleep(0.5)
    try:
        total = int(amount) * price
        break
    except ValueError:
        print("Please enter a numerical number")

print("The total is $" + str(total) + ", your " + str(amount) + " " + str(order) + " will be here in a moment.")

# or, in, and, not (!=), for, print, while True, try, break, except, str, int, input, if, else, elif,
# .lower(), .append(), .insert(), .extend([]), .clear(), remove(), pop(), list = [ ], tuple = (),