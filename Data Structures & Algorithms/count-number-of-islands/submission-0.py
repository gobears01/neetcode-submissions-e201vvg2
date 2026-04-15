class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIs = 0
        ROWS, COLS = len(grid), len(grid[0])
        def DFS(r, c):
            if r>= ROWS or c>= COLS or r<0 or c<0 or grid[r][c] != '1':
                return
            grid[r][c] = '0'
            DFS(r-1,c)
            DFS(r+1,c)
            DFS(r,c-1)
            DFS(r,c+1)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    numIs += 1
                    DFS(r, c)
        return numIs
