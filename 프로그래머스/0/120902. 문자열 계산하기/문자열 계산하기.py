def solution(my_string):
    array = my_string.split()  
    answer = int(array[0])     

    for i in range(1, len(array), 2): 
        operator = array[i]    
        number = int(array[i + 1])

        if operator == '+':
            answer += number
        elif operator == '-':
            answer -= number

    return answer
