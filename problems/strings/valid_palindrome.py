def is_palindrome(s: str) -> bool:
    fmt_str = ''.join(char.lower() for char in s if char.isalnum())
    return fmt_str == fmt_str[::-1]


if __name__ == '__main__':
    string = 'A man, a plan, a canal: Panamaaa'
    result = is_palindrome(string)
    print(f'result -> {result}')
