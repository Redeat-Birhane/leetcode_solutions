class Solution:
    def grayCode(self, n: int) -> List[int]:
        decimals = [i for i in range(2 ** n)]
        result = []
        for decimal in decimals:
            result.append(decimal ^ (decimal >> 1))
        return result

        