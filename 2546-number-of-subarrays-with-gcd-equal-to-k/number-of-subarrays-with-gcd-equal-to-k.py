class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        
        for i in range(n):
            curr_gcd = 0
            for j in range(i, n):
                curr_gcd = gcd(curr_gcd, nums[j])
                if curr_gcd == k:
                    count += 1
                elif curr_gcd < k:
                    break  
        
        return count
