
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # If number of edges is not n - 1, it can't be a tree
        if len(edges) != n - 1:
            return False
        
        # Build the adjacency list for the undirected graph
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Set to track visited nodes
        visited = set()
        
        # DFS function
        def dfs(node, parent):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue  # Skip the edge back to the parent node
                if neighbor in visited:
                    return False  # Found a cycle
                if not dfs(neighbor, node):
                    return False
            return True
        
        # Start DFS from node 0
        if not dfs(0, -1):
            return False
        
        # Check if all nodes were visited (graph is connected)
        return len(visited) == n