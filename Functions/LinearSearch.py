# Linear search algorithm

class SearchAlgo:
    def __init__(self):
        self.item = []

    def linear_search(self, target, my_list):
        for index, value in enumerate(my_list):
            if value == target:
                return index
        return f"{target} not found in the list"
