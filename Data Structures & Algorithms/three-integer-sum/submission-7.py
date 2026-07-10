class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        j = len(nums) - 1
        k = 0
        solution = []

        nums.sort()

        for k, n in enumerate(nums):
            j =  len(nums) - 1
            i  = k + 1

            if n > 0:
                break

            if k > 0 and  nums[k] == nums[k -1]:
                continue

            while i < j:
                if nums[i] + nums[j] == -nums[k]:
                    solution.append([nums[i], nums[j], nums[k]])
                    i += 1
                    while i < j and nums[i] == nums[i-1]:
                        i+=1

                    j -= 1
                    while i < j and nums [j] == nums[j+1]:
                        j -= 1
                    continue

                if (nums[i] + nums[j]) < -nums[k]:
                    i += 1
                    continue
                if (nums[i] + nums[j]) > -nums[k]:
                    j -= 1
                    continue

        return solution



        
        