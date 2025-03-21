from itertools import permutations

def solution(k, dungeons):
    answer = []
    
    for kind in permutations(dungeons, len(dungeons)):
        temp = k
        count = 0
        
        for value in kind:
            mini = value[0]
            somo = value[1]
                      
            if temp >= mini:
                temp -= somo
                count += 1
        answer.append(count)
        
    
    
    return max(answer)