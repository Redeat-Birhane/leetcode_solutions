class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        roots, res = set(dictionary), ""
        sentence = list(sentence.split())
        for word in sentence:
            curr, l = "", 0
            while curr not in roots and l < len(word):
                curr += word[l]
                l += 1
            curr += " "
            res += curr

        return res[:-1]
        

        




        