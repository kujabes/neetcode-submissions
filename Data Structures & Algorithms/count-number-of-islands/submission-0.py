from collections import deque

class Solution:
    def __init__(self):
        self.delta_pairs = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    def numIslands(self, grid: List[List[str]]) -> int:
        self.rn = len(grid)
        self.cn = len(grid[0])
        num_islands = 0
        total_visited = set()

        def bfs(start):
            visited = set([start])
            queue = deque([start])

            while queue:
                node = queue.popleft()

                adj = self.adj_spaces(node[0], node[1])
                for row, col in adj:
                    # if we strike unvisited land, add to bfs queue
                    if grid[row][col] == '1' and (row, col) not in visited:
                        queue.append((row, col))
                        visited.add((row, col))

            print(sorted(list(visited), key=lambda item: item[0]))
            # in-place union to track all previously visited nodes globally
            total_visited.update(visited)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and (i, j) not in total_visited:
                    num_islands += 1
                    bfs((i, j))
                    print(total_visited)
                
        return num_islands
        
    def adj_spaces(self, row, col):
        valid_adj = []
        for row_delta, col_delta in self.delta_pairs:
            new_row = row + row_delta
            new_col = col + col_delta
            if self.bounded(new_row, new_col):
                valid_adj.append((new_row, new_col))

        return valid_adj


    def bounded(self, row, col):
        return (0 <= row < self.rn) and (0 <= col < self.cn)


