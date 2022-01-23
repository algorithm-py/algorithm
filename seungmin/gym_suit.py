def solution(n, lost, reserve):
    res = list(set(reserve) - set(lost))
    los = list(set(lost) - set(reserve))
    ans = n - len(los)

    for l in los:
        if l -1 in res:
            ans +=1
            res.remove(r -1)
        elif l +1 in res:
            ans +=1
            res.remove(r +1)
    return ans
