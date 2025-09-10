class Solution:
    def minimumSteps(self, s: str) -> int:
        s=list(s)
        swaps=0
        black_count=0
        for i in range(len(s)-1,-1,-1):
            if s[i]=="0":
                black_count+=1
            else:
                swaps+=black_count
        return swaps


        
        