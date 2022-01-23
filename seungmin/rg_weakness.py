class DFS:
    def __init__(self, img):
        self.graph = {}
        self.img = img
        self.all_visited = []

    def insert(self, current:tuple, nexts:list):
        self.graph[current] = nexts

    def dfs(self, start):
        stack = [start]
        visited = []
        h, w = start
        color = self.img[h][w]

        while stack:
            current = stack.pop()
            nh, nw = current

            if current not in visited and self.img[nh][nw] == color:
                visited.append(current)
                stack.extend(self.graph[current])

        self.all_visited += visited


if __name__ == "__main__":

    n = int(input())
    image = []
    normal_cnt = 0
    rg_weak_cnt = 0

    for _ in range(n):
        rgb = input()
        if len(rgb) != n:
            raise IndexError
        image.append(rgb)

    normal = DFS(image)

    for h in range(n):
        for w in range(n):
            if h < n-1 and w < n-1:
                normal.insert((h, w), [(h, w+1), (h+1, w)])
            elif h == n-1 and w < n-1:
                normal.insert((h, w), [(h, w+1)])
            elif h < n-1 and w == n-1:
                normal.insert((h, w), [(h+1, w)])
            else:
                normal.insert((h, w), [])

    for h in range(n):
        for w in range(n):
            if (h,w) not in normal.all_visited:
                normal.dfs((h,w))
                normal_cnt += 1

    for h in range(n):
        for w in range(n):
            if image[h][w] == 'G':
                image[h][w] == 'R'

    rg_weak = DFS(image)

    for h in range(n):
        for w in range(n):
            if h < n-1 and w < n-1:
                rg_weak.insert((h, w), [(h, w+1), (h+1, w)])
            elif h == n-1 and w < n-1:
                rg_weak.insert((h, w), [(h, w+1)])
            elif h < n-1 and w == n-1:
                rg_weak.insert((h, w), [(h+1, w)])
            else:
                rg_weak.insert((h, w), [])

    for h in range(n):
        for w in range(n):
            if (h,w) not in rg_weak.all_visited:
                rg_weak.dfs((h,w))
                rg_weak_cnt += 1
    
    print(normal_cnt, rg_weak_cnt)
