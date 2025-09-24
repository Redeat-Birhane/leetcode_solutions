class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def unique_path(i, j):
            if i == m - 1 or j == n - 1:
                return 1
            if (i, j) not in memo:
                memo[(i, j)] = unique_path(i + 1, j) + unique_path(i, j + 1)
            return memo[(i, j)]

        return unique_path(0, 0)
            