"""
Given a 32-bit unsigned integer n, reverse the bits of the binary representation of n and return the result.

Example 1:

Input: n = 00000000000000000000000000010101

Output:    2818572288 (10101000000000000000000000000000)
"""


def reverseBits(n: int) -> int:
    result = 0

    for i in range(32):
        result = result << 1
        result |= n & 1
        n = n << 1
    return result


if __name__ == '__main__':
    n = 0o0000000000000000000000000010101
    ans = reverseBits(n)
    print(ans)