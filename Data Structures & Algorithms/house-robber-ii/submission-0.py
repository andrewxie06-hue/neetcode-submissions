class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        if n == 3:
            return max(nums[0], max(nums[1], nums[2]))

        dp1 = [0] * (n-1)
        dp2 = [0] * (n-1)
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])
        dp2[0] = nums[1]
        dp2[1] = max(nums[2], nums[1])

        for i in range(2, n):
            if i == 2:
                dp1[i] = max(dp1[i-2] + nums[i], dp1[i-1])
            elif i == n - 1:
                dp2[i-1] = max(dp2[i-3] + nums[i], dp2[i-2])
                print(nums[i])
            else:
                dp1[i] = max(dp1[i-2] + nums[i], dp1[i-1])
                dp2[i-1] = max(dp2[i-3] + nums[i], dp2[i-2])
        print(dp1, dp2)
        return max(max(dp1[n-2], dp1[n-3]), max(dp2[n-2], dp2[n-3]))