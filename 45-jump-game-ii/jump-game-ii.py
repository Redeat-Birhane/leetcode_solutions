class Solution:
    def jump(self, nums: List[int]) -> int:
        curr_end, farthest = 0, 0
        jumps = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest,  i + nums[i])
            if i == curr_end:
                jumps += 1
                curr_end = farthest

        return jumps

                

                
        