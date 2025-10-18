class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.sum = 0
class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.map = {}
        

    def insert(self, key: str, val: int) -> None:
        diff = val - self.map.get(key, 0)
        self.map[key] = val
        curr = self.root
        for char in key:
            idx = ord(char) - ord("a")
            if curr.children[idx] == None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
            curr.sum += diff


        

    def sum(self, prefix: str) -> int:
        curr = self.root
        for char in prefix:
            idx = ord(char) - ord("a")
            if curr.children[idx] == None:
                return 0
            curr = curr.children[idx]
        return curr.sum

        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)