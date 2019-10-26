from typing import List

# buy low
# sell high


def max_profit(prices: List[int]) -> int:
    if not prices:
        return 0

    best_buy = prices[0]
    profit = 0

    for price in prices:
        best_buy = min(best_buy, price)
        profit = max(profit, price - best_buy)

    return profit


if __name__ == '__main__':
    prices = [7, 6, 4, 3, 1]
    result = max_profit(prices)
    print(f'result -> {result}')
