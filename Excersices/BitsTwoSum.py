"""
Given two integers a and b, return the sum of the two integers without using the + and - operators.

Example 1:

Input: a = 1, b = 1

Output: 2
"""


def twoSum(a: int, b: int) -> int:
    while (b):
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a


if __name__ =='__main__':
    a = 1
    b = 4
    ans = twoSum(a,b)
    print(ans)
