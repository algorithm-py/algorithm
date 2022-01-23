n = int(input())

for i in range(n):
    stack = input()
    sum = 0

    if stack[0] == ")":
        sum = -1

    elif stack[-1] == "(":
        sum = -1

    else:
        for x in stack:
            if x == "(":
                sum = sum + 1
            elif x == ")":
                sum = sum - 1
            if sum < 0:
                print("NO")
                break

    if sum == 0:
        print("YES")
    elif sum > 0 :
        print("NO")