import copy
from collections import deque
n, m, v = map(int, input().split())
dfs_list = []
dfs_result = [v]
bfs_list = []
bfs_result = []
visited = [False] * (n+1)
visited[0] = True
v_cp = copy.deepcopy(v)

# dfs 노드 삽입
for i in range(n+1):
    x = []
    dfs_list.append(x)
    bfs_list.append(x)

for i in range(m):
    node_fir, node_sec = input().split()
    dfs_list[int(node_fir)].append(int(node_sec))
    dfs_list[int(node_sec)].append(int(node_fir))

bfs_list = copy.deepcopy(dfs_list)
dfs_list[0].append(9999)

def dfs(start_node):

    next_node = min(dfs_list[start_node])
    dfs_result.append(next_node)

    for i in range(len(dfs_list)):
        for j in range(len(dfs_list[i])):
            if dfs_list[i][j] == start_node:
                dfs_list[i][j] = 9999  # 방문처리
    if len(dfs_result) != n:
        dfs(next_node)


def bfs(start_node):

    queue = deque([start_node])

    visited[start_node] = True

    while queue:

        bfs_next = queue.popleft()
        bfs_result.append(bfs_next)

        for i in bfs_list[bfs_next]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(v)
bfs(v_cp)
print(dfs_result)
print(bfs_result)