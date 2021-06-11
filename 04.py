n = int(input())

matrix = []
for row in range(n):
    matrix.append(list(input()))
symbol = input()
position = None

for row in range(n):
    for col in range(n):
        if symbol == matrix[row][col]:
            position = (row, col)
            break
    if position:
        break

print(position if position else f"{symbol} does not occur in the matrix")

