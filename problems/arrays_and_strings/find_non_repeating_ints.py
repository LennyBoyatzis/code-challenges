from typing import List


def find_non_repeating_ints(arr: List[int]) -> List[int]:
    """Find non-repeating ints within an array"""
    store = set()

    for num in arr:
        if num not in store:
            store.add(num)
        else:
            store.remove(num)
    return list(store)


if __name__ == '__main__':
    arr = [1, 2, 4, 4, 7, 9]
    result = find_non_repeating_ints(arr)
    print(f'result -> {result}')
