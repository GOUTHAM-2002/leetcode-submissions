class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        flag=False
        def dfs(i,r,c,check):
            nonlocal flag
            if (r,c) in check:
                return
            if -1 < r < len(board) and -1 < c < len(board[0]):
                if word[i] == board[r][c]:
                    i+=1
                    check.add((r,c))
                    if i == len(word):
                        flag=True
                        return
                    dfs(i,r+1,c,check)
                    dfs(i,r,c+1,check)
                    dfs(i,r-1,c,check)
                    dfs(i,r,c-1,check)
                    check.remove((r,c))
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]==word[0]:
                    dfs(0,r,c,set())
        return flag


        