from typing import List
"""
Given [1,2,3,4,4] ans = True
Given [1,2,3,4,5] ans = False
"""

def find_duplicate(nums: List[int]) -> int:
    ans = False
    for x in range(len(nums) - 1):
        if nums[x] == nums[x+1]:
            ans = True
            break
    return ans

def isAnagram(s: str, t: str) -> bool:
    ans = False
    str1_list = sorted([x for x in s])
    str2_list = sorted([x for x in t])
    # Print sorted lists (for debugging)
    print("Sorted s:", str1_list)
    print("Sorted t:", str2_list)

    # Check if lengths are different
    if len(s) != len(t):
        return False

    if str1_list == str2_list:
        ans = True
    return ans

if __name__ == '__main__':
    #arr = [int(x) for x in input().split()]
    #res = find_duplicate(arr)
    res = isAnagram("tar","rat")
    print(res)
