class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        output = min(nums[0], nums[-1])

        while i <= j:
            m = (i + j) // 2
            output = min(output, nums[m])
            
            if nums[m] < nums[j]:
                j = m - 1 
            else:
                i = m + 1

        return output


        