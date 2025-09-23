class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum= sum(nums)
        if total_sum % 2:
            return False
        target, memo = total_sum // 2, {}
        def dp(i, curr_sum):
            if curr_sum  == 0:
                return True
            if i >= len(nums) or curr_sum < 0:
                return False
            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]
            memo[(i, curr_sum)] = dp(i + 1, curr_sum - nums[i]) or dp(i + 1, curr_sum)
            return memo[(i, curr_sum)]

        return dp(0, target)
        
        
                                                            
        