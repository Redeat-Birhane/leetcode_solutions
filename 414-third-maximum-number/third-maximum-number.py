class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = sorted(set(nums))
        if len(n) >= 3:
            return n[-3]
        else:
            return max(n)