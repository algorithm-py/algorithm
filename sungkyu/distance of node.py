import sys

n,m=map(int,sys.stdin.readline().split())
lst=[]
for i in range(n):
    lst.append([1001]*(n))

for i in range(n-1):
    a, b, d=map(int,sys.stdin.readline().split())
    lst[a-1][b-1]=d
    lst[b - 1][a - 1] = d

for i in range(n):
    lst[i][i]=0



for i in range(n):
    premin = 0
    for j in range(n):
        min=1001
        min_index=0
        for m in range(n):
            if i!=m and lst[i][m]!=premin and lst[i][m]!=1001 and premin<=lst[i][m]<min:
                min=lst[i][m]
                min_index = m
        premin=min

        for k in range(n):
            if lst[min_index][k]!=1001 and min_index!=k:
                if lst[i][k]>lst[i][min_index]+lst[min_index][k]:
                    lst[i][k]=lst[i][min_index]+lst[min_index][k]
                    lst[k][i] = lst[i][min_index]+lst[min_index][k]



for i in range(m):
    x,y = map(int, sys.stdin.readline().split())
    print(lst[x-1][y-1])