class Solution:
    def countVowels(self, word: str) -> int:
        #(i+1)×(n−i) a general combinatory formula to calculate substrings
        vowels = {'a', 'e', 'i', 'o', 'u'}
        res = 0
        for i, char in enumerate(word):
            if char in vowels:
                res += (i + 1) * (len(word) - i)

        return res
        