def solution(A):
    length = len(A)
    A.sort()
    result = 1 if length else 0

    for i in range(1, length):
        if A[i] != A[i - 1]:
            result += 1
    return result
