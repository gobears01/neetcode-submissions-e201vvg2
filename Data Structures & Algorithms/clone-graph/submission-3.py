"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        old_to_new = {}
        old_to_new[node] = Node(node.val)
        q = deque()
        q.append(node)
        while q:
            curr = q.popleft()
            for nei in curr.neighbors:
                if nei not in old_to_new:
                    neiCopy = Node(nei.val)
                    old_to_new[nei] = neiCopy
                    q.append(nei)
                old_to_new[curr].neighbors.append(old_to_new[nei])
        return old_to_new[node]
