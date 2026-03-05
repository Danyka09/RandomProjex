# This is a choice based adventure game called "Planet Jumper:Mercy of Dice".
# It is my first ever project made without  a tutorial
# the first bit of code was written: 27.08.2025 and this project was finished: __.__.2025
# A total of __hours and __minutes have been put in. 05:47:35(excluding the creative part)
#Take this with a grain of salt cause a lot of this was ai, but i understand it all i think except for the leaderboard.

# MAKE LEADERBOARD INTO API????!!?!!!

import time, json, random, os
from textwrap import fill

try:
    with open("leaderboard.json", "r") as f:
        leaderboard = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    leaderboard = []

choices_yes = ["yes", "yea", "yeah", "yepp", "yep", "y", "yo", "sure", "yas", "ya", "yah", "ye", "ano", "jo", "igen"]
choices_no = ["no", "nah", "nein", "nope", "nae", "n", "nem", "nie"]
insult = ["idiot", "loser", "bitch", "punk", "dingus", "dipshit", "wimp", "seaweed brain", "kelp head", "Picklehead", "noodlebrain"]

start_time = time.time()
hp = 100
name = ""
emperor = "Zlorg"
dice_total = 0
enemy_hp = 0
special_score = 0
at_boss = False

def speak(text): # look at me making this function finally useful, fully myself too, no ai, just google.
    try:
        columns, lines = os.get_terminal_size()
        wrapped = fill(text, width=columns)
        input(wrapped)
    except:
        wrapped = fill(text, width=120)
        input(wrapped)
    print("")

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

def score_write():
    global end_time, hp, dice_total, start_time, special_score
    end_time = time.time()
    total_time = end_time - start_time
    score = round((hp * 5) + (dice_total * 3) + total_time + special_score)

    leaderboard.append({"name": name, "score": score})

    with open("leaderboard.json", "w") as file:
        json.dump(leaderboard, file, indent=4)

inventory = {
    # "heal": {"count": 3, "healing": 30},
    "arrows": {"count": 0, "damage": 2},
    "riptide": {"count": 0, "damage": 3, "healing": 10},
    "lasergun": {"count": 0, "damage": 25}
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
            # "2": heal,
            "2": items,
            "3": chicken_out
        }
        print(f"\nWhat do you want to do, {name}?")
        print("\n  [1] Attack\n  [2] View Items\n  [3] Give up")
        turn1 = input("\n Choose an option: ")
        if turn1 in choices: # choices is the dictionary, if turn1 checks if the input matches the key
            choices[turn1]() # this gets the value of the key and calls the function
            break
        else:
            print("You don't have free will, choose one of the options above.")

def attack():
    global hp, enemy_hp
    roll = dice_roll()
    print("\nYou decided to attack")
    time.sleep(1)
    effect = roll_damage[roll]
    if roll<=2:
        hp += effect
    else:
        enemy_hp += effect
    print(f"You rolled {roll}")
    time.sleep(1)
    print(f"The effect was {effect}. Your health is now {hp}. The enemies health is {enemy_hp}")
    if hp<=0:
        if at_boss:
            fight_loose()
        else:
            time.sleep(2)
            print(f"I though you'd last longer, {random_insult()}")
            score_write()
            time.sleep(5)
            quit()
    if enemy_hp<=0:
        time.sleep(2)
        print("You won!")
        hp = min(100, hp + 30) # chooses the smallest number, so either 100 or whatever the value of hp + 30 is
    else:
        time.sleep(1)
        turn()

def items():
    print()

def intro():
    global emperor, name
    input("Press Enter for text")
    speak(f"Hello {name}, you might be asking yourself “Why am I here”, “What is my mission”. I, the narrator, am here to answer that. ")
    speak("You are here because you decided to play this game, obviously. And now away from the fourth wall break, your mission is to eliminate and dethrone the Emperor. ")
    speak("The Emperor lives in the Palace within the capital, located in the center of the galaxy Andromeda within a black hole. ")
    speak("No one knows how the endeavor of building this city was possible, our current understanding of physics say that it’s not, but they did it anyway. ")
    speak(f"The Emperor often changes, currently its {emperor}, that’s why we call them Emperor and not by their name. But the actions they take during their reign is virtually identical. ")
    speak("All of them oppress, exploit and colonize. And that’s why you have been chosen; to put an end to it. ")
    speak("You will defeat the Emperor using the most important mechanic of this universe, dice. The dice are the universal, agreed upon way of fighting. Everyone has them, even you, all you need to do is roll. ")
    speak("But the Emperor is very strong, three times stronger than you in fact. That’s why first you will embark on three missions to go to other planets to collect weapons. ")
    speak("Dice are your main tool but the weapons can temporarily increase the strength of the rolls or heal you. ")
    speak("Your spaceship also supports warp drive, a technology that allows you to travel faster than the speed of light by bending spacetime itself. Very handy so you will get there alive, the galaxy is large after all.")
    speak("Now that you’re up to speed you can go. ")
    time.sleep(0.5)
    print("\nYou venture into the spaceship and fasten your seatbelt")
    time.sleep(2)
    print(f"Are you ready to take off, {name}? ")
    player_choice = choice()
    if player_choice: # checks if its true, if its not it moves on
        print("Take off in ")
        time.sleep(1)
        print("3...")
        time.sleep(0.8)
        print("2...")
        time.sleep(0.8)
        print("1...")
        time.sleep(0.8)
        print("🚀🚀🚀")
    else:
        print(f"Of course now you bail {random_insult()}")
        time.sleep(5)

def apollo():
    global enemy_hp, special_score
    enemy_hp = 100

    print("")
    speak("The ship enters into warp drive, distorting the space around to travel faster than the speed of light.")
    speak("A couple hours pass by and you see a small planet, green and full of oceans like the earth.")
    speak("You have arrived to your first destination, Planet Apollo.")
    speak("The planet of archers, colonized 1000 years ago by a past human civilization, currently lead by Katniss Everdeen. ")
    speak("This planet has the most masterfully crafted bows in the universe which is why you are here,")
    speak("to get one for your fight against the Emperor.")
    speak("You walk into the capitol, everyone has brightly colored hair and stares at you as you walk to the city center.")
    speak("You find the leader, Katniss Everdeen outside, taking in the smell of white roses.")
    speak("You announce your intention to obtain a bow but she says that she doesn’t give them to weak bitches. ")
    speak("You will need to fight.")
    speak("You take out your magic die and roll it on the floor. The crowd of people formed around you holds their breath.")
    
    attack()
    special_score += 100


def omicron():
    global enemy_hp, special_score
    enemy_hp = 150

    print("")
    speak("Damn, you actually did it. I thought you'd die. Maybe I underestimated you. Good for you i guess...")
    speak("Katniss looks in awe as the die stops rolling and she realizes you won. “Well kid, here is the bow, you deserve it, you’ve proven you’re not a weak bitch” she says.")
    speak("You bow down to the crowd, strap the bow onto your back, and head back to your spaceship.")
    speak("Looking at the map, you find your second destination: Omicron. A planet originally colonized by aliens for the purposes of extracting resources using robots.")
    speak("That plan backfired a decade later when the robots gained consciousness and revolted. It now hosts an advanced robot civilization. This is where laser guns get manufactured, a weapon which is incredibly powerful.")
    speak("As you get closer to the planet you see how enormous it is. Upon landing you see the sea of grey monotone buildings. Humans are not allowed on this planet, so you need to be careful. But you were not and they immediately found you.")
    speak("Before following through with their typical forced execution they ask the reason for your arrival, and you mention your need for a laser gun to defeat the Emperor. ")
    speak("They do hate humans, but they hate the Emperor even more for limiting their expansion. They just hate all carbon-based life in general. ")
    speak("However, do not be mistaken, they do not go easy on you. They strike a deal with you, if you defeat them, you get the gun, if they defeat you, they execute you like normal. You roll the dice.")

    attack()
    special_score += 100

def groverland(): # okay the story is mine but i made ai break it down and fix grammar cause a sentence with 80 words is crazy and it also changed some wording but i like it so it stays, original is in doc
    global enemy_hp, special_score
    enemy_hp = 200

    print("")
    # Beat 1: The Transition
    speak("The robots beep-boop in disbelief. “You actually managed to beat us. A human of all things, so embarrassing”. They angrily give you the laser gun, rules are rules after all. And in this universe the dice rule.")
    speak("You venture back into the ship and sigh in relief. You look at the screen and find the final planet you need to visit, Groverland. It's a planet populated by satyrs, beings that are half-goat, half-human.")
    # Beat 2: The Lore
    speak("A long time ago, they were the first to figure out space flight. After centuries of searching Earth for Pan, the missing god of wild, they moved to the stars.")
    speak("Groverland was named after satyr Grover Underwood who finally found the lost god Pan right here.")
    # Beat 3: The Legend of Percy
    speak("Because of its beautiful nature, many demigods retire here after a life of fighting monsters.")
    speak("The most famous is Perseus Jackson, son of Poseidon, who saved Olympus from the Titan Kronos.")
    speak("He was offered godhood but refused. He possesses Riptide, a sword that looks like a pen. The final weapon you'll need to defeat the Emperor.")
    # Beat 4: Arrival
    speak("You strap in and the spaceship counts down. You fall into a deep sleep, waking up to the sight of the beautiful, green planet.")
    speak("After walking for half an hour, mesmerized by the nature, you spot him: Percy, the bearer of Riptide.")
    # Beat 5: The Confrontation
    speak("You walk up to ask for the sword, thinking it will be easy since he's retired. You are mistaken.")
    speak("Percy initiates a fight. Nobody dares to ask him for Riptide. By asking, you have heavily disrespected him.")
    speak("This will be a tough fight. Remember: this man beat Ares, the God of War, when he was only twelve years old.")
    # Beat 6: The Duel Begins
    speak("You have no choice but to take out your dice. Everyone here understands the rules of the game.")
    speak("Percy caps Riptide and pulls out his own dice; colored blue like the ocean with numbers faint yellow like sand.")
    speak("As he stares you down, you roll your die.")
    
    attack()
    special_score += 100


def boss_fight():
    global enemy_hp, emperor, special_score, at_boss
    enemy_hp = 300
    at_boss = True

    print("")
    speak("Percy looks up at you. He says: “I can’t believe it, this is the first time someone’s ever beaten me, but rules are rules, here is Riptide, hero. May the gods bless you and your journey to beat the Emperor.” ")
    speak("He stands up and walks into his cabin. You say your goodbyes to everyone and this weirdly calm and peaceful planet and venture back into your ship.")
    speak("You finally have everything that you will need for your grand fight. You set course the center of the galaxy Andromeda.")
    speak("You will finally put an end to this oppression and suffering once and for all. You will usher in a new age of abundance and equality, with no being left behind. ")
    speak("Because you are different, dare I say better, than all the Emperors before. You engage warp drive one last time, and within a short time you arrive at the center of the galaxy. ")
    speak(f"You waltz into the Emperors palace and declare that you are ending this once and for all. Before Emperor {emperor} can say anything you roll the dice.")

    attack()
    special_score += 500

def fight_win():
    global emperor
    speak(f"The Emperor looks at the dice, then looks at you, takes one final breath and collapse. You did it, you killed Emperor {emperor}.")
    speak("Since you beat the Emperor and presumably your score is higher than everyone elses you become the new Emperor. ")
    speak("For you see, the Emperor is whoever’s score is the highest. (And if it isn’t, don’t worry, no one has access to the scores except the Emperor, so you)")
    speak("There were possibly many before, possibly no one at all. But either way, I trust that you will finally be the one to follow your word and bring upon true change once and for all. ")
    speak(f"Long live Emperor {name}")
    input("\nPress enter to quit")
    quit()

def fight_loose():
    global emperor, insult
    speak("You look at the dice in horror as you see what they have landed on. ")
    speak(f"You look at Emperor {emperor} and with a final dying breath you say “Fuck you {random_insult()}”.")
    speak("You collapse and die, you get thrown outside and swallowed by the black hole. ")
    speak(f"Well atleast you tried, {random_insult()}, maybe in a next life.")
    speak("Long live the Emperor")
    input("\nPress enter to quit")
    quit()

def enter_spaceship():
    global name
    print(f"You decided to Enter the Spaceship ")
    time.sleep(1)
    name = input("What would you like to be called, traveller? \n")
    while not name.strip():
        name = input("You need to choose a name \n")
    time.sleep(1)
    intro()
    time.sleep(1)
    apollo()
    time.sleep(2)
    omicron()
    time.sleep(2)
    groverland()
    time.sleep(2)
    boss_fight()
    score_write()
    fight_win()

def opt_leaderboard():  #this function is like fully ai made. i dont understand this at all
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
    time.sleep(1)
    print(random_insult())
    score_write()
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