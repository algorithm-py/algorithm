import math

def solution(left, right):
    ans = 0
    for num in range(left, right +1):
        num_div = 0
        for i in range(1, int(math.sqrt(num) +1)):
            if (num %i) == 0:
                num_div += 1
                if math.pow(i, 2) != num:
                    num_div += 1
        if (num_div %2) == 0:
            ans += num
        else:
            ans -= num
    return print(ans)
