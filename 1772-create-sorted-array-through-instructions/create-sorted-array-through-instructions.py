class Solution:
    def createSortedArray(self, instructions: list[int]) -> int:
        MOD = 10**9 + 7
        
        sorted_unique = sorted(set(instructions))
        rank = {v: i+1 for i, v in enumerate(sorted_unique)}  
        size = len(sorted_unique) + 2
        
     
        bit = [0] * size
        
        def update(i):
            while i < size:
                bit[i] += 1
                i += i & -i
        
        def query(i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res
        
        cost = 0
        for idx, val in enumerate(instructions):
            r = rank[val]
            left = query(r - 1)
            right = idx - query(r)
            cost += min(left, right)
            update(r)
        
        return cost % MOD
