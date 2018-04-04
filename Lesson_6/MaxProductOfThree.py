def solution(A):
    A.sort()

    if A[-1] > 0 and A[0] * A[1] > A[-2] * A[-3]:
        product = A[0] * A[1] * A[-1]
    else:
        product = A[-1] * A[-2] * A[-3]
    return product
