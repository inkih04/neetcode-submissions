class Solution:
    def search(self, nums: List[int], target: int) -> int:
        j = len(nums) - 1
        return self.binarySearch(nums, 0, j, target)

    
    def binarySearch(self, nums, i, j, target):
        m = int((i + j) / 2)

        if i > j:
            return -1

        if nums[m] == target:
             return m
        elif i == j:
            return -1


        if nums[m] > target:
             return self.binarySearch(nums, i, m - 1, target)
        else:
             return self.binarySearch(nums, m + 1, j, target)
        