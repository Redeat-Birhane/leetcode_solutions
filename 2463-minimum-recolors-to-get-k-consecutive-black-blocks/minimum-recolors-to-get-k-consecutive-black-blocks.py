class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        intial_blocks = deque(blocks[0:k])
        min_ops = sum([1 for block in intial_blocks if block == "W"])
        ans = min_ops
        for i in range(k, len(blocks)):
            popped = intial_blocks.popleft()
            if popped == "W":
                min_ops -= 1
            intial_blocks.append(blocks[i])
            if intial_blocks[-1] == "W":
                min_ops += 1
            ans = min(ans, min_ops)
        return ans
            
            
        