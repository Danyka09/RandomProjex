numbers = list(map(int, input().split()))

M = numbers[0]
N = numbers[1]

output = ((M * N) - ((M * N) % 2)) / 2
print(int(output))