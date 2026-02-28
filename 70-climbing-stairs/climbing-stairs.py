class Solution:
    def climbStairs(self, n: int) -> int:
        x, y = 0, 1
        for i in range(n):
            temp = x + y
            x, y = y, temp

        return temp
