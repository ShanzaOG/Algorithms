# Count unhappy friends

from typing import List

class Solution:
    def unhappyFriends(self, n:int, preferences:List[List[int]], pairs: List[List[int]])->int:
        preference_rankings = [{friend: rank for rank, friend in enumerate(prefs)} for prefs in preferences]

        #Create a dictionary to store each person's friend.
        paired_friends = {}
        for x, y in pairs:
            paired_friends[x] = y
            paired_friends[y] = x

        # Initialize the count for unhappy friends
        unhappy_count = 0

        # Iterate through eah person to determine if they are unhappy
        for x in range (n):
            # the paired friend of 'x'
            y = paired_friends[x]

            # check if there exists a person 'u' who is better preference for 'x'
            # than 'x's paired friend 'y'. We do this by checking the preference
            # rankings in the subset of preference before 'y'
            is_unhappy = any(
                preference_rankings[u][x] < preference_rankings[u][paired_friends[u]]
                for u in preferences[x][:preference_rankings[x][y]]
            )

            if is_unhappy:
                unhappy_count += 1

        return unhappy_count
