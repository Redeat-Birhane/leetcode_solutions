class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        memo, MOD = {}, 10 ** 9 + 7
        def ways(val, steps):
            if steps == 0 :
                if val == endPos:
                    return 1
                return 0

            if (val, steps) not in memo:
                memo[(val, steps)] = ways(val - 1, steps - 1) + ways(val + 1, steps - 1)
            return memo[(val, steps)]

        
        return ways(startPos, k) % MOD
        