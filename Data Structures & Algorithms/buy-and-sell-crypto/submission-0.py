class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
      
        biggest = 0
        if len(prices) == 1:
            return 0
        for right in range(1, len(prices)):
            profit = prices[right] - prices[left]
            biggest = max(biggest, profit)
            if prices[right] < prices[left]:
                left = right;
        return biggest


        