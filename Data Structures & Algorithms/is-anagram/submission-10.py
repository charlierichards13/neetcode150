class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #O(n log(n))
        #O(n)

        # cat
        # tac
        # act act

        # if len(s) != len(t):
        #     return False

        # if sorted(s) == sorted(t):
        #     return True
        # else: return False

        if len(s) != len(t):
            return False

        map_s = {}
        map_t = {}

        for i in range(len(s)):
            map_s[s[i]] = 1 + map_s.get(s[i], 0)
            map_t[t[i]] = 1 + map_t.get(t[i], 0)

        if map_s == map_t:
            return True
        else: 
            return False
