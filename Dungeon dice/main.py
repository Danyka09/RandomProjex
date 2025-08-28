# This is a choice based adventure game called "Planet Jumper:Mercy of Dice".
# It is my first ever project made without  a tutorial
# the first bit of code was written: 27.08.2025 and this project was finished: __.__.2025
# A total of __hours and __minutes have been put in. 00:56:45 (excluding the creative part)
import time
import random
import json

OPT_ONE = "[1] Enter the Spaceship"
OPT_TWO = "[2] View Emperors"
OPT_THREE = "[3] Chicken out"
roll = random.randint(1, 6)
hp = (100)
healing = (+30)

leaderboard = {

}

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

while True:
    menu = input()
    if menu == ("1"):
        print(f"You decided to Enter the Spaceship ")
        time.sleep(1)
        name = input("What would you like to be called? \n")
        while not name.strip():
            name = input("You need to choose a name \n")
        break
    if menu == ("2"):
        print(f"You chose to view the Emperors")
        break
    if menu == ("3"):
        print(f"You chose to chicken out")
        time.sleep(0.5)
        print("loser")
        time.sleep(5)
        quit()
        break
    else:
        print("Please choose a valid option")

print(name)
print(roll)