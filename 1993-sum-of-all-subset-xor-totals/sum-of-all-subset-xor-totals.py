class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = 2 ** (len(nums) - 1)
        or_all = 0
        for num in nums:
            or_all |= num

        return or_all * subsets