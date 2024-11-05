"""
 * * Is Anagram * *

:::> Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

->An anagram is a string that contains the exact same characters as another string,
 but the order of the characters can be different.
"""

"""
def isAnagram(self, s, t):
        #if the length of both strings aren't equal then they arent anagrams. return false.
        if len(s)!=len(t): return False;
        init=set();#declare a new set
        for letter in s:#for every letter in the string s
            if letter not in init:#if the letter is not there in the new set
                init.add(letter)#add the letter to the new set
                if s.count(letter)!=t.count(letter): return False
                #if the no of letters in not the same in both strings s and t, return False.
                #else return True.
        return True
"""


def isAnagram(s: str, t: str) -> bool:
    """

    :param s: String 1
    :param t: String 2
    :return: Boolean
    """
    list1 = sorted([x for x in s])  # Return the sorted List of the split string 1
    list2 = sorted([x for x in t])  # Return the sorted List of the split string 2
    ans = False

    """ If the Length is different the strings can't be anagrams"""
    if len(s) != len(t):
        return ans
    """ If the sorted Lists are the same then they are anagrams, else return false"""
    if list1 == list2:
        ans = True
        return ans


if __name__ == "__main__":
    result = isAnagram("rat", "tar")
    print(result)
