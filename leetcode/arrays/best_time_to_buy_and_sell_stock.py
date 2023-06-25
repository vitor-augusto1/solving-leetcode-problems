from typing import List


def max_profit(prices: List[int]) -> int:
    left = 0
    right = 1
    max_profit = 0
    while right < len(prices):
        current_profit = prices[right] - prices[left]
        if prices[left] < prices[right]:
            max_profit = max(current_profit, max_profit)
        else:
            left = right
        right += 1
    return max_profit


if __name__ == "__main__":
    prices = [7, 6, 4, 3, 1]
    profit = max_profit_brute(prices)
    print(profit)
