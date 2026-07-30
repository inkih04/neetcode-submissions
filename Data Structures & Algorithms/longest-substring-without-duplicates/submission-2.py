class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = set()
        if not s:
            return 0
            
        characters.add(s[0])
        i = 0
        j = 1
        maxLength = 1 

        while j < len(s):
            if s[j] in characters:
                while s[i] != s[j]:
                    characters.remove(s[i])
                    i += 1
                characters.remove(s[i])
                i += 1
                characters.add(s[j])
               
            else:
                characters.add(s[j])
                maxLength = max(maxLength, j - i + 1)

            j += 1

        return maxLength
        
        