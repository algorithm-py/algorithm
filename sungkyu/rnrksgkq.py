import sys
import math

def root(index, start, end, tree):
    if end - start == 1:
        mid = int((start + end) / 2)
    else:
        mid = math.ceil((start + end) / 2)
    if start != end:
        for i in range(start, end + 1):
            tree[index - 1] += lst[i-1]
        root(index * 2, start, mid, tree)
        root(index * 2 + 1, mid + 1, end, tree)
    else:
        tree[index - 1] = lst[start-1]


def change(b, c, start, end, index, tree, ori, dif):
    if tree[index - 1] == ori:
        tree[index - 1] = c
        return 0
    else:
        if end - start == 1:
            mid = int((start + end) / 2)
        else:
            mid = math.ceil((start + end) / 2)
        tree[index - 1] += dif
        if mid >= b:
            change(b, c, start, mid, index * 2, tree, ori, dif)
        else:
            change(b, c, mid+1, end, index * 2 + 1, tree, ori, dif)


def sum(b, c, start,end, index, tree):
    if end-start==1:
        mid = int((start + end) / 2)
    else:
        mid=math.ceil((start+end) / 2)
    if b<=start and c>=end:
        return tree[index - 1]
    elif c<start or b>end:
        return 0
    elif mid >= c:
        return sum(b, c, start,mid, index * 2, tree)
    elif mid < b:
        return sum(b, c, mid+1,end, index * 2 + 1, tree)
    else:
        return sum(b, mid,start,mid, index * 2, tree) + sum(mid + 1, c,mid+1,end, index * 2 + 1,tree)


n, m, k = map(int, sys.stdin.readline().split())
lst = []
for i in range(n):
    lst.append(int(sys.stdin.readline()))

tree = [0] * (len(lst) * 10)

root(1, 1, n, tree)

for i in range(m + k):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        ori = lst[b - 1]
        dif = c - ori
        change(b, c, 1,n, 1, tree, ori, dif)
    elif a == 2:
        print(sum(b, c,1,n, 1, tree))
