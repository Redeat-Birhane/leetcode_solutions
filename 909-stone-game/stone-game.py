class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        def winner(idx, n):
            if idx == n:
                return piles[idx]
            if (idx, n) not in memo:
                memo[(idx, n)] = max(
                piles[idx] - winner(idx + 1, n), 
                piles[n] - winner(idx, n - 1)
                )     
            return memo[(idx, n)]


        return winner(0, len(piles) - 1) > 0

        
            