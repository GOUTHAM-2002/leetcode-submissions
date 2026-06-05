class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r,c):
            if -1 < r < len(grid) and -1 < c < len(grid[0]):
                if grid[r][c]=="1":
                    grid[r][c]=0
                    dfs(r,c+1)
                    dfs(r,c-1)
                    dfs(r+1,c)
                    dfs(r-1,c)
        res=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=="1":
                    res+=1
                    dfs(r,c)
        return res
        