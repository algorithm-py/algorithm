def move(n, a, b, c):
    if n==1:
        print("%d %d" %(a,c))
        return
    else:
        move(n-1,a,c,b)
        print("%d %d" %(a,c))
        move(n-1,b,a,c)
        return

disc=int(input())
num=2**disc-1
print(num)
move(disc,1,2,3)