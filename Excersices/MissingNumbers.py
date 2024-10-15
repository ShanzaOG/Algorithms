"""
Given an array nums containing n integers in the range [0, n] without any duplicates, return the single number in the range that is missing from nums.

Follow-up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

Example 1:

Input: nums = [1,2,3]

Output: 0
"""
from typing import List


def missingNumber(nums: List[int]) -> int:
    result = len(nums)

    for i in range(len(nums)):
        result += (i - nums[i])
    return result


if __name__ == '__main__':
    n = [1,2,3]
    ans = missingNumber(n)
    print(ans)