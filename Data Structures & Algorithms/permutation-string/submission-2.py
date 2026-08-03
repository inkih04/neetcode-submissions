class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        dic = {}

        for c in s1:
            if not c in dic:
                dic[c] = 1
            else:
                dic[c] += 1

        i = 0
        j = 0
        dic2 = defaultdict(int)

        while j < len(s2):
            dic2[s2[j]] += 1

            if j - i + 1 == len(s1):
                if dic ==  dic2:
                    return True

                dic2[s2[i]] -= 1
                if dic2[s2[i]] == 0:
                    del dic2[s2[i]]
            
                i += 1
                    

            j += 1

        return False
            
        