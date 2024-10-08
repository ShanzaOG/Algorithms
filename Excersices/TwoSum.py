"""
* * * Two Integer Sum * * *

Given an array of integers nums and an integer target, return the indices i and j such that
                    nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.
"""
from typing import List


def twoSum_easy(nums: List[int], target: int) -> List[int]:
    left = 0
    right = len(nums) - 1

    # Check for edge case where there's only one number in the list
    if len(nums) == 1 and nums[0] == target:
        return [0]

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left,right]

        if current_sum < target:
            left += 1
        else:
            right -= 1
    return []


def twoSum(nums: List[int], target: int) -> List[int]:
    num_map={}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []


if __name__ == '__main__':
    result = twoSum([3, 4, 5, 6], 7)
    print(result)