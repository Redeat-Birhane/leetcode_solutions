class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = -1 

class WordFilter:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        
        for i, word in enumerate(words):
            long_word = word + '#' + word
            for j in range(len(word) + 1):
                curr = self.root
                for ch in long_word[j:]:
                    if ch not in curr.children:
                        curr.children[ch] = TrieNode()
                    curr = curr.children[ch]
                    curr.index = i  
    
    def f(self, pref: str, suff: str) -> int:
        curr = self.root
        query = suff + '#' + pref
        for ch in query:
            if ch not in curr.children:
                return -1
            curr = curr.children[ch]
        return curr.index
