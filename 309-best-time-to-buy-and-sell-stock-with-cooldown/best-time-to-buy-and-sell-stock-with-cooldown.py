class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n, memo = len(prices), {}
        def max_p(i, last_transaction):
            if i >= n:
                return 0
            if (i, last_transaction) not in memo:
                if last_transaction == 0:
                    include = max_p(i + 2, 1) + prices[i]
                else:
                    include = max_p(i + 1, 0) - prices[i] 
                exclude = max_p(i + 1, last_transaction)
                memo[(i,last_transaction)] = max(include, exclude)
            return memo[(i,last_transaction)]

        return max_p(0, 1)
        