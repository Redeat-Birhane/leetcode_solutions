class Solution:
    def canCross(self, stones: List[int]) -> bool:
        memo = {}
        last_pos, stones = stones[-1], set(stones)
        def frog_jump(pos, last_jump):
            if pos == last_pos:
                return True
            if (pos, last_jump) not in memo:
                for jump in [last_jump - 1, last_jump, last_jump + 1]:
                    if jump > 0 and pos + jump in stones: # checking if jump > o avoids infinite loop
                        if frog_jump(pos + jump, jump):
                            memo[(pos, last_jump)] = True
                            return True

                memo[(pos, last_jump)] = False
                return False
                

        return frog_jump(0, 0) # the current position and the jump i used to reach to this position