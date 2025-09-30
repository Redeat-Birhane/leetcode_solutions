class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def edit_dis(i, j):
            if i >= len(word1) and j >= len(word2):
                return 0
            if i >= len(word1):
                return len(word2) - j 
            if j >= len(word2):
                return len(word1) - i
            if (i, j) not in memo:
                if word1[i] == word2[j]:
                    memo[(i, j)] = edit_dis(i + 1, j + 1)

                else:
                    rep = edit_dis(i + 1, j + 1) + 1
                    ins = edit_dis(i, j + 1) + 1
                    rem = edit_dis(i + 1, j) + 1
                    memo[(i, j)] = min(rep, rem, ins)

            return memo[(i, j)]

        return edit_dis(0, 0)
