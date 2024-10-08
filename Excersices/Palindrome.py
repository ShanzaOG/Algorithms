"""
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward.
It is also case-insensitive and ignores all non-alphanumeric characters.

Input - "Was it a car or a cat I saw?"
Output - True
"""


def is_Palindrome(s: str) -> bool:
    res = False
    list_1 = s.replace(" ","").lower() # Remove spaces
    print("Original String ::> ",list_1)
    list_1 = "".join(x for x in list_1 if x.isalnum()) # Remove special characters only
    print("Formatted string ::> ",list_1)
    list_2 = list_1[::-1]
    print("Reversed string ::> ",list_2)

    if list_1 == list_2:
        res = True
    return res


if __name__ == '__main__':
    result = is_Palindrome("P0P")
    print(result)
