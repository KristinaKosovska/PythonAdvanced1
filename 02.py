rows, column = [int(num) for num in input().split(", ")]

matrix = []
result = 0
for row in range(rows):
    matrix.append([int(el) for el in input().split(" ")])

for col in range(column):
    for index in range(rows):
        result += matrix[index][col]
    print(result)
    result = 0