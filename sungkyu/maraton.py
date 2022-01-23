def solution(participant, completion):
    dic={}
    dic2={}
    for i in range(len(participant)):
        dic[participant[i]]=i
        dic2[i]=participant[i]
    for i in range(len(participant)):
        participant[i]=dic[participant[i]]
    for i in range(len(completion)):
        completion[i]=dic[completion[i]]
    i=0
    while i<len(completion):
        for j in range(len(participant)):
            if participant[j]==completion[i]:
                participant[j]=-1
                break
        i+=1
    for i in range(len(participant)):
        if participant[i] >= 0:
            participant[0]=dic2[participant[i]]
    answer = participant[0]
    return answer

p=["mislav", "mislav", "mislav", "ana"]
c=["mislav", "ana", "mislav"]
print(solution(p,c))