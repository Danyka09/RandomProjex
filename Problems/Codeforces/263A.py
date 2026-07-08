matrix = []
for i in range(5):
    line = list(map(int, input().split()))
    matrix.append(line)

counter = 0

# while matrix[2][2] == 0:
#     counter += 1
#     if

for index_row, row in enumerate(matrix):
    for index_column, column in enumerate(matrix[index_row]):
        # print(index_row, row, index_column, column)
        if matrix[index_row].index(1):
            print(matrix[index_row].index(1))


#print(matrix[2][2])