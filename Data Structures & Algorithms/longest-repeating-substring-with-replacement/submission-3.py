class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = {}
        freq[s[0]] = 1
        max_window = 1
        window_size = 0
        for right in range(1 , len(s)):
            window_size = right - left + 1
            freq[s[right]] = freq.get(s[right], 0) + 1
           
            if window_size - max(freq.values()) <= k:
                max_window = max(max_window, window_size)
            else:
                while(right - left + 1) - max(freq.values()) > k:
                    freq[s[left]] -= 1
                    left += 1
            
        return max_window



        