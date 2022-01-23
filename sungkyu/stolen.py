def solution(n, lost, reserve):
    b = 0
    i = 0
    while i < len(lost):
        a = 0
        a += reserve.count(lost[i] + 1)
        a -= reserve.count(lost[i] - 1)
        if a == -1:
            temp = lost[i]
            lost.remove(temp)
            reserve.remove(temp - 1)
            b += 1
            i -= 1
        elif a == -1:
            temp = lost[i]
            lost.remove(temp)
            reserve.remove(temp + 1)
            b += 1
            i -= 1
        if i == len(lost) - 1 and b:
            i = 0
            b = 0
            continue
        i += 1

    i=0
    while i < len(lost):
        if reserve.count(lost[i] - 1):
            temp = lost[i]
            lost.remove(temp)
            reserve.remove(temp - 1)
            i -= 1
        elif reserve.count(lost[i] + 1):
            temp = lost[i]
            lost.remove(temp)
            reserve.remove(temp + 1)
            i -= 1
        i+=1

    answer = n - len(lost)
    return answer

n=int(input())
l=list(map(int,input().split()))
r=list(map(int,input().split()))
print(solution(n,l,r))