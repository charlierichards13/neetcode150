class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        map_s = {}

        map_t = {}


        for i in range(len(s)):
            if s[i] in map_s:
                map_s[s[i]] += 1

            else:

                map_s[s[i]] = 1

        for i in range(len(t)):
            if t[i] in map_t:
                map_t[t[i]] += 1

            else:

                map_t[t[i]] = 1


        if map_s == map_t:
            return True
        else:
            return False