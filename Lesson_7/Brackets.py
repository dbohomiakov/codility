def solution(S):
    if len(S) % 2:
        return 0

    bracket_pairs = {'{': '}', '[': ']', '(': ')'}
    open_brackets = bracket_pairs.keys()
    closed_brackets = bracket_pairs.values()
    
    stack = []
    stack_length = 0
    
    for bracket in S:
        if bracket in open_brackets:
            stack.append(bracket)
            stack_length += 1
        else:
            if not stack or bracket_pairs[stack.pop()] != bracket:
                return 0
            stack_length -= 1
    return 0 if stack_length else 1

