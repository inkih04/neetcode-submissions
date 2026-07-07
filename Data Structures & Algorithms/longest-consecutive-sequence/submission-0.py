class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        temp = set(nums)
        maxSeq = 0

        for n in nums:
            if (n - 1) not in temp:
                length = 0
                while (n + length ) in temp:
                    length += 1
                    maxSeq = max(length, maxSeq)

        return maxSeq

        