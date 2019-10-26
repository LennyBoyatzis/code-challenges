from typing import List


def rob(nums: List[int]) -> int:
    prev_max = 0
    curr_max = 0
    for num in nums:
        temp = curr_max
        curr_max = max(prev_max + num, curr_max)
        prev_max = temp
    return curr_max


if __name__ == '__main__':
    nums = [1, 3, 1, 3, 100]
    result = rob(nums)
    print(f'result -> {result}')
