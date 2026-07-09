class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = defaultdict(int)

        for i, n in enumerate(numbers):
            if target - n in dic:
                return [dic[target-n] +1, i + 1 ]
            dic[n] = i
        
        return [-1, -1]

        