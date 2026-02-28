class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def DP(step):
            if step == n:
                return 1
            if step > n:
                return 0

            if step not in memo:
                memo[step] = DP(step + 1) + DP(step + 2)

            return memo[step]


        return DP(0)