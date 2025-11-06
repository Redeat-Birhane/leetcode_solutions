class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        mod = total % p
        if mod == 0:
            return 0

        prefix_mod = 0
        store = {0: -1}
        res = len(nums)

        for i, num in enumerate(nums):
            prefix_mod = (prefix_mod + num) % p
            target = (prefix_mod - mod) % p
            if target in store:
                res = min(res, i - store[target])
            store[prefix_mod] = i

        return res if res < len(nums) else -1
