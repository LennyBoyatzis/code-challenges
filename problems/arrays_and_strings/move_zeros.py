from typing import List


def move_zeros(nums: List[int]) -> int:
    counter = 0
    num_zeros = 0

    for i in range(len(nums)):
        if nums[i] is not 0:
            nums[counter] = nums[i]
            counter += 1
        else:
            num_zeros += 1

    for i in range(1, num_zeros + 1):
        nums[-i] = 0


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    result = move_zeros(nums)
    print(f'result -> {result}')
