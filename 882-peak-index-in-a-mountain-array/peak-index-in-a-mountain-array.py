class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        #This is a mountain array(first strictly increases and then strictly decreases)
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] < arr[mid + 1]:# peak is on the right
                low = mid + 1
            else:
                high = mid - 1 # peak is on the left

        return low


        