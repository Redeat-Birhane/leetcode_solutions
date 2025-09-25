class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [-1] * len(s)
        def wordBreak(i):
            if i == len(s):
                return True
            if i > len(s):
                return False
            if memo[i]== -1:
                memo[i]= False
                for j in range(i, len(s)):
                    curr_word = s[i: j +1]
                    if curr_word in wordDict:
                        memo[i] = memo[i] or wordBreak(j + 1)
            return memo[i]

        return wordBreak(0)


                

        