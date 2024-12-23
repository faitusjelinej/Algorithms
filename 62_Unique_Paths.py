class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for i in range(n)] for j in range(m)]

        for col in range(len(grid[0])):
            grid[0][col] = 1

        for row in range(len(grid)):
            grid[row][0] = 1

        for row in range(1, len(grid)):
            for col in range(1, len(grid[0])):
                grid[row][col] = grid[row-1][col] + grid[row][col-1]    

        return grid[m-1][n -1]     
