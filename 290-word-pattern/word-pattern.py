class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        seen = set()
        s = s.split()
        if len(s) != len(pattern):
            return False

        mapp = {}         
        rev_mapp = {}      

        for i in range(len(s)):
            c, w = pattern[i], s[i]

            if c in mapp and mapp[c] != w:
                return False
            if w in rev_mapp and rev_mapp[w] != c:
                return False

            mapp[c] = w
            rev_mapp[w] = c
            seen.add(c)  

        return True
