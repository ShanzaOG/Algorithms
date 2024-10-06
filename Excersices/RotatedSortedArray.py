"""
Question -> ##
You are given an array of length n which was originally sorted in ascending order.
It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Notice that rotating the array 4 times moves the last four elements of the array to the beginning.
Rotating the array 6 times produces the original array.

Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?


**************************
Problem Definition: -> We have a rotated sorted Array. we need to return the minimum in the sorted array.
                        eg [3,4,5,6,1,2] ans = 1, [4,5,0,1,2,3] ans = 0, [4,5,6,7] ans = 7
"""

from typing import List


def find_min_rotated_val(nums: List[int]) -> int:
    """
    Key Point -> Solution of log(n)
    :param nums: List of rotated sorted array
    :return: Min in the rotated array
    """

    left = 0
    right = len(nums) - 1
    result = nums[0]

    while left <= right:
        mid = (left + right) // 2
        # print('mid:',mid)
        # print('mid_val num:',nums[mid])
        # print('left_val num:', nums[left])
        # print('right_val num:', nums[right])

        if nums[mid] <= nums[left]:
            result = nums[mid]
            # print("the val is: ",result)
            break

        #result = min(result, nums[mid])

        if nums[mid] < nums[left]:
            right = mid - 1
        else:
            left = mid + 1
    return result


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    res = find_min_rotated_val(arr)
    print(res)
