class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dp(num):
            if num in memo:
                return memo[num]
            if num == len(nums) - 1:
                return nums[num]
            if num == len(nums) - 2:
                return max(nums[num], nums[num + 1])
            memo[num] = max(nums[num] + dp(num + 2), dp(num + 1))
            return memo[num]
        return dp(0)
            

        