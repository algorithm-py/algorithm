def hanoi(n, start, end, aux):
    if n == 1:
        print(start, end)
        return

    hanoi(n - 1, start, aux, end)  # n-1개의 원판이 보조 기둥에 있어야함
    print(start, end)  # 맨 아래 n번째 원판은 end 기둥으로 이동
    hanoi(n - 1, aux, end, start)  # 보조 기둥에 있는 n-1개의 원판이 목표 기둥으로 이동


n = int(input())
print(2 ** n - 1) #생각해보기
hanoi(n, 1, 3, 2)