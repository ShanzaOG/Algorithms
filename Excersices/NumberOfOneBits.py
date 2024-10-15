"""
You are given an unsigned integer n. Return the number of 1 bits in its binary representation.

You may assume n is a non-negative integer which fits within 32-bits.

Example 1:

Input: n = 00000000000000000000000000010111

Output: 4
"""


def hammingWeight(n: int) -> int:
    ans = 0
    while n:
        ans += n % 2 # If we find mode n, it's either 1 or 0
        n = n >> 1 # then shift the number to the right be 1
    return ans


if __name__ == '__main__':
    n = 0o0000000000000000000000000010111

    result = hammingWeight(n)
    print(result)

