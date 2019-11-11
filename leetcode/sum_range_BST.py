# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = [10,5,15,3,7,None,18]

node = TreeNode(root)
print(node.val)