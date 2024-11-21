import math

def solution(n):
    
    answer = 0
    
    for i in range(4,n+1):
        target = int(math.sqrt(i))
        for j in range(2,target+1):
            if i % j == 0:
                answer += 1
                break
        
    return answer