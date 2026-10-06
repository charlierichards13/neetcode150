from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_map = defaultdict(list)
        result = []


        for s in strs:
            sorted_s = tuple(sorted(s))
            hash_map[sorted_s].append(s)

        for value in hash_map.values():
            result.append(value)

        return result




        