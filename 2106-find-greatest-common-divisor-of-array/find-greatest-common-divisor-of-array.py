class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minn, maxx = min(nums), max(nums)
        def primeFact(num):
            factorization = defaultdict(int)
            d = 2
            while d * d <= num:
                while num % d == 0:
                    factorization[d] += 1
                    num //= d

                d += 1

            if num > 1:
                factorization[num] += 1

            return factorization

        min_fact = primeFact(minn)
        max_fact = primeFact(maxx)
        prime_factors = []
        for prime in min_fact:
            if prime in max_fact:
                prime_factors.append((prime, min(min_fact[prime], max_fact[prime])))

        if len(prime_factors) == 0:
            return 1

        answer = 1
        for i, j in prime_factors:
            answer *= (i ** j)

        return answer




        