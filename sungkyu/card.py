import copy

n = int(input())
p = [0]
string = input()
p = string.split()
p.insert(0, 0)

for i in range(n + 1):
    p[i] = int(p[i])

dp = copy.deepcopy(p)

i = 1
while i <= n:
    j = 1
    while j <= i:
        dp[i] = max(dp[i], dp[i - j] + p[j])
        j += 1
    i += 1

print(dp[n])
