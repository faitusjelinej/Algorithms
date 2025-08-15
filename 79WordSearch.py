class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row , col = len(board), len(board[0])


        def dfs(r,c,index):
            if index == len(word):
                return True

            if r < 0 or r >= row or c <0 or c >= col or board[r][c] != word[index]:
                return False

            temp = board[r][c]
            board[r][c] = "#"

            result = (dfs(r+1,c, index+1) or 
                    dfs(r-1,c, index+1) or 
                    dfs(r,c+1, index+1) or
                    dfs(r,c-1, index+1)  )    

            board[r][c] = temp
            return result            

        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0] and dfs(r,c,0):
                    return True
        return False
