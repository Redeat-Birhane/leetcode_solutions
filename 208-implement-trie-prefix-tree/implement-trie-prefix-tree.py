
class TrieNode:
    def __init__(self):
        self.end = False
        self.children = [ None for _ in range(26) ]
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            idx = ord(c) - ord("a")
            if curr.children[idx] == None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]

        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            idx = ord(c) - ord("a")
            if curr.children[idx] == None:
                return False
            curr = curr.children[idx]
        if curr.end == True:
            return True

        return False
        

        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            idx = ord(c) - ord("a")
            if curr.children[idx] == None:
                return False
            curr = curr.children[idx]

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)