class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo, n = {}, len(coins)
        def few_coins(i, rem_amount):
            if i >= n:
                return float("inf")
            if rem_amount == 0:
                return 0
            if (i, rem_amount) not in memo:
                include = float("inf")
                if rem_amount >= coins[i]:
                    include = 1 + few_coins(i, rem_amount - coins[i])
                exclude = few_coins(i + 1, rem_amount)
                memo[(i, rem_amount)] = min(exclude, include)
            return memo[(i, rem_amount)]

        ans = few_coins(0, amount)
        return ans if ans != float("inf") else -1
        

        