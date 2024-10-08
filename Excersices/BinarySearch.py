"""
You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.
"""
from typing import List


def binarySearch(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (high+low)//2
        mid_val = nums[mid]

        if mid_val == target:
            return mid
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1



if __name__ == '__main__':
    result = binarySearch([-1,0,2,4,6,8],4)
    print(result)