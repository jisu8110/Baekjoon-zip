def solution(M, N):
    count = 0
    return cutting(M, N, count)


def cutting(M, N, count):
    if M == 1:
        return count + (N - 1)
    if N == 1:
        return count + (M - 1)
    
    M_1 = M // 2
    M_2 = M - M_1
    count += 1 
    
    count = cutting(M_1, N, count)
    count = cutting(M_2, N, count)
    
    return count
