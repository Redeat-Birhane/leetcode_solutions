class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans = letters[0]
        for i in range(len(letters)):
            letters[i] = ord(letters[i])
        letters.sort()
        curr = bisect.bisect_right(letters, ord(target))
        if curr < len(letters):
            return chr(letters[curr])

        return ans


        