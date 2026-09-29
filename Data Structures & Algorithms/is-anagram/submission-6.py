class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        if len(t) != len(s):
            return False

        
        map_1 = {}

        map_2 = {}


        for i in range(len(t)):
            if t[i] in map_1:
                map_1[t[i]] += 1

            else:
                map_1[t[i]] = 1


        for i in range(len(s)):
            if s[i] in map_2:
                map_2[s[i]] += 1

            else:
                map_2[s[i]] = 1


        if map_1 == map_2:
            return True
        else:
            return False
