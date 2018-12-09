from math import inf


def solution(A):
    board_length = len(A)
    die_numbers = list(range(1, 7))
    sum_per_square = [A[0]] + [-inf] * (length - 1)
    
    for square_idx in range(1, board_length):
        for die_num in die_numbers:
            if square_idx < die_num:
                break
            
            max_sum_per_square[square_idx] = max(
                max_sum_per_square[square_idx - die_num] + A[square_idx],
                max_sum_per_square[square_idx]
            )

    return max_sum_per_square[-1]

