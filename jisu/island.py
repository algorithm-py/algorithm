import sys
sys.setrecursionlimit(10**6) #재귀 깊이 limit 선언 - 런타임 에러 해결

def dfs(x,y):
    if x <= -1 or x >= h or y <= -1 or y >= w:
        return False

    if data[x][y] == 1:
        data[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x-1, y + 1)
        dfs(x+1, y + 1)
        dfs(x+1, y - 1)
        dfs(x-1, y - 1)
        return True

    return False

while(1):
    w, h = map(int, input().split())
    data = []
    result = 0

    for i in range(h):
        data.append(list(map(int,input().split())))


    result = 0
    if w == 0 and h == 0:
        break
    else:

        for i in range(h):
            for j in range(w):
                if dfs(i, j) == True:
                    result += 1

        print(result)