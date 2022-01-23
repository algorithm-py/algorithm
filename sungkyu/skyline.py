class build:
    def __init__(self, l, h, r):
        self.l = l
        self.h = h
        self.r = r


n = int(input())
if n>100000:
    quit()
lst = []
i = 0
while i < n:
    l, h, r = map(int, input().split())
    if i == 0 and l != 1:
        lst.append(build(1, 0, l))
        n += 1
        i += 1
    t = 0
    if i > 0:
        if l > lst[i - 1].r:
            lst.append(build(lst[i - 1].r, 0, l))
            n += 1
            i += 1
        if not (l >= lst[i - 1].r or r <= lst[i - 1].l):
            if l > lst[i - 1].l and r < lst[i - 1].r and lst[i - 1].h < h:
                lst.append(build(r, lst[i - 1].h, lst[i - 1].r))
                lst[i - 1].r = l
                n += 1
                i += 1
                t = i - 1
            elif l < lst[i - 1].l and r > lst[i - 1].r and lst[i - 1].h > h:
                lst.append(build(l, h, lst[i - 1].l))
                l = lst[i - 1].r
                temp = lst[i - 1]
                lst[i - 1] = lst[i]
                lst[i] = temp
                n += 1
                i += 1
            elif l < lst[i - 1].r:
                if h > lst[i - 1].h:
                    lst[i - 1].r = l
                else:
                    l = lst[i - 1].r
            elif r > lst[i - 1].l:
                if h > lst[i - 1].h:
                    lst[i - 1].l = r
                else:
                    r = lst[i - 1].l
    if i>0 and lst[i-1].l>=lst[i-1].r:
        lst[i-1]=build(l, h, r)
        n-=1
        continue
    else:
        lst.append(build(l, h, r))
    if lst[i].l>=lst[i].r:
        lst.pop()
        n-=1
        continue
    if t:
        temp = lst[i - 1]
        lst[i - 1] = lst[i]
        lst[i] = temp
    i += 1

lst.append(build(lst[n - 1].r, 0, lst[n - 1].r + 1))

for k in range(n + 1):
    print(lst[k].l, lst[k].h, end=' ')
