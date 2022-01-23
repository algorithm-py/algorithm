deque = []
num = int(input())
for i in range(num):
    string = input()
    if string == "size":
        print(len(deque))
    elif string == "empty":
        if deque:
            print(0)
        else:
            print(1)
    elif string == "front":
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif string == "back":
        if deque:
            print(deque[- 1])
        else:
            print(-1)
    elif string == "pop_front":
        if deque:
            print(deque[0])
            del deque[0]
        else:
            print(-1)
    elif string == "pop_back":
        if deque:
            print(deque[- 1])
            del deque[- 1]
        else:
            print(-1)
    else:
        string, x = string.split()
        if string == "push_front":
            deque.insert(0, x)
        elif string == "push_back":
            deque.append(x)