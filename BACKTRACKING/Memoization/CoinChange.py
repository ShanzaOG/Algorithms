"""
You are given coins of different denominations and an amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
Input: coins = [1, 2, 5], amount = 11

Output: 3

Explanation:
11 = 5 + 5 + 1, 3 total coins
"""
from typing import List
from math import inf


def coin_change(coins: List[int], amount: int) -> int:
    memo = [-1] * (amount + 1)

    def min_coins(coins, amount, sum, memo):
        if sum == amount:
            return 0
        if sum > amount:
            return inf
        if memo[sum] != -1:
            return memo[sum]
        ans = inf
        for coin in coins:
            result = min_coins(coins, amount, sum + coin, memo)
            if result == inf:
                continue
            ans = min(ans, result + 1)
        memo[sum] = ans
        return ans

    result = min_coins(coins, amount, 0, memo)
    return result if result != inf else -1


if __name__ == '__main__':
    coins = [int(x) for x in input().split()]
    amount = int(input())
    res = coin_change(coins, amount)
    print(res)
