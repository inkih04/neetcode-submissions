class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = 0
        freq = defaultdict(int)
        maxOutput = 0

        while j < len(s):
            
            freq[s[j]] += 1
            mostFreq = self.getMostFreq(freq)
            windowRange = j - i + 1
            while windowRange - mostFreq > k:
                freq[s[i]] -= 1 
                i += 1
                mostFreq = self.getMostFreq(freq)
                windowRange = j - i + 1
                
            maxOutput = max(maxOutput, j - i + 1)
            
            j += 1
            
        
        return maxOutput
    
    def getMostFreq(self, freq):
        mostFreq = 0
        for v in freq.values():
            mostFreq = max(v, mostFreq)
        
        return mostFreq

        