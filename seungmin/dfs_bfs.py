from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}
        self.dfs_visited = []
        self.bfs_visited = []

    def insert(self, x1 : int, x2 : int) -> None:
        if x1 not in self.graph.keys():
            self.graph[x1] = [x2]
        else:
            self.graph[x1].append(x2)

        if x2 not in self.graph.keys():
            self.graph[x2] = [x1]
        else:
            self.graph[x2].append(x1)

    def set_sort(self):
        for i in self.graph.keys():
            self.graph[i].sort()

    def dfs(self, root : int):
        print(root, end=' ')

        self.dfs_visited.append(root)

        for child in self.graph[root]:
            if child not in self.dfs_visited:
                self.dfs(child)

    def bfs(self, root : int):
        self.bfs_visited.append(root)

        queue = deque()
        queue.append(root)

        while queue:
            parent = queue.popleft()
            print(parent, end= ' ')

            for child in self.graph[parent]:
                if child not in self.bfs_visited:
                    queue.append(child)
                    self.bfs_visited.append(child)

if __name__ == "__main__":
    n, m, v = map(int, input().split())
    g = Graph()

    for _ in range(m):
        x1, x2 = map(int, input().split())
        g.insert(x1, x2)

    g.set_sort()
    g.dfs(v)
    print()
    g.bfs(v)






