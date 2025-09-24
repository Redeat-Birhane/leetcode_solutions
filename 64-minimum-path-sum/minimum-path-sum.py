class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        memo = {}
        def min_path(i, j):
            if i == n - 1 and j == m - 1:
                return grid[i][j]
            if i >= n or j >= m:
                return float("inf")
            if (i, j) not in memo:
                memo[(i,j)] = grid[i][j] + min(min_path(i + 1, j), min_path(i, j + 1))

            return memo[(i,j)]

        return min_path(0, 0)

                
