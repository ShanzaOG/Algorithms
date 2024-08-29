"""
"Generate All Valid Parentheses" is a strong indication this is a combinatorial problem and
    should be solved using backtracking.
->Starting with an empty string, we can add ( or ) and continue to do that until the length reaches 2 * n.

Time Complexity -> O(4^n * n)
Space Complexity -> O(4^n * n)
"""

from typing import List


def generate_parentheses(n: int) -> List[str]:
    def dfs(start_index, path, open_count, close_count, res):
        if start_index == 2 * n:
            res.append(''.join(path))
            return
        if open_count < n:
            path.append('(')
            dfs(start_index + 1, path, open_count + 1,close_count, res)
            path.pop()
        if close_count < open_count:
            path.append(')')
            dfs(start_index + 1, path, open_count, close_count + 1, res)
            path.pop()
    res = []
    dfs(0, [], 0, 0, res)
    return res


if __name__ == '__main__':
    n = int(input())
    res = generate_parentheses(n)
    for line in sorted(res):
        print(line)
