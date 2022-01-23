from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck=deque(truck_weights)
    b=[]
    for i in range(bridge_length):
        b.append(0)
    bridge=deque(b)
    on=0
    while len(truck)>0 or on!=0:
        on-=bridge[0]
        bridge.popleft()
        if len(truck)>0 and on+truck[0]<=weight and bridge_length>len(bridge):
            on+=truck[0]
            bridge.append(truck.popleft())
        else:
            bridge.append(0)
        answer+=1
    return answer

bridge_length=2
weight=10
truck_weights=[7,4,5,6]

print(truck_weights)

print(solution(bridge_length,weight,truck_weights))
