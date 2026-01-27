# This is a choice based adventure game called "Planet Jumper:Mercy of Dice".
# It is my first ever project made without  a tutorial
# the first bit of code was written: 27.08.2025 and this project was finished: __.__.2025
# A total of __hours and __minutes have been put in. 05:47:35(excluding the creative part)
import time
import random
import json

try:
    with open("leaderboard.json", "r") as f:
        leaderboard = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    leaderboard = []

choices_yes = ["yes", "yea", "yeah", "yepp", "yep", "y", "yo", "sure", "yas", "ya", "yah", "ye"]
choices_no = ["no", "nah", "nein", "nope", "nae", "n"]
insult = ["idiot", "loser", "bitch", "punk", "dingus", "dipshit", "wimp", "seaweed brain", "kelp head", "Picklehead", "noodlebrain"]

start_time = time.time()
hp = 100
name = ""
dice_total = 0
enemy_hp = 0

def speak(text):
    input(text)

def clear_screen():
    print("\n" * 10)

def dice_roll():
    global dice_total
    roll = random.randint(1, 6)
    dice_total = dice_total + roll
    return roll

def random_insult():
    return random.choice(insult)

def choice():
    global choices_yes, choices_no, insult
    while True:
        answer = input("").lower()
        if answer in choices_yes:
            return True
        elif answer in choices_no:
            return False
        else:
            print(f"Invalid choice, try again, {random_insult()}")

inventory = {
    "heal": {"count": 3, "healing": 30},
    "arrows": {"count": 0, "damage": 30},
    "pensword": {"count": 0, "damage": 50, "healing": 30, "boss_only": True},
    "lasergun": {"count": 0, "damage": 30}
}
#1,2 is player taking damage, the rest is enemy taking damage
roll_damage = {
    1: -20,
    2: -10,
    3: -10,
    4: -25,
    5: -30,
    6: -40
}
def turn():
    while True:
        choices = {
            "1": attack,
            "2": heal,
            "3": items,
            "4": chicken_out
        }
        print(f"What do you want to do, {name}?")
        print("\n  [1] Attack\n  [2] Heal\n  [3] View Items\n  [4] Give up")
        turn1 = input("\n Choose an option: ")
        if turn1 in choices:
            choices[turn1]()
            break
        else:
            print("You don't have free will, choose one of the options above.")

def attack():
    global hp, enemy_hp
    roll = dice_roll()
    print("You decided to attack")
    time.sleep(0.5)
    effect = roll_damage[roll]
    if roll<=2:
        hp += effect
    else:
        enemy_hp += effect
    print(f"You rolled {roll}. The effect was {effect}. Your health is now {hp}. The enemies health is {enemy_hp}")
    if hp<=0:
        print(f"I though you'd last longer, {random_insult()}")
    if enemy_hp<=0:
        print("Damn, you actually did it. I thought you'd die. Good for you i guess...")
    else:
        turn()

def heal():
    print()
def items():
    print()

def apollo():
    global enemy_hp
    enemy_hp = 100
    input("Press Enter for more text")
    speak("The ship enters into warp drive, distorting the space around to travel faster than the speed of light.")
    speak("A couple hours pass by and you see a small planet, green and full of oceans like the earth.")
    speak("You have arrived to your first destination, Planet Apollo.")
    speak("The planet of archers, colonized 1000 years ago by a past human civilization, currently lead by Katniss Everdeen. ")
    speak("This planet has the most masterfully crafted bows in the universe which is why you are here,")
    speak("to get one for your fight against the Emperor.")
    speak("You walk into the capitol, everyone has brightly colored hair and stares at you as you walk to the city center.")
    speak("You find the leader, Katniss Everdeen outside, taking in the smell of the flowers.")
    speak("You announce your intention to obtain a bow but she says that she doesn’t give them to weak bitches. ")
    speak("You will need to fight.")
    speak(f"You take out your magic die and roll it on the floor. The crowd of people formed around you holds their breath.\n")
    attack()

def groverland():
    print()

def delta():
    print()

def enter_spaceship():
    global name
    print(f"You decided to Enter the Spaceship ")
    time.sleep(1)
    name = input("What would you like to be called, traveller? \n")
    while not name.strip():
        name = input("You need to choose a name \n")
    print("You venture into the spaceship and fasten your seatbelt")
    time.sleep(1)
    print(f"Are you ready to take off, {name}? ")
    player_choice = choice()
    if player_choice:
        print("Take off in ")
        time.sleep(1.2)
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print("🚀🚀🚀")
        apollo()
    else:
        print(f"Of course now you bail {random_insult()}")
        time.sleep(1)

def opt_leaderboard():
    global leaderboard
    sorted_list = sorted(leaderboard, key=lambda x: x["score"], reverse=True)[:9]
    print(f"You chose to view the Emperors")
    time.sleep(0.5)
    print ("\n      Leaderboard 🏆")
    print("-" * 25)
    for rank, entry in enumerate(sorted_list, 1):
        print(f'{rank}. {entry["name"]:<15} | {entry["score"]:<5}')
    time.sleep(1)
    input("\nPress Enter to return to menu ")
    clear_screen()
    menu()

def chicken_out():
    print(f"You chose to chicken out")
    time.sleep(0.5)
    print(random_insult())
    time.sleep(5)
    quit()

def menu():
    choices = {
        "1": enter_spaceship,
        "2": opt_leaderboard,
        "3": chicken_out
    }
    print("\n Planet Jumper: Mercy of Dice \n\n  [1] Enter the Spaceship\n  [2] View Emperors\n  [3] Chicken out ")
    while True:
        menu1 = input("\n Choose an option: ")
        if menu1 in choices:
            choices[menu1]()
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
print(random_insult())