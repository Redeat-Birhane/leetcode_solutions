# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = TreeNode(val)
        def BST(temp):
            if not temp:
                temp = node
                return temp
            if val > temp.val:
                if not temp.right:
                    temp.right = node
                    return root
                return BST(temp.right)
                
            else:
                if not temp.left:
                    temp.left = node
                    return root
                return BST(temp.left)
        ans = BST(root)
        return ans
                

        