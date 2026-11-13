class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        s = 0
        c = 0
        for i in range(k):
            s += arr[i]
        right = k -1
        while right < len(arr) - 1:
            if s/k >= threshold:
                c += 1
            s -= arr[left]
            s += arr[right + 1]
            left +=1
            right += 1
        if s/k >= threshold:
            c += 1
        return c
