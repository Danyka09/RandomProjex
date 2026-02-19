dic = {
    "Key": "Value"
}
#the key is what we use to access the dictionary and the value is what we get
# the : is what connects them

contacts = {
    "Bob": "bob@gmail.com",
    "Wendy": "wendy@wendy.wendy",
    "Yo": "YO@YO.YOYO"
}

contacts['Bob']
print(contacts['Bob'])

#a more advanced dictionary
inventory = {
    "heal": {"count": 3, "healing": 30},
    "arrows": {"count": 0, "damage": 30},
    "pensword": {"count": 0, "damage": 50, "healing": 30, "boss_only": True},
    "lasergun": {"count": 0, "damage": 30}
}

print(inventory["arrows"])

# RULE 1 - Values can be any type; like int, str, float or boolean
# RULE 2 - Multiple keys can have the same value
# RULE 3 - Keys must be unique
# RULE 4 - Keys don't need to be strings

contacts['Alex'] = 'coolalex@gmail.com'
contacts.pop('Wendy')
print(contacts)

print(contacts.keys())
for key in contacts.keys():
    if key == 'Alex':
        print('Yup hes here')
    else:
        print("Nope")

print(contacts.values())

for key, value in contacts.items():
    if value == 'bob@gmail.com':
        print(value, '->', key)