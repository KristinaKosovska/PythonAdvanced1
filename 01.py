rows, column = [int(num) for num in input().split(", ")]

matrix = []
result = 0
for row in range(rows):
    matrix.append([int(el) for el in input().split(", ")])
    result += sum(matrix[row])

print(result)
print(matrix)

