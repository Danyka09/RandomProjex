# This is a choice based adventure game called "Planet Jumper:Mercy of Dice".
# It is my first ever project made without  a tutorial
# the first bit of code was written: 27.08.2025 and this project was finished: __.__.2025
# A total of __hours and __minutes have been put in. 03:21:08(excluding the creative part)
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
dice_total = 0
start_time = time.time()

def clear_screen():
    print("\n" * 10)

def dice_roll():
    global dice_total
    roll = random.randint(1, 6)
    dice_total = dice_total + roll
    return roll

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

def opt_one():
    global name
    print(f"You decided to Enter the Spaceship ")
    time.sleep(1)
    name = input("What would you like to be called? \n")
    while not name.strip():
        name = input("You need to choose a name \n")

def opt_two():
    global leaderboard
    sorted_list = sorted(leaderboard, key=lambda x: x["score"], reverse=True)
    print(f"You chose to view the Emperors")
    time.sleep(0.5)
    print ("\n  Leaderboard 🏆")
    print("-" * 20)
    for rank, entry in enumerate(sorted_list, 1):
        print(f'{rank}. {entry["name"]:<10} | {entry["score"]:<5}')
    time.sleep(1)
    input("\nPress Enter to return to menu ")
    clear_screen()
    menu()

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

def menu():
    print("\n Planet Jumper: Mercy of Dice \n\n  [1] Enter the Spaceship\n  [2] View Emperors\n  [3] Chicken out ")
    while True:
        menu = input("\n Choose an option: ")
        if menu in choices:
            choices[menu]()
            break
        else:
            print("You don't have free will, choose one of the options above.")

menu()

#test rolls
print(dice_roll())
print(dice_roll())
print(dice_roll())

end_time = time.time()
total_time = end_time - start_time
score = round(hp * 10 + dice_total * 3 - total_time / 10)

leaderboard.append({"name":name, "score":score})

with open("leaderboard.json", "w") as file:
    json.dump(leaderboard, file, indent=4)

#Test prints
print(dice_total)
print(start_time)
print(end_time)
print(total_time)
print(name)
print(score)