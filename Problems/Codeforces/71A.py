multi_input = []
while True:
    try: # fine i used ai to figure out why it didnt work. only problem was me not adding a try except. it worked for me but they dont print an empty line they just dont do anything idk why its different but it is. also i misread it so 9 needed to be changed to 10
        input1 = input()
        if input1 != "":
            multi_input.append(input1)
    except EOFError:
        break

multi_input.pop(0)

for word in multi_input:
    if len(word) > 10:
        first_character = word[0]
        last_character = word[-1]
        new_word = first_character + str(len(word) -2) + last_character
        print(new_word)
    else:
        print(word)