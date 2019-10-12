def licence_key_formatting(string: str, num: int) -> str:
    fmt_string = ''.join(string.split('-'))
    new_string = ''

    for index, char in enumerate(fmt_string[::-1]):
        new_string = new_string + char
        if (index + 1) % num == 0 and index != len(fmt_string) - 1:
            new_string = new_string + '-'
    return new_string[::-1]


if __name__ == '__main__':
    string = '5F3Z-2e-9-w'
    num = 4
    result = licence_key_formatting(string, num)
    print(f'result: {result}')

    string_2 = '2-5G-3J'
    num_2 = 2
    result_2 = licence_key_formatting(string_2, num_2)
    print(f'result_2: {result_2}')
