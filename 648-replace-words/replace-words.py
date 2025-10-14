class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        def insert(word):
            curr = self.root
            for char in word:
                idx = ord(char) - ord('a')
                if curr.children[idx] is None:
                    curr.children[idx] = TrieNode()
                curr = curr.children[idx]
            curr.is_end = True

    
        def search(word):
            curr, res = self.root, ""
            for char in word:
                idx = ord(char) - ord('a')
                if curr.children[idx] is None:
                    return word  
                res += char
                curr = curr.children[idx]
                if curr.is_end:
                    return res
            return word  

        for word in dictionary:
            insert(word)

        replaced_words = [search(word) for word in sentence.split()]
        return " ".join(replaced_words)
