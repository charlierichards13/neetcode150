class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we have an array of integers, and we are looking to return an output of multiplication
        # excluding the index of i
        
        output = []
        # O(n)
        for i in range(len(nums)):
            prod = 1
            # O(n^2)
            for j in range(len(nums)):
                # skip i
                if (i != j):
                    prod *= nums[j]
            # write back array with product
            output.append(prod)

        return output
