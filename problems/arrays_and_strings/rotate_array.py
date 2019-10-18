from typing import List


def rotate_array(nums: List[int], k: int) -> List[int]:
    for index in range(k):
        last_element = nums.pop()
        print(f'last_element {last_element}')
        nums = [last_element] + nums
    return nums



if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    result = rotate_array(nums, 3)
    print(f'result -> {result}')
