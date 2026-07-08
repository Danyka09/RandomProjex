line_1 = str(input().lower())
line_2 = str(input().lower())

if line_1 == line_2:
    print(0)
elif line_1 < line_2:
    print(-1)
else:
    print(1)