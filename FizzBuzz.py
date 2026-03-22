y = int(input("Up to what number do you want to go? "))
for x in range(1, y+1):
	if x % 3 == 0 and x % 5 == 0: # okay so python first does x % 3 == 0 and if its not a zero its true and same for the other which means that its doing the opposite so i fixed it with a not (with help of ai to figure it out). cause any integer thats not 0 is evaluated as true so True and True are True
		print("Fizzbuzz")
	elif x % 5 == 0:
		print("Buzz")
	elif x % 3 == 0:
		print("Fizz")
	else:
		print(x)
input()