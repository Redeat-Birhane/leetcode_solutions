class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #using bottom-up(tabulation) approach
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]

        