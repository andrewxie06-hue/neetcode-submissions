class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left = 0
        maxSum = float('-inf')
        curr = 0
        if len(nums) == 1:
            return nums[0]
        for i in range(0, len(nums)):
            curr += nums[i]
            maxSum = max(maxSum, curr)
            if curr < 0 and i < len(nums) - 1:
                left = nums[i + 1]
                curr = 0
                

        return maxSum


        