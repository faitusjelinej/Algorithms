class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visted = set()

        def dfs(r,c):
            if r >= 0 and r <len(board) and c>= 0 and c< len(board[0]) and (r,c) not in visted and board[r][c] != 'X':
                visted.add((r,c))
                dfs(r,c+1)
                dfs(r,c-1)
                dfs(r-1,c)
                dfs(r+1,c)
            else:
                return None

        for i in range(len(board)):
            dfs(i,0)
            dfs(i, len(board[0])-1)

        for i in range(len(board[0])):
            dfs(0,i)
            dfs(len(board)-1,i)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i,j) not in visted:
                    board[i][j] = 'X'                    
