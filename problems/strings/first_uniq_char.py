from typing import List
from collections import Counter


def first_uniq_char(string: str) -> int:
    if not string:
        return -1

    counter = Counter(string)

    for index, char in enumerate(string):
        count = counter[char]
        if count == 1:
            return index

    return -1


if __name__ == '__main__':
    string = 'loveleetcode'
    result = first_uniq_char(string)
    print(f'result -> {result}')
