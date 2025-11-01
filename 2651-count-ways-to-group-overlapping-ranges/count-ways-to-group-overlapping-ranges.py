class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        ranges.sort()
        start, end = ranges[0]
        groups = 1
        for i in range(1, len(ranges)):
            curr_s, curr_e = ranges[i]
            if curr_s > end:
                groups += 1
                start, end = ranges[i]
            else:
                end = max(end, curr_e)

        return (2 ** groups) % MOD
            
        