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

        hash_map = {}

        for i in range(len(s)):
            hash_map[s[i]] =  1 + hash_map.get(s[i], 0)
            hash_map[t[i]] = hash_map.get(t[i], 0) -1

        if all(value == 0 for value in hash_map.values()):
            return True
        else:
            return False

