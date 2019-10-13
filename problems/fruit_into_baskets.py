from typing import List

# 0 - fruit type 1
# 1 - fruit type 2
# 2 - fruit type 3
# 3 - fruit type 2
# 4 - fruit type 2


def fruit_into_baskets(tree: List[int]) -> int:
    fruit_pairs = tree[:2]
    max_pair_count = 0
    current_pair_count = 0

    for index, fruit_type in enumerate(tree):
        if fruit_type in fruit_pairs:
            current_pair_count += 1
        else:
            max_pair_count = max(current_pair_count, max_pair_count)
            current_pair_count = 2
            fruit_pairs = tree[index-1:index+1]
    return max(max_pair_count, current_pair_count)


if __name__ == '__main__':
    tree = [0, 0, 1, 1]
    result = fruit_into_baskets(tree)
    print(f'result: {result}')
