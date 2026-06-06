from collections import deque

class Solution:
    def __init__(self) -> None:
        self.delta_array = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def numIslands(self, grid: list[list[str]]) -> int:
        self.grid = grid
        num_islands = 0
        self.visited = set()

        # bfs search from start node
        def dfs(start: tuple[int, int]):
            self.visited.add(start)
            stack = [start]

            while stack:
                node = stack.pop()

                for new_node in self.directions(node):
                    if self.grid[new_node[0]][new_node[1]] == '1' and new_node not in self.visited:
                        stack.append(new_node)
                        self.visited.add(new_node)

        # Exhaustive search to ensure all nodes are touched
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.grid[i][j] == '1' and (i, j) not in self.visited:
                    num_islands += 1
                    dfs((i, j))

        return num_islands

    def directions(self, node: tuple[int, int]):
        valid_nodes = []
        for dx, dy in self.delta_array:
            new_node = (node[0] + dx, node[1] + dy)
            if self.bounded(new_node):
                valid_nodes.append(new_node)
        
        return valid_nodes

    def bounded(self, node: tuple[int, int]):
        i, j = node[0], node[1]
        return 0 <= i < len(self.grid) and 0 <= j < len(self.grid[0])
