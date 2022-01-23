from collections import deque
import sys
n = int(input())
data = deque()

for i in range(n):
    order = sys.stdin.readline().split()

    if order[0]=='push_front' :
        num = order[1]
        data.appendleft(num)

    if order[0] == 'push_back' :
        num = order[1]
        data.append(num)

    if order[0] == 'pop_front' :
        if not data:
            print(-1)
        else:
            print(data[0])
            data.popleft()

    if order[0] == 'pop_back' :
        if not data:
            print(-1)
        else:
            print(data[-1])
            data.pop()

    if order[0] == 'size' :
        print(len(data))

    if order[0] == 'empty' :
        if not data:
            print(1)
        else:
            print(0)

    if order[0] == 'front' :
        if not data:
            print(-1)
        else:
            print(data[0])

    if order[0] == 'back' :
        if not data:
            print(-1)
        else:
            print(data[-1])