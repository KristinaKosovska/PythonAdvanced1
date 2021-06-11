n = int(input())
matrix = []
for row in range(n):
    matrix.append([int(el) for el in input().split(" ")])

result = 0
for i in range(n):
    result += matrix[i][i]
print(result)