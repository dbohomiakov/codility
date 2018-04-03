# If array is sorted simply check triplet of values.


def solution(A):
    sorted_A = sorted(A)
    length = len(A)

    for idx in range(length - 2):
        if sorted_A[idx] + sorted_A[idx + 1] > sorted_A[idx + 2]:
            return 1
    return 0
