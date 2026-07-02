class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicateArray = set()
        for n in nums:
            if n in duplicateArray:
                return True
            duplicateArray.add(n)

        return False 
        