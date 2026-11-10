class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        freq = {}
        freq2 = {}
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            freq[s1[i]] = freq.get(s1[i], 0) + 1
            freq2[s2[i]] = freq2.get(s2[i], 0) + 1
        print(freq, freq2)
        for right in range(len(s1), len(s2)):
            if freq == freq2:
                return True
           
            freq2[s2[left]] -= 1
            if freq2[s2[left]] == 0:
                del freq2[s2[left]]
            left += 1
            freq2[s2[right]] = freq2.get(s2[right], 0) + 1
            print(freq2)
            
            
        return freq == freq2

