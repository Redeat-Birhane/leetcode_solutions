class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        n, m = len(s1), len(s2)
        dp = [False] * (m + 1)

        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0 and j == 0:
                    dp[j] = True
                elif i == 0:
                    dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
                elif j == 0:
                    dp[j] = dp[j] and s1[i-1] == s3[i-1]
                else:
                    dp[j] = (dp[j] and s1[i-1] == s3[i+j-1]) or \
                            (dp[j-1] and s2[j-1] == s3[i+j-1])
        return dp[m]
