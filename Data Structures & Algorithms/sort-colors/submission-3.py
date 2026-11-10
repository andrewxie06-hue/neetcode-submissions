class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i , j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        left = 0
        right = len(nums) - 1
        i = 0
        while i <= right:
            if nums[i] == 0:
                swap(i, left)
                left += 1
                
            elif nums[i] == 2:
                swap(i, right)
                i -= 1
                right -= 1
            i+= 1