class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        prime_factors = set()
        for num in nums:
            while num % 2 == 0:
                prime_factors.add(2)
                num //= 2

            i = 3
            while i * i <= num:
                while num % i == 0:
                    prime_factors.add(i)
                    num //= i

                i += 2

            if num > 2:
                prime_factors.add(num)

        return len(prime_factors)
        