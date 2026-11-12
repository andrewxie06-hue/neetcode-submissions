class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
    
        d = {}
        for right in range(len(nums)):
            if right - left > k:
                d[nums[left]] -= 1
                left += 1
            if d.get(nums[right], 0) > 0:
                return True
            d[nums[right]] = d.get(nums[right], 0) + 1
        return False


         