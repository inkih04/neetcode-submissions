class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        sol = [ [] for i in range(len(nums) + 1)]

        for n in nums:
            dic[n] += 1

        for key, n in dic.items():
            sol[n].append(key)

        res = []

        for s in sol[::-1]:
            for ss in s:
                res.append(ss)
                if len(res) == k:
                    return res





            
        