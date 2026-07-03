class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = []
        for w in strs:
            
            found = False
            for i, checkedWord in enumerate(sol):
                if len(w) == len(checkedWord[0]) and self.checkSameChars(w, checkedWord[0]):
                    sol[i].append(w)
                    found = True
                    break
            if not found:
                sol.append([w])

        return sol
            
    
    def checkSameChars(self, w1, w2):
        s = defaultdict(int)
        for c in w1:
            s[c] += 1

        for c in w2:
            if not c in s or s[c] == 0:
                return False
            s[c] -= 1
        
        return True
            
        