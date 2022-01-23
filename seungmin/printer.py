def solution(priorities, location):
   ans= 0

   while len(priorities):
       if priorities[0]== max(priorities):
           ans+= 1
           priorities.pop(0)
           if location== 0:
               return ans
           else:
               location-= 1
        else:
            tmp = priorities.pop(0)
            priorities.append(tmp)
            if location== 0:
                location= len(priorities)- 1
            else:
                location-= 1

    return ans
