class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        staticDict = defaultdict(int)
        for c in t:
            staticDict[c] += 1

        need = len(staticDict)
        have = 0

        mutableDict = defaultdict(int)
        
        lengthWindow = len(s) + 1
        bi, bj = -1, -1

        i = 0
        for j in range(len(s)):
            char_right = s[j]
            mutableDict[char_right] += 1

            if char_right in staticDict and mutableDict[char_right] == staticDict[char_right]:
                have += 1

            while have == need:
                if (j - i + 1) < lengthWindow:
                    lengthWindow = j - i + 1
                    bi = i
                    bj = j

                char_left = s[i]
                mutableDict[char_left] -= 1
                
                if char_left in staticDict and mutableDict[char_left] < staticDict[char_left]:
                    have -= 1
                
                i += 1  

        if bi == -1:
            return ""
            
        return s[bi:bj + 1]