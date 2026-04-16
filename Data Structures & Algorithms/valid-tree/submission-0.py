class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for i in range(n)]
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        seen = set()
        def DFS(node, parent):
            if node in seen and node != parent:
                return False
            seen.add(node)
            for nei in adj[node]:
                if not DFS(nei, node):
                    return False
            return True
        return DFS(0, -1) and len(seen) == n


    
        