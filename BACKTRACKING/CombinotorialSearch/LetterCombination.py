"""
Given a non-negative integer n, find all n-letter words composed by 'a' and 'b',
return them in a list of strings in lexicographical order.

Applying the backtracking template to get the solution.

is_leaf: when word is n letters, we have reached a leaf (solution).
get_edges: each letter is either 'a' or 'b'.
"""
from typing import List


def letter_combination(n: int) -> List[str]:
    """

    :param n: integer to tell us what level we have to go
    :return: List[Str]
    """
    # Define List res[] to hold our answer
    res = []

    def dfs(start_index, path):
        # If the
        if start_index == n:
            res.append(''.join(path))
            return
        for letter in ['a', 'b']:
            path.append(letter)
            dfs(start_index + 1, path)
            path.pop()

    dfs(0, [])
    return res


if __name__ == '__main__':
    n = int(input())
    res = letter_combination(n)
    for line in sorted(res):
        print(line)