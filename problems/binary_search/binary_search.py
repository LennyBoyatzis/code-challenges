from typing import List


def binary_search(arr: List[int], target: int) -> int:
    """Returns index of target value if found otherwise -1"""

    left = 0
    right = len(arr) - 1

    while left <= right:
        pivot = left + (right - left) // 2

        if arr[pivot] == target:
            return pivot

        if arr[pivot] < target:
            left = pivot + 1
        else:
            right = pivot - 1

    return -1


if __name__ == '__main__':
    arr = [1, 3, 7, 9, 10, 14]
    result = binary_search(arr, 14)
    print(f'result {result}')
