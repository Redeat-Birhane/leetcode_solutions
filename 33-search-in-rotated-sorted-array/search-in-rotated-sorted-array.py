class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low, high = 0, n - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        pivot = low


        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            real_mid = (mid + pivot) % n  
            if nums[real_mid] == target:
                return real_mid
            elif nums[real_mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1
