class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = set()
        i = 0
        maxLength = 0 

        for j, c  in enumerate(s):
            while c in characters:
                characters.remove(s[i])
                i += 1

            characters.add(c)
            maxLength = max(maxLength, len(characters))

        return maxLength
        
        