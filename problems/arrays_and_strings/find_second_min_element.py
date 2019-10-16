from typing import List


def find_second_min(nums: List[int]) -> int:
    """Finds the second minimum element of an array"""
    first = second = float('inf') # Sentinel value as inf is always greater

    for num in nums:
        if num <= first:
            first, second = num, first
        elif num < second:
            second = num
    return second


if __name__ == '__main__':
    nums = [1, 8, 10, 12, 49, 80]
    result = find_second_min(nums)
    print(f'result: {result}')
