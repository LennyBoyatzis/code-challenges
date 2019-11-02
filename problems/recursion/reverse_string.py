from typing import List


def reverse_string(s: List[str]) -> None:

    first = 0
    last = len(s) - 1

    def swap(s: List[str], first: int, last: int) -> None:
        if first < last:
            s[first], s[last] = s[last], s[first]
            swap(s, first+1, last-1)
        return s

    return swap(s, first, last)


if __name__ == '__main__':
    string = ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
    result = reverse_string(string)
    print(f'here is the result {result}')
