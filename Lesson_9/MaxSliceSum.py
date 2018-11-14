from math import inf


def solution(A):
    prev_max_sum = -inf
    max_sum = -inf
    
    for num in A:
        sum_ = max(prev_max_sum, 0) + num
        
        if sum_ >= max_sum:
            max_sum = sum_
        
        prev_max_sum = sum_
    
    return max_sum

