from typing import List


def merge_two_sorted_arrays(arr1: List[int], arr2: List[int]) -> List[int]:
    """Merges two sorted arrays"""
    new_arr = [0] * (len(arr1) + len(arr2))
    numsone_index = 0
    numstwo_index = 0

    for index in range(len(new_arr) - 1):
        numsone_head = numsone[numsone_index]
        numstwo_head = numstwo[numstwo_index]
        if numsone_head <= numstwo_head:
            new_arr[index] = numsone_head
            numsone_index += 1
        else:
            new_arr[index] = numstwo_head
            numstwo_index += 1
    return new_arr


if __name__ == '__main__':
    numsone = [1, 8, 10, 12, 49, 80]
    numstwo = [11, 14, 15, 99]

    result = merge_two_sorted_arrays(numsone, numstwo)
    print(f'result: {result}')
