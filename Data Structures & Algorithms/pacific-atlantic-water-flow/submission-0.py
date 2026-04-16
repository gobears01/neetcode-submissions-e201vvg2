class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        ROWS, COLS = len(heights), len(heights[0])
        
        def DFS(r, c, seen, minHeight):
            if r == ROWS or c == COLS or r< 0 or r< 0 or heights[r][c] < minHeight or ((r,c) in seen):
                return
            seen.add((r,c))
            DFS(r + 1, c, seen, heights[r][c])
            DFS(r - 1, c, seen, heights[r][c])
            DFS(r, c + 1, seen, heights[r][c])
            DFS(r, c + 1, seen, heights[r][c])
        for c in range(COLS):
            DFS(0, c, pac, 0)
            DFS(ROWS-1, c, atl, 0)
        for r in range(ROWS):
            DFS(r, COLS - 1, atl, 0)
            DFS(r, 0, pac, 0)
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res 


            
            
        