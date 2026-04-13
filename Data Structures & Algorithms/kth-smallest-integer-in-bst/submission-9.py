# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.treeList = []
        self.count = 7
        def inOrder(root):
            if not root:
                return
            inOrder(root.left)
            self.treeList.append(root.val)
            if self.count == 0:
                return self.treeList.pop()
            inOrder(root.right)
        return inOrder(root)
