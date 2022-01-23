solution(bridge_len, limit, waiting):
    ans = 0
    passing = [0 for _ in range(bridge_len)]
    trucks = 0
    
    while len(passing):
        ans += 1
        passed = passing.pop(0)
        trucks -= passed
        if waiting:
            if trucks + waiting[0] <= limit:
                truck = waiting.pop(0)
                trucks += truck
                passing.append(truck)
            else:
                passing.append(0)
        
        
    return ans
