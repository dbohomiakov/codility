def solution(A):
    """Calculate for each element of array MAX SUM before and after it, except first and last element. Choose from the results the max one."""
    length = len(A)
    sums_per_elem = {}

    def calc_elem_sum(nums, num_length, reversed=False):
        nonlocal sums_per_elem
        max_cur_sum = 0

        if reversed:
            idx_range = range(length - 2, 0, -1)
        else:
            idx_range = range(1, length - 1)

        for i in idx_range:
            sums_per_elem[i] = sums_per_elem.setdefault(i, 0) + max_cur_sum
            max_cur_sum = max(max_cur_sum + nums[i], 0)

    calc_elem_sum(A, length)
    calc_elem_sum(A, length, reversed=True)

    return max(sums_per_elem.values())


if __name__ == '__main__':
    b = [3, 2, 6, -1, 4, 5, -1, 2]
    print(solution(b))

