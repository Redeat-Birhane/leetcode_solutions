class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo, n = {}, len(nums)
        def min_expressions(i, curr_amount):
            if i == n and curr_amount == target:
                return 1
            if i >= n:
                return 0
            if (i, curr_amount) not in memo:
                memo[(i, curr_amount)] = min_expressions(i + 1, curr_amount - nums[i]) + min_expressions(i + 1, curr_amount + nums[i])

            return memo[(i, curr_amount)]
        return min_expressions(0, 0)
        print(memo)  

        
            
        