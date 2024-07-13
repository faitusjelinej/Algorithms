class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rowlen = len(grid)
        collen = len(grid[0])

        for c in range(1,collen):
            grid[0][c] += grid[0][c-1]

        for r in range(1,rowlen):
            grid[r][0] += grid[r-1][0]

        for r in range(1,rowlen):
            for c in range(1,collen):
                grid[r][c] += min(grid[r-1][c],grid[r][c-1]) 

        return grid[rowlen-1][collen-1]    
