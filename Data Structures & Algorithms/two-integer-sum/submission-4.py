class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        map1 = {}  # we can store the value and index in map

        for i, n in enumerate(nums):
            map1[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in map1:
                if map1[diff] != i:
                    return [i, map1[diff]]
