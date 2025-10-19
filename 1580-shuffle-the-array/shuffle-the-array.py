class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        l, r = 0, n
        while l <= n - 1 and r < len(nums):
            res.append(nums[l])
            res.append(nums[r])
            l += 1
            r += 1

        return res
        