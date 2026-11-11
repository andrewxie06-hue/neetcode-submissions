class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        center = 0
        maxlen = 0
        res = ""
        for i in range(len(s)):
            left = i -1
            right = i + 1
            pal = s[i]
            while left >= 0 and right < len(s) and s[left] == s[right]:
                pal = s[left] + pal + s[right]
                left -= 1
                right += 1
            if len(pal) > maxlen:
                res = pal
                maxlen = len(pal)
            if i < len(s) - 1:
                left = i
                right = i + 1
            else:
                continue
            pal = ""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                pal = s[left] + pal + s[right]
                left -= 1
                right += 1
        
            if len(pal) > maxlen:
                res = pal
                maxlen = len(pal)
        return res
                    
