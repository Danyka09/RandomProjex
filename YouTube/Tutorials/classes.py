# you make a class by writing class like a function. you do class Classname and then a function within that initializes.
# self doesn't need to be called self but its commonplace. its always first; self = name (warrior)
# and after self you write all the class attributes into the parameters and within the function you do self.attributes/parameters
# = the variable name (typically the same ig)

class Character:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed
    def take_damage(self, amount): # amount is what we get when we do health - damage (amount)
        self.health -= amount

# then you use that class, in this case characters by making variables and assigning the class (like a function) to the variables
# and in the same order add all the parameters. then you can call that by doing class_variable.attribute_variable
# in this case you have a warrior character and want to know the speed so you do warrior.speed and use as wished

ninja = Character(80, 40 ,40)
guy = Character(100, 50, 10)

print(f"Guy health: {guy.health}")
print(f"Ninja speed: {ninja.speed}\n")

# self is the object you are creating;
# the name after the . is the attribute of that object;
# after = is the variable that stores the value

""" CLASS INHERITANCE """
# everything from parent class gets inherited into child class; example: everything in character class is also is warrior class
# but we can now add child class specific parameters.

class Warrior(Character):
    def __init__(self, health, damage, speed, luck): # we add new attributes here but first copy the old ones
        super().__init__(health, damage, speed) # super is current classes parent class; this is how we pass parameters from parent to child class; necessary so it doesnt override.
        self.luck = luck
        self.toughness_modifier = 0.90
    def take_damage(self, amount): # amount comes from original parent method (function)
        modified_amount = amount * self.toughness_modifier
        super().take_damage(modified_amount)

warrior = Warrior(100, 50, 10, 67)

print(f"Initial health: {warrior.health}")
warrior.take_damage(ninja.damage) # warrior takes amount of damage the ninja gives (50) so 100-40=60 but there is a 0.9x toughness modified so its actually 100-(40*0.9)=64
# the parameter here is the (amount)

print(f"Health after damage: {warrior.health}")
print(f"Warrior posseses {warrior.luck} luck")

# classes are objects which are split into attributes and methods
# attributes are data about the object like speed, color, size, length
# methods are like functions, they give functionality; we can use them to do things like change the color or speed or take damage