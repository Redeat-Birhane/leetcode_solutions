class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #using bottom-up(tabulation) approach
        # dp = [[1] * n for _ in range(m)]
        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # return dp[m-1][n-1]
        #using top_down(memoizaton + recursion) approach
        memo = {}
        def dfs(i, j):
            if i == m or j == n:
                return 0
            if i == m - 1 and j == n - 1:
                return 1

            if (i, j) in memo:
                return memo[(i, j)]

            memo[(i, j)] = dfs(i + 1, j) + dfs(i, j + 1)
            return memo[(i,j)]

        return dfs(0, 0)



        