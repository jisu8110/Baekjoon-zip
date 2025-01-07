def solution(clothes):
    
    from collections import Counter
    
    counter = Counter([value for key, value in clothes])
    answer = 1
    
    for key, value in counter.items():
        answer *= value + 1
    
    
    return answer - 1

# def solution(clothes):
    
#     clothes_dict = {}
#     answer = 1
    
#     for cloth in clothes:
#         if cloth[1] in clothes_dict:
#             clothes_dict[cloth[1]] += 1
#         else:
#             clothes_dict[cloth[1]] = 1
    
#     for key, value in clothes_dict.items():
#         answer*= clothes_dict[key] + 1
    
    
#     return answer - 1