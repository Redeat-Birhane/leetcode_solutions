class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        low, high = 1, min(ranks) * cars ** 2
        def checker(time):
            count = 0
            for rank in ranks:
                count += floor(sqrt(time // rank))

            if count >= cars:
                return True

            return False

        while low <= high:
            mid = (low + high) // 2
            if checker(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low