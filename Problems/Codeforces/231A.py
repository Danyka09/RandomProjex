multi_input = []
while True:
    try:
        input1 = input()
        if input1 != "":
            multi_input.append(input1)
    except EOFError:
        break

multi_input.pop(0)

problems_sent = 0

for problem in multi_input:
    numbers = list(map(int, problem.split())) # okay so this was the only ai. ykw im somewhat getting better ig. its always the stupid little things that get me, specifically reading data
    if sum(numbers) >= 2:
        problems_sent += 1
    else:
        continue

print(problems_sent)