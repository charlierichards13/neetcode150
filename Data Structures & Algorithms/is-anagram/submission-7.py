class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_1 = {}
        hash_2 = {}


        if len(s) != len(t):
            return False


        for i in range(len(s)):
            if s[i] in hash_1:
                hash_1[s[i]] += 1
            else:
                hash_1[s[i]] = 1

        for i in range(len(t)):
            if t[i] in hash_2:
                hash_2[t[i]] += 1
            else:
                hash_2[t[i]] = 1


        if hash_1 == hash_2:
            return True
        else:
            return False
