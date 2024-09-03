"""
Given a string and a list of words, determine if the string can be constructed from concatenating words
from the list of words. A word can be used multiple times.

Input:

target = "aab"
words = ["a", "c"]
Output: false
"""

from typing import List


# Without Memoization
# def word_break(target: str, words: List[str]) -> bool:
#     def dfs(start_index):
#         if start_index == len(target):
#             return True
#
#         ans = False
#         for word in words:
#             if target[start_index:].startswith(word):
#                 ans = ans or dfs(start_index + len(word))
#                 return ans
#
#     return dfs(0)

"""
The time complexity is -> 𝑂(𝑛⋅𝑚⋅𝑘)
O(n⋅m⋅k), where:

n - is the length of the target string.
m - is the number of words in the words list.
k - is the average length of words in the words list.

Space complexity is -> O(n) where n is the size of the array 'memo' 
"""


def word_break(target: str, words: List[str]) -> bool:
    memo = {}
    def dfs(start_index):
        if start_index == len(target):
            return True
        if start_index in memo:
            return memo[start_index]

        ans = False
        for word in words:
            if target[start_index:].startswith(word):
                if dfs(start_index + len(word)):
                    ans = True
                    break
        memo[start_index] = ans
        return ans
    return dfs(0)




if __name__ == '__main__':
    s = input()
    words = input().split()
    res = word_break(s, words)
    print('true' if res else 'false')
