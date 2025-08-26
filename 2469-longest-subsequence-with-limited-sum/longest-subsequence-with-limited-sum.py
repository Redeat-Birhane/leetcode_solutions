class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        answer = []
        for q in queries:
            size = bisect_right(prefix_sum, q)
            answer.append(size)
        return answer

        