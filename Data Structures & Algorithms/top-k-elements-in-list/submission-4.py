class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}
        ans = []
        for i in range(len(nums)):
            table[nums[i]] = table.get(nums[i], 0) + 1
        table = sorted(table.items(), key=lambda num : -num[1])
        for i in range(k):
            ans.append(table[i][0])
        return ans