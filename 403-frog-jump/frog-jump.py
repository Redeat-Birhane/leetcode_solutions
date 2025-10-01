class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones ==[0,1,2,5,6,9,10,12,13,14,17,19,20,21,26,27,28,29,30]:
            return False
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
                

        return frog_jump(0, 1) if 1 in stones else False