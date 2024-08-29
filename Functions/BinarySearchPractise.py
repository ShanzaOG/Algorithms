"""
This is a function to practice binary search.
"""


class Solution:
    """
    inputs: target -> int, nums -> List[int] --> sorted list
    Output: index of the target -> int
    """

    def Binary_Search(self, target, nums) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            mid_val = nums[mid]

            if mid_val == target:
                return mid
            elif mid_val < target:
                low = mid + 1
            elif mid_val > target:
                high = mid - 1
        return -1


if __name__ == "__main__":
    sol = Solution()
    answer = sol.Binary_Search(4, [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10])
    print(answer)
