from typing import List


class Solution:
    def Two_Sum(self, target: int, nums: List[int]) -> List[int]:
        low = 0
        high = len(nums) - 1

        while low <= high:
            two_sum = nums[low] + nums[high]
            if two_sum == target:
                return [low, high]
            if two_sum < target:
                low += 1
            else:
                high -= 1


if __name__ == "__main__":
    sol = Solution()
    ans = sol.Two_Sum(6, [0,1,2,4])
    print(ans)
