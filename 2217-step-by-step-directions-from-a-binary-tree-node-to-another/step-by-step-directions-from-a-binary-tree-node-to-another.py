# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def findPath(node, target, path):
            if not node:
                return False
            if node.val == target:
                return True
            
            path.append("L")
            if findPath(node.left, target, path):
                return True
            path.pop()
            
            path.append("R")
            if findPath(node.right, target, path):
                return True
            path.pop()
            
            return False
        
        startPath, destPath = [], []
        findPath(root, startValue, startPath)
        findPath(root, destValue, destPath)
       
        i = 0
        while i < len(startPath) and i < len(destPath) and startPath[i] == destPath[i]:
            i += 1
        
        
        upMoves = "U" * (len(startPath) - i)
        downMoves = "".join(destPath[i:])
        
        return upMoves + downMoves
