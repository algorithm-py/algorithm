import sys
n, m = map(int,sys.stdin.readline().split())
sum = 0
data = [int(i) for i in sys.stdin.readline().split()]
data_sum =[0]*(n+1)
for i in range(1,n+1):
    data_sum[i] = data[i-1]+data_sum[i-1]

for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    if x==y :
        sum = data[x-1]
    else:
        sum = data_sum[y]-data_sum[x-1]

    print(sum)
    sum = 0
