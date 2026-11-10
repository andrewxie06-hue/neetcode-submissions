class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        length = 1
        last_seen = {}
       
        if len(s) == 1:
            return 1
        elif len(s) == 0:
            return 0
        last_seen[s[0]] = 0

        for right in range(1, len(s)):
            if s[right] in last_seen and last_seen[s[right]] >= left:
                length = max(length, right - left)
                
                left = last_seen[s[right]] + 1
            last_seen[s[right]] = right
          
        length = max(length, len(s) - left)

        return length

            
            


