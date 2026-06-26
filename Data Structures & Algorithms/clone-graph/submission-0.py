"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        adj_map = {}

        def bfs(start):
            if start == None: return
            queue = deque([start])
            visited = set([start])

            while queue:
                node = queue.popleft()
                adj_map[node.val] = [nei.val for nei in node.neighbors]

                for nei in node.neighbors:
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)
        bfs(node)

        seen = {}
        for key in adj_map:
            if key not in seen:
                node = Node(key, neighbors=None)
                seen[key] = node
            else:
                node = seen[key]

            for val in adj_map[key]:
                if val not in seen:
                    new_node = Node(val, neighbors=None)
                    seen[val] = new_node
                else:
                    new_node = seen[val]
                node.neighbors.append(new_node)

        return seen.get(1, None)

        

        
    

    