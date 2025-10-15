class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.words = [] 

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        curr = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if curr.children[idx] is None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
            curr.words.append(word)
            curr.words.sort()
            if len(curr.words) > 3:
                curr.words.pop() 

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        products.sort()
        for product in products:
            self.insert(product)

        res = []
        curr = self.root
        for char in searchWord:
            idx = ord(char) - ord('a')
            if curr and curr.children[idx]:
                curr = curr.children[idx]
                res.append(curr.words)
            else:
                curr = None
                res.append([])

        return res
