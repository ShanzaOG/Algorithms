"""
Given a phone number that contains digits 2-9,
 find all possible letter combinations the phone number could translate to.
"""

from typing import List

KEYBOARD = {
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PQRS',
    '8': 'TUV',
    '9': 'WXYZ'
}


def letter_combinations_of_phone_number(digits: str) -> List[str]:
    def dfs(start_index, path):
        """

        :param start_index: denotes the start index
        :param path: path of our nodes
        :return: res = List[str]
        """
        if start_index == len(digits):
            """
            If its the base case; leaf node
            """
            res.append(''.join(path))  # add a copy of the path to the result
            return
        next_digit = digits[start_index]
        for letter in KEYBOARD[next_digit]:
            path.append(letter)
            dfs(start_index + 1, path)
            path.pop()

    res = []
    dfs(0, [])
    return res


if __name__ == '__main__':
    digits = input()
    res = letter_combinations_of_phone_number(digits)
    print(' '.join(res))
