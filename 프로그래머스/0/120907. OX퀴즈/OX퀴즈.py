def solution(quiz):
    answer = []
    for target in quiz:
        array = target.split()
        if array[1] == '+':
            if int(array[0]) + int(array[2]) == int(array[4]):
                answer.append("O")
            else:
                answer.append("X")
        elif array[1] == '-':
            if int(array[0]) - int(array[2]) == int(array[4]):
                answer.append("O")
            else:
                answer.append("X")
    return answer