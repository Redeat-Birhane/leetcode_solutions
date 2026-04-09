class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def mincost(idx):
            if idx >= len(cost):
                return 0

            if idx not in memo:
                memo[idx] = cost[idx] + min(mincost(idx + 1), mincost(idx + 2))

            return memo[idx]

        return min(mincost(0), mincost(1))
        