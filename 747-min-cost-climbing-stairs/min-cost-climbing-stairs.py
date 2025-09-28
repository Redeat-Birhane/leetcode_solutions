class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo, n = {}, len(cost)
        def min_cost(i):
            if i >= n:
                return 0
            if i not in memo:
                memo[i] = cost[i] + min(min_cost(i + 1), min_cost(i + 2))

            return memo[i]

        return min(min_cost(0), min_cost(1))

            
        