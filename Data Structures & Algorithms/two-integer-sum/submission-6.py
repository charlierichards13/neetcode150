class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        nut_sak = {} # 3:0 


        for index, value in enumerate(nums):

            difference = target - value

            if difference in nut_sak:
                return [nut_sak[difference], index]

                
            nut_sak[value] = index
