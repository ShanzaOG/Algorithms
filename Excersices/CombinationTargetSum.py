"""
You are given an array of distinct integers nums and a target integer target.
Your task is to return a list of all unique combinations of nums where the chosen numbers sum to target.

The same number may be chosen from nums an unlimited number of times.
Two combinations are the same if the frequency of each of the chosen numbers is the same, otherwise they are different.

You may return the combinations in any order and the order of the numbers in each combination can be in any order.

Example 1:

Input:
nums = [2,5,6,9]
target = 9

Output: [[2,2,5],[9]]
"""

from typing import List


def combinationSum(nums: List[int], target: int) -> List[List[int]]:
    result = []

    def backtrack(remain, path, start):
        if remain == 0:
            result.append(path)
            return
        elif remain < 0:
            return

        for i in range(start, len(nums)):
            backtrack(remain - nums[i], path + [nums[i]], i)

    backtrack(target, [], 0)
    return result


if __name__ == '__main__':
    nums = [2, 4, 5, 6, 9]
    target = 9
    result = combinationSum(nums, target)
    print(result)
