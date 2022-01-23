solution(number, k):
    answer = ''
    prev = number[0]
    
    ans = [prev]
    number = number[1:]
    
    for n in number:
        while ans and int(ans[-1]) < int(n) and k > 0:
            ans.pop()
            k -= 1
        
            if k == 0:
                break
        ans.append(n)
    
    if k > 0:
        for i in range(k):
            ans.pop()
                    
    return ''.join(ans)
