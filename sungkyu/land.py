def search(point, y, x):
    if point[y][x] != 0:
        if point[y][x + 1]:
            point[y][x] = 0
            search(point, y, x + 1)
        if point[y][x - 1]:
            point[y][x] = 0
            search(point, y, x - 1)
        if point[y + 1][x]:
            point[y][x] = 0
            search(point, y + 1, x)
        if point[y - 1][x]:
            point[y][x] = 0
            search(point, y - 1, x)
        if point[y + 1][x + 1]:
            point[y][x] = 0
            search(point, y + 1, x + 1)
        if point[y - 1][x - 1]:
            point[y][x] = 0
            search(point, y - 1, x - 1)
        if point[y + 1][x - 1]:
            point[y][x] = 0
            search(point, y + 1, x - 1)
        if point[y - 1][x + 1]:
            point[y][x] = 0
            search(point, y - 1, x + 1)
        if point[y][x]:
            point[y][x] = 0


import sys
sys.setrecursionlimit(10 ** 9)

cnt = 0
row, col = 1, 1

while 1:
    row, col = map(int, input().split())
    if row == 0 and col == 0:
        break
    board = [[0] * (row + 2) for _ in range(col + 2)]
    for i in range(col):
        str = input()
        for j in range(row):
            board[i + 1][j + 1] = int(str[j * 2])

    for i in range(1, col + 1):
        for j in range(1, row + 1):
            if board[i][j] != 0:
                search(board, i, j)
                cnt += 1

    print(cnt)

    cnt = 0
