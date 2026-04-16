class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        neighbors = [[] for i in range(n)]
        numCompo = 0
        for v1, v2 in edges:
            neighbors[v1].append(v2)
            neighbors[v2].append(v1)

        def DFS(node):
            for nei in neighbors[node]:
                if nei not in visited:
                    visited.add(nei)
                    DFS(nei)
        for node in range(n):
            if node not in visited:
                DFS(node)
                visited.add(node)
                numCompo += 1
        return numCompo
            
