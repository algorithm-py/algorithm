import sys

def nmk(N, M, K):
    num = []
    sort_num = []
    ans = []
    idx = 0

    if N < M+K-1 or N > M*K:
        return print(-1)

    for i in range(N):
        num.append(i+1)

    for i in range(M):

        if idx+ K < N- M+ i+ 1:
            temp = idx+ K
        else:
            temp = N- M+ i+ 1
        sort_num = num[idx:temp]
        sort_num.reverse()
        ans.extend(sort_num)
        idx = temp

    for i in ans:
        print(i, end=' ')

if __name__ == "__main__":
    n, m, k = map(int, sys.stdin.readline().split())
    nmk(n,m,k)

