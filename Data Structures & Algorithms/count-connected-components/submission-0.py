class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        preMap = {}
        for i in range(n):
            preMap[i]=[]
        for e in edges:
            preMap[e[0]].append(e[1])
            preMap[e[1]].append(e[0])
        visited=set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for i in preMap[node]:
                dfs(i)
                dfs(i)
        res=0
        for i in range(n):
            if i not in visited:
                res+=1
                dfs(i)
        return res
        


            

        