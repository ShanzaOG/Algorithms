# Binary Search

class Binary_search:
    def __init__(self):
        self.items = []

    def binary_search(self, target, sorted_list):
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
