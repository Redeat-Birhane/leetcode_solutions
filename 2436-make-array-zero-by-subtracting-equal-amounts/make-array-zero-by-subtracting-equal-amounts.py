class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums = [num for num in nums if num != 0]
        if not nums:
            return 0
        minn, maxx = min(nums), max(nums)
        ops = 0
        while maxx > 0:
            for i in range(len(nums)):
                nums[i] -= minn
            ops += 1
            nums = [num for num in nums if num != 0]  
            if not nums:
                break
            minn, maxx = min(nums), max(nums)

            

        return ops

        