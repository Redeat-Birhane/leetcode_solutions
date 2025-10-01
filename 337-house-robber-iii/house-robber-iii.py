class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def robber(node):
            if not node:
                return 0
            if node not in memo:
                include = node.val
                if node.right:
                    include += robber(node.right.left) + robber(node.right.right)
                if node.left:
                    include += robber(node.left.left) + robber(node.left.right) 

                exclude = robber(node.right) + robber(node.left)

                memo[node] = max(include, exclude)

            return memo[node]

        return robber(root)

        