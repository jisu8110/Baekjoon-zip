def solution(array, commands):
    answer = []
    
    for command in commands:
        i,j,k = command
        answer.append(slice_sort(array, i, j, k))
    
    return answer

def slice_sort(array, i, j, k):
    sorted_array = sorted(array[i-1:j])
    return sorted_array[k-1]