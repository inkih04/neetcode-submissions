class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1

        while i <= j:
            m = (i + j) // 2
            
            if nums[m] == target:
                return m
                                                       
            if nums[i] <= nums[m]:
                if  nums[m] >= target >= nums[i]:
                    j = m - 1
                else:
                    i = m + 1
            else:
                if nums[j] >= target >= nums[m]:
                    i = m + 1
                else:
                    j = m - 1


        return -1