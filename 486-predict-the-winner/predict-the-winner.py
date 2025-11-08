class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        n = len(nums)
        
        
        memo = {}
        
        def dp(i, j):
            if i == j:
                return nums[i]
            if (i, j) in memo:
                return memo[(i, j)]
            
          
            pick_left = nums[i] - dp(i+1, j)
            pick_right = nums[j] - dp(i, j-1)
            memo[(i, j)] = max(pick_left, pick_right)
            return memo[(i, j)]
        
        
        return dp(0, n-1) >= 0
