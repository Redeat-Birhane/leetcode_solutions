class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[-1] * (n + 1) for _ in range(n + 1)]

        def dp(i, last_index):
            if i == n:
                return 0

            if memo[i][last_index + 1] == -1:
                exclude = dp(i + 1, last_index)

                include = 0
                if last_index == -1 or nums[last_index] < nums[i]:
                    include = 1 + dp(i + 1, i)

                memo[i][last_index + 1] = max(exclude, include)

            return memo[i][last_index + 1]

        return dp(0, -1)
