class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        result = [-1] * (len(intervals))
        sorted_starts = sorted((intervals[i][0], i) for i in range(len(intervals)))
        starts = [start[0] for start in sorted_starts]
        for i , (start, end) in enumerate(intervals):
            idx = bisect.bisect_left(starts, end)
            if idx < len(intervals):
                result[i] = sorted_starts[idx][1]

        return result