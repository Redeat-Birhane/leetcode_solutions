class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def comb2(m):
            return m * (m - 1) // 2 if m >= 2 else 0
        
        total = comb2(n + 2)
        
        if n >= limit + 1:
            total -= 3 * comb2(n - limit + 1)
        
        if n >= 2 * limit:
            total += 3 * comb2(n - 2 * limit)
        
        if n >= 3 * limit + 1:
            total -= comb2(n - 3 * limit - 1)
        
        return total