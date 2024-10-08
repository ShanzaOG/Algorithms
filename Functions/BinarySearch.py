# Binary Search
"""
Time Complexity -> Log(n)
"""


class Solution:
    def __init__(self):
        self.items = []

    def binary_search(self, target, sorted_list):
        """

        :param target: integer Value
        :param sorted_list: List[int]
        :return: int -> index of the target value
        """
        low = 0
        high = len(sorted_list) - 1

        while low <= high:
            mid = (low + high) // 2
            mid_value = sorted_list[mid]

            if mid_value == target:
                return mid
            elif mid_value < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1


if __name__ == '__main__':
    obj = Solution()
    result = obj.binary_search(4,[-1,0,2,4,6,8])
    print(result)