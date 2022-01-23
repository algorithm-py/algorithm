priorities = [1,1,9,1,1,1,1]
pri = []
new = [] #새로 정렬된 리스트
sopri = []
cnt = 0
pri = [(i, v) for i, v in enumerate(priorities)] #대기열의 인덱스와 value를 튜플로 pri에 저장
totalmx = max(priorities)
mx = 0
length = len(pri) #pri의 길이
buf = 0
big = []
small = []
answer = []

while (any(priorities) != False) :
        mx = max(priorities)  # 대기열의 max value 찾기

        if mx == totalmx : #총 대기열의 max값일때, 처음 분류

            new = [i for i in range(length) if  pri[i][1]== mx] #pri의 value에서 mx와 같은 값을 찾아 pri의 인덱스를 new에 넣는다
            buf = new[-1] #buf는 현재 우선순위의 가장 나중 인덱스, 다음 우선순위 정할때 기준이 됨
            for i in new:
                priorities.pop(i)
                priorities.insert(i,0)
                sopri.append(i)

        else : #두번째 max값 부터
            new = [i for i in range(length) if  pri[i][1]== mx] #pri의 value에서 mx와 같은 값을 찾아 pri의 인덱스를 new에 넣는다
            big = [new[i] for i in range(len(new)) if new[i]>buf] #이전 우선순위의 마지막 인덱스보다 큰 인덱스를 big에 넣는다
            small = [new[i] for i in range(len(new)) if new[i] < buf] #작은 인덱스는 small에 넣는다.

            buf = new[-1]
            for i in big: #big 안에 있는 인덱스 먼저 처리
                priorities.pop(i)
                priorities.insert(i,0)
                sopri.append(i)

            for i in small: #그 다음 small에 있는 인덱스 처리
                priorities.pop(i)
                priorities.insert(i, 0)
                sopri.append(i)
print(big)
print(small)
print(new)
print(sopri)
print(priorities)

for i in sopri:
   answer  = [pri[i] for i in sopri if  pri[i][0]== i]
print(answer) #최종 정렬된 대기목록의 index, value