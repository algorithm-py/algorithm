n,m=map(int,input().split())
temp=list(map(int,input().split()))
lst=[]
lst.append(temp[0])
for k in range(n-1):
    lst.append(lst[k]+temp[k+1])
print(lst)
for k in range(m):
    i,j=map(int,input().split())
    if i==1:
        print(lst[j-1])
    else:
        print(lst[j-1]-lst[i-2])
