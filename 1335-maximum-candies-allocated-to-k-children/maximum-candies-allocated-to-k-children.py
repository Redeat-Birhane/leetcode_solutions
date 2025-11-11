class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        low, high = 1, max(candies) + 1
        def checker(value):
            children = 0
            for candy in candies:
                children += candy // value
            return children >= k


        while low <= high:
            mid = (low + high) // 2
            if checker(mid):
                low = mid + 1
            else:
                high = mid - 1

        return high


        