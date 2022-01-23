n, m, k = map(int, input().split())
if n < m + k - 1 or n > m * k:
    print(-1)
    quit()
a = []
for i in range(1, n + 1):
    a.append(i)
if k == 1:
    print(*a, sep=' ', end=' ')
else:
    temp = a[0:m]
    del a[0:m - 1]
    a[0] = temp
    i = 1
    j = (n - m) % (k - 1)
    while i < k:
        if j > 0:
            temp = a[i:i + int((n - m) / (k - 1)) + 1]
            del a[i:int((n - m) / (k - 1)) + i]
            a[i] = temp
            j -= 1
        else:
            temp = a[i:i + int((n - m) / (k - 1))]
            del a[i:(int((n - m) / (k - 1)) + i - 1)]
            a[i] = temp
        i += 1

    a.reverse()

    for i in range(k):
        print(*a[i], sep=' ', end=' ')
