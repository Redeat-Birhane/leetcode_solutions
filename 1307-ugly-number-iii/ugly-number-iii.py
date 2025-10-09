class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def LCM(a,b):
            return (a * b) // math.gcd(a, b)

        ab = LCM(a, b)
        ac = LCM(a, c)
        bc = LCM(b, c)
        abc = LCM(ab, c)

        def count(num):
            return num // a + num // b + num // c - num // ab - num // ac - num // bc + (num // abc)

        low, high, answer = 1, 2 * (10 ** 9), -1
        while low <= high:
            mid = (low + high) // 2
            if count(mid) < n:
                low = mid + 1

            else:
                answer = mid
                high = mid - 1
            

        return answer



        