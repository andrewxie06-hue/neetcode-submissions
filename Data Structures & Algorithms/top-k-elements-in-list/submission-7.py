class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}
        ans = []
        for i in range(len(nums)):
            table[nums[i]] = table.get(nums[i], 0) + 1
        lists = [[] for row in range(len(nums) + 1)]
        for number, count in table.items():
            lists[count].append(number)
        ite = 0
        for i in range(len(lists) - 1, 0, -1):
            if len(lists[i]) == 0:
                continue
            else:
                ans.extend(lists[i])
                ite += len(lists[i])
            if ite == k:
                break

        return ans