def longest_substring(string: str) -> int:
    chars = set()
    max_len = 0

    for index in range(len(string)):
        if string[index] not in chars:
            chars.add(string[index])
        else:
            chars = set()
            chars.add(string[index])
        max_len = max(len(chars), max_len)
    return max_len


if __name__ == '__main__':
    string = 'dvdf'
    result = longest_substring(string)
    print(f'result: {result}')
