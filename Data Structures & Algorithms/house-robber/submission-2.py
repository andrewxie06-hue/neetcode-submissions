class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        curr = 0
        prev1 = max(nums[0], nums[1])
        prev2 = nums[0]
        for i in range(2, n):
            curr = max(nums[i] + prev2, prev1)

            prev2 = prev1
            prev1 = curr
        return max(prev2, prev1)