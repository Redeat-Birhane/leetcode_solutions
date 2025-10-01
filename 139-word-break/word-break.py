class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def word(idx):
            if idx >= len(s):
                return True

            if idx not in memo:
                for i in range(idx, len(s)):
                    if s[idx:i + 1] in wordDict:
                        if word(i + 1):
                            memo[idx] = True
                            return True
                memo[idx] = False
                return False
            
        return word(0)

        