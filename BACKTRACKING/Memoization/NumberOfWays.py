"""
We have a message consisting of digits 0-9 to decode. Letters are encoded to digits by their positions in the alphabet

A -> 1
B -> 2
C -> 3
...
Y -> 25
Z -> 26
Given a non-empty string of digits, how many ways are there to decode it?

Input: "18"
Output: 2

Explanation: "18" can be decoded as "AH" or "R"
"""


def decode_ways(digits):
    memo = {}

    def dfs(start_index, memo):
        if start_index in memo:
            return memo[start_index]
        if start_index == len(digits):
            return 1
        ways = 0
        # can't decode string with leading 0
        if digits[start_index] == '0':
            return ways

        # decode two digits
        ways = ways + dfs(start_index + 1, memo)

        # decode two digits
        if 10 <= int(digits[start_index: start_index + 2]) <= 26:
            ways = ways + dfs(start_index + 2, memo)
        memo[start_index] = ways
        return ways

    return dfs(0, memo)


if __name__ == '__main__':
    digits = input()
    res = decode_ways(digits)
    print(res)
