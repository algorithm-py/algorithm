from collections import deque

def solution(island):
    is_island = deque()
    visited = []

    dx = [1, 1, 1, 0, -1, -1, -1, 0]
    dy = [1, 0, -1, -1, -1, 0, 1, 1]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if island[i][j]==1 and ((i,j) not in visited):
                is_island.append((i,j))
                visited.append((i,j))

                while is_island:
                    x, y = is_island.popleft()
                    for n in range(len(dx)):
                        mx, my = x + dx[n], y + dy[n]
                        if 0<=mx<h and 0<=my<w and island[mx][my] == 1 and ((mx,my) not in visited):
                            is_island.append((mx,my))
                            visited.append((mx,my))
                cnt +=1

    print(cnt)



if __name__ == "__main__":

    while True:
        h, w = map(int, input().split())

        if (h, w) == (0,0):
            break

        island = []

        for i in range(h):
            loc = list(map(int, input().split()))
            if len(loc) != w:
                raise IndexError
            island.append(loc)

        solution(island)




