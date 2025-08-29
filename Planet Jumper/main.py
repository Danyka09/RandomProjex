# This is a choice based adventure game called "Planet Jumper:Mercy of Dice".
# It is my first ever project made without  a tutorial
# the first bit of code was written: 27.08.2025 and this project was finished: __.__.2025
# A total of __hours and __minutes have been put in. 02:52:52(excluding the creative part)
import time
import random
import json

try:
    with open("leaderboard.json", "r") as f:
        leaderboard = json.load(f)
except:
    leaderboard = []

hp = 100
healing = 30
name = ""

def dice_roll():
    return random.randint(1, 6)
roll = dice_roll()

inventory = {
    "heal": 3,
    "arrows": 0,
    "pensword": 0,
    "lasergun": 0
}

roll_damage = {
    1: -20,
    2: -5,
    3: +10,
    4: +25,
    5: +30,
    6: +40
}

print("\n Planet Jumper: Mercy of Dice \n\n  [1] Enter the Spaceship\n  [2] View Emperors\n  [3] Chicken out ")

def opt_one():
    global name
    print(f"You decided to Enter the Spaceship ")
    time.sleep(1)
    name = input("What would you like to be called? \n")
    while not name.strip():
        name = input("You need to choose a name \n")

def opt_two():
    global leaderboard
    print(f"You chose to view the Emperors")
    print (leaderboard)

def opt_three():
    print(f"You chose to chicken out")
    time.sleep(0.5)
    print("loser")
    time.sleep(5)
    quit()

choices = {
    "1": opt_one,
    "2": opt_two,
    "3": opt_three
}

while True:
    menu = input("\n Choose an option: ")
    if menu in choices:
        choices[menu]()
        break
    else:
        print("You don't have free will, choose one of the options above.")

score = 200

leaderboard.append({"name":name, "score":score})

with open("leaderboard.json", "w") as file:
    json.dump(leaderboard, file, indent=4)

print(leaderboard)
print(roll)
print(name)
