def solution(num, prices): #Bottom-up
    cache = [0 for _ in range(num+1)]
    p = [0] + [int(price) for price in prices]
    cache[1] = p[1]
    for n in range(2, num+1):
        for k in range(1, n+1):
            if cache[n] < p[k] + cache[n-k]:
                cache[n] = p[k] + cache[n-k]

    return cache[n]


if __name__ == "__main__":
    n = int(input())
    prices = list(input().split())
    ans = solution(n, prices)
    print(ans)   
