def search(point, y, x, ori):
    if point[y][x] != 0:
        if ori == point[y][x + 1]:
            point[y][x] = 0
            search(point, y, x + 1, ori)
        if ori == point[y][x - 1]:
            point[y][x] = 0
            search(point, y, x - 1, ori)
        if ori == point[y + 1][x]:
            point[y][x] = 0
            search(point, y + 1, x, ori)
        if ori == point[y - 1][x]:
            point[y][x] = 0
            search(point, y - 1, x, ori)
        if point[y][x] == ori:
            point[y][x] = 0


cnt = 0
col = int(input())
str = input()
row = len(str)
board = [[0] * (row + 2) for _ in range(col + 2)]
board2 = [[0] * (row + 2) for _ in range(col + 2)]

for i in range(row):
    board[1][i + 1] = str[i]
    board2[1][i + 1] = str[i]
for i in range(col - 1):
    str = input()
    for j in range(row):
        board[i + 2][j + 1] = str[j]
        board2[i + 2][j + 1] = str[j]

for i in range(1, col + 1):
    for j in range(1, row + 1):
        if board[i][j] != 0:
            search(board, i, j, board[i][j])
            cnt += 1

print(cnt, end=' ')

cnt = 0

for i in range(1, col + 1):
    for j in range(1, row + 1):
        if board2[i][j] == 'G':
            board2[i][j] = 'R'

for i in range(1, col + 1):
    for j in range(1, row + 1):
        if board2[i][j] != 0:
            search(board2, i, j, board2[i][j])
            cnt += 1

print(cnt)
