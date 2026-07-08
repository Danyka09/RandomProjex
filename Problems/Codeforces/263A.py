matrix = []
for i in range(5):
    line = list(map(int, input().split()))
    matrix.append(line)

a = 0
b = 0

for index_row, row in enumerate(matrix):
    if 1 in row:
        a = index_row
        b = matrix[index_row].index(1)
        # print(a, b)

x = abs(2 - a)
y = abs(2 - b)
z = x + y

print(z)
