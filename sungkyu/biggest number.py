from collections import deque

def solution(number, k):
    answer = ''
    lst=deque(list(map(int, number)))
    lst_sorted=list(map(int, number))
    lst_sorted.sort(reverse=True)
    i = 0
    while k > 0:
        if len(lst) == k:
            lst = []
            break
        if lst_sorted[i] in lst:
            if k >= lst.index(lst_sorted[i]):
                while lst[0] != lst_sorted[i]:
                    lst.popleft()
                    k -= 1
                answer += str(lst.popleft())
                i = 0
                continue
        i += 1
    while len(lst)>0:
        answer += str(lst.popleft())
    return answer

number="4177252841"
k=4
print(solution(number,k))