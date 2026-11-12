class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows = 0
        i = 1
        num = n
        while num >= i:
            num -= i
            rows += 1
            i += 1
        
        return rows