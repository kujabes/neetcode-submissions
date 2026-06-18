from collections import deque

class Solution:
    def __init__(self):
        self.delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.visited = set()
        max_area = 0

        def bfs(start: tuple[int, int]):
            queue = deque([start])
            self.visited.add(start)

            while queue:
                node = queue.popleft()

                for new_node in self.directions(node):
                    i, j = new_node[0], new_node[1]
                    if new_node not in self.visited and self.grid[i][j]:
                        self.visited.add(new_node)
                        queue.append(new_node)
        
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] and (i, j) not in self.visited:
                    start = len(self.visited)
                    bfs((i, j))
                    end = len(self.visited)
                    max_area = max(max_area, end - start)
        
        return max_area

    def directions(self, node: tuple[int, int]):
        valid_dirs = []
        for dx, dy in self.delta:
            new_node = (node[0] + dx, node[1] + dy)
            if self.is_valid(new_node):
                valid_dirs.append(new_node)

        return valid_dirs

    def is_valid(self, node: tuple[int, int]):
        return 0 <= node[0] < len(self.grid) and 0 <= node[1] < len(self.grid[0])