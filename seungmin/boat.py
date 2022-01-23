def solution(people, limit):
    
    people.sort()
    cnt = 0
    start = 0
    end = len(people) -1
    
    while start <= end:
        if people[start] + people[end] <= limit:
            start +=1
        end -=1
        cnt +=1
    return cnt
