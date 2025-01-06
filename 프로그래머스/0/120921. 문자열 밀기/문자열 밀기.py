def solution(A, B):
    if A == B:
        return 0

    for i in range(len(A)):
        rotated_A = A[-i:] + A[:-i]  # A를 i번 회전
        if rotated_A == B:
            return i

    return -1