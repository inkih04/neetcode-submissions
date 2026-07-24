class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        i = 1
        j = piles[-1]
        k = piles[-1]

        while i <= j:
            valid = True
            time = h
            m = (i + j) // 2
            for banana in piles:
                time =  time - math.ceil(banana / m)
                if time < 0:
                    valid = False 
                    i = m + 1
                    break

            if valid:
                k = min(k, m)
                j = m - 1
                
        return k



