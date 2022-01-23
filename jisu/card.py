n = int(input()) #구매할 카드 개수
mx_price = [0] * (n+1) # 계산된 결과값 memoization 위한 리스트 초기화
p = [0] + (list(map(int,input().split())))

for i in range(1,n+1): # 1부터 n까지
    for j in range(1,i+1): # 1부터 n-1까지
        mx_price[i] = max(mx_price[i],mx_price[i-j]+p[j]) #부등호로 수정

print(mx_price[n])