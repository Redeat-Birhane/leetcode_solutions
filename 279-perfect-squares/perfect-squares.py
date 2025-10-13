class Solution:
    def numSquares(self, n: int) -> int:
        perfect_squares, dp = [], [inf] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            root = int(math.sqrt(i))
            if root * root == i:
                perfect_squares.append(i)

        for i in range(1, n + 1):
            for perfect_square in perfect_squares:
                if i >= perfect_square:
                    dp[i] = min(dp[i], dp[i - perfect_square] + 1)

        return dp[n]

        


        