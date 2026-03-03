class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def house_robber(index):
            if index >= len(nums):
                return 0
            if index not in memo:
                rob = nums[index] + house_robber(index + 2)
                not_rob = house_robber(index + 1)
                memo[index] = max(rob, not_rob)

            return memo[index]

        return house_robber(0)
            
