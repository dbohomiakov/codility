def solution(A):
    # write your code in Python 3.6
    length = len(A)
    min_avg = (A[0] + A[1]) / 2.0
    result = 0

    for i in range(1, length - 1):
        num_3_min = (A[i - 1] + A[i] + A[i + 1]) / 3.0

        temp_min = (A[i] + A[i + 1]) / 2.0
        temp_result = i

        if num_3_min <= temp_min:
            temp_result -= 1
            temp_min = num_3_min

        if min_avg > temp_min:
            result = temp_result
            min_avg = temp_min
    return result
