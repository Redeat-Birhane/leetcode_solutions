class Solution:
    def countGood(self, nums: list[int], k: int) -> int:
        n = len(nums)
        count = defaultdict(int)
        total_pairs = 0
        left = 0
        res = 0
        
        for right in range(n):
            total_pairs += count[nums[right]]  
            count[nums[right]] += 1
            
            while total_pairs >= k:
                count[nums[left]] -= 1
                total_pairs -= count[nums[left]]
                left += 1
            
            res += left
        
        return res
