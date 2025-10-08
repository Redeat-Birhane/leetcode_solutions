class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        factorization = defaultdict(int)
        d = 2
        while d * d <= n:
            while n % d == 0:
                factorization[d] += 1
                n //= d
            d += 1
        if n > 1:
            factorization[n] += 1

        for key in factorization.keys():
            if key !=  2 and key != 5 and key != 3:
                return False
        return True