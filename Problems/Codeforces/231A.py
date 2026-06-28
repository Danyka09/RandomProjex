multi_input = []
while True:
    try:
        input1 = input()
        if input1 != "":
            multi_input.append(input1)
    except EOFError:
        break