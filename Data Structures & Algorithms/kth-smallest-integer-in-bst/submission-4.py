# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        treeList = []
        k = k
        def inOrder(root):
            if not root:
                return
            
            inOrder(root.left)
            treeList.append(root.val)
            k -= 1
            if k == 0:
                return treeList.pop()
            inOrder(root.right)
        inOrder(root)
        return treeList.pop()