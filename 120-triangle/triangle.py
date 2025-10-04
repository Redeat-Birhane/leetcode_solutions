class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        def dfs(i, j):
            if i == len(triangle) - 1:
                return triangle[i][j]
            if (i, j) not in memo:
                left = dfs(i + 1, j)
                right = dfs(i + 1, j + 1)
                memo[(i, j)] = triangle[i][j] + min(left, right)
            return memo[(i, j)]
        return dfs(0, 0)
