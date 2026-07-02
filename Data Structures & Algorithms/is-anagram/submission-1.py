class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic= defaultdict(int)

        if len(s) != len(t):
            return False

        for c in s:
                dic[c] += 1

        for c in t:
            if not c in dic:
                return False
            else:
                dic[c] -= 1
                if dic[c] == 0:
                    dic.pop(c)
        
        if not dic:
            return True





        