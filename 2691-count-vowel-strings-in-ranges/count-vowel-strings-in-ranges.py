class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set("aeiou")

        is_vowel_word = [1 if word[0] in vowels and word[-1] in vowels else 0 for word in words]
        n = len(words)
        prefix = [0] * n
        prefix[0] = is_vowel_word[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] + is_vowel_word[i]

        ans = []
        for l, r in queries:
            if l == 0:
                ans.append(prefix[r])
            else:
                ans.append(prefix[r] - prefix[l-1])
        
        return ans
