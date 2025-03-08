from collections import Counter

def solution(participant, completion):
    
    counter_p = Counter(participant)
    counter_c = Counter(completion)
    
    for item, value in counter_p.items():
        if item in counter_c:
            if value == counter_c[item]:
                pass
            else:
                return item
        else:
            return item