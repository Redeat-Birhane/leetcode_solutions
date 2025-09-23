class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n, memo = len(nums), {}
        def robber(idx):
            if idx == len(nums) - 1:
                return nums[idx]
            if idx == len(nums) - 2:
                return max(nums[idx], nums[idx + 1])
            if idx not in memo:
                memo[idx] = max(nums[idx] + robber(idx + 2), robber(idx + 1))
            return memo[idx]
        ans1 = robber(1)
        memo = {}
        nums.pop()
        ans2 = robber(0)
        return max(ans1, ans2)

        