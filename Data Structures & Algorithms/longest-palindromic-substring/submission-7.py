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
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if len(s[left+1:right]) > maxlen:
                res = s[left+1:right]
                maxlen = len(s[left+1:right])
            if i < len(s) - 1:
                left = i
                right = i + 1
            else:
                continue
      
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
        
            if len(s[left+1:right]) > maxlen:
                res = s[left+1:right]
                maxlen = len(s[left+1:right])
        return res
                    
