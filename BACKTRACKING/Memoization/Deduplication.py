"""
Me To Myself -> Itabidi umeelewa hii kitu otherwise Itakurakaz Mbaya!
"""

from typing import List


def twoSum(nums: List[int], twoTarget: int) -> List[List[int]]:
    num_set = set()
    result = []
    seen = set()

    for num in nums:
        complement = twoTarget - num
        if complement in num_set and (complement, num) not in seen:
            result.append([complement, num])
            seen.add((complement, num))
            seen.add((num, complement))
        num_set.add(num)

    return result


def threeSum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()  # Sort the array to handle duplicates and simplify the two-pointer approach
    result = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicate elements

        two_target = target - nums[i]
        two_sum_results = twoSum(nums[i + 1:], two_target)

        for two_sum in two_sum_results:
            triplet = [nums[i]] + two_sum
            result.append(triplet)

    return result


# Example usage
nums = [1, 2, -1, 0, -2, 1, -1]
target = 0
print(threeSum(nums, target))
