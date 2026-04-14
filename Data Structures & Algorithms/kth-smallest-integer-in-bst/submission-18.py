# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [k]
        res = [0]
        def inOrder(root):
            if not root:
                return
            inOrder(root.left)
            count[0] -= 1
            if count[0] == 0:
                res[0] = root.val
            if count[0] > 0:
                inOrder(root.right)    
        inOrder(root)
        return res[0]
