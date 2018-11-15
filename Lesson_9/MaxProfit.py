def solution(A):
    length = len(A)
    
    if not length:
        return 0

    max_diff = 0
    min_elem = A[0]
    
    for i in range(1, length):
        diff = A[i] - min_elem
        
        if diff >= max_diff:
            max_diff = diff
        
        min_elem = min(min_elem, A[i])
    
    return max_diff

