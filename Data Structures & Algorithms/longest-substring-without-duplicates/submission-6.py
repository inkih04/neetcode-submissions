class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = set()
        i = 0
        j = 0
        maxLength = 0 

        while j < len(s):
            while s[j] in characters:
                characters.remove(s[i])
                i += 1

            characters.add(s[j])
            maxLength = max(maxLength, j - i + 1)
            j += 1

        return maxLength
        
        