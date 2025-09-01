class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        def is_zero_after_k_queries(k: int) -> bool:
            diff = [0] * (n + 1)
            for i in range(k):
                l, r, val = queries[i]
                diff[l] += val
                if r + 1 < n:
                    diff[r + 1] -= val

            total_decrement = [0] * n
            curr = 0
            for i in range(n):
                curr += diff[i]
                total_decrement[i] = curr

            for i in range(n):
                if nums[i] > total_decrement[i]:
                    return False
            return True

        left, right = 0, len(queries)
        answer = -1
        while left <= right:
            mid = (left + right) // 2
            if is_zero_after_k_queries(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer