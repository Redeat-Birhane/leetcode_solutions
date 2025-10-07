class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        frequencies = [0] * k
        for n in arr:
            frequencies[n % k] += 1

        if k % 2 == 0 and frequencies[k//2] % 2 == 1:
            return False
        for i in range(1,len(frequencies)):
            if frequencies[i] != frequencies[(-i) % k]:
                return False

        return True
        # Two numbers are additive inverse of eachother if the module of their sum is 0
        # the additive inverse of a is (-a) % k
            
        