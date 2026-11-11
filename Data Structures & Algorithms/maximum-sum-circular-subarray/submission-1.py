class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        left = 0
        maxSum = float('-inf')
        curr = 0
        totalSum = 0
        if len(nums) == 1:
            return nums[0]
        for i in range(0, len(nums)):
            totalSum += nums[i]
            curr += nums[i]
            maxSum = max(maxSum, curr)
            if curr < 0 and i < len(nums) - 1:
                left = nums[i + 1]
                curr = 0

        left = 1
        minSum = float('inf')
        curr = 0
    
        for i in range(1, len(nums) - 1):
            curr += nums[i]
            minSum = min(minSum, curr)
            if curr > 0:
                left = nums[i + 1]
                curr = 0
        print(minSum, totalSum)
        return max(totalSum - minSum, maxSum)
