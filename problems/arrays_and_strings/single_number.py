from typing import List


def single_number(nums: List[int]) -> int:
    store = set()
    for num in nums:
        if num in store:
            store.remove(num)
        else:
            store.add(num)
    return list(store)[0]


if __name__ == '__main__':
    nums = [4, 1, 2, 1, 2]
    result = single_number(nums)
    print(f'result -> {result}')
