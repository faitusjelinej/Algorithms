class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix) , len(matrix[0])
        dp = [[0]*n for i in range(m)] 

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 1:
                    if r == 0 or c == 0:
                        dp[r][c] = 1
                    else:
                        dp[r][c] = 1 + min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])

        return sum(sum(row) for row in dp)      
