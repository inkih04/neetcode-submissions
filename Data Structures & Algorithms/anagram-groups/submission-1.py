class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = defaultdict(list)

        for w in strs:
            alphabet = [0] * 26

            for c in w:
                alphabet[ord(c) - ord('a')] += 1
            
            sol[tuple(alphabet)].append(w)
        return list(sol.values())            
        