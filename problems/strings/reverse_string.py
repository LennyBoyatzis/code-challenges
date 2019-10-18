from typing import List


def reverse_string(chars: List[str]) -> None:
    start = 0
    end = len(chars) - 1

    while start < end:
        chars[start], chars[end] = chars[end], chars[start]
        start, end = start + 1, end - 1
    return chars


if __name__ == '__main__':
    chars = list('hello')
    result = reverse_string(chars)
    print(f'result after: {result}')
