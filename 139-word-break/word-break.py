class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        memo = {}

        def dfs(start):
            if start == len(s):
                return True
            if start in memo:
                return memo[start]

            for word in word_set:
                if s.startswith(word, start):
                    if dfs(start + len(word)):
                        memo[start] = True
                        return True

            memo[start] = False
            return False

        return dfs(0)
