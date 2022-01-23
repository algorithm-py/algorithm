import copy
n = int(input())

graph = [] # 2차원 리스트
graph_rg = []
for i in range(n):
    graph.append(list((input())))

graph_rg = copy.deepcopy(graph)
for i in range(n):
    for j in range(n):
        if graph_rg[i][j] == 'G':
            graph_rg[i][j] = 'R'

def dfs(x,y,value): # 적록색약 아닌사람
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if graph[x][y] == value:
        graph[x][y] = 'X' # 방문 완료
        dfs(x - 1, y,value)
        dfs(x, y-1,value)
        dfs(x+1,y,value)
        dfs(x, y+1,value)
        return True

    return False

def dfs_rg(x,y,value): # 적록색약인 사람
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph_rg[x][y] == value:
        graph_rg[x][y] = 'X'
        dfs_rg(x - 1, y,value)
        dfs_rg(x, y-1,value)
        dfs_rg(x+1,y,value)
        dfs_rg(x, y+1,value)
        return True

    return False

result = 0
result_rg = 0

for i in range(n):
    for j in range(n):
        if dfs(i,j,'R') == True:
            result += 1
        elif dfs(i,j,'G') == True:
            result += 1
        elif dfs(i,j,'B') == True:
            result += 1

for i in range(n):
    for j in range(n):
        if dfs_rg(i,j,'R') == True:
            result_rg += 1
        elif dfs_rg(i,j,'B') == True:
            result_rg += 1


print(result, ' ', result_rg)


