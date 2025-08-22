class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x, n):
            if n == 0:
                return 1
            res = pow(x, n // 2)
            if n % 2 == 0:
                return res * res
            else:
                return res * res * x
        ans = pow(x, abs(n))
        return 1 / ans if n < 0 else ans
       
    

        