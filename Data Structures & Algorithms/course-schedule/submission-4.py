class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq = [[] for i in range(numCourses)]
        for course, pr in prerequisites:
            preq[course].append(pr)
        visited = set()
        visiting = set()
        def DFS(node, visiting):
            if node in visiting:
                return False
            visiting.add(node)
            for nei in preq[node]:
                if not DFS(nei, visiting):
                    return False
            visited.add(node)
            visiting.remove(node)
            return True
        for i in range(numCourses):
            if i in visited:
                continue
            if not DFS(i, visiting):
                return False
        return True
                