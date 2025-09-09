class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        m = len(requests)
        result = 0

        for mask in range(1 << m):
            balance = [0] * n
            count = 0

            for i in range(m):
                if mask & (1 << i):
                    frm, to = requests[i]
                    balance[frm] -= 1
                    balance[to] += 1
                    count += 1

            if all(x == 0 for x in balance):
                result = max(result, count)

        return result
