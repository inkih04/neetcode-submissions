class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post, out = [1] * (len(nums)), [1]*(len(nums)), [1] * (len(nums))
        static = 1

        for i, n in enumerate(nums):
            static = static  * n
            pre[i] = static

        static = 1
        for i in range(len(nums) -1, -1, -1):
            static = static * nums[i]
            post[i] = static
        
        for i in range(len(nums)):
            if i > 0 :
                out[i] = pre[i-1]
            
            if i + 1  < len(nums):
                out[i] = out[i] * post[i+1]
        return out