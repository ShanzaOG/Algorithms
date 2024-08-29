"""
A Palindrome is a word that is pronounced the same when in reverse order.
  -> Eg. 'aa', 'sas', 'kak', 'a', 'boob', 'mum', 'dad'
  -> 'aab', 'cat', 'ab' are not palindromes.

For each letter in the input string, we can either include it as a previous string or start a new string with it.
With those two choices, the total number of operations is 2^n. We also need O(n) to check if the string is a palindrome.
In total, the complexity is O(2^n * n).
"""

from typing import List


def partition(s: str) -> List[List[str]]:
    res = []

    def is_palindrome(word):
        if word == word[::-1]:
            return word

    def dfs(start_index, path):  # Leaf node/Base case
        if start_index == len(s):
            res.append(path)
            return
        for end in range(start_index + 1, (len(s) + 1)):
            prefix = s[start_index:end]  # For each 'end' the substring 'prefix = s[start: end]' is extracted.
            if is_palindrome(prefix):
                dfs(end, path+[prefix])
    dfs(0,[])
    return res


if __name__ == '__main__':
    s = input()
    res = partition(s)
    for row in res:
        print(' '.join(row))
