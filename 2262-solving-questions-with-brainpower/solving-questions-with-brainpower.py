class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = {}
        def brainPower(idx):
            if idx >= len(questions):
                return 0
            if idx not in memo:
                memo[idx] = max(questions[idx][0] + brainPower(idx + questions[idx][1] + 1), brainPower(idx + 1))

            return memo[idx]

        return brainPower(0)

        