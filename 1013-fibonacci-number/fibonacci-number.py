class Solution:
    memo = {}
    def fib(self, n: int) -> int:
        if n not in self.memo:
            if n == 0:
                return 0

            if n == 1:
                return 1

            self.memo[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.memo[n]
        
