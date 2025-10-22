class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False
        self.prefix_count = 0

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        def insert(word):
            curr = self.root
            for char in word:
                idx = ord(char) - ord('a')
                if curr.children[idx] is None:
                    curr.children[idx] = TrieNode()
                curr = curr.children[idx]
                curr.prefix_count += 1  
            curr.is_end = True

        def search(word):
            curr = self.root
            score = 0
            for char in word:
                idx = ord(char) - ord('a')
                if curr.children[idx] is None:
                    return score
                curr = curr.children[idx]
                score += curr.prefix_count
            return score

       
        for word in words:
            insert(word)

        return [search(word) for word in words]
