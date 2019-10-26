def my_atoi(string: str) -> int:
    int_max = 2**31 - 1
    int_min = -2**31

    new_str = ''
    stripped = string.lstrip()

    for char in stripped:
        if char in ['+', '-'] or char.isdigit():
            new_str += char
        elif char.isalpha() or char == ' ':
            return int(new_str)

    return int(new_str)




if __name__ == '__main__':
    string = 'words and 987'
    result = my_atoi(string)
    print(f'result -> {result}')
