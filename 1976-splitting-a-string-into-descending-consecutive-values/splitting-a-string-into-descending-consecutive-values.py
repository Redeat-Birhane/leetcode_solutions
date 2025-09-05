class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        
        def dfs(idx, prev):
            if idx == n:
                return True
            for j in range(idx+1, n+1):
                num = int(s[idx:j])
                if num == prev - 1:
                    if dfs(j, num):
                        return True
    
                if num > prev - 1:
                    break
            return False
        
        for i in range(1, n):
            num = int(s[:i])
            if dfs(i, num):
                return True
        return False