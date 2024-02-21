'''
NAME: BARECHA ASHENAFI
ID: 0546/13
COURSE_CODE: SEng4081
'''
class Graph:
    def __init__(self):
        # Initialize an empty graph represented as an adjacency list
        self.graph = {}

    def add_edge(self, u, v):
        # Add an edge to the graph
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start_node):
        # Perform depth-first search starting from the specified node
        visited = set()  # Set to keep track of visited nodes
        self._dfs_recursive(start_node, visited)

    def _dfs_recursive(self, node, visited):
        # Recursive function for depth-first search
        if node not in visited:
            print(node, end=' ')  # Print the current node
            visited.add(node)  # Mark the current node as visited
            if node in self.graph:
                # Explore neighbors of the current node
                for neighbor in self.graph[node]:
                    self._dfs_recursive(neighbor, visited)


# Example usage:
if __name__ == "__main__":
    # Create a graph and add edges
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 6)
    g.add_edge(3, 7)

    # Perform depth-first search starting from node 1
    print("Depth-First Search starting from node 1:")
    g.dfs(1)
