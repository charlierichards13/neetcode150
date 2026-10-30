class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_s = set()

        l = 0
        result = 0

        for r in range(len(s)):
            while s[r] in longest_s:
                longest_s.remove(s[l])
                l+=1
            longest_s.add(s[r])
            result = max(result, r - l + 1)

        return result