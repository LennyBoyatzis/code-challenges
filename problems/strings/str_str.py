# Knuth-Morris-Pratt
# Take advantage of successful comparisons

# Improvement on a O(n * m) complexity
# After a mismatch...
# Can we find a suffix that is also a prefix
# Build a prefix-suffix tabl@e

def pattern_matching_substring(haystack: str, needle: str) -> int:
    pass

def str_str(haystack: str, needle: str) -> int:
    """Returns index of the first occurrence of needle in haystack or -1"""
    needle_len = len(needle)
    needle_counter = 0

    for index, char in enumerate(haystack):
        if char == needle[needle_counter]:
            needle_counter += 1
            if needle_counter == needle_len:
                return (index + 1) - needle_counter
        else:
            needle_counter = 0
    return -1


if __name__ == '__main__':
    needle = 'issip'
    haystack = 'mississippi'
    result = str_str(haystack, needle)
    print(f'result -> {result}')
