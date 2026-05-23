class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_matrix = [[0]*n for _ in range(n)]
        for edge in edges:
            i, j = edge[0], edge[1]
            adj_matrix[i][j] = 1
            adj_matrix[j][i] = 1
        

        return self.countGraphs(n, adj_matrix)
    
    def countGraphs(self, n, adj_matrix):
        num_graphs = 0
        unseen_nodes = {i for i in range(n)}
        visited = set()

        def dfs(node):
            visited.add(node)
            for neighbor, connected in enumerate(adj_matrix[node]):
                if connected and neighbor not in visited:
                    dfs(neighbor)
        
        while unseen_nodes:
            dfs(unseen_nodes.pop())
            num_graphs += 1
            unseen_nodes.difference_update(visited)

        return num_graphs

