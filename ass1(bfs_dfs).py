from collections import deque
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        self.graph.setdefault(u, []).append(v)
        self.graph.setdefault(v, []).append(u)

    def dfs_util(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=" ")

        for neighbor in self.graph.get(vertex, []):
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, start):
        visited = set()
        self.dfs_util(start, visited)


    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)  # Mark the starting vertex as visited

        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")

            for neighbor in self.graph.get(vertex, []):
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)  # Mark the neighbor as visited

    

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)

print("Depth-First Search (DFS):")
g.dfs(0)
print("\nBreadth-First Search (BFS):")
g.bfs(0)
