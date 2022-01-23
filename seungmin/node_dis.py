from collections import deque
import sys

class Graph:
    def __init__(self):
        self.graph = {}

    def insert(self, x1, x2, dis):
        if x1 not in self.graph.keys():
            self.graph[x1] = [[x2, dis]]
        else:
            self.graph[x1].append([x2, dis])

        if x2 not in self.graph.keys():
            self.graph[x2] = [[x1, dis]]
        else:
            self.graph[x2].append([x1, dis])

    def bfs(self, start, end):
        queue = deque()
        visit = []

        queue.append([start, 0])
        visit.append(start)

        while queue:
            current, cur_dis = queue.popleft()
            if current == end:
                return cur_dis
            
            for next_, next_dis in self.graph[current]:
                if next_ not in visit:
                    visit.append(next_)
                    queue.append([next_, next_dis + cur_dis])

if __name__ == '__main__':
    N, M = list(map(int, sys.stdin.readline().split()))
    g = Graph()
    for _ in range(N-1):
        x1, x2, dis = list(map(int, sys.stdin.readline().split()))
        g.insert(x1, x2, dis)
    for _ in range(M):
        start, end = list(map(int, sys.stdin.readline().split()))
        print(g.bfs(start, end))


