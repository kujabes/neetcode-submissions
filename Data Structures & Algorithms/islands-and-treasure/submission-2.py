from collections import deque
class Solution:
    def __init__(self):
            self.dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            self.inf = 2147483647

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        self.grid = grid
    
        def bfs(start: tuple[int, int]):
            queue = deque([(start, 1)])
            visited = set([(start, 1)])
            
            while queue:
                node, depth = queue.popleft()
                positions = self.valid_dirs(node)

                for i, j in positions:
                    val = self.grid[i][j]
                    if val not in [-1, 0] and (i, j) not in visited:
                        self.grid[i][j] = min(val, depth)
                        queue.append(((i, j), depth + 1))
                        visited.add((i, j))
                        
                    
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 0:
                    positions = self.valid_dirs((i, j))
                    bfs((i, j))
        
                    
    def valid_dirs(self, node: tuple[int, int]):
        bounded = lambda node: 0 <= node[0] < len(self.grid) and \
                               0 <= node[1] < len(self.grid[0])

        valid_pos = []
        for dx, dy in self.dirs:
            x = node[0] + dx
            y = node[1] + dy

            if bounded((x, y)):
                valid_pos.append((x, y))

        
        return valid_pos

        


