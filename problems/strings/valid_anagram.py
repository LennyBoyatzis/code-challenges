from collections import Counter


def valid_anagram(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    string_one_ctr = Counter(s1)
    string_two_ctr = Counter(s2)

    result = string_one_ctr - string_two_ctr
    return len(result.keys()) == 0


if __name__ == '__main__':
    string1 = 'anagram'
    string2 = 'nagarammmm'
    result = valid_anagram(string1, string2)
    print(f'result -> {result}')
