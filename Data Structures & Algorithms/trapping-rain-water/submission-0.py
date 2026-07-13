class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        maxArea = 0

        for i in range(len(height)):
            if i == 0:
                continue
            maxLeft[i] = max(maxLeft[i - 1], height[i - 1])
        
        i = len(height) - 2
        while i >= 0:
            maxRight[i] = max(height[i + 1], maxRight[i+1]) 
            i -= 1

        for i, h in enumerate(height):
            maxArea += max(min(maxLeft[i], maxRight[i]) - h , 0) 


        return maxArea