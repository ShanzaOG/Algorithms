"""
Given a string of unique letters, find all of its distinct permutations.

    *is_leaf: start_index == letter.length
    *get_edges: each letter in the input
    *is_valid: if a letter is used used[i] == True, then we skip it
    *...additional states: used to record which letter is used in the current path
    *revert(...additional states): set used[i] = False

->We have n letters to choose in the first level, n - 1 choices in the second level and
   so on therefore the number of strings we generate is n * (n - 1) * (n - 2) * ... * 1, or O(n!)
   Since each string has length n, generating all the strings requires O(n * n!) time.

Time Complexity ->  O(n * n!)
Space Complexity ->  O(n * n!)
"""
from typing import List


def permutations(letters: str) -> List[str]:
    def dfs(start_index, path, used, res):
        if start_index == len(letters):
            res.append(''.join(path))
            return
        for i, letter in enumerate(letters):
            # skip used letters
            if used[i]:
                continue
            # add letter to permutation, mark letter as used
            path.append(letter)
            used[i] = True
            dfs(start_index + 1, path, used, res)
            # Remove letter from permutation, mark letter as not used
            path.pop()
            used[i] = False

    res = []
    dfs(0, [], [False] * len(letters), res)
    return res


if __name__ == '__main__':
    letters = input()
    res = permutations(letters)
    for line in sorted(res):
        print(line)
