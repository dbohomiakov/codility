def solution(S):
    
    if len(S) % 2:
        return 0

    opened = 0
    
    for s in S:
        if opened < 0:
            return 0
        
        if s == '(':
            opened += 1
        else:
            opened -= 1
    return 1 if not opened else 0

