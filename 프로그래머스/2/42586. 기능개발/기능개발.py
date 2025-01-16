from collections import deque

def solution(progresses, speeds):
    
    total_days = 0
    count = 0
    answer = []
    n = len(progresses)
    
    total_days = calculate_day(progresses[0], speeds[0])
    
    for i in range(n):
        if total_days * speeds[i] + progresses[i] >= 100:
            count += 1
            pass
        else:
            answer.append(count)
            count = 0
            
            total_days = calculate_day(progresses[i], speeds[i])
            count += 1
            
    answer.append(count)
        
    return answer

def calculate_day(progresses, speeds):
    
    total_days = (100 - progresses) / speeds
    total_days = total_days if total_days == int(total_days) else int(total_days) + 1
    
    return total_days