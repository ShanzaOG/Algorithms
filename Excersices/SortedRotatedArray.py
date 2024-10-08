"""
You are given an array of length n which was originally sorted in ascending order.
It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Given the rotated sorted array nums and an integer target, return the index of target within nums,
    or -1 if it is not present.
"""
from typing import List


def binary_search(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = nums[mid]

        if mid_val == target:
            return mid

        if nums[low] <= mid_val:
            if nums[low] <= target < mid_val:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if mid_val < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


if __name__ == '__main__':
    result = binary_search([3,4,5,6,1,2],1)
    print(result)