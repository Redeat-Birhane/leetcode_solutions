class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if curr.children[idx] is None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.is_end

            char = word[i]
            if char == ".":
                for child in node.children:
                    if child and dfs(child, i + 1):
                        return True

                return False

            else:
                idx = ord(char) - ord("a")
                if node.children[idx] == None:
                    return False

                return dfs(node.children[idx], i + 1)

        return dfs(self.root, 0)
        
