class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(check, j):
            if sum(check) == target:
                ans.append(check[:])
                return
            if sum(check) > target:
                return 
            for i in range(j, len(candidates)):
                check.append(candidates[i])
                backtrack(check, i)
                check.pop()
                
        backtrack([], 0)
        return ans

        
        

        