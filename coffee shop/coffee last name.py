#Barista https://youtu.be/IXr0-J5XXMA?si=Hc8t1IaoHawlUdD5
import time

yes = ["yes" , "yea" , "yeah" , "yepp" , "yep" , "y" , "yo" , "sure" , "yas"]
no = ["no" , "nah" , "nein" , "nope" , "nae" , "n"]

print("Hello, welcome to NewtworkChuck Coffee!!!!!")
time.sleep(1)

name = input("What is your name? \n")
time.sleep(0.5)

if name.lower() == "adam":
    evil_status = input("Is your last name Čipka? ")
    if evil_status.lower() in yes:
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
    order = input("We have Black Coffee for $3\n        Cappucino for $5\n        Latte for $7.50\n        Frappucino for $9.99\n") 
    time.sleep(0.5)
  
    if order.lower() == "black coffee":
        price = 3
        break
    elif order.lower() == "cappucino":
        price = 5
        break
    elif order.lower() == "latte":
        cream = input("Would you like whipped cream for an extra $2.50?\n")
        if cream.lower() in yes:
            price = 10
        else:
            price = 7.50
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
