def solution(s):
    
#     array = s.split(" ")
#     handle = ""
#     answer = 0
    
#     for i in array:
#         if i != 'Z': 
#             handle = i
#             answer += int(handle)
#         else:
#             answer -= int(handle)

    stack = []
    array = s.split()
    
    for i in array:
        if i != 'Z':
            stack.append(int(i))
        else:
            stack.pop()
            
    return sum(stack)