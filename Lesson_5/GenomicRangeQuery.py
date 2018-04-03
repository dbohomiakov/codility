# Calculate changing of nums of nucleotides in DNA per step.
# Difference between nums on start position and end position of slice shows if
# nucleotide exists in the slice.


def solution(S, P, Q):
    S_length = len(S)
    sum_A = [0] * (S_length + 1)
    sum_C = [0] * (S_length + 1)
    sum_G = [0] * (S_length + 1)
    sum_T = [0] * (S_length + 1)
    results = []

    for idx, letter in enumerate(S):
        sum_A[idx + 1] = sum_A[idx]
        sum_C[idx + 1] = sum_C[idx]
        sum_G[idx + 1] = sum_G[idx]
        sum_T[idx + 1] = sum_T[idx]

        if letter == 'A':
            sum_A[idx + 1] += 1
        elif letter == 'C':
            sum_C[idx + 1] += 1
        elif letter == 'G':
            sum_G[idx + 1] += 1
        else:
            sum_T[idx + 1] += 1

    for idx, slice_range in enumerate(zip(P, Q)):
        start = slice_range[0]
        end = slice_range[1] + 1

        if sum_A[end] - sum_A[start] > 0:
            results.append(1)
        elif sum_C[end] - sum_C[start] > 0:
            results.append(2)
        elif sum_G[end] - sum_G[start] > 0:
            results.append(3)
        else:
            results.append(4)

    return results
