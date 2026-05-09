from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        
        int_map = defaultdict(int)
        
        #result = []

        for i in nums:
            int_map[i] += 1
            #result.append(i)
        


            if (int_map[i] > 1):
                return True
        else:
            return False