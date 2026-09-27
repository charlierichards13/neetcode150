class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        

        solution = set()

        for n in nums:
            if n in solution:
                return True
            else:
                solution.add(n)

        return False