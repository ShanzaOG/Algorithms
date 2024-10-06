"""
* * Duplicate Integer * *

:::> Given an integer array nums, return true if any value appears more than once in the array, otherwise return false
"""
from typing import List


def isDuplicate(nums: List[int]) -> bool:
    nums = sorted(nums)  # First sort the List if not sorted
    ans = False
    for x in range(len(nums) - 1):
        if nums[x] == nums[x + 1]: # If two consecutive numbers are the same return true and break
            ans = True
            break
    return ans


if __name__ == '__main__':
    result = isDuplicate([1, 2, 3])
    print(result)
